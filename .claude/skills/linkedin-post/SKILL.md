---
name: linkedin-post
description: Generate a storytelling-style LinkedIn post for a given day of the 60 Days of Claude AI Challenge. Use when the user runs "/linkedin-post <day number>" or asks for a LinkedIn post about a specific day's work.
---

# LinkedIn post generator — 60 Days of Claude AI Challenge

Generates a LinkedIn post for a specific day of the challenge, written in storytelling mode with a hook-line opener, and saves it into that day's folder.

## Input

The user invokes this as `/linkedin-post <day number>` (e.g. `/linkedin-post 48`). If no day number is given, ask for one — do not guess.

## Steps

1. Resolve the folder for that day: look for `Day <n>` (case-insensitive, tolerate `Day-<n>` / `day<n>`) at the repo root.
2. Read what was actually built that day: list the folder's files and read the main deliverable (HTML app, README, or notes file) to understand what the project does, what problem it solves, and any interesting detail worth telling a story about. Do not invent features that aren't in the files.
3. Write the post to `<day folder>/linkedin-post.md` using the structure below.

## Post structure (storytelling mode)

1. **Hook line** — the first 1-2 sentences must stand alone as a scroll-stopper. Not a summary of the day, a specific, concrete, slightly surprising moment or tension pulled from the actual work (a decision, a problem, a small "wait, it did what?" beat). No generic openers like "Today I built..." or "Excited to share...".
2. **The setup** — 2-4 short sentences establishing the real problem being solved, in plain language a non-technical connection would still follow.
3. **The turn** — what Claude/the build actually did, told as a small narrative beat (what was tried, what worked, one specific detail that makes it feel real rather than templated). Avoid vague praise ("amazing", "incredible") — use one concrete specific instead.
4. **The takeaway** — one sentence distilling what this taught about working with AI, tools, or building — the "why this mattered" line.
5. **Closing line**: exactly `Day <n> of 60 done. Building in public, one decision-worthy tool at a time.` (adjust the trailing clause only if it doesn't fit that day's project, keep the `Day <n> of 60 done.` prefix verbatim).
6. **Hashtags** — 5-8 relevant tags, always include `#60DaysOfAI` and `#ClaudeAI`.
7. **Final line, on its own** (required, exact prefix, do not omit or paraphrase):
   `— Day <n> completed of my 60 Days of Claude AI Challenge, by abtaalks.`

## Style rules

- No emojis.
- No em dashes inside body paragraphs (the closing attribution line's leading em dash is the one exception, per the exact format above).
- Write like a person telling a colleague what happened, not like marketing copy. Short sentences. Specific nouns.
- Never fabricate metrics, user counts, or outcomes that aren't in the day's actual files.
- Keep total length in the 150-250 word range (LinkedIn posts that run long lose readers before the hook pays off).

## Output

After writing the file, tell the user the path and show the post text in the reply.
