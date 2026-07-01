# THEME_SPEC.md

# LEAP Theme Architecture

LEAP supports ONE canonical interface architecture.

The visual presentation may change through themes.

---

## Theme 1

### Enterprise Mission Control

File:

- 02_THEME_DARK.md

Purpose:

- developer productivity,
- governance analysis,
- technical investigation.

Characteristics:

- dark matte surfaces,
- high information density,
- premium enterprise feel.

---

## Theme 2

### Enterprise Cognitive Workspace

File:

- 03_THEME_LIGHT_TEAL.md

Purpose:

- daily enterprise usage,
- business users,
- executives,
- governance teams.

Characteristics:

- LEAP teal identity,
- calm surfaces,
- cognitive readability.

---

## Theme 3

### Current LEAP Evolution

File:

- 04_THEME_CLASSIC.md

Purpose:

- preserve existing LEAP identity.

Characteristics:

- current LEAP colors,
- current warning cards,
- modernized layout.

---

## Warning System

Use:

- 05_WARNING_COMPONENT.md

This component is canonical.

---

## Critical Rule

Do NOT create three interfaces.

Create:

```text
One architecture
       ↓
Three interchangeable themes
```

All themes share:

- layout,
- components,
- navigation,
- KPI workflow,
- governance behavior,
- formula rendering,
- alert behavior,
- sidebar behavior,
- footer behavior.

Only visual presentation changes.

---

## Dynamic Theme Switching

Preferred implementation:

```html
<body data-theme="dark">

<body data-theme="light-teal">

<body data-theme="classic">
```

or equivalent design token architecture.

---

## Default Theme

The default production theme is:

Enterprise Cognitive Workspace
(Light Teal)