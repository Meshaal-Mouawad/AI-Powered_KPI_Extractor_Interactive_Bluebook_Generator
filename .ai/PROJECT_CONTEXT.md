# PROJECT_CONTEXT.md

## 1. Product understanding
Leap is an automated "Executable Knowledge System" that extracts KPIs and business logic from source code, validates them against governance rules, and generates narrative "Blue Book" documentation (in RST format).
- **Users:** Engineers, Business Analysts, Governance/Compliance officers.
- **Problem Solved:** Bridges the semantic disconnect between executable code and business definitions.
- **Difference:** Unlike static docs or dashboards, LEAP is evidence-based and derived directly from code execution/structure.

## 2. Research understanding
Focuses on "Executable Knowledge Systems" (PhD research). Uses static analysis (via `kpi_extractor.py`) and governance mapping to transform raw code into explainable business narratives.

## 3. Repository understanding
- **Entry Points:** `bluebook_generator/main.py`, `bluebook_generator/__main__.py`, `bluebook_generator/cli.py`.
- **Core Modules:**
    - `bluebook_generator/kpi_extractor.py`: Source code scanner.
    - `bluebook_generator/governance.py`: Governance rule validation.
    - `bluebook_generator/ai_generator.py`: AI-assisted narrative drafting.
- **Output:** `docs/` (RST documentation generated via Sphinx).
- **Samples/Tests:** `sample_project/`, `sample_project_50/`, `phase3/`.

## 4. Domain understanding
- **KPI:** A business metric embedded in code logic.
- **Extraction:** Scans files (SQL, Python, etc.) to link code to business metrics.
- **Governance:** Uses `governance_rules.json` to enforce organizational policy on discovered KPIs.

## 5. User workflows
- **Developer:** Run `bluebook_generator` to verify code-documentation alignment.
- **Governance Reviewer:** Inspect generated RSTs for policy adherence.

## 6. Architecture summary
```text
Source Code Project
    ↓
bluebook_generator/kpi_extractor.py (Extraction)
    ↓
bluebook_generator/governance.py (Governance/Validation)
    ↓
bluebook_generator/ai_generator.py (Narrative generation)
    ↓
docs/ (Blue Book output - Sphinx)
```

## 7. Key files and responsibilities
| File / folder | Responsibility | Notes |
|---|---|---|
| `bluebook_generator/main.py` | Orchestration | Monolithic; contains core pipeline logic. Needs confirmation on separation of concerns. |
| `bluebook_generator/kpi_extractor.py` | Extraction | Analyzes source files for KPI logic. |
| `bluebook_generator/governance.py` | Validation | Validates extracted KPIs against `governance_rules.json`. |
| `docs/` | Output | Directory containing final RST documentation. |

## 8. Current limitations
- `main.py` is overly large (>100k bytes) and likely contains mixed concerns.
- Governance logic is currently tightly coupled with extraction.
- Regression testing of generated documentation is not yet automated.

## 9. Enterprise readiness
Needs audit logging and security review for API calls made by `ai_generator.py`. Governance rules are partially externalized (`governance_rules.json`) but need full audit trail.

## 10. Open questions
- Is the current `main.py` intended to be the central monolith, or should it be decomposed? (Needs confirmation)
