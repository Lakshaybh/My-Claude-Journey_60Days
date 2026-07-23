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

---

*Next: Day 54 (Blueprint Day 3) — replace the `/api/generate` stub with the real Claude API call (prompt template + JSON parsing).*
