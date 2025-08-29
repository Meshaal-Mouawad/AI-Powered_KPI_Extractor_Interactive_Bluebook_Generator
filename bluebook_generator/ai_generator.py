import os
import json
import time
from typing import Dict, Any
import ast  # <-- add

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables (expects OPENAI_API_KEY in .env)
load_dotenv()


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


def generate_kpi_details(kpi_name: str, code_context: str) -> Dict[str, Any]:
    """
    Generate plain-English KPI details using the OpenAI API.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file.")

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are an expert technical writer. Based on the KPI name and code below, generate a JSON object containing plain English descriptions.

RULES:
1) Write each field as a natural language paragraph or sentence.
2) DO NOT use lists, bullet points, semicolons, or any special formatting.
3) DO NOT generate any LaTeX or mathematical formulas.
4) For "unit_of_measure", infer the most specific unit you can from the KPI name and code (e.g., "%", "tons/day", "hours per failure").

KPI Name: "{kpi_name}"
Code Context:
```
{code_context}
```

Generate a JSON object with these exact keys:
"description", "objective", "formula_description", "used_in_kpis",
"input_measure", "unit_of_measure", "reporting_source", "comments".
""".strip()

    # Robust retry with exponential backoff
    retries = 8
    delay = 8  # initial delay
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                response_format={"type": "json_object"},
                temperature=0.1,
            )
            content = response.choices[0].message.content
            details = json.loads(content)

            # Post-fix the unit of measure if the AI left it vague
            details["unit_of_measure"] = _infer_unit_of_measure(
                kpi_name, code_context, details.get("unit_of_measure")
            )
            return details

        except Exception:
            if attempt < retries - 1:
                time.sleep(delay)
                delay = min(delay * 2, 60)
                continue
            # Final fallback to ensure the docs builder never breaks
            details = {
                "description": f"{kpi_name} is a key performance indicator used to assess process efficiency and operational performance.",
                "objective": f"The objective of {kpi_name} is to provide a clear measure that supports monitoring, decision making, and continuous improvement.",
                "formula_description": "Calculated directly from the inputs found in the code implementation.",
                "used_in_kpis": "This KPI can serve as an input to higher-level operational and performance dashboards.",
                "input_measure": "Derived from the variables used in the code calculation for this KPI.",
                "unit_of_measure": "unit not specified",
                "reporting_source": "Typically sourced from process historians, production logs, or execution systems.",
                "comments": "This content was auto-filled due to a temporary generation issue. Regenerate later to replace with richer descriptions."
            }
            details["unit_of_measure"] = _infer_unit_of_measure(
                kpi_name, code_context, details.get("unit_of_measure")
            )
            return details


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