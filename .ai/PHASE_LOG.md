# PHASE_LOG.md

## 2026-07-01 — Phase 4A Rendering Stability

### Event
Resolved recurring MathJax formula corruption for explicit LaTeX formulas in generated KPI dossiers.

### Root cause
Explicit source-provided LaTeX was being passed into the code-expression formula renderer. That renderer tokenizes operands and is not safe for LaTeX command strings.

### Verification
- `python -m py_compile bluebook_generator/main.py`
- `python run_generation.py sample_project`
- Confirmed `docs/mean_time_between_failures_mtbf.rst` and generated HTML contain valid `\mathrm` / `\frac` output.
