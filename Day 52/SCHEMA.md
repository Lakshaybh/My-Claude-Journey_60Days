# SCHEMA.md — QueryMind

## 1. Does this project need a database?

**No.** Per the PRD (Section 4 & 7): no user accounts, no saved history, no query execution against a real database. Every request is fully self-contained — the user supplies the schema and the question in the same request that produces the answer. There is nothing to persist between requests.

Adding a database here would be scope creep with no PRD-backed justification — flagged and rejected per the "no unnecessary scope" rule.

## 2. Validation against PRD user stories

| User story (from PRD) | Requires persistence? | Notes |
|---|---|---|
| Paste schema as text | No | Held in-memory for the duration of one request only |
| Ask a plain-English question | No | Same as above |
| Receive generated SQL | No | Returned directly in the API response |
| Receive plain-English explanation | No | Same request/response cycle |
| Copy SQL to clipboard | No | Client-side only, no backend involvement |
| No login | No | Confirms no user table is needed |

Every user story is satisfiable with a single stateless request/response — confirming no database is required for v1.0.

## 3. In-Memory / Request Data Model (not a database — request & response shape only)

Since there's no persistent storage, the "schema" for this project is really the **shape of data passed between frontend and backend**, defined as Pydantic models in the backend (to be implemented Day 3, not today).

### `GenerateRequest` (incoming)
| Field | Type | Constraints |
|---|---|---|
| `schema_text` | string | required, non-empty, max length ~8000 characters (protects against abuse and excessive token usage) |
| `question` | string | required, non-empty, max length ~500 characters |

### `GenerateResponse` (outgoing)
| Field | Type | Constraints |
|---|---|---|
| `sql` | string | the generated SQL query |
| `explanation` | string | plain-English explanation of the query |
| `warning` | string \| null | present only if the validation step detects the SQL references a table/column not found in the pasted schema |

No relationships, no constraints beyond field-level validation, no migrations — because there are no persisted entities.

## 4. Future Scope Note
If **Future Scope** items are ever built (query history, accounts), a real database (e.g., free-tier PostgreSQL on Render or SQLite for a simple start) would be introduced then — explicitly out of scope for v1.0 and not designed today.
