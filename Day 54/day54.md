# Day 54 — Core Feature Implementation (QueryMind Capstone)

Part of the 10-day QueryMind capstone (Days 51-60) in the 60 Days of Claude AI Challenge by AB Talks.
All project code lives in `Day 52/querymind/` (kept in one place across the capstone) — this file documents what Day 54's session built there.

## What we did today

Built the real, working core feature of QueryMind: the part that actually reads a database schema and a plain-English question, and generates a correct SQL query with an explanation.

**Files created/modified in `Day 52/querymind/`:**
- `app/prompts/sql_prompt.py` (new) — the instructions given to the AI: act as a SQL expert, only use tables/columns from the given schema, respond with strict JSON (`sql` + `explanation`). Includes a defensive JSON extractor in case the AI adds extra text around the JSON.
- `app/core/groq_client.py` (new) — the code that actually sends the request to the AI service and gets a response back.
- `app/core/config.py` (updated) — now loads the AI service's API key from the `.env` file.
- `app/api/generate.py` (updated) — the `/api/generate` endpoint now calls the real AI instead of returning fake placeholder text, and handles errors cleanly (bad AI response, service unavailable, etc.).
- `requirements.txt` (updated) — added the `groq` package.
- `.env.example` (updated) — documents the new required key.

**Tested and verified working** with real requests: a simple single-table schema, a multi-table schema with joins, and a question requiring grouping + sorting + limiting results (top 3 best-selling products). All returned correct SQL and clear explanations.

## A key decision made today: switching AI providers

The plan was to use Claude's API. When we tried to actually connect it, the Anthropic account had no usable credit balance and wasn't eligible for free trial credits. Rather than add paid billing (explicitly something we wanted to avoid) or install a large local AI model (which needed more disk space than was available), we switched to **Groq**, a service that provides free API access (no card required) to a capable open-source AI model (Llama 3.3).

This was a real, documented tradeoff — the project no longer literally uses Claude's API for its AI feature, even though it's built for the Claude AI Challenge. This is written about openly in `Day 52/ARCHITECTURE.md` rather than hidden, since transparency matters more than pretending nothing changed.

## Documentation updated today
- `Day 52/ARCHITECTURE.md` — AI provider section rewritten to explain the Groq switch and why
- `Day 52/ENVIRONMENT.md` — environment variable and dependency tables updated
- `Day 52/PROJECT-STRUCTURE.md` — file statuses updated to show what's built vs. still planned
- `Day 51/Product Discovery & Sprint Planning/Implementation_Blueprint_Days2-10.md` — Day 3 section marked complete, updated to reflect the Groq change

## Key learnings from today

1. **Plans meet reality, and that's normal.** The original design assumed Claude's API would just work. It didn't, because of a billing account issue outside our control. The right response wasn't to panic or force it — it was to pause, explain the tradeoffs of each alternative honestly, and make a clear decision.

2. **"No API key" almost never really means no AI at all.** When asked to avoid "API things," the real underlying worries were about cost and disk space, not about calling an AI service in general. Asking clarifying questions one at a time uncovered the actual constraint instead of guessing wrong and building the wrong thing.

3. **Free doesn't have to mean worse.** Groq's free tier produced correct, well-structured SQL across every test case today, including a 3-table join with grouping and sorting — proving a $0 solution can still meet the project's quality bar.

4. **Documenting a pivot honestly is part of the job.** Instead of quietly swapping Claude for Groq and hoping nobody noticed, every design doc affected by the change was updated to say exactly what changed and why — so the project stays trustworthy and explainable on Day 10.

5. **API keys pasted into a chat should be treated as exposed.** Even though the keys never touched git (`.env` is git-ignored), pasting them into a conversation is still a real exposure — good practice is to revoke and regenerate them afterward, which is one of today's small but important housekeeping lessons.

## What's next
Day 55 (Blueprint Day 5): stress-test the AI with harder schemas and messier questions, and add a safety-net warning for when the AI's answer references something outside the given schema.
