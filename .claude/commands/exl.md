---
description: Build or restyle a page to the EXL branding spec
argument-hint: [what to build, e.g. "a supply-chain dashboard" or "restyle the open file"]
---

Use the **exl-branding** skill (`.claude/skills/exl-branding/SKILL.md`, full spec in
its `reference.md`) to build or restyle to the EXL design system.

Request: **$ARGUMENTS**

Rules:
- If the request names or implies an existing file (or says "this / the open file"),
  restyle that file in place. Otherwise build a new self-contained HTML page.
- Load the EXL tokens, typography, spacing, and components from the skill. Light
  theme is the default; only add the `[data-theme="dark"]` block if dark is asked for.
- One primary orange action per viewport. Lucide icons only, no emoji. Follow the
  skill's writing rules for all copy (no em dashes, no AI slop).
- Marketing pages use the full hero; apps and dashboards use the slim app header.
- Before finishing, run the skill's ship checklist.

If `$ARGUMENTS` is empty, ask what to build or which file to restyle.
