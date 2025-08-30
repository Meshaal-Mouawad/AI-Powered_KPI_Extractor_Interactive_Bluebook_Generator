import os
import json
import time
from typing import Dict, Any
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


import re
import ast  # ensure availability for _extract_function_block


def _infer_unit_of_measure(kpi_name: str, code_context: str, current_value: str | None) -> str:
    """
    Best-effort unit inference from KPI name and code context.
    Only overrides if current_value is missing or looks generic.
    """
    def is_generic(v: str | None) -> bool:
        if not v:
            return True
        v_low = v.strip().lower()
        return (
            v_low == "n/a"
            or "see calculation" in v_low
            or "not specified" in v_low
            or "context" in v_low
            or len(v_low) < 3
        )

    if not is_generic(current_value):
        return current_value  # keep a specific unit provided by the AI

    name = (kpi_name or "").lower()
    ctx = (code_context or "").lower()

    # 1) Explicit from name
    if "tons/day" in name or "ton/day" in name:
        return "tons/day"
    if "oee" in name or "overall equipment effectiveness" in name:
        return "%"
    if "yield" in name or "percentage" in name:
        return "%"
    if "ratio" in name:
        return "ratio (dimensionless)"
    if "mtbf" in name or "mean time between failures" in name:
        return "hours per failure"

    # 2) From code context hints
    if "tons/day" in ctx or "ton/day" in ctx:
        return "tons/day"
    if "np.var(" in ctx or "variance" in ctx:
        return "variance (units^2)"

    # Heuristic for throughput using tons and hours
    if "throughput" in name or "throughput" in ctx:
        has_tons = "ton" in ctx or "tons" in ctx
        divides_hours = "/ hours" in ctx or "/hours" in ctx or " / 24" in ctx
        times_24 = "* 24" in ctx or "*24" in ctx
        if has_tons and divides_hours and times_24:
            return "tons/day"
        if has_tons and divides_hours:
            return "tons/hour"

    # Generic presence of percentage-like calculation
    if "* 100" in ctx or "*100" in ctx:
        return "%"

    # Fall back to a safe default if nothing detected
    return current_value or "unit not specified"


def generate_formula_from_code(code_context: str) -> dict:
    """
    Analyzes the raw code to programmatically generate a perfect HTML/MathJax block.
    This is 100% reliable.
    """
    formula_data = {
        "formula_html": "<p>See code context for implementation details.</p>"
    }

    # Pick the best calculation-like assignment line (skip constants and strip inline comments).
    calculation_line = ""
    for raw in code_context.splitlines():
        line = raw.strip()
        if '=' not in line or line.startswith(('#', '"""', "'''")):
            continue

        lhs, rhs = [p.strip() for p in line.split('=', 1)]

        # Strip inline comments to avoid MathJax '#' errors
        if '#' in rhs:
            rhs = rhs.split('#', 1)[0].strip()

        # Ignore empty or trivial RHS (constants only, like "5.0")
        is_constant = bool(re.fullmatch(r"[0-9.+\-eE]+", rhs))
        # Prefer calculation-like expressions
        is_calc = (
            any(op in rhs for op in ('*', '/', '+', '-'))
            or 'len(' in rhs
            or 'np.' in rhs
            or '(' in rhs  # function call patterns
        )

        if is_calc and not is_constant:
            calculation_line = f"{lhs} = {rhs}"
            break

    # Fallback: try to find any assignment and strip inline comments (last resort)
    if not calculation_line:
        m = re.search(r'([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(.+)', code_context)
        if m:
            lhs, rhs = m.groups()
            rhs = rhs.split('#', 1)[0].strip()
            calculation_line = f"{lhs.strip()} = {rhs}"

    if not calculation_line:
        return formula_data

    result_var, expression = [p.strip() for p in calculation_line.split('=', 1)]

    def pretty_name(v: str) -> str:
        # Convert snake_case to Title Case with spaces
        v = re.sub(r'[_\s]+', ' ', v).strip().title()
        return v

    def fmt_var(v: str) -> str:
        # Handle len(x) specially
        m = re.fullmatch(r'len\((.+)\)', v.strip())
        if m:
            inner = pretty_name(m.group(1))
            return r"\mathrm{Len}\!\left(\mathrm{%s}\right)" % inner
        return r"\mathrm{%s}" % pretty_name(v)

    latex_str = ""
    notes_list = []

    # --- Logic for different formula types ---
    # (a / b) * 100
    m = re.search(r'\((.*?)\s*/\s*(.*?)\)\s*\*\s*100', expression)
    if m:
        num, den = [s.strip() for s in m.groups()]
        latex_str = r"%s = \frac{%s}{%s} \times 100" % (fmt_var(result_var), fmt_var(num), fmt_var(den))
        notes_list.append(f"<i>{pretty_name(num)}:</i> The numerator of the fraction.")
        notes_list.append(f"<i>{pretty_name(den)}:</i> The denominator of the fraction.")
    # (a / b) * c
    elif re.search(r'\((.*?)\s*/\s*(.*?)\)\s*\*\s*([0-9]+(?:\.[0-9]+)?)', expression):
        m = re.search(r'\((.*?)\s*/\s*(.*?)\)\s*\*\s*([0-9]+(?:\.[0-9]+)?)', expression)
        num, den, scalar = m.groups()
        num, den = num.strip(), den.strip()
        latex_str = r"%s = \frac{%s}{%s} \times %s" % (fmt_var(result_var), fmt_var(num), fmt_var(den), scalar)
        notes_list.append(f"<i>{pretty_name(num)}:</i> The numerator of the fraction.")
        notes_list.append(f"<i>{pretty_name(den)}:</i> The denominator of the fraction.")
    # a / b
    elif '/' in expression:
        parts = [s.strip() for s in expression.split('/')]
        if len(parts) == 2:
            latex_str = r"%s = \frac{%s}{%s}" % (fmt_var(result_var), fmt_var(parts[0]), fmt_var(parts[1]))
    # a * b * c
    elif '*' in expression:
        parts = [s.strip() for s in expression.split('*')]
        latex_str = r"%s = %s" % (fmt_var(result_var), r' \times '.join(fmt_var(p) for p in parts))
    # a - b
    elif '-' in expression and all(p.strip() for p in expression.split('-', 1)):
        parts = [s.strip() for s in expression.split('-')]
        if len(parts) == 2:
            latex_str = r"%s = %s - %s" % (fmt_var(result_var), fmt_var(parts[0]), fmt_var(parts[1]))
    # len(a) / len(b)
    elif re.search(r'len\((.*?)\)\s*/\s*len\((.*?)\)', expression):
        m = re.search(r'len\((.*?)\)\s*/\s*len\((.*?)\)', expression)
        num, den = m.groups()
        latex_str = r"%s = \frac{%s}{%s}" % (fmt_var(result_var), fmt_var(f"len({num})"), fmt_var(f"len({den})"))

    if latex_str:
        notes_html = "<ul>" + "".join(f"<li>{n}</li>" for n in notes_list) + "</ul>" if notes_list else ""
        formula_data["formula_html"] = f'<div class="math-equation">$$ {latex_str} $$</div>{notes_html}'
    else:
        formula_data["formula_html"] = "<p>See code context for implementation details.</p>"

    return formula_data


def generate_kpi_details(kpi_name: str, code_context: str) -> Dict[str, Any]:
    """Uses OpenAI's GPT model to generate plain text descriptions ONLY."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file.")

    client = OpenAI(api_key=api_key)

    prompt = f"""
    You are an expert technical writer. Based on the KPI name and code below, generate a JSON object containing plain English descriptions.
    **RULES:**
    1. Write each field as a natural language paragraph or sentence.
    2. **DO NOT use lists, bullet points, semicolons, or any special formatting.**
    3. **DO NOT generate any LaTeX or mathematical formulas.**

    **KPI Name:** "{kpi_name}"
    **Code Context:** ```python\n{code_context}\n```

    Generate a JSON object with these exact keys: "description", "objective", "formula_description", "used_in_kpis", "input_measure", "unit_of_measure", "reporting_source", "comments".
    """

    retries = 8
    delay = 8  # shorter initial delay to speed up a bit
    for i in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                temperature=0.1,
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            if i < retries - 1:
                time.sleep(delay)
                delay = min(delay * 2, 60)
            else:
                return {
                    "description": f"{kpi_name} is a key performance indicator used to assess process efficiency and operational performance.",
                    "objective": f"The objective of {kpi_name} is to provide a clear measure that supports monitoring, decision making, and continuous improvement.",
                    "formula_description": "Calculated directly from the inputs found in the code implementation.",
                    "used_in_kpis": "This KPI can serve as an input to higher-level operational and performance dashboards.",
                    "input_measure": "Derived from the variables used in the code calculation for this KPI.",
                    "unit_of_measure": "See calculation and context for the most appropriate unit.",
                    "reporting_source": "Typically sourced from process historians, production logs, or execution systems.",
                    "comments": ""
                }


def _extract_function_block(code_context: str, anchor_line_number: int):
    """
    Returns (scoped_function_block, start_index_in_original_context).

    Prefer AST-based slicing to get the exact function that contains anchor_line_number.
    Falls back to indentation-based heuristic if AST parsing fails.
    """
    lines = code_context.splitlines()
    if not lines or anchor_line_number <= 0 or anchor_line_number > len(lines):
        return code_context, 0

    # 1) AST-based extraction (robust)
    try:
        tree = ast.parse(code_context)
        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                start = node.lineno
                end = getattr(node, "end_lineno", None)
                if end is None:
                    # Compute end by walking the body (for older Python, but kept as safeguard)
                    last = node.body[-1]
                    end = getattr(last, "end_lineno", getattr(last, "lineno", start))
                if start <= anchor_line_number <= end:
                    return "\n".join(lines[start - 1:end]), start - 1
        # If not found via AST, continue to heuristic
    except Exception:
        pass

    # 2) Heuristic fallback (improved)
    anchor_idx = anchor_line_number - 1

    # Find the start of the function that contains the anchor
    start_idx = 0
    for i in range(anchor_idx, -1, -1):
        if lines[i].lstrip().startswith("def "):
            start_idx = i
            break

    def_indent = len(lines[start_idx]) - len(lines[start_idx].lstrip())

    # End at next def with same/less indent OR any non-empty line whose indent drops below def indent
    end_idx = len(lines)
    for j in range(start_idx + 1, len(lines)):
        stripped = lines[j].strip()
        indent = len(lines[j]) - len(lines[j].lstrip())
        if not stripped:
            continue
        if indent < def_indent:
            end_idx = j
            break
        if lines[j].lstrip().startswith("def ") and indent <= def_indent:
            end_idx = j
            break
        # Also stop at common top-level blocks
        if indent == 0 and (stripped.startswith("#") or stripped.startswith("if __name__")):
            end_idx = j
            break

    return "\n".join(lines[start_idx:end_idx]), start_idx