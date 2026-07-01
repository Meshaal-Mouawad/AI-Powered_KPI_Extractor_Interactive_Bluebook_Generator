# UI_DESIGN_SYSTEM.md

# LEAP Enterprise Cognitive Design System (ECDS)

## Purpose

This file defines the visual and emotional design language for LEAP.

LEAP must feel trustworthy, competent, calm, and safe enough for enterprise users to rely on it daily.

---

## Core Design Philosophy

People do not use enterprise software because it is beautiful.

They use it because it feels:

- trustworthy,
- competent,
- safe,
- predictable,
- authoritative.

For LEAP, visual design must align with:

- governance,
- traceability,
- auditability,
- explainability,
- enterprise decision confidence.

LEAP must not feel like consumer beauty.

It must feel like an enterprise cognitive system.

---

## System Identity

LEAP is not:

- a dashboard,
- a reporting tool,
- a documentation site,
- a generic analytics UI.

LEAP is:

- an enterprise knowledge system,
- a governance platform,
- a cognitive workspace,
- a KPI correctness engine,
- an executable knowledge system.

---

## Design Language Name

LEAP follows:

# Enterprise Cognitive Design System (ECDS)

Inspired by:

- OpenAI
- Apple Human Interface
- Linear
- Notion
- Stripe
- Palantir Foundry

The goal is not to copy any product, but to borrow their emotional qualities:

- OpenAI: calm intelligence
- Apple: precision and confidence
- Linear: developer flow and speed
- Notion: clarity and softness
- Stripe: trust and enterprise polish
- Palantir: mission-critical seriousness

---

## Emotional Goals

The interface must create:

- confidence,
- authority,
- calmness,
- curiosity,
- safety,
- trust,
- daily usability.

The user should feel:

> I trust this system enough to make important business decisions.

---

## Shape Language

Avoid:

- sharp corners,
- hard rectangles,
- aggressive borders,
- cramped containers.

Prefer:

- 12px radius,
- 16px radius,
- 20px radius,
- floating cards,
- soft containers,
- calm nested panels.

Recommended:

```css
--radius-sm: 10px;
--radius-md: 14px;
--radius-lg: 18px;
--radius-xl: 22px;
```

---

## Surface Design

Avoid:

- pure black,
- pure white,
- harsh contrast,
- decorative gradients,
- glassmorphism,
- neumorphism.

Prefer:

- matte surfaces,
- soft warm grays,
- low-contrast backgrounds,
- subtle shadows,
- document-grade surfaces.

Recommended palette:

```css
--page-bg: #F8F7F4;
--surface: #FFFFFF;
--surface-soft: #F8FAFC;
--border: #E2E8F0;
--text-primary: #111827;
--text-secondary: #374151;
--text-muted: #9CA3AF;
--brand-primary: #004E5A;
--action-primary: #1B3A6B;
--action-primary-hover: #162F5C;
```

---

## Shadows

Use soft ambient shadows only.

Avoid heavy shadows.

Recommended:

```css
--shadow-soft: 0 8px 32px rgba(0,0,0,0.06);
--shadow-card: 0 4px 18px rgba(15,23,42,0.05);
```

---

## Typography

Preferred fonts:

- Inter
- SF Pro
- Geist
- JetBrains Mono for code and hashes

Type scale:

| Element | Size | Weight | Color |
|---|---:|---:|---|
| Page title | 24px | 600 | #111827 |
| Section header | 16px | 500 | #1E293B |
| Card title | 13px | 600 | #1E293B |
| Section label | 11px | 600 | #6B7280 |
| Body text | 13px | 400 | #374151 |
| Metadata | 11px | 400 | #9CA3AF |
| Buttons | 12px | 600 | contextual |
| Code | 12px | 400 | JetBrains Mono |

---

## Motion

Use subtle 150–250ms transitions.

Apply to:

- cards,
- buttons,
- tabs,
- KPI interactions,
- alerts,
- sidebar actions.

Avoid:

- flashy animations,
- bouncy motion,
- game-like transitions.

---

## Enterprise KPI Page Requirements

Every KPI page should contain:

- KPI Knowledge Dossier,
- status badge,
- formula visualization,
- code evidence,
- governance panel,
- source provenance,
- operational actions,
- review queue,
- extraction method,
- footer.

---

## Sidebar Requirements

The right sidebar must include, when applicable:

1. System Integrity
2. Governance Scope
3. Source Provenance
4. Operational Actions
5. Review Queue
6. Extraction Method

If data is missing, do not remove the section silently.

Instead show:

- `UNDETERMINED`
- `Needs Review`
- `Pending Evidence`

---

## Alert Design

All alerts must appear only in the right sidebar.

Alerts must be:

- clear,
- concise,
- traceable,
- calm but visible.

Alert levels:

- Validated
- Needs Review
- Critical

---

## Forbidden Design Styles

Do not use:

- glassmorphism,
- neumorphism,
- gaming UI,
- consumer dashboard UI,
- flashy animations,
- sharp edges,
- marketing website patterns,
- decorative gradients,
- fake certification language.

---

## Design Success Criteria

LEAP UI succeeds when the user feels:

> This system understands the KPI, shows the evidence, explains the risk, and gives me control.
