# REPOSITORY_SCOPE.md

This file defines the authoritative classification of repository contents for agent behavior.

## Classification Definitions

- **A. Canonical source:** Core logic, definitions, business rules, and configuration.
- **B. Diagnostic evidence:** Test samples, logs, experimental artifacts, and docs source. Use only to reproduce bugs.
- **C. Generated artifact:** Build outputs and rendered documentation. **Never patch.**
- **D. Ignore:** Environment, IDE configs, and temporary system files.
- **E. Never inspect:** Legacy staging folders or deprecated work-in-progress unless explicitly tasked.
- **F. Human verification evidence:** Human-provided feedback (e.g., screenshots, annotated images). Inspect only when user explicitly requests visual comparison.

## Scope Assignments

| Path | Class | Reasoning |
| :--- | :--- | :--- |
| `.ai/` | **A** | Meta-system source of truth. |
| `bluebook_generator/` | **A** | Core application logic. |
| `kb/` | **A** | Essential Knowledge Base data. |
| `app.py`, `run_generation.py`, `test_app.py` | **A** | Entry points and tests. |
| `requirements.txt`, `pyproject.toml` | **A** | Build configuration. |
| `phase3/` | **B** | Experimental/validation artifacts; inspect only when related to the task. |
| `docs/*.rst` | **B** | Generated diagnostic evidence. May be inspected when debugging rendering, formulas, governance display, or documentation generation. Never patch as final fix. |
| `docs/_build/*.html` | **C** | Rendered output. **Never patch.** |
| `research/` | **B** | Human-generated logs for historical context. |
| `sample_projects/` | **B** | Verification data/samples. |
| `Design Audit for LEAP Interface/` | **B** | UI design reference material. Read only during UI/UX tasks. |
| `figuersConverting/` | **B** | Diagnostic/Experimental image conversions. |
| `.venv/`, `.idea/`, `.git/` | **D** | Environment/Tooling noise. |
| `Update3/`, `Updated NOT Implemented yet_underPlan/` | **E** | Unstable legacy/WIP. |
| `screenshots/` | **F** | Human verification evidence (if present). |

## Cheapkeeper Rule

Before scanning a repository:

1. Identify the subsystem.
2. Read only files relevant to that subsystem.
3. Avoid recursive repository scans.
4. Prefer human verification over repeated regeneration.
5. Use stronger agents only when diagnosis complexity exceeds local implementation cost.
