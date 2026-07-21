# Product Requirements Document (PRD)

## Project Name
**QueryMind** — AI-Powered SQL Query Generator for Data Analysts
*(working name — can be finalized/rebranded on Day 2 if desired)*

## 1. Problem Statement
Data analysts (and interns) spend significant time each day translating business questions into correct SQL syntax — remembering joins, functions, and matching questions to the right tables/columns in a schema they may not fully know. This is repetitive, error-prone, and slows down actual analysis work.

## 2. Target Users
- **Primary:** Data analyst interns/students who work across different schemas and need quick, correct SQL without memorizing syntax.
- **Secondary:** Junior data analysts, BI trainees, and non-technical stakeholders who understand their data but not SQL syntax.

## 3. Solution Overview
A single-page web tool where a user:
1. Pastes their database schema as `CREATE TABLE` statements.
2. Types a business question in plain English.
3. Receives a correct, ready-to-use SQL query **and** a plain-English explanation of what the query does.

No login, no file uploads, no live database connection, no chat — one clean, focused, single-shot interaction.

## 4. v1.0 Scope (In)
| Feature | Description |
|---|---|
| Schema input | Text area to paste `CREATE TABLE` statements |
| Question input | Text area for a plain-English question |
| SQL generation | Claude generates a syntactically correct SQL query based on the schema + question |
| Plain-English explanation | A short explanation of what the generated query does, in non-technical language |
| Copy/clean output | Formatted, readable SQL output the user can copy |
| Polished UI | Clean, professional, minimal interface — the top priority for demo quality |
| Public deployment | Live, publicly accessible link, no login required |

## 5. v1.0 Scope (Out — explicitly deferred to "Future Scope")
- DAX / Power BI query generation
- Live query execution against a real database
- Multi-turn / chat-style conversation and query refinement
- Schema file uploads (.sql/.csv)
- User accounts, authentication, saved history
- Auto-generated example questions from schema
- Table/column usage highlighting

## 6. Success Criteria (Day 10 Definition of Done)
- Tool is live and publicly accessible via a shareable URL.
- A user can paste any reasonable schema, ask a question, and reliably get back a correct SQL query + explanation.
- UI is clean, professional, and free of visual bugs across desktop and mobile widths.
- A clear demo story (problem → solution → impact) exists and can be told in under 2 minutes.
- Basic error handling exists (e.g., empty inputs, malformed schema) — no crashes during a live demo.

## 7. Constraints
- Builder has ~1 hour/day of focused time for 9 remaining days.
- Builder is comfortable with Python, SQL, Excel, and at least one web framework — no time budgeted for learning a new stack from scratch.
- No paid tools/services will be used unless explicitly requested.
- Tech stack to be decided on Day 2, not today.

## 8. Key Risks & Mitigations
| Risk | Mitigation |
|---|---|
| Scope creep (chat, execution, DAX) | Strict adherence to "Out" list above; anything new goes to Future Scope |
| AI generates incorrect/invalid SQL | Prompt engineering with schema-grounding + clear disclaimers ("AI-generated, review before use") |
| Limited daily time causes slippage | Each day scoped to fit inside ~1 hour with a clear, minimal checklist |
| UI polish eats into functional time | UI work is scheduled in dedicated days after core logic works, not mixed in |

## 9. Future Scope (Post-v1.0)
- DAX/Power BI query generation
- Live execution against a connected sample database
- Multi-turn conversational refinement
- Schema file upload support
- Query history and saved sessions (would require accounts)
- Auto-suggested example questions per schema

## 10. Success Metric for the Challenge
A polished, working, publicly deployed v1.0 by Day 10, with a clear PRD, blueprint, and pitch deck showing a complete, real software development lifecycle.
