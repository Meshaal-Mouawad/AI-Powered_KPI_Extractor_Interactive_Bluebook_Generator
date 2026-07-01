# HANDOFF.md

## Last session
Agent: Codex
Task: Fix recurring MathJax formula corruption in KPI pages.

## Updates made
- Identified that explicit LaTeX formulas were being routed through `generate_formula_from_code()`, which tokenized LaTeX commands as plain business text and produced invalid output such as `\Mathrm` and `\Frac`.
- Added deterministic LaTeX detection, command normalization, and MathJax wrapping helpers in `bluebook_generator/main.py`.
- Updated annotation selection so explicit LaTeX formulas use executable source expressions for annotation tokens instead of splitting LaTeX command strings.
- Regenerated the Blue Book with `python run_generation.py sample_project`.

## Verification
- `python -m py_compile bluebook_generator/main.py` succeeded.
- `python run_generation.py sample_project` succeeded; Sphinx build successful.
- `docs/mean_time_between_failures_mtbf.rst` now contains `\mathrm{MTBF} = \frac{\mathrm{Operating\ Hours}}{\mathrm{Number\ of\ Failures}}`.
- Generated `docs/` and `docs/_build/` no longer contain corrupted `\Mathrm` or `\Frac` output.

## Next action
System stable. Monitor for future sidebar regressions and strictly follow formula rendering invariants defined in `.ai/LESSONS_LEARNED.md`.

## Important warning
- Do not route explicit LaTeX through `generate_formula_from_code()`.
- Explicit LaTeX is presentation syntax and must not be processed as executable code (reference `.ai/LESSONS_LEARNED.md`).
- Do not patch generated `_build` artifacts as the source of truth.
