# ARCHITECTURE.md — QueryMind

## 1. Tech Stack (Finalized)

| Layer | Choice | Why |
|---|---|---|
| Frontend | Hand-built HTML/CSS/JS (vanilla, no framework) | Full styling control for the polished UI priority from the PRD; no build tooling needed, keeps daily 1-hour sessions simple; served directly as static files by the backend. |
| Backend | Python + **FastAPI** | Builder already knows Python; FastAPI has automatic request validation (Pydantic), auto-generated docs at `/docs` for free manual testing, async support, and is free/open-source. |
| Server | **Uvicorn** | Standard ASGI server for FastAPI, minimal config. |
| Database | **None** | PRD explicitly excludes accounts, history, and persistence. The app is stateless — every request is self-contained (schema + question in, SQL + explanation out). Adding a DB would violate the "no unnecessary scope" rule. |
| Authentication | **None** | PRD explicitly excludes login (Scope Out, item: "User accounts, authentication"). |
| AI Model/API | **Claude API** (Anthropic Messages API, Claude Sonnet model) | Core requirement from PRD. Sonnet is used (not Haiku) because SQL correctness matters more than raw speed for a low-volume demo tool — accuracy is the product's core value. |
| Hosting | **Render (Free Web Service tier)** | Free, deploys directly from a GitHub repo (supports a "Root Directory" setting so we can point it at `Day 52/querymind` without needing a separate repo), supports environment variables for the API key, and runs Python/Uvicorn natively. |
| Other libraries | `anthropic` (official Python SDK), `python-dotenv` (local env vars), `pydantic` (bundled with FastAPI, request/response validation) | All free, minimal, and match the "no new stack to learn" constraint. |

### Architecture improvement over the original Day 2 blueprint sketch
The original blueprint implied a separate frontend/backend running on different ports (flagging CORS as a "common issue"). Today we simplify: **FastAPI serves the static frontend files directly** (via `StaticFiles`), so frontend and backend are one deployed service. This eliminates CORS entirely and means only one Render service needs to be configured on Day 9 instead of two. This does not change scope or the PRD — it's a pure implementation simplification, so no approval gate is needed, but flagging it here for the record.

---

## 2. Component Diagram

```mermaid
graph TD
    User[User's Browser] -->|loads page| Static[Static Frontend<br/>index.html / style.css / script.js]
    User -->|POST /api/generate| API[FastAPI Backend]
    API -->|calls| Claude[Claude API<br/>Anthropic Messages API]
    Claude -->|SQL + explanation JSON| API
    API -->|JSON response| User
    Static -.served by.-> API
```

**Components:**
- **Static Frontend** — served by the backend itself, no separate hosting needed.
- **FastAPI Backend** — one process, two responsibilities: serve static files, and expose `POST /api/generate`.
- **Claude API** — the only external service. Called once per user request, no state kept between calls.

---

## 3. Data Flow

```mermaid
flowchart LR
    A[User pastes schema] --> B[User types question]
    B --> C[Click Generate]
    C --> D[Frontend validates: both fields non-empty]
    D -->|valid| E[POST /api/generate]
    D -->|invalid| F[Show inline error, no request sent]
    E --> G[Backend validates + builds prompt]
    G --> H[Claude API call]
    H --> I[Backend parses JSON: sql + explanation]
    I --> J{References only<br/>given schema?}
    J -->|yes| K[Return sql + explanation]
    J -->|no| L[Return sql + explanation + warning flag]
    K --> M[Frontend renders output]
    L --> M
```

---

## 4. Request Lifecycle (Sequence Diagram)

```mermaid
sequenceDiagram
    participant U as User (Browser)
    participant F as Frontend (JS)
    participant B as FastAPI Backend
    participant C as Claude API

    U->>F: Paste schema, type question, click Generate
    F->>F: Client-side validation (non-empty fields)
    F->>B: POST /api/generate {schema, question}
    B->>B: Pydantic validation (length limits, non-empty)
    alt invalid request
        B-->>F: 422 Validation Error
        F-->>U: Show error message
    else valid request
        B->>C: Messages API call with schema-grounded prompt
        C-->>B: JSON: {sql, explanation}
        B->>B: Parse JSON, strip markdown fences if present
        B->>B: Validate SQL references only given tables/columns
        B-->>F: 200 OK {sql, explanation, warning?}
        F->>F: Render SQL block + explanation
        F-->>U: Display result with copy button
    end
```

---

## 5. AI Interaction Detail

- **Model:** Claude Sonnet (via Anthropic Messages API).
- **Prompt strategy:** System prompt instructs Claude to act as a SQL expert, to use ONLY the tables/columns provided in the pasted schema, and to always respond with strict JSON (`{"sql": "...", "explanation": "..."}`) — no markdown, no extra prose outside the JSON.
- **Statelessness:** Each request is independent — no conversation history is sent or stored (matches the "single-shot, no chat" PRD requirement).
- **Post-processing:** Backend strips any accidental markdown code fences and validates the JSON shape before returning it to the frontend, so the frontend never has to handle malformed AI output directly.

---

## 6. External Services

| Service | Purpose | Cost |
|---|---|---|
| Anthropic Claude API | Core SQL generation + explanation | Free tier / pay-as-you-go — builder to confirm current Anthropic API pricing/credits before Day 3 |
| Render (Free Web Service) | Hosting the deployed app | Free tier |
| GitHub | Source control (existing repo) | Free |

No other external services, databases, or third-party integrations are required for v1.0.
