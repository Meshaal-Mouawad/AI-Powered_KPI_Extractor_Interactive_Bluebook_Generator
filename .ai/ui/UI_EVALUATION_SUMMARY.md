# UI_EVALUATION_SUMMARY.md

## Purpose

This file summarizes the Figma UI/UX evaluation and translates it into LEAP design direction.

---

## High-Level Evaluation

The Figma audit positions LEAP as an enterprise-grade product, not a startup dashboard.

The main evaluation message is:

> LEAP must look and feel like a serious institutional product for government, oil and gas, audit, consulting, and enterprise environments.

---

## Critical Figma Audit Themes

### 1. Remove marketing patterns

The audit recommends removing the large marketing-style footer because LEAP is an application, not a consumer website.

A government or enterprise client should not see website-style columns such as:

- Company
- Developers
- Resources
- Use Cases
- National Alignment

The footer should become compact, institutional, and legal-safe.

---

### 2. Hide raw terminal output by default

The audit recommends renaming `Execution Terminal` to `Processing Log`.

Reason:

- enterprise buyers are not always developers,
- raw logs in the hero area reduce executive trust,
- raw logs should be available but collapsed.

Default state should show a clean message:

> Ready. Enter a project folder path and click Run Extraction to begin.

---

### 3. Use institutional language

The audit recommends replacing casual action labels.

Examples:

| Old | New |
|---|---|
| Generate Bluebook | Run Extraction |
| Submit to AI Engine | Run Extraction |
| Create New Scan | New Scan |
| Clear Build & Start Fresh | Reset Workspace |
| Open Existing Bluebook | Open Bluebook |

Reason:

Enterprise UI should use precise operational language.

---

### 4. Remove unfinished tabs

The audit says empty `Analytics` and `Reports` tabs should be removed or replaced with structured empty states.

Reason:

Empty tabs signal unfinished software during demos.

---

### 5. Replace native confirm dialogs

Native browser `confirm()` dialogs feel unprofessional and may be blocked in enterprise environments.

Use inline two-click confirmation instead.

---

### 6. Avoid legal overclaiming

The button `Export Certified Bluebook` should be renamed because `Certified` implies formal legal verification.

Preferred:

> Print Bluebook (PDF)

---

### 7. Remove hardcoded statistics

Hardcoded values such as `93.2%` and `62 KPIs` destroy trust if they do not match the actual scan result.

Stats must come from real backend values.

---

### 8. Consolidate CSS tokens

The audit found repeated color variables pointing to the same value.

Recommendation:

```css
--brand-primary: #004E5A;
--success: var(--brand-primary);
--teal: var(--brand-primary);
--matte-teal: var(--brand-primary);
--matte-olive: var(--brand-primary);
```

---

### 9. Improve accessibility

Interactive button text should not be below 12px.

---

### 10. Remove prototype visual artifacts

The audit recommends removing:

- magenta/pink toggle flicker,
- gradient dividers,
- square confidence dots,
- internal comment blocks,
- overly sharp UI elements.

---

## Proposed Visual Direction

The Figma audit suggests an institutional design system:

- warm document-grade background,
- deep navy primary actions,
- soft enterprise cards,
- Inter typography,
- JetBrains Mono for code,
- collapsed raw logs,
- calm status panels,
- precise action language.

---

## LEAP Design Interpretation

The Figma audit is not just asking for cosmetic changes.

It is pushing LEAP from:

> Research prototype

toward:

> Enterprise cognitive system

The correct direction is:

- less marketing,
- less raw developer noise,
- more governance clarity,
- more trust,
- better cognitive hierarchy,
- more institutional confidence.

---

## Relationship to ECDS

The Figma evaluation is the current-state audit.

`UI_DESIGN_SYSTEM.md` is the future-state design philosophy.

Together:

```text
Figma Audit
    ↓
what is wrong / risky

UI Design System
    ↓
what LEAP should become
```
