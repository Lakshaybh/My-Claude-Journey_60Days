# Future Scope — QueryMind

How this specific project could realistically evolve past v1.0.0. Every item here is scoped against what QueryMind already is today: a stateless, single-shot, no-login SQL generator built on FastAPI + Groq, deliberately kept small to ship in 10 days. This is not a generic roadmap — it's the actual next layer on top of the actual v1.0.0 architecture.

## Next 3 Months — Depth on the core feature

The core loop (schema in, SQL out) is proven. The next phase makes that loop smarter and more trustworthy, without changing its shape.

- **Column-level validation**, extending `app/prompts/validator.py` beyond table-name checking (a deliberate v1.0.0 scope cut, documented in Day 55) to also flag hallucinated column names — carefully, to avoid the false-positive risk that caused the original scope cut.
- **DAX/Power BI generation** as a second output mode alongside SQL — the exact feature deferred on Day 51 when SQL vs. DAX was chosen as v1.0.0's single focus. The prompt architecture in `app/prompts/sql_prompt.py` already isolates prompt logic cleanly enough to add a parallel `dax_prompt.py` without touching the API layer.
- **Schema file upload** (`.sql` file, not just pasted text) — removes the copy-paste friction that's currently the biggest onboarding cost for a first-time user.
- **A real automated test suite** (pytest) around `app/prompts/validator.py` and `app/prompts/sql_prompt.py`'s JSON extraction — today's testing (Days 55 and 58) was thorough manual/scripted verification, not a committed, repeatable test suite a future contributor could run.

## Next 6 Months — From tool to workflow

Once the core is battle-tested, the natural next step is making QueryMind fit into how analysts actually work day to day, not just a one-off question box.

- **Multi-turn refinement** ("now filter to last quarter") — deliberately excluded from v1.0.0 (Day 51) to keep the interaction single-shot and buildable in one session. With the core generation logic proven reliable, this becomes the highest-leverage feature to add, since it's the single biggest gap between "cool demo" and "tool I use daily."
- **Query history** (would require the database layer that v1.0.0 explicitly has none of, per `SCHEMA.md`) — even a lightweight SQLite table on Render would let users revisit past questions without needing full accounts.
- **A VS Code extension or CLI**, since the underlying `/api/generate` contract is already a clean, documented REST endpoint (`API.md`) that doesn't care what the frontend looks like — the current web UI is one client, not the only possible one.

## Next 12 Months — Positioning as a real product

- **Team/workspace support**: shared schemas within a team, so a company's actual database structure doesn't need to be re-pasted by every analyst — this is the point where the "no accounts" decision from Day 51 would need deliberate revisiting, not casual scope creep.
- **Direct integration with BI tools** (Power BI, Looker, Metabase) as a plugin, using the DAX support from the 3-month phase as the entry point.
- **A hosted, paid tier** on top of the still-free core tool, if usage patterns from the live deployment (Render) show real recurring demand — the free/open-core v1.0.0 stays exactly as it is; a paid tier would be additive, not a replacement.

## What stays out of scope, permanently

Live query execution against a real database was excluded from Day 51 onward as a deliberate security and simplicity boundary (confirmed as a real security benefit during Day 58's testing — injection-style input is harmless specifically because nothing ever runs the generated SQL). Any future roadmap that reintroduces execution needs to treat that as a first-class security redesign, not a feature toggle.
