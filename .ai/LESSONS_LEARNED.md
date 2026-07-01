# LESSONS_LEARNED.md

## Title
Do not pass explicit LaTeX through executable-code formula renderers.

## Problem
Explicit LaTeX formulas from source comments were being passed into `generate_formula_from_code()`, which is designed for executable expressions, not LaTeX command strings.

## Root cause
The renderer tokenized LaTeX commands like `\mathrm` and `\frac` as normal text tokens, corrupting them into invalid output such as `\Mathrm`, `\Frac`, and escaped `\text{...}`.

## Correct rule
If a formula is already explicit LaTeX, preserve it as MathJax input.
Do not re-tokenize it as code.
Use executable source expressions only for annotation tokens when needed.

## Affected area
- `bluebook_generator/main.py`
- formula rendering
- MathJax output
- KPI dossier generation

## Verification pattern
- Run `python -m py_compile bluebook_generator/main.py`
- Run `python run_generation.py sample_project`
- Inspect generated RST and HTML.
- Confirm valid LaTeX uses `\mathrm` and `\frac`.
- Confirm generated docs do not contain `\Mathrm` or `\Frac`.

## Future Invariant
“Explicit LaTeX is presentation syntax and must not be processed as executable code.”
