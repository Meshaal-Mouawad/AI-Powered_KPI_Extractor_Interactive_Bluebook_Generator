# BUSINESS_RULES.md

## Purpose

This file protects the business and enterprise meaning of Leap.

## Source-backed truth policy

Leap must not invent certified business facts.

Evidence strength order:

1. Source code.
2. Explicit code comments.
3. Owner-approved overrides.
4. Governance rule files.
5. Deterministic extraction.
6. AI-generated draft interpretation.

## KPI rules

A KPI should have identifiable business or metric context, source-code evidence, calculation logic/formula evidence, traceability to file/function/line where possible, and generated or approved narrative.

## Blue Book rules

A Blue Book entry should expose KPI name, business meaning, formula, formula explanation, code evidence, source location, governance status, validation/override status, and missing evidence clearly marked.

## Governance rules

- Do not guess ownership.
- Do not hide missing lineage.
- Do not certify AI output without human approval.
- Show conflicts between business definition and actual execution.
- Preserve auditability.

## AI enrichment rule

AI may help generate draft explanations, but it must not override source truth, remove uncertainty, invent data lineage, or certify assumptions.

## Enterprise rule

Enterprise customers must be able to ask “Why does this KPI mean this?” and Leap must answer with evidence, not vibes.
