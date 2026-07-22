# API.md — QueryMind

No implementation today — this is the full contract to build against on Day 3. All endpoints are unauthenticated (no login, per PRD).

---

## 1. `GET /`

**Purpose:** Serve the frontend application (index.html + static assets).

**Request:** No parameters.

**Response:** `200 OK`, `text/html` — the main page.

**Validation:** None (static file serve).

**Authentication:** None.

**Error cases:** None expected — if static files are missing, this is a deployment bug, not a user-facing error case.

---

## 2. `POST /api/generate`

**Purpose:** Core endpoint. Accepts a pasted schema and a plain-English question, returns generated SQL and a plain-English explanation.

**Request:**
```json
{
  "schema_text": "CREATE TABLE customers (...); CREATE TABLE orders (...);",
  "question": "Show total sales by region for last quarter"
}
```

**Response (success):**
```json
{
  "sql": "SELECT region, SUM(amount) AS total_sales\nFROM orders\nJOIN customers ON orders.customer_id = customers.id\nWHERE order_date >= '...'\nGROUP BY region;",
  "explanation": "This query joins orders and customers to total sales per region, filtered to last quarter.",
  "warning": null
}
```

**Response (success, with schema-mismatch warning):**
```json
{
  "sql": "...",
  "explanation": "...",
  "warning": "This query references a column that wasn't found in your pasted schema. Please double-check before using it."
}
```

**Validation:**
- `schema_text`: required, non-empty after trimming whitespace, max ~8000 characters.
- `question`: required, non-empty after trimming whitespace, max ~500 characters.
- Both fields validated via Pydantic at the FastAPI layer — invalid requests never reach the Claude API call (saves cost and time).

**Authentication:** None.

**Error cases:**
| Case | Status | Response body |
|---|---|---|
| Empty/missing `schema_text` or `question` | `422 Unprocessable Entity` | FastAPI's default Pydantic validation error detail |
| Input exceeds max length | `422 Unprocessable Entity` | Same as above |
| Claude API call fails (timeout, rate limit, API error) | `502 Bad Gateway` | `{"error": "AI service is temporarily unavailable. Please try again."}` |
| Claude returns unparseable output (malformed JSON after retries) | `500 Internal Server Error` | `{"error": "Could not generate a valid response. Please try rephrasing your question."}` |

---

## 3. `GET /api/health`

**Purpose:** Simple health check endpoint — useful for confirming the deployed service is up (especially after Render free-tier cold starts on Day 9), and as a "warm-up" ping before a live demo.

**Request:** No parameters.

**Response:**
```json
{ "status": "ok" }
```

**Validation:** None.

**Authentication:** None.

**Error cases:** None expected — if the server process is running, this always returns 200.

---

## 4. Endpoint Summary Table

| Method | Path | Purpose | Auth |
|---|---|---|---|
| GET | `/` | Serve frontend | None |
| POST | `/api/generate` | Generate SQL + explanation | None |
| GET | `/api/health` | Health check | None |

Three endpoints total — deliberately minimal, matching the single-shot, no-account PRD scope.
