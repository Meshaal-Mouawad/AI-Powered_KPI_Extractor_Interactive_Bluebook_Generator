# PROJECT_CONTEXT.md

## Purpose

This file is intentionally generic at first.

Gemini CLI should fill it by analyzing the local Leap repository as if it joined the project for the first time.

Do not treat this file as final until Gemini has inspected the local codebase.

## Gemini task

Read the full repository and complete this file using source evidence.

Do not invent. Mark uncertain items as `Needs confirmation`. Cite exact files/modules where possible.

## 1. Product understanding

Determine:

- What does Leap do?
- Who are the users?
- What business problem does it solve?
- Why is it different from a normal documentation generator?
- How does it apply literate programming?
- How does it bridge business and technical teams?
- What are the primary outputs?

## 2. Research understanding

Determine how the implementation supports executable knowledge systems, literate programming, explainability, traceability, KPI governance, code-to-business transformation, and Blue Book generation.

## 3. Repository understanding

Determine entry points, package structure, CLI commands, major modules, dependencies, generated artifacts, tests, sample projects, experimental folders, and deprecated/legacy files.

## 4. Domain understanding

Determine what counts as a KPI, how KPIs are detected, how formulas are extracted, how formula evidence is represented, how business descriptions are generated, how governance is attached, and how Blue Book output is built.

## 5. User workflows

Document workflows for developer, business analyst, governance reviewer, PhD evaluator, and enterprise customer.

## 6. Architecture summary

After analyzing the repository, summarize the actual pipeline using real module names.

```text
Input source project
    ↓
Extraction
    ↓
Semantic structuring
    ↓
Governance / validation
    ↓
Narrative generation
    ↓
Blue Book output
```

## 7. Key files and responsibilities

Fill this table:

| File / folder | Responsibility | Notes |
|---|---|---|
| TODO | TODO | TODO |

## 8. Current limitations

Identify technical debt, missing tests, risky heuristics, unclear ownership, incomplete governance, scalability concerns, and PhD demo risks.

## 9. Enterprise readiness

Determine what is enterprise-ready, what needs hardening, what needs audit logging, what needs security/privacy review, and what documentation is missing.

## 10. Open questions

List unknowns requiring Meshaal’s confirmation.
