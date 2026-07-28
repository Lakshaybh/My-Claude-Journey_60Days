# Capstone Project Log — QueryMind

Tracks daily progress for the 10-day capstone (Days 51-60 of the 60 Days of Claude AI Challenge by AB Talks).

---

## Day 51 — Product Discovery & Sprint Planning
- Interviewed to discover the project idea from scratch (no prior idea).
- Selected: **QueryMind** — AI-powered SQL query generator for data analysts (paste schema → ask in plain English → get SQL + explanation).
- Locked v1.0 scope: no login, no execution, no chat, no file upload, no DAX (deferred to future scope).
- Deliverables: PRD, 9-day Implementation Blueprint (Days 2-10), Pitch Deck — saved in `Day 51/Product Discovery & Sprint Planning/`.

## Day 52 — System Design
- Finalized tech stack: FastAPI + vanilla HTML/CSS/JS (single service, no CORS), no database, no auth, Claude API (Sonnet), Render free-tier hosting.
- Decided to keep the app inside the existing challenge-journal repo, under `Day 52/querymind/`, rather than a separate repo.
- Produced full technical design: `ARCHITECTURE.md`, `SCHEMA.md`, `API.md`, `UI-WIREFRAMES.md`, `PROJECT-STRUCTURE.md` — all saved in `Day 52/`.
- Scaffolded the empty project folder structure under `Day 52/querymind/app/` (no production code yet, per capstone rules).
- Updated the Day 51 Implementation Blueprint to reflect finalized file paths and the no-CORS architecture decision.
- Day 3 readiness check: on track, no scope creep, no blockers — Day 3 can begin implementation immediately using `API.md` as the exact contract.
- Pending: builder to create an Anthropic API key before Day 3 (local development only; nothing goes live until Day 9).

## Day 53 — Project Setup & Foundation
- Closed out Day 2's leftover checklist: created venv, installed dependencies (FastAPI, Uvicorn, Anthropic SDK, python-dotenv), set up `.env.example`/`.gitignore`.
- Built and verified the FastAPI foundation locally: `main.py`, Pydantic request/response models, `GET /api/health`, and a **stubbed** `POST /api/generate` (routing/validation confirmed working, no Claude call yet).
- Built a plain hello-world frontend served directly by FastAPI (no CORS needed, per Day 2's architecture).
- Verified all three routes locally (`/`, `/api/health`, `/api/generate`) — all working.
- Decided branching strategy: direct-to-`main`, small commits (no feature branches — solo, time-constrained build).
- Deliverables: `SETUP.md`, `ENVIRONMENT.md`, `DAY3-SUMMARY.md`, updated `PROJECT-STRUCTURE.md` — saved in `Day 52/`.
- Pending: builder still needs to create the Anthropic API key before Day 4 (only blocker for tomorrow).

## Day 54 — Core Feature Implementation
- Replaced the `/api/generate` stub with real AI-powered SQL generation (schema-grounded prompt + defensive JSON parsing).
- Anthropic account had no usable credit and paid billing was ruled out; switched AI provider to **Groq** (Llama 3.3 70B, free, no card, no disk footprint). Documented transparently in `ARCHITECTURE.md`.
- Verified with multi-table joins, aggregation, and `LIMIT` queries — all correct.
- Deliverables: `Day 54/day54.md` summary + key learnings.

## Day 55 — Reliability Pass + Frontend Build
- Built `app/prompts/validator.py` — flags generated SQL that references tables not present in the pasted schema (hallucination safety net).
- Caught and fixed a gap: Blueprint Day 4's frontend form had never actually been built (only a hello-world stub existed) — built it today so the warning/disclaimer UI had somewhere to attach.
- Ran 11 total test cases (8 varied schema/question pairs including multi-table FKs, ambiguous columns, vague/unrelated questions, typos, special characters; 3 validator unit tests) — all passed, zero false positives.
- Added the "AI-generated — please review" disclaimer to the UI.
- Deliverables: `Day 55/day55.md` summary + key learnings.

## Day 56 — Complete the MVP & Deliver a Working Demo
- Today's prompt asked for a full MVP + live deployment, ahead of the original Day 9 deployment schedule — treated as a deliberate scope compression: lightweight presentable styling now (card layout, styled SQL block, responsive), full branding pass deferred to Day 7.
- Added the required footer: "Built with Claude as part of the AB Talks 60-Day Claude AI Challenge."
- **Deployed live to Render (free tier):** https://querymind-3msv.onrender.com — Root Directory `Day 52/querymind`, `GROQ_API_KEY` set via Render's environment variables (never touched git).
- Caught a real mistake: the first deploy check showed the *old* unstyled site live, because today's changes had been tested locally but not yet pushed to GitHub. Committed, pushed, and confirmed the fresh deploy went live.
- Verified the live public URL end-to-end: styled homepage, footer present, health check passing, and a real AI-generated SQL query returned correctly through the live server.
- Deliverables: `Day 56/day56.md` summary + key learnings.

## Day 57 — Product Refinement & User Experience
- Full senior-level UI/UX polish pass on top of Day 56's MVP: automatic dark mode (via CSS variables + `prefers-color-scheme`), refined typography/spacing, numbered step badges, loading spinner, smooth result fade-in with auto-scroll, improved Copy button with success state, bordered error styling, Enter-to-submit.
- Accessibility pass: `aria-live` regions, visible focus rings, screen-reader-only labels, reduced-motion support.
- No changes to core logic or the API contract — same element IDs throughout, so nothing broke.
- Committed, pushed, confirmed Render auto-deployed, and re-verified the live URL (footer, health check, real multi-table AI generation all still working).
- Deliverables: `Day 57/day57.md` summary + key learnings.

## Day 58 — Testing, Debugging & Production Optimization
- Senior QA/security/performance review of the full codebase found 6 real production-readiness gaps (not new features): no rate limiting, narrow error handling, no request timeout, no server-side logging, missing favicon (console error), no basic security headers.
- Fixed all 6: added `app/core/rate_limit.py` (per-IP, 15 req/min), broadened exception handling with a global JSON error handler, added a 30s timeout + retry to the Groq client, added logging, added an inline favicon, added security headers middleware.
- Ran 14 edge-case test categories (empty/missing/malformed/oversized input, wrong content-type, wrong method, 404s, injection-style text, unicode/emoji, rate-limit triggering, malformed-AI-response resilience) — all passed.
- Confirmed the no-SQL-execution design (from Day 51) doubles as a security boundary — injection-style input is harmless since nothing ever runs the generated SQL.
- Deployed, and re-verified everything on the live public URL (not just localhost).
- Deliverables: `Day 58/day58.md` summary + key learnings.

---

*Next: Day 59 — final documentation pass, README polish, and demo/pitch prep ahead of Day 60's submission.*
