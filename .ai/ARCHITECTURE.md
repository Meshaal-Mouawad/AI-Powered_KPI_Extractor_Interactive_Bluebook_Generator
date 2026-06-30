# ARCHITECTURE.md

## Conceptual architecture
The system operates as an extraction-to-narrative pipeline:
`Source Code -> Extraction -> Semantic Structuring -> Governance -> Narrative Generation -> Blue Book`

## Components
| Component | Responsibility |
|---|---|
| `cli.py` | CLI argument handling and entry point. |
| `kpi_extractor.py` | AST/static analysis to identify KPI patterns. |
| `governance.py` | Rule-based engine checking KPIs against `governance_rules.json`. |
| `ai_generator.py` | LLM-based narrative drafting (Evidence-backed). |
| `docs/` | Sphinx project structure for final rendering. |

## Data-flow
1. `kpi_extractor` scans `sample_projects/` or target codebase.
2. `governance` applies constraints from `governance_rules.json`.
3. `ai_generator` drafts narrative.
4. `main.py` writes output to `docs/`.

## Architecture risks
- Heuristic-based extraction in `kpi_extractor.py` may be brittle.
- `main.py` contains monolithic orchestration; risk of technical debt.

## Gemini update
The architecture is functional but needs modularization. `main.py` should be decomposed into separate orchestration and processing classes.
