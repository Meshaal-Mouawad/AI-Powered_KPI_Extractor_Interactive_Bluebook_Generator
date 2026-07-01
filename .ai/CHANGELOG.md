# CHANGELOG.md

## 2026-07-01 — Gemini CLI — UI Foundation Phase 4B.1 Implemented
- Implemented Enterprise Cognitive Design System (ECDS) design tokens in `.ui/LEAPui/ECDS_TOKENS.css`.
- Defined design tokens for border radii, shadows, motion, and typography.
- Established three supported themes (`light-teal`, `dark`, `classic`) with dynamic `data-theme` switching.
- Verification: Validated theme token compilation.

## 2026-07-01 — Codex — MathJax Formula Rendering Fixed

- Fixed recurring formula corruption where explicit LaTeX from source comments rendered as `\Mathrm` / `\Frac`.
- Added deterministic LaTeX preservation in `bluebook_generator/main.py` instead of re-parsing explicit LaTeX as code.
- Updated formula annotation behavior so LaTeX business formulas use executable source expressions for annotation tokens.
- Verification: `python -m py_compile bluebook_generator/main.py` and `python run_generation.py sample_project`; verified MTBF output in generated RST/HTML.

## 2026-07-01 — Gemini CLI — KPI Sidebar Regression Resolved
- Resolved RISK-008: Renamed 'Dependency Decomposition' to 'Source Provenance' in `templates/kpi_template.rst.j2` to restore structural consistency across KPI dossiers.
- Verification: Ran `run_generation.py` on `sample_project`; verified generated HTML files contain "Source Provenance".
- Created `.ai/LESSONS_LEARNED.md` to document the LaTeX formula rendering tokenization bug and establish an invariant against processing presentation-syntax LaTeX as executable code.
