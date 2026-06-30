# ARCHITECTURE.md

## Purpose

This file describes HOW Leap works.

Gemini should refine this after local repository analysis.

## Conceptual architecture

```text
Source Code Project
        ↓
KPI Extraction
        ↓
Semantic Structuring
        ↓
Formula / Evidence Mapping
        ↓
Governance / Validation
        ↓
Narrative Generation
        ↓
Blue Book Rendering
        ↓
Interactive Business + Developer Documentation
```

## Expected components

| Component | Expected responsibility |
|---|---|
| CLI layer | Run generation commands |
| Extractor | Scan source code and identify KPI candidates |
| Parser / formula logic | Extract calculation structures |
| AI/detail generator | Create draft descriptions or deterministic details |
| Governance layer | Attach ownership, audit, validation, and lineage metadata |
| Override layer | Apply owner-approved or manually curated values |
| Template layer | Render RST/HTML documentation |
| Sphinx docs | Build final Blue Book |

## Important data-flow principle

Leap must preserve this chain:

```text
KPI → Formula → Code → Evidence → Narrative → Governance
```

## Architecture risks to verify

- Formula extraction may be heuristic-heavy.
- Governance logic may be spread across multiple files.
- AI enrichment can create compliance risk if not labeled as draft.
- Generated documentation may be hard to regression-test.
- Local repository may differ from public GitHub state.

## Gemini update task

After inspecting the local repo, replace this file with actual module names, function/class responsibilities, data structures, execution flow, build commands, test commands, and an updated architecture diagram if useful.
