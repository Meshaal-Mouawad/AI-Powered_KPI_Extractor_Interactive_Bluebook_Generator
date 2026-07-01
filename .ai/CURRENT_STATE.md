# CURRENT_STATE.md

## Current phase
Math formula rendering defect resolved and verified. UI Foundation (Phase 4B.1C) implemented: Theme switcher wired with localStorage persistence.

## Current engineering strategy
Preserve explicit source-provided LaTeX as MathJax input instead of routing it through the code-expression renderer. Use source-code expressions for annotated formula tokens when the business formula is explicit LaTeX.

## Current immediate task
Monitor future KPI generations for formula rendering regressions, especially source comments that contain LaTeX commands such as `\mathrm` and `\frac`.

## Known context
- Root cause was backend formula handling in `bluebook_generator/main.py`, not Sphinx or MathJax configuration.
- `generate_formula_from_code()` is correct for executable source expressions but unsafe for explicit LaTeX strings.
- `sample_project/vb_kpi.vb` now generates a valid MTBF formula in `docs/mean_time_between_failures_mtbf.rst`.
