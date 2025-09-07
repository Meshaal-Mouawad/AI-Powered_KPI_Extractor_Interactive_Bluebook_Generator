# ...existing code...

def extract_formula_from_comments(code_lines):
    """
    Look for lines containing 'Formula:' and return the formula string.
    """
    for line in code_lines:
        if "Formula:" in line:
            # Extract everything after 'Formula:'
            return line.split("Formula:", 1)[1].strip()
    return None

def find_kpis_in_directory(directory):
    # ...existing code...
    for file in files:
        # ...existing code...
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # ...existing code...
        # Try to extract formula from comments
        formula = extract_formula_from_comments(lines)
        kpi = {
            # ...existing code...
            "formula": formula,
            # ...existing code...
        }
        # ...existing code...
    # ...existing code...

