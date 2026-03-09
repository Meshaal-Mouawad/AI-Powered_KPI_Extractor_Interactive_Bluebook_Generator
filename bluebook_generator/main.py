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
        raise ImportError(
            "bluebook_generator.ai_generator.generate_kpi_details is not defined."
        )
    generate_kpi_details = getattr(_ai, "generate_kpi_details")

# Public API from this module
__all__ = ["generate_bluebook"]

ROOT_DIR = Path(__file__).parent.parent
DOCS_SOURCE_DIR = ROOT_DIR / "docs"
TEMPLATE_DIR = ROOT_DIR / "templates"


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
    items = re.split(r"[.;,]\s*", safe)
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
                    return "\n".join(lines[start - 1 : end]), start - 1
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
        if indent == 0 and (
            stripped.startswith("#") or stripped.startswith("if __name__")
        ):
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

    # Helpers (keep your latest versions; shown trimmed here)
    def latex_escape(s: str) -> str:
        repl = [
            ("\\", r"\\"),
            ("{", r"\{"),
            ("}", r"\}"),
            ("#", r"\#"),
            ("$", r"\$"),
            ("%", r"\%"),
            ("&", r"\&"),
            ("_", r"\_"),
            ("^", r"\^"),
            ("~", r"\~"),
        ]
        out = s
        for a, b in repl:
            out = out.replace(a, b)
        return out

    def sanitize_token(t: str) -> str:
        t = t.strip()
        t = re.sub(r"^[{}\[\]();,\s]+|[{}\[\]();,\s]+$", "", t)
        t = re.sub(r"[:\.]+", " ", t)
        t = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", t)
        t = t.replace("_", " ")
        t = re.sub(r"(?i)(maintenance)to(operating)", r"\1 to \2", t)
        t = re.sub(r"(?i)(cost)ratio", r"\1 ratio", t)
        t = re.sub(r"(?i)(feedstock)throughput", r"\1 throughput", t)
        t = re.sub(r"(?i)(error)rate", r"\1 rate", t)
        t = re.sub(r"(?i)(extraction)rate", r"\1 rate", t)
        t = re.sub(r"\s+", " ", t).strip()
        t = latex_escape(t)
        return t.title()

    def L(v: str) -> str:
        return r"\mathit{{{}}}".format(v)

    def strip_inline_comments(line: str) -> str:
        cleaned = line  # Rename from 'l' to 'cleaned'
        cleaned = re.split(r"--", cleaned, maxsplit=1)[0]
        cleaned = re.split(r"//", cleaned, maxsplit=1)[0]
        cleaned = re.split(r"\(\*", cleaned, maxsplit=1)[0]
        cleaned = re.split(r"(?<!:)\s'", cleaned, maxsplit=1)[0]
        cleaned = re.split(r"#", cleaned, maxsplit=1)[0]
        return cleaned.rstrip(" ;\t")

    def unwrap_sql_expr(expr: str) -> str:
        e = expr.strip()
        # Use a consistent group name 'inner' and access the same
        m = re.search(r"(?is)\bCAST\s*\(\s*(?P<inner>.+?)\s+AS\s+[^\)]+\)", e)
        if m:
            e = m.group("inner").strip()
        m = re.search(r"(?is)\bCOALESCE\s*\(\s*(?P<inner>.+?)\s*,\s*.+?\)", e)
        if m:
            e = m.group("inner").strip()
        e = re.sub(r"(?is)\bNULLIF\s*\(\s*(.+?)\s*,\s*.+?\)", r"\1", e)
        e = re.sub(r"[;{}]+$", "", e).strip()
        e = e.strip()
        if e.startswith("(") and e.endswith(")"):
            e = e[1:-1].strip()
        return e

    def split_top_level_division(expr: str) -> tuple[str, str] | None:
        depth = 0
        for idx, ch in enumerate(expr):
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth = max(depth - 1, 0)
            elif ch == "/" and depth == 0:
                lhs = expr[:idx].strip()
                rhs = expr[idx + 1 :].strip()
                if lhs and rhs:
                    return lhs, rhs
        return None

    def infer_oil_gas_definition(term: str) -> str:
        raw = term.lower().replace("_", " ")
        if "total" in raw and "gas" in raw:
            return "Total gas handled in the reporting period (feed, flare, or processed volume as applicable)."
        if "recovered" in raw and "gas" in raw:
            return "Recovered gas volume captured for reuse instead of flaring or venting."
        if "mass flow" in raw or "massflow" in raw:
            return "Measured mass flow rate from process instrumentation during the reporting period."
        if "vol flow" in raw or "volflow" in raw or "volume flow" in raw:
            return "Measured volumetric flow rate used to normalize concentration or yield calculations."
        if raw.strip() == "total":
            return "Total measured quantity for the KPI scope during the reporting period."
        if "operating" in raw and "cost" in raw:
            return "Total operating expenditure for the unit/asset in the reporting period."
        if "maintenance" in raw and "cost" in raw:
            return "Total maintenance expenditure (planned + unplanned) for the reporting period."
        if "throughput" in raw:
            return "Total processed feedstock or product volume through the unit over the reporting period."
        if "emissions" in raw or "sox" in raw:
            return "SOx concentration or emission reading measured from analyzer or stack monitoring data."
        return f"Measured value for {sanitize_token(term)} in the KPI calculation context."

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

    def build_html(
        result_var: str, expression: str, notes: list[str] | None = None
    ) -> dict:
        rv = sanitize_token(result_var)
        expr = unwrap_sql_expr(expression.strip().rstrip(";"))
        notes = notes or []
        latex_str = ""

        symbol_pool = ["X", "Y", "Z", "A", "B", "C", "D"]

        def symbolic_terms(terms: list[str]) -> tuple[list[str], list[str]]:
            mapped: list[str] = []
            defs: list[str] = []
            for i, term in enumerate(terms):
                clean_term = sanitize_token(term)
                if not clean_term:
                    continue
                sym = symbol_pool[i] if i < len(symbol_pool) else f"V{i+1}"
                mapped.append(sym)
                defs.append(f"<i>{sym}:</i> {infer_oil_gas_definition(clean_term)}")
            return mapped, defs

        # (a/b)*100 or 100*(a/b)
        m = re.search(r"\((.*?)\s*/\s*(.*?)\)\s*\*\s*100", expr)
        if m:
            syms, defs = symbolic_terms([m.group(1), m.group(2)])
            if len(syms) == 2:
                latex_str = r"{} = \frac{{{}}}{{{}}} \times 100".format(
                    L(rv), L(syms[0]), L(syms[1])
                )
                notes += defs
        elif re.search(r"100\s*\*\s*\((.*?)\s*/\s*(.*?)\)", expr):
            m = re.search(r"100\s*\*\s*\((.*?)\s*/\s*(.*?)\)", expr)
            syms, defs = symbolic_terms([m.group(1), m.group(2)])
            if len(syms) == 2:
                latex_str = r"{} = 100 \times \frac{{{}}}{{{}}}".format(
                    L(rv), L(syms[0]), L(syms[1])
                )
                notes += defs
        # a / b
        elif "/" in expr and not re.search(r"//", expr):
            div_parts = split_top_level_division(expr) or tuple(
                p.strip() for p in expr.split("/", 1)
            )
            if len(div_parts) == 2 and div_parts[0] and div_parts[1]:
                syms, defs = symbolic_terms([div_parts[0], div_parts[1]])
                if len(syms) == 2:
                    latex_str = r"{} = \frac{{{}}}{{{}}}".format(
                        L(rv), L(syms[0]), L(syms[1])
                    )
                    notes += defs
        # product
        elif "*" in expr:
            parts = [p for p in re.split(r"\*", expr) if p.strip()]
            syms, defs = symbolic_terms(parts)
            if len(syms) >= 2:
                latex_str = r"{} = {}".format(
                    L(rv), r" \times ".join([L(p) for p in syms])
                )
                notes += defs
        # subtraction / addition
        elif "-" in expr:
            parts = [p.strip() for p in expr.split("-", 1)]
            syms, defs = symbolic_terms(parts)
            if len(syms) == 2:
                latex_str = r"{} = {} - {}".format(L(rv), L(syms[0]), L(syms[1]))
                notes += defs
        elif "+" in expr:
            parts = [p.strip() for p in expr.split("+", 1)]
            syms, defs = symbolic_terms(parts)
            if len(syms) == 2:
                latex_str = r"{} = {} + {}".format(L(rv), L(syms[0]), L(syms[1]))
                notes += defs

        if latex_str:
            notes_html = (
                "<p><b>Where:</b></p><ul>" + "".join(f"<li>{n}</li>" for n in notes) + "</ul>"
                if notes
                else ""
            )
            return {
                "formula_html": f'<div class="math-equation">$$ {latex_str} $$</div>{notes_html}'
            }
        return {"formula_html": "<p>See code context for implementation details.</p>"}

    # 1) DAX multi-line
    m = re.search(
        r"(?is)\bDEFINE\s+MEASURE\s+[^\[]*\[(?P<name>[^\]]+)\]\s*=\s*(?P<body>.+?)(?:$|\n\s*\n)",
        ctx,
    )
    if m:
        name = gd(m, "name")
        body = gd(m, "body")
        if name and body:
            m_ret = re.search(r"(?is)\bRETURN\b\s*(?P<expr>.+)", body)
            expr = gd(m_ret, "expr", body)
            return build_html(name, expr)

    # 1b) DAX simple
    m = re.search(
        r"(?is)^(?P<name>[A-Za-z0-9 _\[\]\.%]+?)\s*=\s*(?P<expr>.+?)(?:$|\n\s*\n)",
        ctx,
        flags=re.M,
    )
    if m:
        name = gd(m, "name")
        expr = gd(m, "expr")
        if (
            name
            and expr
            and not re.match(r"\s*(VAR|RETURN|EVALUATE)\b", name, flags=re.I)
        ):
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
                expr = gd(last, "expr")
                if alias and expr:
                    alias = re.sub(r'^[\[\("\']|[\]\)"\']$', "", alias)
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
        expr = gd(last, "expr")
        if alias and expr:
            alias = re.sub(r'^[\[\("\']|[\]\)"\']$', "", alias)
            # Prefer percent-style sub-expr if present
            m_pct = re.search(
                r"(?is)100\s*\*\s*\((.+?/.+?)\)|\((.+?/.+?)\)\s*\*\s*100", expr
            )
            if m_pct:
                expr = (m_pct.group(1) or m_pct.group(2)).strip()
            else:
                # Prefer last division inside expr
                divs = list(
                    re.finditer(
                        r"(?is)([A-Za-z0-9_().\s]+)\s*/\s*([A-Za-z0-9_().\s]+)", expr
                    )
                )
                if divs:
                    a, b = divs[-1].groups()
                    expr = f"{a.strip()} / {b.strip()}"
            return build_html(alias, expr)

    # 2c) Strong T‑SQL percent fallback (covers CAST/NULLIF with or without AS match)
    m_tsql_pct = re.search(
        r"(?is)100\s*\*\s*\(([^)]+?/[^)]+?)\)|\(([^)]+?/[^)]+?)\)\s*\*\s*100", ctx
    )
    if m_tsql_pct:
        expr_inner = (m_tsql_pct.group(1) or m_tsql_pct.group(2) or "").strip()
        if expr_inner:
            m_alias_near = re.search(
                r"(?is)\bAS\s+(\[[^\]]+\]|\"[^\"]+\"|'[^']+'|[A-Za-z_][A-Za-z0-9_]*)",
                ctx,
            )
            result_name = "Result"
            if m_alias_near:
                alias = m_alias_near.group(1)
                result_name = (
                    re.sub(r'^[\[\("\']|[\]\)"\']$', "", alias).strip() or result_name
                )
            return build_html(result_name, expr_inner)

    # 2d) CAST(...) AS <alias> direct fallback (extract inner first arg of CAST)
    m_cast_as = re.search(
        r'(?is)CAST\s*\(\s*(?P<inner>.+?)\s+AS\s+[^\)]+\)\s+AS\s+(?P<alias>\[[^\]]+\]|"[^"]+"|\'[^\']+\'|[A-Za-z_][A-Za-z0-9_]*)',
        ctx,
    )
    if m_cast_as:
        alias = re.sub(r'^[\[\("\']|[\]\)"\']$', "", m_cast_as.group("alias")).strip()
        expr = unwrap_sql_expr(m_cast_as.group("inner"))
        if alias and expr:
            return build_html(alias, expr)

    # 2e) JSON/HANA-style column expression fallback
    m_json_expr = re.search(
        r'(?is)"name"\s*:\s*"(?P<name>[^"]+)".*?"expression"\s*:\s*"(?P<expr>[^"]+)"',
        ctx,
    )
    if m_json_expr:
        name = gd(m_json_expr, "name")
        expr = gd(m_json_expr, "expr")
        if name and expr:
            return build_html(name, expr)

    # 3) return <expr>;
    return_matches = list(re.finditer(r"(?im)\breturn\b\s+(?P<expr>[^;\r\n]+)", ctx))
    if return_matches:
        for m in reversed(return_matches):
            expr = gd(m, "expr").strip()
            if any(op in expr for op in ("*", "/", "+", "-")):
                return build_html("Result", expr)

    # 3b) VB Return: handle at line start with optional indent (e.g., "Return operatingHours / numberOfFailures")
    m_vb_return = re.search(r"(?im)^\s*return\s+(?P<expr>[^\r\n]+)$", ctx)
    if m_vb_return:
        expr = m_vb_return.group("expr").strip()
        if expr:
            return build_html("Result", expr)

    # 4) assignment with =
    for line in ctx.splitlines():
        cleaned = strip_inline_comments(line.strip())
        if not cleaned or cleaned.startswith(("#", "--", "//", "/*", "*", "'")):
            continue
        if ":=" in cleaned:  # FIXED
            continue
        if "=" in cleaned and not re.search(  # FIXED
            r"(?i)\b(create|def|function|procedure|view)\b",
            cleaned,  # FIXED
        ):
            lhs_rhs = cleaned.split("=", 1)  # FIXED
            if len(lhs_rhs) == 2:
                lhs, rhs = [p.strip() for p in lhs_rhs]
                if any(op in rhs for op in ("*", "/", "+", "-")):
                    return build_html(lhs, rhs)

    # 4b) Python/any-language assignment with math on the same line (take last match)
    assigns = list(
        re.finditer(r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<expr>.+)$", ctx)
    )
    if assigns:
        for mm in reversed(assigns):
            expr = mm.group("expr").strip()
            if any(op in expr for op in ("*", "/", "+", "-")):
                lhs = mm.group(1)
                return build_html(lhs, expr)

    # 4c) ABAP assignment ending with period (e.g., lv_rate = (...) * 100.)
    m_abap = re.search(
        r"(?im)^\s*([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<expr>.+?)\.\s*$", ctx
    )
    if m_abap:
        lhs = m_abap.group(1)
        expr = m_abap.group("expr").strip()
        if any(op in expr for op in ("*", "/", "+", "-")):
            return build_html(lhs, expr)

    # 5) IEC ST assignment :=
    for line in ctx.splitlines():
        cleaned = strip_inline_comments(line.strip())  # Rename from 'l' to 'cleaned'
        if ":=" in cleaned:
            lhs_rhs = cleaned.split(":=", 1)
            if len(lhs_rhs) == 2:
                lhs, rhs = [p.strip() for p in lhs_rhs]
                if any(op in rhs for op in ("*", "/", "+", "-")):
                    return build_html(lhs, rhs)

    # 5b) Domain fallback: SOx concentration snippets with variable declarations
    if re.search(r"(?i)sox\s*conc|soxconc", ctx) and re.search(r"(?i)sox\s*mass\s*flow|soxmassflow", ctx) and re.search(r"(?i)vol\s*flow|volflow", ctx):
        return build_html("soxConc", "soxMassFlow / volFlow")

    # 6) NEW: last-resort generic sweep — pick the last math-like line
    #    Works for VB/Python/C-like/SQL-ish snippets when earlier patterns miss.
    candidate = None
    result_name = "Result"

    # Prefer percent-style expressions first
    pct = list(
        re.finditer(r"(?is)100\s*\*\s*\((.+?/.+?)\)|\((.+?/.+?)\)\s*\*\s*100", ctx)
    )
    if pct:
        grp = pct[-1].groups()
        expr = (grp[0] or grp[1] or "").strip()
        if expr:
            candidate = expr

    # Next prefer divisions a / b
    if not candidate:
        divs = list(
            re.finditer(r"(?is)([A-Za-z0-9_().\s]+)\s*/\s*([A-Za-z0-9_().\s]+)", ctx)
        )
        if divs:
            a, b = divs[-1].groups()
            candidate = f"{a.strip()} / {b.strip()}"

    # If we found a math expression, try to extract a nearby result name
    if candidate:
        # Try to use an alias or LHS nearby as the result variable
        #  - alias: "... AS some_name"
        m_alias = re.search(
            r"(?is)\bAS\s+(\[[^\]]+\]|\"[^\"]+\"|'[^']+'|[A-Za-z_][A-Za-z0-9_]*)", ctx
        )
        if m_alias:
            alias = m_alias.group(1)
            result_name = (
                re.sub(r'^[\[\("\']|[\]\)"\']$', "", alias).strip() or result_name
            )
        else:
            # Look for a nearby assignment LHS like "name = ...", "name := ..."
            m_lhs = re.search(
                r"(?is)^\s*([A-Za-z_][A-Za-z0-9_\.]*)\s*[:=]=?\s*.*$", ctx, flags=re.M
            )
            if m_lhs:
                result_name = m_lhs.group(1)

        return build_html(result_name, candidate)

    return formula_data


# add `ai_time_seconds` param
def create_rst_file(
    kpi_data: dict,
    details: dict,
    template: jinja2.Template,
    ai_time_seconds: float | None = None,
):
    """Generates and saves a .rst file for a single KPI (all languages)."""
    from html import escape
    import os
    import time  # NEW

    render_start = time.perf_counter()  # NEW: start render timing

    # 1) Find the KPI marker line within the provided code context (for line highlighting)
    kpi_line_in_context = 0
    context_lines = (kpi_data.get("code_context") or "").split("\n")
    kpi_name = kpi_data.get("name") or ""
    for i, line in enumerate(context_lines):
        if (
            f"# KPI: {kpi_name}" in line
            or f"-- KPI: {kpi_name}" in line
            or f"' KPI: {kpi_name}" in line
            or f"/* KPI: {kpi_name}" in line
        ):
            kpi_line_in_context = i + 1
            break
    kpi_data["context_line_number"] = kpi_line_in_context

    # 2) Determine file extension and possibly scope Python to function block
    file_path = kpi_data.get("file_path") or ""
    _, ext = os.path.splitext(str(file_path).lower())

    if ext == ".py":
        # Scope to the function that contains the KPI marker for cleaner context
        scoped_context, start_idx = _extract_function_block(
            kpi_data.get("code_context", ""), kpi_line_in_context
        )
        kpi_data["code_context"] = scoped_context
        # Recompute relative line number inside the scoped block
        if kpi_line_in_context > 0:
            rel = kpi_line_in_context - start_idx
            kpi_data["context_line_number"] = rel if rel > 0 else 0
        else:
            kpi_data["context_line_number"] = 0
        programmatic_formula = generate_formula_from_code(scoped_context)
    else:
        # Keep full context for SQL-like/ABAP/etc.
        programmatic_formula = generate_formula_from_code(
            kpi_data.get("code_context", "")
        )

    # 3) Build final_details consistently for all languages
    final_details = {
        "description_html": format_text_as_html_list(details.get("description", "")),
        "objective_html": format_text_as_html_list(details.get("objective", "")),
        "formula_description": escape(details.get("formula_description", "") or ""),
        "used_in_kpis_html": format_text_as_html_list(details.get("used_in_kpis", "")),
        "input_measure_html": format_text_as_html_list(
            details.get("input_measure", "")
        ),
        "unit_of_measure": escape(details.get("unit_of_measure", "") or ""),
        "reporting_source": escape(details.get("reporting_source", "") or ""),
        "comments": escape(details.get("comments", "") or ""),
        **(programmatic_formula or {}),
    }

    # --- Compute extraction/error rates ---
    # Fields we expect from AI text generation
    fields_to_check = [
        "description_html",
        "objective_html",
        "formula_description",
        "used_in_kpis_html",
        "input_measure_html",
        "unit_of_measure",
        "reporting_source",
        "comments",
    ]

    # Helper: consider a field populated if it has a non-trivial value after stripping
    import re as _re

    def _non_empty(val: str | None) -> bool:
        if not isinstance(val, str):
            return False
        s = val.strip()
        if len(s) <= 2:
            return False
        return not _re.fullmatch(r"[\s\W_]*", s)

    filled = sum(1 for k in fields_to_check if _non_empty(final_details.get(k)))

    # Formula counts as filled only if we didn’t fall back to the generic placeholder
    formula_html = final_details.get("formula_html") or ""
    formula_is_specific = bool(formula_html) and (
        "See code context" not in formula_html
    )
    filled_total = filled + (1 if formula_is_specific else 0)
    possible_total = len(fields_to_check) + 1  # +1 for formula

    extraction_rate_pct = round(100.0 * filled_total / possible_total, 1)
    error_rate_pct = round(100.0 - extraction_rate_pct, 1)

    final_details["extraction_rate_pct"] = extraction_rate_pct
    final_details["error_rate_pct"] = error_rate_pct
    # --- end metrics ---

    # NEW: attach timing metrics
    def _fmt_seconds(s: float) -> str:
        s = max(0.0, float(s))
        if s < 60:
            return f"{s:.1f}s"
        m = int(s // 60)
        r = int(round(s - m * 60))
        return f"{m}m {r}s"

    render_time_seconds = time.perf_counter() - render_start
    total_kpi_time_seconds = (ai_time_seconds or 0.0) + render_time_seconds

    final_details["ai_time_seconds"] = round(ai_time_seconds or 0.0, 3)
    final_details["render_time_seconds"] = round(render_time_seconds, 3)
    final_details["total_kpi_time_seconds"] = round(total_kpi_time_seconds, 3)
    final_details["generation_time_display"] = (
        f"{_fmt_seconds(total_kpi_time_seconds)} "
        f"(AI {_fmt_seconds(ai_time_seconds or 0.0)} + Render {_fmt_seconds(render_time_seconds)})"
    )
    # If an explicit LaTeX formula was provided in kpi_data, prefer it
    explicit_formula = kpi_data.get("formula")
    if explicit_formula:
        final_details["formula_html"] = (
            f'<div class="math-equation">$$ {explicit_formula} $$</div>'
        )

    # 4) Compute safe filename and write the .rst file
    safe_name = "".join(
        c for c in (kpi_name or "") if c.isalnum() or c in (" ", "_")
    ).rstrip()
    filename = (safe_name.replace(" ", "_").lower() or "kpi") + ".rst"
    output_path = DOCS_SOURCE_DIR / filename

    content = template.render(kpi=kpi_data, details=final_details)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    return filename

    # ------------- Minimal index.rst writer -------------


def update_index_rst(page_filenames):
    """
    Write docs/index.rst with a toctree listing for the generated KPI pages.
    Defensive against None or non-string entries.
    Additionally, always include a :glob: wildcard to ensure the index lists
    all .rst pages even if explicit names drift or are missing.
    """
    index_path = DOCS_SOURCE_DIR / "index.rst"
    title = "KPI Bluebook"
    lines = [
        title,
        "=" * len(title),
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "   :caption: Key Performance Indicators:",
        "   :glob:",
        "",
    ]
    # Add explicit filenames when provided
    for fname in page_filenames or []:
        if not fname:
            continue
        try:
            base = os.path.basename(str(fname))
            stem = os.path.splitext(base)[0]
            if stem:
                lines.append(f"   {stem}")
        except Exception:
            continue
    # Always include wildcard to pick up any generated pages
    lines.append("   *")

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
    run_start = time.perf_counter()  # measure total wall time

    # 1) Remove old generated .rst files (keep index.rst if present)
    for item in DOCS_SOURCE_DIR.glob("*.rst"):
        if item.is_file() and item.name != "index.rst":
            item.unlink()
    yield "Cleaned old documentation files."

    # 2) Optionally remove previous HTML build (clean build on demand)
    build_dir = DOCS_SOURCE_DIR / "_build"
    if os.environ.get("CLEAN_BUILD") and build_dir.exists():
        import shutil

        shutil.rmtree(build_dir, ignore_errors=True)
        yield "Removed previous Sphinx _build directory (CLEAN_BUILD set)."

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

    # Phase A: run AI generation in parallel
    from concurrent.futures import ThreadPoolExecutor, as_completed

    def _trim_context(kpi: dict, max_lines: int = 120, around: int = 60) -> str:
        ctx = kpi.get("code_context", "")
        line_no = int(kpi.get("file_line") or 0)
        lines = ctx.splitlines()
        if not lines:
            return ctx
        if 1 <= line_no <= len(lines):
            start = max(0, line_no - around - 1)
            end = min(len(lines), line_no + around)
            return "\n".join(lines[start:end])
        # fallback: cap total lines
        return "\n".join(lines[:max_lines])

    def _ai_task(k):
        name = k.get("name") or "KPI"
        t0 = time.perf_counter()
        try:
            trimmed = _trim_context(k)
            if len(trimmed) > 6000:
                trimmed = trimmed[:3000] + "\n...\n" + trimmed[-3000:]
            details = generate_kpi_details(name, trimmed)
            ai_time = time.perf_counter() - t0
            return (k, details, ai_time, None)
        except Exception as e:
            fallback = {
                "description": f"{name} description unavailable.",
                "objective": "",
                "formula_description": "",
                "used_in_kpis": "",
                "input_measure": "",
                "unit_of_measure": "",
                "reporting_source": "",
                "comments": "",
            }
            return (k, fallback, 0.0, e)

    max_workers = int(os.environ.get("KPI_AI_WORKERS", "4"))
    results = []  # (k, details, ai_time)

    yield f"AI phase: processing {len(kpis)} KPIs with {max_workers} workers..."
    ai_phase_start = time.perf_counter()
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        future_map = {ex.submit(_ai_task, k): k for k in kpis}
        for fut in as_completed(future_map):
            k, details, ai_time, err = fut.result()
            name = k.get("name") or "KPI"
            if err:
                yield f"AI details generation failed for '{name}': {err}"
            else:
                yield f"AI ready for '{name}' (AI {ai_time:.2f}s)."
            results.append((k, details, ai_time))
    ai_wall = time.perf_counter() - ai_phase_start

    # Phase B: render & collect filenames
    page_files = []
    for k, details, ai_time in results:
        name = k.get("name") or "KPI"
        try:
            page = create_rst_file(k, details, template, ai_time_seconds=ai_time)
            page_files.append(page)
            yield f"Rendered '{name}'."
        except Exception as e:
            yield f"Failed to render page for '{name}': {e}"

    # Brief timing summary — distinguish wall time from summed model latency
    if results:
        total_ai = sum(ai for _, _, ai in results)
        avg_ai = total_ai / len(results)
        avg_wall_per_kpi = ai_wall / len(results)
        yield (
            f"AI phase wall time: {ai_wall:.2f}s for {len(results)} KPIs with {max_workers} workers."
        )
        yield (
            f"Model latency (sum across KPIs): {total_ai:.2f}s; avg per KPI latency: {avg_ai:.2f}s; "
            f"avg wall time per KPI (wall/num): {avg_wall_per_kpi:.2f}s"
        )

    # Update index.rst
    try:
        update_index_rst(page_files)
        yield f"Updated index.rst with {len(page_files)} entries."
    except Exception as e:
        yield f"Failed to update index.rst: {e}"

    # Run Sphinx (parallel), optional skip via env var
    try:
        if os.environ.get("SKIP_SPHINX"):
            yield "Skipped sphinx-build (SKIP_SPHINX set)."
        else:
            jobs = os.environ.get("SPHINX_JOBS", "auto")
            cp = subprocess.run(
                [
                    "sphinx-build",
                    "-j",
                    jobs,
                    "-b",
                    "html",
                    str(DOCS_SOURCE_DIR),
                    str(DOCS_SOURCE_DIR / "_build"),
                ],
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if cp.returncode == 0:
                yield "Sphinx build successful."
            else:
                err = (cp.stderr or b"").decode("utf-8", errors="ignore")
                yield f"Sphinx build finished with code {cp.returncode}.\n{err[:500]}"
    except Exception as e:
        yield f"sphinx-build not run: {e}"

    # Final total wall time
    total_wall = time.perf_counter() - run_start
    yield f"Total wall time: {total_wall:.2f}s"
