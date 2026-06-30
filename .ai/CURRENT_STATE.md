# CURRENT_STATE.md

## Current phase

PhD proposal approved. Target PhD completion: December.

## Current engineering strategy

Use a simple, auditable multi-agent workflow:

```text
ChatGPT Plus → architecture / planning
Codex → hard bugs / root cause / final review
Gemini CLI → main implementation / local repo analysis
GitHub Copilot → autocomplete / inline help
Kimi → second-opinion review
Air → local workspace for supported providers
Qwen → future optional coding agent
DeepSeek → future optional low-cost reasoning backup
```

## Current decision

Do not add complex memory databases such as Mem0, Cognee, or AgentMemory yet.

Reason: `.ai` + Git is deterministic, auditable, aligned with Leap's philosophy, and safer before the PhD deadline.

## Current immediate task

1. Put updated `.ai` folder in repository.
2. Run Gemini CLI with:

```text
Read `.ai/PROMPTS/gemini_bootstrap_project_memory.md` and execute it.
```

3. Let Gemini fill `PROJECT_CONTEXT.md` from the local repository.
4. Commit the `.ai` updates.

## Known context

- GitHub Education is verified.
- Codex student credits were used up.
- ChatGPT Plus subscription is active.
- Qwen account was registered for possible future use.
- Air appears to support limited providers only: Codex/OpenAI, Gemini, Anthropic, JetBrains.
- Keep the workflow simple for now.
