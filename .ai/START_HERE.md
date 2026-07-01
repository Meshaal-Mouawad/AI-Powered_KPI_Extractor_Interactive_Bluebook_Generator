# START_HERE.md

# LEAP Agentic Literate Programming Bootloader

## Purpose

This file is the mandatory entry point for every AI session.

Use it:

- for every new AI agent,
- for every new chat,
- after another agent modified the repository,
- when an agent appears confused,
- before major implementation,
- before code review,
- before final verification.

Conversation history is NOT shared memory.

The `.ai` directory is the single source of truth.

---

# Required Reading Order

Read the following files in order.

## 1. Scientific Context

1. `.ai/RESEARCH_CONTEXT.md`
   - WHY LEAP exists
   - Scientific contribution
   - PhD goals

---

## 2. Agent Behavior

2. `.ai/AI_AGENT.md`
   - How agents must behave
   - Collaboration rules
   - Safety constraints

---

## 3. Project Understanding

3. `.ai/PROJECT_CONTEXT.md`
   - WHAT LEAP does

4. `.ai/ARCHITECTURE.md`
   - HOW LEAP works

---

## 4. Behavioral Specifications

5. `.ai/SYSTEM_BEHAVIOR_SPEC.md`
   - System identity
   - Phase definitions
   - User workflow
   - Non-negotiable system invariants

6. `.ai/GOVERNANCE_SPEC.md`
   - Governance conflict detection
   - Formula validation
   - ISO validation
   - Code drift detection
   - Human overrides

7. `.ai/UI_BEHAVIOR_SPEC.md`
   - Alert placement rules
   - Sidebar requirements
   - Footer behavior
   - Enterprise UI rules

---

## 5. Business Constraints

8. `.ai/BUSINESS_RULES.md`
   - Rules that must never be broken

---

## 6. Current Project State

9. `.ai/CURRENT_STATE.md`
   - Current implementation phase

10. `.ai/PHASE_LOG.md`
    - Historical implementation progress

11. `.ai/HANDOFF.md`
    - Previous agent session

12. `.ai/BUGS.md`
    - Known issues and risks

13. `.ai/DECISIONS.md`
    - Architectural decisions

14. `.ai/CHANGELOG.md`
    - Recent modifications

---

# After Reading

Before editing any code, respond with:

### 1. Understanding

- What LEAP is.
- What LEAP is NOT.

### 2. Relevant Subsystem

Identify the subsystem involved:

Examples:

- extraction
- governance
- validation
- rendering
- UI
- interaction
- compliance
- simulation

### 3. Files To Inspect

List the files you intend to inspect.

---

### 4. Safe Plan

Provide:

- root cause hypothesis,
- implementation strategy,
- verification strategy,
- rollback strategy.

---

### 5. Execution Ownership

State whether this task is best suited for:

- Gemini
- Codex
- Copilot
- Kimi
- Manual implementation

---

# Shared Memory Rules

Conversation history is NOT shared memory.

No diagnosis,
decision,
bug analysis,
architecture reasoning,
or implementation plan
is considered complete until it has been written into `.ai`.

---

# Before Ending

Update:

- `.ai/CURRENT_STATE.md`
- `.ai/HANDOFF.md`
- `.ai/CHANGELOG.md`
- `.ai/BUGS.md` (if risks changed)
- `.ai/DECISIONS.md` (if decisions changed)
- `.ai/PHASE_LOG.md` (if phase status changed)
- `.ai/SESSIONS/YYYY-MM-DD-topic.md` (for long sessions)

---

# Final Report Required

Before finishing:

1. Show which `.ai` files were modified.
2. Show the relevant `git diff .ai`.
3. Explain why each update was made.
4. Show verification evidence.
5. If no `.ai` files were updated, explicitly state:

> Shared memory was NOT updated.

---

# Never

Do NOT:

- invent business facts,
- silently remove traceability,
- break KPI behavior,
- break governance,
- certify AI interpretation as truth,
- hardcode generated output,
- patch generated `_build` artifacts,
- remove alerts to hide problems,
- remove sidebar sections when data is missing,
- perform broad refactors during PhD-critical debugging.
- Do not route explicit LaTeX formulas through executable-code renderers.
- Do not treat presentation syntax as executable expression syntax.

---

# LEAP Identity

LEAP is NOT:

- documentation,
- visualization,
- reporting.

LEAP is:

- a KPI correctness engine,
- a governance system,
- an explainable enterprise layer,
- an executable knowledge system.