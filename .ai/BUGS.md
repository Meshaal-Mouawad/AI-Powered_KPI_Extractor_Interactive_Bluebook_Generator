# BUGS.md

## Active risks

### RISK-001 — Technical Debt in `main.py`
**Status:** Open
**Severity:** Medium
**Description:** `bluebook_generator/main.py` is >100KB, indicating a likely violation of SRP.
**Next action:** Plan refactor/decomposition.

### RISK-002 — Extraction Robustness
**Status:** Open
**Severity:** High
**Description:** `kpi_extractor.py` uses heuristic parsing which may fail on complex code structures.
**Next action:** Audit extraction success rates on `sample_project_50/`.

### RISK-003 — AI Trustworthiness
**Status:** Open
**Severity:** High
**Description:** AI-generated narrative draft certification risk.
**Next action:** Enforce "Draft" labels in documentation generation.
