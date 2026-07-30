# 30-Day Growth Plan — QueryMind v1.0.0 → v2.0

A realistic, one-milestone-per-day roadmap building directly on the existing stack (FastAPI + Groq + vanilla JS + Render, no database in v1.0.0). Each day assumes ~1 hour, same pace as the original 10-day build. Use `daily-build-prompt.md` each day, changing only the day number.

## Week 1 — Automated testing & column-level validation (Days 1-7)
The highest-leverage gap from the retrospective: v1.0.0 has no committed automated test suite.

1. Install `pytest`, write the first test file for `app/prompts/validator.py`'s table-detection logic.
2. Add tests for `extract_json` in `app/prompts/sql_prompt.py` (clean JSON, fenced JSON, broken JSON).
3. Add tests for `GenerateRequest`/`GenerateResponse` schema validation edge cases.
4. Add integration tests hitting `/api/generate` with a mocked Groq client (no real API calls in CI).
5. Set up GitHub Actions to run the test suite on every push.
6. Design column-level validation carefully (the feature deliberately cut on Day 55) — start with a conservative rule: only flag unqualified column names with zero ambiguity.
7. Implement and test the column validator; ship it behind the existing `warning` field, no API contract change.

## Week 2 — DAX support (Days 8-14)
The feature explicitly deferred to "future scope" on Day 51.

8. Write `app/prompts/dax_prompt.py`, mirroring `sql_prompt.py`'s structure.
9. Add a `query_type` field to `GenerateRequest` (`"sql"` or `"dax"`, default `"sql"` — backward compatible).
10. Wire the new prompt into `/api/generate`, routed by `query_type`.
11. Test DAX generation against 5+ Power BI-style schemas.
12. Add a toggle in the frontend UI (SQL / DAX) — minimal, matches existing design system.
13. Update `API.md` and the README to document the new mode.
14. Deploy and verify both modes live.

## Week 3 — Schema upload & UX depth (Days 15-21)
Removing the biggest onboarding friction: manually pasting schema text.

15. Add a file input for `.sql` schema files, parsed client-side, populating the existing textarea (no backend change needed).
16. Add drag-and-drop for the schema file input.
17. Add 2-3 example schemas as one-click "try it" presets, so a first-time visitor doesn't face a blank page.
18. Add a lightweight query-history feature using `localStorage` (client-side only — no backend/database needed, respects the v1.0.0 no-database decision).
19. Polish the history UI (list of recent questions, click to reload).
20. Full mobile QA pass on the new features.
21. Deploy and verify.

## Week 4 — Real persistence, positioning, and hardening (Days 22-30)
This week deliberately revisits the "no database" decision — the first time it should be revisited, now that demand is proven.

22. Decide and provision the lightest viable persistence (SQLite on Render's disk, or a free-tier Postgres) — document the decision like Day 52 did for the original no-DB choice.
23. Add an opt-in "save this query" feature (still no accounts — a shareable link per saved query, e.g. via a short random ID).
24. Build the `/q/{id}` route to view a saved query.
25. Add basic abuse protection for the new persistence layer (the same rate-limiting instinct from Day 58, applied to a new surface).
26. Write a CONTRIBUTING.md if opening the repo to outside contributors (intentionally skipped in v1.0.0 as out of scope).
27. Full accessibility re-audit now that new UI surfaces exist (file upload, history, saved-query view).
28. Write real screenshots and update the README's screenshot section (left as a placeholder in v1.0.0).
29. Tag and release v2.0.0 following the same process as `Day 60/day60.md`'s v1.0.0 release.
30. Write a v2.0.0 retrospective — same honest, decision-by-decision format as `challenge-retrospective.md` — and decide the next 30-day plan based on what actually got used.
