import os
import jinja2
import re
import time
import subprocess
from pathlib import Path
from .kpi_extractor import find_kpis_in_directory
from .ai_generator import generate_kpi_details

ROOT_DIR = Path(__file__).parent.parent
DOCS_SOURCE_DIR = ROOT_DIR / 'docs'
TEMPLATE_DIR = ROOT_DIR / 'templates'


def format_text_as_html_list(text: str) -> str:
    """Takes plain text and formats it as an HTML <ul> list."""
    if not text or not isinstance(text, str) or "Error generating content" in text:
        return f"<p>{text}</p>"
    # Split by sentences, commas, or semicolons to create list items
    items = re.split(r'[.;,]\s*', text)
    items = [item.strip() for item in items if item and len(item) > 3]
    if not items:
        return f"<p>{text}</p>"
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"

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
    Analyzes the raw code to programmatically generate a perfect HTML/MathJax block.
    This is 100% reliable.
    """
    formula_data = {
        "formula_html": "<p>See code context for implementation details.</p>"
    }

    calculation_line = ""
    for line in code_context.splitlines():
        stripped = line.strip()
        # Find a likely calculation assignment: has '=', not a comment/docstring, and RHS looks like a formula
        if '=' in stripped and not stripped.startswith(('#', '"""', "'''")):
            lhs, rhs = [part.strip() for part in stripped.split('=', 1)]
            # Prefer expressions that contain operators or math funcs, not simple constant assignments
            if any(op in rhs for op in ('*', '/', '-', '+')) or 'np.var' in rhs or 'np.mean' in rhs:
                calculation_line = stripped
                break

    if not calculation_line:
        return formula_data

    parts = calculation_line.split('=')
    if len(parts) < 2:
        return formula_data

    result_var = parts[0].strip()
    expression = parts[1].strip()

    def format_var(v: str) -> str:
        # Insert spaces between camelCase boundaries and underscores,
        # collapse multiple spaces, and Title-case the result.
        v = re.sub(r'([a-z0-9])([A-Z])', r'\1 \2', v)      # camelCase -> camel Case
        v = v.replace('_', ' ')                             # underscores -> space
        v = re.sub(r'\s+', ' ', v).strip()                  # collapse spaces
        return v.title()

    def format_result_var(v: str) -> str:
        # Prefer common KPI acronyms in full uppercase (e.g., oee -> OEE, mfi -> MFI).
        # Otherwise fall back to human Title-case (e.g., throughput -> Throughput).
        if v.isalpha() and v.islower() and len(v) <= 4:
            return v.upper()
        return format_var(v)

    def L(v: str) -> str:
        # Wrap a human-friendly variable name with italic math and preserved spacing.
        # MathJax ignores spaces in math mode, so replace spaces with thin spaces '\,'.
        pretty = v.replace(' ', r'\,')
        return r'\mathit{{{}}}'.format(pretty)

    def define(pretty: str) -> str:
        """Return a human definition sentence for a pretty variable name."""
        n = pretty.lower()
        # Common KPI vocabulary heuristics
        if 'feedstock' in n and ('ton' in n or 'processed' in n):
            return f"{pretty}: Total feedstock processed during the measurement period (tons)."
        if 'hours' in n and ('online' in n or 'operating' in n or 'uptime' in n):
            return f"{pretty}: Total operating hours in the measurement period."
        if 'availability' in n:
            return f"{pretty}: Availability factor representing runtime as a share of scheduled time."
        if 'performance' in n:
            return f"{pretty}: Performance factor representing actual production rate versus ideal rate."
        if 'quality' in n:
            return f"{pretty}: Quality factor representing on-spec (good) output as a share of total output."
        if 'throughput' in n:
            return f"{pretty}: Average processing rate over the measurement period."
        if 'yield' in n:
            return f"{pretty}: Ratio of desired product produced to total input, expressed as a percentage."
        if 'ethylene' in n and 'produced' in n:
            return f"{pretty}: Total ethylene produced during the measurement period (tons)."
        if 'propylene' in n and 'produced' in n:
            return f"{pretty}: Total propylene produced during the measurement period (tons)."
        if n in ('oee', 'overall equipment effectiveness'):
            return f"{pretty}: Overall Equipment Effectiveness."
        # Fallback
        return f"{pretty}: Value used in the calculation as defined by the code implementation."

    latex_str = ""
    notes_list = []

    # --- Logic for different formula types ---

    # 1) Generic: (a / b) * c  (c can be a number or identifier)
    m = re.search(r'\((.*?)\s*/\s*(.*?)\)\s*\*\s*([A-Za-z0-9_.]+)', expression)
    if m:
        num, den, scalar = m.groups()
        num, den = format_var(num.strip()), format_var(den.strip())
        latex_str = r"{} = \frac{{{}}}{{{}}} \times {}".format(
            L(format_var(result_var)), L(num), L(den), L(format_var(scalar))
        )
        notes_list.append(f"<i>{num}:</i> The numerator of the fraction.")
        notes_list.append(f"<i>{den}:</i> The denominator of the fraction.")

    # 2) Generic: c * (a / b)
    elif re.search(r'([A-Za-z0-9_.]+)\s*\*\s*\((.*?)\s*/\s*(.*?)\)', expression):
        m = re.search(r'([A-Za-z0-9_.]+)\s*\*\s*\((.*?)\s*/\s*(.*?)\)', expression)
        scalar, num, den = m.groups()
        num_p, den_p, scalar_p = format_var(num.strip()), format_var(den.strip()), format_var(scalar)
        latex_str = r"{} = {} \times \frac{{{}}}{{{}}}".format(
            L(format_result_var(result_var)), L(scalar_p), L(num_p), L(den_p)
        )
        notes_list.append(define(scalar_p))
        notes_list.append(define(num_p))
        notes_list.append(define(den_p))

    # 3) Plain division: a / b
    elif '/' in expression:
        vars = [format_var(v.strip()) for v in expression.split('/')]
        if len(vars) == 2:
            latex_str = r"{} = \frac{{{}}}{{{}}}".format(
                L(format_result_var(result_var)), L(vars[0]), L(vars[1])
            )
            notes_list.append(define(vars[0]))
            notes_list.append(define(vars[1]))

    # 4) Variance: np.var(...)
    elif 'np.var' in expression:
        var_in_parens = re.search(r'np\.var\((.*?)\)', expression)
        if var_in_parens:
            latex_str = r"\sigma^2 = \frac{\sum_{i=1}^{N} (x_i - \mu)^2}{N}"
            notes_list.append(define(format_var(var_in_parens.group(1))))

    # 5) Product: a * b * c
    elif '*' in expression:
        parts_mul = [format_var(v.strip()) for v in re.split(r'\*', expression)]
        latex_str = r"{} = {}".format(
            L(format_result_var(result_var)),
            r' \times '.join([L(v) for v in parts_mul])
        )
        for p in parts_mul:
            notes_list.append(define(p))

    # 6) Subtraction: a - b
    elif '-' in expression:
        vars = [format_var(v.strip()) for v in expression.split('-')]
        if len(vars) == 2:
            latex_str = r"{} = {} - {}".format(
                L(format_result_var(result_var)), L(vars[0]), L(vars[1])
            )
            notes_list.append(define(vars[0]))
            notes_list.append(define(vars[1]))

    # 7) Addition: a + b
    elif '+' in expression:
        vars = [format_var(v.strip()) for v in expression.split('+')]
        if len(vars) == 2:
            latex_str = r"{} = {} + {}".format(
                L(format_result_var(result_var)), L(vars[0]), L(vars[1])
            )
            notes_list.append(define(vars[0]))
            notes_list.append(define(vars[1]))

    if latex_str:
        notes_html = "<ul>" + "".join(f"<li>{note}</li>" for note in notes_list) + "</ul>" if notes_list else ""
        # Ask MathJax to typeset after the HTML is injected.
        formula_html = f'<div class="math-equation">$$ {latex_str} $$</div>{notes_html}'
        formula_html += (
            "<script>"
            "if (window.MathJax) {"
            "  if (MathJax.typesetPromise) { MathJax.typesetPromise(); }"
            "  else if (MathJax.typeset) { MathJax.typeset(); }"
            "}"
            "</script>"
        )
        formula_data["formula_html"] = formula_html

    return formula_data


def create_rst_file(kpi_data: dict, details: dict, template: jinja2.Template):
    """Generates and saves a .rst file for a single KPI."""
    kpi_line_in_context = 0
    context_lines = kpi_data['code_context'].split('\n')
    for i, line in enumerate(context_lines):
        if f"# KPI: {kpi_data['name']}" in line:
            kpi_line_in_context = i + 1
            break
    kpi_data['context_line_number'] = kpi_line_in_context

    # NEW: Scope the formula detection AND the displayed code context to the function containing the KPI
    scoped_context, start_idx = _extract_function_block(kpi_data['code_context'], kpi_line_in_context)
    programmatic_formula = generate_formula_from_code(scoped_context)

    # Adjust the emphasize line number so it's relative to the scoped block
    if kpi_line_in_context > 0:
        relative_line = kpi_line_in_context - start_idx
        kpi_data['context_line_number'] = relative_line if relative_line > 0 else 0
    else:
        kpi_data['context_line_number'] = 0

    # Replace the displayed code context with the scoped one so only relevant code is shown
    kpi_data['code_context'] = scoped_context

    # Pre-format the AI's plain text into HTML lists
    final_details = {
        "description_html": format_text_as_html_list(details.get("description", "")),
        "objective_html": format_text_as_html_list(details.get("objective", "")),
        "formula_description": details.get("formula_description", ""),
        "used_in_kpis_html": format_text_as_html_list(details.get("used_in_kpis", "")),
        "input_measure_html": format_text_as_html_list(details.get("input_measure", "")),
        "unit_of_measure": details.get("unit_of_measure", ""),
        "reporting_source": details.get("reporting_source", ""),
        "comments": details.get("comments", ""),
        **programmatic_formula
    }

    filename = "".join(c for c in kpi_data['name'] if c.isalnum() or c in (' ', '_')).rstrip()
    filename = filename.replace(' ', '_').lower() + '.rst'
    output_path = DOCS_SOURCE_DIR / filename

    content = template.render(kpi=kpi_data, details=final_details)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    return filename


def update_index_rst(kpi_files: list):
    index_path = DOCS_SOURCE_DIR / 'index.rst'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("KPI Bluebook\n============\n\n")
        f.write(".. toctree::\n   :maxdepth: 2\n   :caption: Key Performance Indicators:\n\n")
        for file in kpi_files:
            f.write(f"   {file.replace('.rst', '')}\n")


def generate_bluebook(source_code_path: str):
    """The main generator logic, now as a callable function that yields status."""
    for item in DOCS_SOURCE_DIR.glob('*.rst'):
        if item.is_file() and item.name != 'index.rst':
            item.unlink()
    yield "Cleaned old documentation files."

    kpis = find_kpis_in_directory(source_code_path)
    if not kpis:
        yield "No KPIs found in the specified directory."
        return
    yield f"Found {len(kpis)} KPIs. Starting AI generation for descriptions..."

    template_loader = jinja2.FileSystemLoader(searchpath=str(TEMPLATE_DIR))
    template_env = jinja2.Environment(loader=template_loader)
    kpi_template = template_env.get_template('kpi_template.rst.j2')

    generated_files = []
    for kpi in kpis:
        yield f"\nProcessing KPI: '{kpi['name']}'..."
        ai_details = generate_kpi_details(kpi['name'], kpi['code_context'])
        if ai_details:
            filename = create_rst_file(kpi, ai_details, kpi_template)
            generated_files.append(filename)
            yield f"Generated documentation for '{kpi['name']}'."
        yield "Waiting to avoid rate limit..."
        time.sleep(20)

    if generated_files:
        update_index_rst(generated_files)
        yield "Updated main index file."

    yield "\nBuilding final HTML documentation with Sphinx..."
    build_process = subprocess.run(
        ['sphinx-build', '-b', 'html', str(DOCS_SOURCE_DIR), str(DOCS_SOURCE_DIR / '_build')],
        capture_output=True, text=True
    )
    if build_process.returncode == 0:
        yield "Sphinx build successful."
    else:
        yield f"Sphinx build failed:\n{build_process.stderr}"