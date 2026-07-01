# GOVERNANCE_SPEC.md

## LEAP Governance Philosophy
LEAP is a KPI correctness and governance engine.

## Governance Conflict Detection
Compare:
- business KPI intent
- declared formula
- extracted code formula

Detect:
- operator mismatch
- variable mismatch
- missing components
- structural inconsistencies
- invalid aggregation
- missing normalization

Output:
- `kpi.governance_conflict = True|False`
- `kpi.conflict_reason`
- `kpi.severity`

Requirements:
- deterministic
- traceable
- evidence-based
- no vague explanations

## ISO / Compliance Validation
Detect:
- ISO 22400 violations
- enterprise policy violations
- invalid KPI patterns

## Code Drift Detection
Track:
- code_hash
- source file
- version/commit

If code_hash changes:
- trigger drift alert
- set status = Needs Review
- pause approval

## Human Override
Read `kb/overrides.json` before validation.
If KPI id and code hash match:
- apply override
- suppress review alerts
- mark approved

## System Invariants
Never break:
- traceability
- governance
- formula validation
- evidence mapping
- deterministic behavior
