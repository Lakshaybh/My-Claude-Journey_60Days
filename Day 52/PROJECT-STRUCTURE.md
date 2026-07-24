# PROJECT-STRUCTURE.md — QueryMind

## 1. Full Folder Structure

```
Day 52/
├── ARCHITECTURE.md
├── SCHEMA.md
├── API.md
├── UI-WIREFRAMES.md
├── PROJECT-STRUCTURE.md
├── SETUP.md
├── ENVIRONMENT.md
├── DAY3-SUMMARY.md
└── querymind/                     <- deployable app root (Render "Root Directory" points here)
    ├── venv/                      <- local virtual environment (git-ignored, not committed)
    ├── app/
    │   ├── __init__.py
    │   ├── main.py                <- FastAPI app entrypoint: creates app, mounts static, includes routers ✅ built Day 3
    │   ├── api/
    │   │   ├── __init__.py
    │   │   ├── generate.py        <- POST /api/generate route handler — ✅ real AI call wired up Day 4
    │   │   └── health.py          <- GET /api/health route handler ✅ built Day 3
    │   ├── core/
    │   │   ├── __init__.py
    │   │   ├── config.py          <- loads GROQ_API_KEY via python-dotenv ✅ built Day 3, updated Day 4
    │   │   └── groq_client.py     <- thin wrapper around the Groq SDK call (was claude_client.py — see ARCHITECTURE.md) ✅ built Day 4
    │   ├── prompts/
    │   │   ├── __init__.py
    │   │   └── sql_prompt.py      <- schema-grounded prompt template + JSON parsing/validation ✅ built Day 4
    │   ├── models/
    │   │   ├── __init__.py
    │   │   └── schemas.py         <- Pydantic request/response models (GenerateRequest, GenerateResponse) ✅ built Day 3
    │   └── static/                <- the entire frontend, served directly by FastAPI ✅ hello-world built Day 3
    │       ├── index.html
    │       ├── css/
    │       │   └── style.css
    │       └── js/
    │           └── script.js
    ├── requirements.txt           <- fastapi, uvicorn, groq, python-dotenv ✅ installed Day 3, updated Day 4
    ├── .env.example                <- documents required env vars (GROQ_API_KEY) without real secrets ✅ created Day 3, updated Day 4
    ├── .gitignore                  <- excludes .env, __pycache__, venv, *.log ✅ created Day 3
    └── README.md                   <- project-specific README — ⏳ to be finalized Day 9/10
```

**Status legend:** ✅ = built and verified working today (Day 3/53). ⏳ = scaffolded in design docs, implementation scheduled for a later day — do not build early.

## 2. What Every Folder Is Responsible For

| Folder/File | Responsibility |
|---|---|
| `app/main.py` | Wires everything together: creates the FastAPI instance, mounts `app/static` as the served frontend, registers the `api/` routers. This is the only file that "assembles" the app. |
| `app/api/` | HTTP layer only — each file handles one route's request/response cycle. No business logic lives here beyond calling into `core/` and `prompts/`. |
| `app/core/` | Cross-cutting concerns: configuration/env loading and the Claude API client wrapper. Anything another route might need to reuse lives here. |
| `app/prompts/` | All prompt-engineering logic in one place — the system prompt text, the JSON-parsing/cleanup logic, and the schema-validation check (does the SQL only reference given tables/columns). Isolating this makes Day 5's "reliability pass" easy to do without touching route code. |
| `app/models/` | Pydantic schemas — the single source of truth for what a valid request/response looks like. FastAPI uses these automatically for validation and for the auto-generated `/docs` page. |
| `app/static/` | The entire frontend. Kept as plain HTML/CSS/JS, no build step, so any change is a direct file edit with no compile step to slow down 1-hour sessions. |
| `requirements.txt` | Pinned dependency list for reproducible installs and for Render to install on deploy. |
| `.env.example` | Documents `ANTHROPIC_API_KEY` (and any other future var) without ever committing the real key. |
| `README.md` (inside `querymind/`) | App-specific documentation — setup instructions, live link (added Day 9), screenshots (added Day 10). Distinct from the top-level challenge-journal README. |

## 3. Where Future Code Will Live
- Day 3 (backend logic): `app/prompts/sql_prompt.py`, `app/core/claude_client.py`, `app/api/generate.py`, `app/models/schemas.py`.
- Day 4 (frontend wiring): `app/static/index.html`, `app/static/js/script.js`.
- Day 5 (reliability pass): edits confined to `app/prompts/sql_prompt.py` and validation logic in `app/api/generate.py`.
- Day 6–7 (UI polish/motion): `app/static/css/style.css`, `app/static/js/script.js`.
- Day 9 (deployment): `requirements.txt`, `.env.example`, plus a Render service configuration (done in the Render dashboard, not a repo file).

## 4. Why This Structure Was Chosen
- **Single deployable unit** (`querymind/`) — avoids the two-service/CORS complexity flagged in the original blueprint; Render can point its "Root Directory" setting at this one folder even though it lives inside the larger challenge-journal repo.
- **Separation by responsibility, not by file type** — `api/`, `core/`, `prompts/`, `models/` each have one job, so a fresh AI conversation on any future day can be pointed at exactly one folder without needing full-repo context.
- **No build tooling for the frontend** — matches the 1-hour/day constraint; every frontend change is a direct, immediately-visible file edit.
- **Flat and shallow** — no nested app-within-app complexity; a small v1.0 product doesn't need more than this.
