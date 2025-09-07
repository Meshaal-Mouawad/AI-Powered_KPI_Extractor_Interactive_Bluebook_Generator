import os
import jinja2
import re
import time
import subprocess
from pathlib import Path
from .kpi_extractor import find_kpis_in_directory
# Replace brittle name import with a robust module import
try:
    from .ai_generator import generate_kpi_details
except Exception:
    # Fallback ensures the module loads even if symbol export is delayed,
    # and raises a clearer error if the function is truly missing.
    import importlib
    _ai = importlib.import_module(".ai_generator", package=__package__)
    if not hasattr(_ai, "generate_kpi_details"):
        raise ImportError("bluebook_generator.ai_generator.generate_kpi_details is not defined.")
    generate_kpi_details = getattr(_ai, "generate_kpi_details")

# Public API from this module
__all__ = ["generate_bluebook"]

ROOT_DIR = Path(__file__).parent.parent
DOCS_SOURCE_DIR = ROOT_DIR / 'docs'
TEMPLATE_DIR = ROOT_DIR / 'templates'

def _sanitize_text(text: str) -> str:
    """
    Remove any HTML tags and script/style blocks from user/override text,
    then normalize whitespace. This prevents stray tags like </td></tr>... appearing.
    """
    if not isinstance(text, str):
        text = "" if text is None else str(text)

    s = text

    # Drop script/style blocks completely
    s = re.sub(r"(?is)<\s*(script|style)\b.*?>.*?<\s*/\s*\1\s*>", "", s)

    # Remove all remaining HTML tags
    s = re.sub(r"(?s)<[^>]+>", "", s)

    # Normalize whitespace
    s = re.sub(r"\s+", " ", s).strip()

    return s

# Public API from this module
import json

def format_text_as_html_list(text: str) -> str:
    """Takes plain text and formats it as an HTML <ul> list.

    SECURITY + SANITATION:
    - Strips any HTML first so pasted fragments cannot leak into the page.
    - Then escapes the remaining text to ensure it renders as text only.
    """
    from html import escape

    cleaned = _sanitize_text(text)
    safe = escape(cleaned)

    if not safe or "Error generating content" in safe:
        return f"<p>{safe}</p>"

    # Split into short bullet items by sentence/phrase boundaries
    items = re.split(r'[.;,]\s*', safe)
    items = [i.strip() for i in items if i and len(i.strip()) > 1]

    if not items:
        return f"<p>{safe}</p>"

    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def _extract_function_block(code_context: str, anchor_line_number: int):
    """
    Returns (scoped_function_block, start_index_in_original_context).

    Robust version:
    1) Uses AST to find the exact function that contains the anchor line.
    2) Falls back to a refined indentation heuristic if AST parsing fails.

    This ensures we do not include any trailing top-level code (e.g., demo blocks or comments)
    that follow the function in its source file.
    """
    import ast

    lines = code_context.splitlines()
    if not lines or anchor_line_number <= 0 or anchor_line_number > len(lines):
        return code_context, 0

    # --- AST-based extraction ---
    try:
        tree = ast.parse(code_context)
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                start = node.lineno
                end = getattr(node, "end_lineno", None)
                if end is None:
                    # Conservative end calculation
                    last = node.body[-1]
                    end = getattr(last, "end_lineno", getattr(last, "lineno", start))
                if start <= anchor_line_number <= end:
                    # Slice exactly this function
                    return "\n".join(lines[start - 1:end]), start - 1
        # If no function covered anchor, fall back
    except Exception:
        pass

    # --- Heuristic fallback (refined) ---
    anchor_idx = anchor_line_number - 1

    # Find the start (the def that contains the anchor)
    start_idx = 0
    for i in range(anchor_idx, -1, -1):
        if lines[i].lstrip().startswith("def "):
            start_idx = i
            break

    def_indent = len(lines[start_idx]) - len(lines[start_idx].lstrip())

    # Find the end: next def at same/less indent, indent drop to < def_indent,
    # or common top-level markers (comments or if __name__...)
    end_idx = len(lines)
    for j in range(start_idx + 1, len(lines)):
        raw = lines[j]
        stripped = raw.strip()
        indent = len(raw) - len(raw.lstrip())

        if not stripped:
            continue

        # New function at same or lower indentation -> end current block
        if raw.lstrip().startswith("def ") and indent <= def_indent:
            end_idx = j
            break

        # Any non-empty line that drops below the function indent -> end
        if indent < def_indent:
            end_idx = j
            break

        # Hard stop on common top-level constructs
        if indent == 0 and (stripped.startswith("#") or stripped.startswith("if __name__")):
            end_idx = j
            break

    scoped = "\n".join(lines[start_idx:end_idx])
    return scoped, start_idx

def generate_formula_from_code(code_context: str) -> dict:
    """
    Programmatically generate a MathJax block from code context.
    Supports:
    - DAX: DEFINE MEASURE 'T'[Name] = ... RETURN <expr> | Name = <expr>
    - SQL/T-SQL/HANA: SELECT <expr> AS <alias> (multi-line, CAST/CASE supported)
    - C#/VB/PLSQL/ABAP: return <expr>; or <var> = <expr>;
    - IEC 61131-3 ST: <var> := <expr>;
    - Generic fallback: pick the most math-like expression (percent or division) anywhere in the block.
    """
    formula_data = {
        "formula_html": "<p>See code context for implementation details.</p>"
    }

    ctx = code_context

    # 0) Helpers
    def latex_escape(s: str) -> str:
        # Escape LaTeX special chars to prevent MathJax brace/parse errors
        # Order matters: backslash first
        repl = [
            ('\\', r'\\'),
            ('{', r'\{'),
            ('}', r'\}'),
            ('#', r'\#'),
            ('$', r'\$'),
            ('%', r'\%'),
            ('&', r'\&'),
            ('_', r'\_'),
            ('^', r'\^'),
            ('~', r'\~'),
        ]
        out = s
        for a, b in repl:
            out = out.replace(a, b)
        return out

    def sanitize_token(t: str) -> str:
        t = t.strip()
        t = re.sub(r'[:\.]+', ' ', t)                 # namespaces/members
        t = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', t) # camelCase
        t = t.replace('_', ' ')
        t = re.sub(r'\s+', ' ', t).strip()
        t = latex_escape(t)
        return t.title()

    def L(v: str) -> str:
        return r'\mathit{{{}}}'.format(v.replace(' ', r'\,'))

    def strip_inline_comments(line: str) -> str:
        l = line
        l = re.split(r"--", l, maxsplit=1)[0]
        l = re.split(r"//", l, maxsplit=1)[0]
        l = re.split(r"(?<!:)\s'", l, maxsplit=1)[0]
        l = re.split(r"#", l, maxsplit=1)[0]
        return l.rstrip(" ;\t")

    # Remove outer SQL wrappers like CAST(...), COALESCE(...), NULLIF(...), parentheses
    def unwrap_sql_expr(expr: str) -> str:
        e = expr.strip()
        # FIX: use the correct group name "inner" consistently
        m = re.search(r"(?is)\bCAST\s*\(\s*(?P<inner>.+?)\s+AS\s+[^\)]+\)", e)
        if m:
            e = m.group("inner").strip()
        m = re.search(r"(?is)\bCOALESCE\s*\(\s*(?P<inner>.+?)\s*,\s*.+?\)", e)
        if m:
            e = m.group("inner").strip()
        m = re.search(r"(?is)\bNULLIF\s*\(\s*(?P<inner>.+?)\s*,\s*.+?\)", e)
        if m:
            e = m.group("inner").strip()
        e = e.strip()
        if e.startswith("(") and e.endswith(")"):
            e = e[1:-1].strip()
        return e
    # Clean lines for single-line patterns
    cleaned = []
    for raw in ctx.splitlines():
        s = raw.strip()
        if not s:
            continue
        if s.startswith(("#", "--", "//", "/*", "*", "'")):
            continue
        cleaned.append(strip_inline_comments(raw).strip())

    def build_html(result_var: str, expression: str, notes: list[str] | None = None) -> dict:
        rv = sanitize_token(result_var)
        expr = expression.strip().rstrip(";")

        # CASE ... END → try to pull the mathy part
        m_case = re.search(r"(?is)\bcase\b.*?\bend\b", expr)
        if m_case:
            inner = m_case.group(0)
            m_inner = re.search(r"\((.*?)\s*/\s*(.*?)\)\s*\*\s*100", inner, flags=re.S)
            if not m_inner:
                m_inner = re.search(r"([A-Za-z0-9_().\s]+)\s*/\s*([A-Za-z0-9_().\s]+)", inner, flags=re.S)
            if m_inner:
                expr = m_inner.group(0)

        expr = unwrap_sql_expr(expr)

        latex_str = ""
        notes = notes or []

        # (a/b)*100 or 100*(a/b)
        m = re.search(r"\((.*?)\s*/\s*(.*?)\)\s*\*\s*100", expr)
        if m:
            num, den = [sanitize_token(s) for s in m.groups()]
            latex_str = r"{} = \frac{{{}}}{{{}}} \times 100".format(L(rv), L(num), L(den))
            notes += [f"<i>{num}:</i> The numerator of the fraction.", f"<i>{den}:</i> The denominator of the fraction."]
        elif re.search(r"100\s*\*\s*\((.*?)\s*/\s*(.*?)\)", expr):
            m = re.search(r"100\s*\*\s*\((.*?)\s*/\s*(.*?)\)", expr)
            num, den = [sanitize_token(s) for s in m.groups()]
            latex_str = r"{} = 100 \times \frac{{{}}}{{{}}}".format(L(rv), L(num), L(den))
            notes += [f"<i>{num}:</i> The numerator of the fraction.", f"<i>{den}:</i> The denominator of the fraction."]
        # a / b
        elif '/' in expr and not re.search(r'//', expr):
            parts = [p.strip() for p in expr.split('/', 1)]
            if len(parts) == 2 and parts[0] and parts[1]:
                a, b = sanitize_token(parts[0]), sanitize_token(parts[1])
                latex_str = r"{} = \frac{{{}}}{{{}}}".format(L(rv), L(a), L(b))
        # product
        elif '*' in expr:
            parts = [sanitize_token(p) for p in re.split(r'\*', expr)]
            if len(parts) >= 2:
                latex_str = r"{} = {}".format(L(rv), r' \times '.join([L(p) for p in parts]))
        # subtraction / addition
        elif '-' in expr:
            parts = [sanitize_token(p) for p in expr.split('-', 1)]
            if len(parts) == 2:
                latex_str = r"{} = {} - {}".format(L(rv), L(parts[0]), L(parts[1]))
        elif '+' in expr:
            parts = [sanitize_token(p) for p in expr.split('+', 1)]
            if len(parts) == 2:
                latex_str = r"{} = {} + {}".format(L(rv), L(parts[0]), L(parts[1]))

        if latex_str:
            notes_html = "<ul>" + "".join(f"<li>{n}</li>" for n in notes) + "</ul>" if notes else ""
            return {"formula_html": f'<div class="math-equation">$$ {latex_str} $$</div>{notes_html}'}
        return {"formula_html": "<p>See code context for implementation details.</p>"}

    # Helpers (keep your latest versions; shown trimmed here)
    def latex_escape(s: str) -> str:
        repl = [
            ('\\', r'\\'), ('{', r'\{'), ('}', r'\}'), ('#', r'\#'),
            ('$', r'\$'), ('%', r'\%'), ('&', r'\&'), ('_', r'\_'),
            ('^', r'\^'), ('~', r'\~'),
        ]
        out = s
        for a, b in repl:
            out = out.replace(a, b)
        return out

    def sanitize_token(t: str) -> str:
        t = t.strip()
        t = re.sub(r'[:\.]+', ' ', t)
        t = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', t)
        t = t.replace('_', ' ')
        t = re.sub(r'\s+', ' ', t).strip()
        t = latex_escape(t)
        return t.title()

    def L(v: str) -> str:
        return r'\mathit{{{}}}'.format(v.replace(' ', r'\,'))

    def strip_inline_comments(line: str) -> str:
        l = line
        l = re.split(r"--", l, maxsplit=1)[0]
        l = re.split(r"//", l, maxsplit=1)[0]
        l = re.split(r"(?<!:)\s'", l, maxsplit=1)[0]
        l = re.split(r"#", l, maxsplit=1)[0]
        return l.rstrip(" ;\t")

    def unwrap_sql_expr(expr: str) -> str:
        e = expr.strip()
        m = re.search(r"(?is)\bCAST\s*\(\s*(?P<i>.+?)\s+AS\s+[^\)]+\)", e)
        if m: e = m.group("i").strip()
        m = re.search(r"(?is)\bCOALESCE\s*\(\s*(?P<i>.+?)\s*,\s*.+?\)", e)
        if m: e = m.group("i").strip()
        m = re.search(r"(?is)\bNULLIF\s*\(\s*(?P<i>.+?)\s*,\s*.+?\)", e)
        if m: e = m.group("i").strip()
        e = e.strip()
        if e.startswith("(") and e.endswith(")"): e = e[1:-1].strip()
        return e

    # NEW: safe group accessor to avoid "no such group" errors
    def gd(m: re.Match | None, key: str, default: str = "") -> str:
        if not m:
            return default
        try:
            return m.groupdict().get(key, default)
        except Exception:
            return default

    # Prepare cleaned single lines for non-multiline patterns
    cleaned = []
    for raw in ctx.splitlines():
        s = raw.strip()
        if not s or s.startswith(("#", "--", "//", "/*", "*", "'")):
            continue
        cleaned.append(strip_inline_comments(raw).strip())

    def build_html(result_var: str, expression: str, notes: list[str] | None = None) -> dict:
        rv = sanitize_token(result_var)
        expr = unwrap_sql_expr(expression.strip().rstrip(";"))
        notes = notes or []
        latex_str = ""

        # (a/b)*100 or 100*(a/b)
        m = re.search(r"\((.*?)\s*/\s*(.*?)\)\s*\*\s*100", expr)
        if m:
            num, den = [sanitize_token(s) for s in m.groups()]
            latex_str = r"{} = \frac{{{}}}{{{}}} \times 100".format(L(rv), L(num), L(den))
            notes += [f"<i>{num}:</i> The numerator of the fraction.", f"<i>{den}:</i> The denominator of the fraction."]
        elif re.search(r"100\s*\*\s*\((.*?)\s*/\s*(.*?)\)", expr):
            m = re.search(r"100\s*\*\s*\((.*?)\s*/\s*(.*?)\)", expr)
            num, den = [sanitize_token(s) for s in m.groups()]
            latex_str = r"{} = 100 \times \frac{{{}}}{{{}}}".format(L(rv), L(num), L(den))
            notes += [f"<i>{num}:</i> The numerator of the fraction.", f"<i>{den}:</i> The denominator of the fraction."]
        # a / b
        elif '/' in expr and not re.search(r'//', expr):
            parts = [p.strip() for p in expr.split('/', 1)]
            if len(parts) == 2 and parts[0] and parts[1]:
                a, b = sanitize_token(parts[0]), sanitize_token(parts[1])
                latex_str = r"{} = \frac{{{}}}{{{}}}".format(L(rv), L(a), L(b))
        # product
        elif '*' in expr:
            parts = [sanitize_token(p) for p in re.split(r'\*', expr)]
            if len(parts) >= 2:
                latex_str = r"{} = {}".format(L(rv), r' \times '.join([L(p) for p in parts]))
        # subtraction / addition
        elif '-' in expr:
            parts = [sanitize_token(p) for p in expr.split('-', 1)]
            if len(parts) == 2:
                latex_str = r"{} = {} - {}".format(L(rv), L(parts[0]), L(parts[1]))
        elif '+' in expr:
            parts = [sanitize_token(p) for p in expr.split('+', 1)]
            if len(parts) == 2:
                latex_str = r"{} = {} + {}".format(L(rv), L(parts[0]), L(parts[1]))

        if latex_str:
            notes_html = "<ul>" + "".join(f"<li>{n}</li>" for n in notes) + "</ul>" if notes else ""
            return {"formula_html": f'<div class="math-equation">$$ {latex_str} $$</div>{notes_html}'}
        return {"formula_html": "<p>See code context for implementation details.</p>"}

    # 1) DAX multi-line
    m = re.search(r"(?is)\bDEFINE\s+MEASURE\s+[^\[]*\[(?P<name>[^\]]+)\]\s*=\s*(?P<body>.+?)(?:$|\n\s*\n)", ctx)
    if m:
        name = gd(m, "name")
        body = gd(m, "body")
        if name and body:
            m_ret = re.search(r"(?is)\bRETURN\b\s*(?P<expr>.+)", body)
            expr = gd(m_ret, "expr", body)
            return build_html(name, expr)

    # 1b) DAX simple
    m = re.search(r"(?is)^(?P<name>[A-Za-z0-9 _\[\]\.%]+?)\s*=\s*(?P<expr>.+?)(?:$|\n\s*\n)", ctx, flags=re.M)
    if m:
        name = gd(m, "name")
        expr = gd(m, "expr")
        if name and expr and not re.match(r"\s*(VAR|RETURN|EVALUATE)\b", name, flags=re.I):
            return build_html(name, expr)

    # 2) SQL/TSQL/HANA: SELECT ... <expr> AS <alias> ... FROM ...
    m = re.search(r"(?is)\bSELECT\b\s+(?P<select>.+?)\bFROM\b", ctx)
    if m:
        select_list = gd(m, "select")
        if select_list:
            alias_pattern = r"""(?is)
                (?P<expr>[^,]+?)         # expression
                \s+AS\s+
                (?P<alias>
                    \[[^\]]+\] | "[^"]+" | '[^']+' | [A-Za-z_][A-Za-z0-9_]*
                )
                \s*(?:,|$)
            """
            matches = list(re.finditer(alias_pattern, select_list, flags=re.X))
            if matches:
                last = matches[-1]
                alias = gd(last, "alias")
                expr  = gd(last, "expr")
                if alias and expr:
                    alias = re.sub(r'^[\[\("\']|[\]\)"\']$', '', alias)
                    return build_html(alias, expr)

    # 2b) SQL fallback: any "<expr> AS <alias>" anywhere
    alias_global = r"""(?is)
        (?P<expr>.+?) \s+ AS \s+
        (?P<alias>\[[^\]]+\] | "[^"]+" | '[^']+' | [A-Za-z_][A-Za-z0-9_]*)
    """
    matches = list(re.finditer(alias_global, ctx, flags=re.X))
    if matches:
        last = matches[-1]
        alias = gd(last, "alias")
        expr  = gd(last, "expr")
        if alias and expr:
            alias = re.sub(r'^[\[\("\']|[\]\)"\']$', '', alias)
            # Prefer percent-style sub-expr if present
            m_pct = re.search(r"(?is)100\s*\*\s*\((.+?/.+?)\)|\((.+?/.+?)\)\s*\*\s*100", expr)
            if m_pct:
                expr = (m_pct.group(1) or m_pct.group(2)).strip()
            else:
                # Prefer last division inside expr
                divs = list(re.finditer(r"(?is)([A-Za-z0-9_().\s]+)\s*/\s*([A-Za-z0-9_().\s]+)", expr))
                if divs:
                    a, b = divs[-1].groups()
                    expr = f"{a.strip()} / {b.strip()}"
            return build_html(alias, expr)

    # 2c) Strong T‑SQL percent fallback (covers CAST/NULLIF with or without AS match)
    m_tsql_pct = re.search(r"(?is)100\s*\*\s*\(([^)]+?/[^)]+?)\)|\(([^)]+?/[^)]+?)\)\s*\*\s*100", ctx)
    if m_tsql_pct:
        expr_inner = (m_tsql_pct.group(1) or m_tsql_pct.group(2) or "").strip()
        if expr_inner:
            m_alias_near = re.search(r"(?is)\bAS\s+(\[[^\]]+\]|\"[^\"]+\"|'[^']+'|[A-Za-z_][A-Za-z0-9_]*)", ctx)
            result_name = "Result"
            if m_alias_near:
                alias = m_alias_near.group(1)
                result_name = re.sub(r'^[\[\("\']|[\]\)"\']$', '', alias).strip() or result_name
            return build_html(result_name, expr_inner)

    # 2d) CAST(...) AS <alias> direct fallback (extract inner first arg of CAST)
    m_cast_as = re.search(
        r'(?is)CAST\s*\(\s*(?P<inner>.+?)\s+AS\s+[^\)]+\)\s+AS\s+(?P<alias>\[[^\]]+\]|"[^"]+"|\'[^\']+\'|[A-Za-z_][A-Za-z0-9_]*)',
        ctx
    )
    if m_cast_as:
        alias = re.sub(r'^[\[\("\']|[\]\)"\']$', '', m_cast_as.group("alias")).strip()
        expr = unwrap_sql_expr(m_cast_as.group("inner"))
        if alias and expr:
            return build_html(alias, expr)

    # 3) return <expr>;
    m = re.search(r"(?is)\breturn\b\s+(?P<expr>.+)", ctx)
    if m and gd(m, "expr"):
        return build_html("Result", gd(m, "expr"))

    # 3b) VB Return: handle at line start with optional indent (e.g., "Return operatingHours / numberOfFailures")
    m_vb_return = re.search(r"(?im)^\s*return\s+(?P<expr>[^\r\n]+)$", ctx)
    if m_vb_return:
        expr = m_vb_return.group("expr").strip()
        if expr:
            return build_html("Result", expr)

    # 4) assignment with =
    for line in ctx.splitlines():
        l = strip_inline_comments(line.strip())
        if not l or l.startswith(("#", "--", "//", "/*", "*", "'")):
            continue
        if ':=' in l:
            continue
        if '=' in l and not re.search(r"(?i)\b(create|def|function|procedure|view)\b", l):
            lhs_rhs = l.split('=', 1)
            if len(lhs_rhs) == 2:
                lhs, rhs = [p.strip() for p in lhs_rhs]
                if any(op in rhs for op in ('*', '/', '+', '-')):
                    return build_html(lhs, rhs)

    # 4b) Python/any-language assignment with math on the same line (take last match)
    assigns = list(re.finditer(r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<expr>.+)$", ctx))
    if assigns:
        for mm in reversed(assigns):
            expr = mm.group("expr").strip()
            if any(op in expr for op in ("*", "/", "+", "-")):
                lhs = mm.group(1)
                return build_html(lhs, expr)

    # 4c) ABAP assignment ending with period (e.g., lv_rate = (...) * 100.)
    m_abap = re.search(r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<expr>.+?)\.\s*$", ctx)
    if m_abap:
        lhs = m_abap.group(1)
        expr = m_abap.group("expr").strip()
        if any(op in expr for op in ("*", "/", "+", "-")):
            return build_html(lhs, expr)

    # 5) IEC ST assignment :=
    for line in ctx.splitlines():
        l = strip_inline_comments(line.strip())
        if ':=' in l:
            lhs_rhs = l.split(':=', 1)
            if len(lhs_rhs) == 2:
                lhs, rhs = [p.strip() for p in lhs_rhs]
                if any(op in rhs for op in ('*', '/', '+', '-')):
                    return build_html(lhs, rhs)

    # 6) NEW: last-resort generic sweep — pick the last math-like line
    #    Works for VB/Python/C-like/SQL-ish snippets when earlier patterns miss.
    candidate = None
    result_name = "Result"

    # Prefer percent-style expressions first
    pct = list(re.finditer(r"(?is)100\s*\*\s*\((.+?/.+?)\)|\((.+?/.+?)\)\s*\*\s*100", ctx))
    if pct:
        grp = pct[-1].groups()
        expr = (grp[0] or grp[1] or "").strip()
        if expr:
            candidate = expr

    # Next prefer divisions a / b
    if not candidate:
        divs = list(re.finditer(r"(?is)([A-Za-z0-9_().\s]+)\s*/\s*([A-Za-z0-9_().\s]+)", ctx))
        if divs:
            a, b = divs[-1].groups()
            candidate = f"{a.strip()} / {b.strip()}"

    # If we found a math expression, try to extract a nearby result name
    if candidate:
        # Try to use an alias or LHS nearby as the result variable
        #  - alias: "... AS some_name"
        m_alias = re.search(r"(?is)\bAS\s+(\[[^\]]+\]|\"[^\"]+\"|'[^']+'|[A-Za-z_][A-Za-z0-9_]*)", ctx)
        if m_alias:
            alias = m_alias.group(1)
            result_name = re.sub(r'^[\[\("\']|[\]\)"\']$', '', alias).strip() or result_name
        else:
            # Look for a nearby assignment LHS like "name = ...", "name := ..."
            m_lhs = re.search(r"(?is)^\s*([A-Za-z_][A-Za-z0-9_\.]*)\s*[:=]=?\s*.*$", ctx, flags=re.M)
            if m_lhs:
                result_name = m_lhs.group(1)

        return build_html(result_name, candidate)

    return formula_data

def create_rst_file(kpi_data: dict, details: dict, template: jinja2.Template):
    """Generates and saves a .rst file for a single KPI (all languages)."""
    from html import escape
    import os

    # 1) Find the KPI marker line within the provided code context (for line highlighting)
    kpi_line_in_context = 0
    context_lines = (kpi_data.get('code_context') or '').split('\n')
    kpi_name = kpi_data.get('name') or ''
    for i, line in enumerate(context_lines):
        if f"# KPI: {kpi_name}" in line or f"-- KPI: {kpi_name}" in line or f"' KPI: {kpi_name}" in line or f"/* KPI: {kpi_name}" in line:
            kpi_line_in_context = i + 1
            break
    kpi_data['context_line_number'] = kpi_line_in_context

    # 2) Determine file extension and possibly scope Python to function block
    file_path = kpi_data.get('file_path') or ''
    _, ext = os.path.splitext(str(file_path).lower())

    if ext == ".py":
        # Scope to the function that contains the KPI marker for cleaner context
        scoped_context, start_idx = _extract_function_block(kpi_data.get('code_context', ''), kpi_line_in_context)
        kpi_data['code_context'] = scoped_context
        # Recompute relative line number inside the scoped block
        if kpi_line_in_context > 0:
            rel = kpi_line_in_context - start_idx
            kpi_data['context_line_number'] = rel if rel > 0 else 0
        else:
            kpi_data['context_line_number'] = 0
        programmatic_formula = generate_formula_from_code(scoped_context)
    else:
        # Keep full context for SQL-like/ABAP/etc.
        programmatic_formula = generate_formula_from_code(kpi_data.get('code_context', ''))

    # 3) Build final_details consistently for all languages
    final_details = {
        "description_html": format_text_as_html_list(details.get("description", "")),
        "objective_html": format_text_as_html_list(details.get("objective", "")),
        "formula_description": escape(details.get("formula_description", "") or ""),
        "used_in_kpis_html": format_text_as_html_list(details.get("used_in_kpis", "")),
        "input_measure_html": format_text_as_html_list(details.get("input_measure", "")),
        "unit_of_measure": escape(details.get("unit_of_measure", "") or ""),
        "reporting_source": escape(details.get("reporting_source", "") or ""),
        "comments": escape(details.get("comments", "") or ""),
        **(programmatic_formula or {}),
    }

    # If an explicit LaTeX formula was provided in kpi_data, prefer it
    explicit_formula = kpi_data.get("formula")
    if explicit_formula:
        final_details["formula_html"] = f'<div class="math-equation">$$ {explicit_formula} $$</div>'

    # 4) Compute safe filename and write the .rst file
    safe_name = "".join(c for c in (kpi_name or '') if c.isalnum() or c in (' ', '_')).rstrip()
    filename = (safe_name.replace(' ', '_').lower() or 'kpi') + '.rst'
    output_path = DOCS_SOURCE_DIR / filename

    content = template.render(kpi=kpi_data, details=final_details)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return filename
# ------------- Minimal index.rst writer -------------
def update_index_rst(page_filenames):
    """
    Write docs/index.rst with a toctree listing for the generated KPI pages.
    """
    index_path = DOCS_SOURCE_DIR / "index.rst"
    title = "KPI Bluebook"
    lines = [
        title,
        "=" * len(title),
        "",
        ".. toctree:",
        "   :maxdepth: 2",
        "   :caption: Key Performance Indicators:",
        "",
    ]
    for fname in page_filenames:
        stem = os.path.splitext(os.path.basename(fname))[0]
        lines.append(f"   {stem}")
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

# ------------- Public pipeline -------------

def generate_bluebook(source_code_path: str):
    """
    Pipeline that yields progress messages consumed by the web UI:
      1) Clean docs/*.rst (except index.rst) and docs/_build
      2) Scan KPIs
      3) Render .rst pages
      4) Update index.rst
      5) Try sphinx-build (non-fatal if missing)
    """
    # 1) Remove old generated .rst files (keep index.rst if present)
    for item in DOCS_SOURCE_DIR.glob("*.rst"):
        if item.is_file() and item.name != "index.rst":
            item.unlink()
    yield "Cleaned old documentation files."

    # 2) Remove previous HTML build
    build_dir = DOCS_SOURCE_DIR / "_build"
    if build_dir.exists():
        import shutil
        shutil.rmtree(build_dir, ignore_errors=True)
        yield "Removed previous Sphinx _build directory."

    yield f"Scanning for KPIs in: {source_code_path}"
    kpis = find_kpis_in_directory(source_code_path)
    yield f"Scanner result: {len(kpis)} items"

    if not kpis:
        yield "No KPIs found in the specified directory."
        return

    # Load template
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(str(TEMPLATE_DIR)))
    try:
        template = env.get_template("kpi_template.rst.j2")
    except Exception:
        # Minimal fallback template if the file is missing
        template = env.from_string(
            "{{ kpi.name }}\n{{ '=' * (kpi.name|length) }}\n\n"
            ".. raw:: html\n\n   {{ details.formula_html|safe }}\n\n"
            ".. admonition:: Code Context\n   :class: dropdown\n\n"
            "   .. code-block:: text\n      :linenos:\n\n"
            "      {{ kpi.code_context | e }}\n"
        )

    page_files = []
    for idx, k in enumerate(kpis, start=1):
        name = k.get("name") or f"KPI {idx}"
        yield f"Processing KPI: '{name}'..."

        # AI narrative (safe fallback on error)
        try:
            details = generate_kpi_details(name, k.get("code_context", ""))
        except Exception as e:
            details = {
                "description": f"{name} description unavailable.",
                "objective": "",
                "formula_description": "",
                "used_in_kpis": "",
                "input_measure": "",
                "unit_of_measure": "",
                "reporting_source": "",
                "comments": "",
            }
            yield f"AI details generation failed for '{name}': {e}"

        # Render page
        try:
            page = create_rst_file(k, details, template)
            page_files.append(page)
            yield f"Generated documentation for '{name}'."
        except Exception as e:
            yield f"Failed to render page for '{name}': {e}"

        time.sleep(0.05)  # gentle pacing

    # Update index.rst
    try:
        update_index_rst(page_files)
        yield f"Updated index.rst with {len(page_files)} entries."
    except Exception as e:
        yield f"Failed to update index.rst: {e}"

    # Try sphinx-build; do not fail pipeline if missing
    try:
        subprocess.run(
            ["sphinx-build", "-b", "html", str(DOCS_SOURCE_DIR), str(DOCS_SOURCE_DIR / "_build")],
            check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        yield "Triggered sphinx-build (if available)."
    except Exception as e:
        yield f"sphinx-build not run: {e}"
