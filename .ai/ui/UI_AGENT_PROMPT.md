# UI_AGENT_PROMPT.md

## Purpose

Use this prompt when asking Gemini, Copilot, Codex, DeepSeek, or another agent to work on LEAP UI/UX.

---

## Prompt

Read:

- `.ai/START_HERE.md`
- `.ai/UI_DESIGN_SYSTEM.md`
- `.ai/UI_BEHAVIOR_SPEC.md`
- `.ai/SYSTEM_BEHAVIOR_SPEC.md`
- `.ai/PHASE_LOG.md`
- `.ai/LEAP_MASTER_ROADMAP.md`
- `.ai/CURRENT_STATE.md`
- `.ai/HANDOFF.md`
- `.ai/BUGS.md`

This task concerns LEAP UI/UX and Phase 4A unless stated otherwise.

Goal:

Design and repair LEAP according to the Enterprise Cognitive Design System (ECDS).

LEAP must feel:

- trustworthy,
- competent,
- calm,
- safe,
- authentic,
- enterprise-grade,
- suitable for government and top-tier companies.

Preserve:

- governance,
- traceability,
- explainability,
- auditability,
- KPI correctness,
- backend generation pipeline,
- Sphinx rendering pipeline.

Improve:

- enterprise trust,
- visual hierarchy,
- developer productivity,
- interaction quality,
- emotional confidence,
- daily usability,
- rounded smooth interface language,
- matte surfaces,
- subtle shadows,
- calm spacing.

Target visual references:

- OpenAI
- Apple Human Interface
- Linear
- Notion
- Stripe
- Palantir Foundry

Do NOT create:

- consumer UI,
- flashy dashboard UI,
- glassmorphism,
- neumorphism,
- gaming UI,
- hard sharp-corner interface,
- marketing landing page UI.

Do NOT:

- hardcode generated HTML,
- patch `docs/_build`,
- bypass Sphinx,
- remove governance logic,
- remove traceability,
- remove sidebar sections when data is missing,
- hide alerts to make UI look clean.

Required behavior:

- all alerts appear only in the right sidebar,
- missing data appears as `UNDETERMINED` / `Needs Review`,
- footer is visible and consistent,
- right sidebar sections are preserved,
- generated pages remain connected to real backend data.

Before implementation:

1. Explain what LEAP is.
2. Explain the relevant UI subsystem.
3. Identify what files you need to inspect.
4. State root-cause hypotheses.
5. Provide a safe plan.

After implementation:

1. Show changed files.
2. Explain each change.
3. Show verification evidence.
4. Update `.ai/HANDOFF.md`, `.ai/CHANGELOG.md`, `.ai/BUGS.md`, and `.ai/CURRENT_STATE.md`.

The user should feel:

> I trust this system enough to make important business decisions.
