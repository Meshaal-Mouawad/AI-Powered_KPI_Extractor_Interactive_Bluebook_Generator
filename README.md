# AI-Powered KPI Extractor & Interactive Bluebook Generator

This tool scans your Python code for KPI comments inside functions, generates clean documentation pages with readable math, and builds an interactive HTML “Bluebook” using Sphinx.

## Features
- AST-precise “Code Context” (only the function that implements the KPI)
- Programmatic LaTeX/MathJax formulas with italic readable labels and correct operator precedence
- AI-generated descriptions/objectives/notes
- Smart unit-of-measure inference (%, tons/day, hours per failure, ratio, …)
- One-command CLI

## Requirements
- Python 3.10+
- virtualenv + pip
- Packages: click, jinja2, requests (installed automatically by your project)
- Sphinx for building docs: `pip install sphinx`

## Install
Bash `python -m venv .venv && source .venv/bin/activate pip install -e`

## If you don’t have a setup.py, simply run from the repo root:
bash `python -m bluebook_generator.cli generate path/to/your/source`

## Set your OpenAI key:
bash 'export OPENAI_API_KEY=sk-...'


## How to Use
1) Tag KPIs in code inside a function with a single-line comment:
'python def calculate_oee(...): # KPI: Overall Equipment Effectiveness (OEE) oee = availability * performance * quality * 100 return oee'
2) Generate: bash 'bluebook generate ./path/to/your/repo'
3) Open `docs/_build/index.html`.

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

Packaging (optional) If you’d like a console script named bluebook, add this to your pyproject.toml or setup.cfg. Example for setup.cfg:
[metadata]
name = bluebook-generator
version = 1.0.0
description = AI-Powered KPI Extractor & Interactive Bluebook Generator

[options]
packages = find:
install_requires =
    click
    jinja2
    python-dotenv
    openai
    sphinx

[options.entry_points]
console_scripts =
    bluebook = bluebook_generator.cli:main

