# UI_BEHAVIOR_SPEC.md

## LEAP UI Philosophy
LEAP pages are enterprise knowledge dossiers.

## Alert Placement Rule
ALL alerts MUST appear ONLY in the right sidebar.

Forbidden:
- formula section
- walkthrough section
- narrative section
- main content area

## Alert Types
### Governance Alert
Display:
⚠ Governance Conflict — Needs Review

Include:
- explanation
- severity
- evidence source

### ISO Alert
Display standards violations.

### Technical Validation Alert
Display:
- formula mismatch
- logic inconsistency
- structural errors

### Data Integrity Alert
Display:
- division by zero risk
- NULL handling issues
- scaling problems

## Alert Levels
- Validated
- Needs Review
- Critical

## Required KPI Page Components
- status badge
- alert panel
- formula visualization
- traceability
- governance
- review queue
- footer

## Sidebar Sections
- System Integrity
- Governance Scope
- Source Provenance
- Operational Actions
- Review Queue
- Extraction Method

If data missing:
- show UNDETERMINED
- show Needs Review
Never silently remove sections.
