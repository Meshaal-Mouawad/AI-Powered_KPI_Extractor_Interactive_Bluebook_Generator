AI-Powered KPI Extractor & Interactive Bluebook Generator

Step-by-step guide location: see USAGE.md in the repository root.

Quick view: After generation, open `docs/_build/index.html`.

## How it Works
- `kpi_extractor.py` finds `# KPI:` markers within functions.
- `main.py` scopes the function with AST, generates MathJax from code, and renders a Jinja template.
- `ai_generator.py` calls OpenAI to create narrative fields and infers a specific unit when the AI is vague.
- Sphinx converts `.rst` into an HTML Bluebook.

## Customization
- Edit `templates/kpi_template.rst.j2` for layout.
- Add rules to `ai_generator._infer_unit_of_measure` to refine units.
- Extend variable definitions in `main.generate_formula_from_code`.

## Troubleshooting
- Missing API key → set `OPENAI_API_KEY`.
- “No KPIs found” → ensure `# KPI: Your KPI Name` is inside a function.
- Broken LaTeX → check expressions or open an issue with the example.

## Example KPIs
- Overall Equipment Effectiveness (OEE)
- Ethylene Yield Percentage
- Daily Feedstock Throughput (tons/day)
- Mean Time Between Failures (hours per failure)
- Propylene to Ethylene (P/E) Ratio

## CLI usage
- Basic:
  - bash `bluebook generate path/to/your/source`
- Options:
  - `--clean-build` to delete `docs/_build` before building
  - `--workers N` to set the number of parallel AI workers (defaults to env `KPI_AI_WORKERS` or 4)

Alternative (without installing as a script):
- bash `python -m bluebook_generator.cli generate path/to/your/source`

