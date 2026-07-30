# Portfolio Materials — QueryMind

## Project descriptions

**One-liner (for a resume/LinkedIn header):**
> QueryMind — an AI-powered SQL query generator that turns a database schema and a plain-English question into a correct, explained SQL query. Built and shipped solo in 10 days.

**Short (for a portfolio site card, ~40 words):**
> QueryMind lets data analysts paste a database schema and ask a question in plain English to get back correct, ready-to-run SQL with a clear explanation. Built end-to-end — from product discovery through production deployment — in a 10-day solo sprint using FastAPI, Groq, and Render.

**Long (for a portfolio project page, ~150 words):**
> QueryMind is a live, publicly deployed web tool that solves a real problem: data analysts spend significant time translating business questions into correct SQL, especially against unfamiliar schemas. The tool takes a pasted database schema and a plain-English question, and returns a correct SQL query with a plain-English explanation — grounded strictly in the given schema, with a built-in safety check against AI hallucination.
>
> Built solo over a 10-day sprint following a full software development lifecycle — product discovery and PRD, system architecture and API design, implementation, a mid-build AI-provider pivot handled transparently, UI/UX design (including a full interface redesign that was built, evaluated, and cleanly reverted), a dedicated security/QA hardening pass, and production deployment.
>
> Stack: Python, FastAPI, vanilla JavaScript (no framework), Groq (Llama 3.3 70B), deployed on Render's free tier. Live at querymind-3msv.onrender.com.

## Resume bullet points

Pick 2-4 depending on the role and space available:

- Designed and shipped a full-stack AI web application (FastAPI, JavaScript, Groq LLM API) solo in a 10-day sprint, from product discovery through production deployment
- Built a schema-grounded prompt engineering pipeline with defensive JSON parsing and a hallucination-detection safety check, reducing incorrect AI output reaching end users
- Diagnosed and resolved a mid-project AI-provider blocker (Anthropic API access) by evaluating cost, infrastructure, and product-fit tradeoffs, and migrated the integration without downtime or feature loss
- Conducted a structured QA/security review of a production web application, identifying and fixing 6 real gaps (rate limiting, error handling, timeouts, logging, security headers) validated by 14 categories of edge-case testing
- Wrote complete technical documentation (PRD, system architecture, API contracts, database rationale) before implementation, keeping a 10-day solo build on scope and schedule
- Deployed and maintained a production web service on Render with environment-based secret management and zero committed credentials across the project's full history

## Interview talking points

**"Tell me about a project you're proud of."**
Lead with the Day 51 discovery process — you didn't pick a project idea, you interviewed yourself to find a real problem (the DAX/SQL pain point from your own data analyst internship), then deliberately cut scope (no DAX, no execution, no chat) to make a 10-day solo build actually finishable. That scoping discipline is the real story, not just "I built an app."

**"Tell me about a time you had to change your approach mid-project."**
The Day 54 Claude → Groq pivot. Walk through it as a real decision process: cost was ruled out (no paid billing), a local model was considered and ruled out (disk space), and Groq was chosen because it was the only option satisfying both real constraints — and you documented the tradeoff transparently instead of hiding it. This shows engineering judgment under a real external blocker, not just "I found a workaround."

**"How do you handle bugs or gaps you didn't catch immediately?"**
The Day 55 story: found that an entire planned feature (the frontend form) had been skipped, not by a bug report, but by reviewing existing code before adding to it. Pair it with the Day 56/59 "local vs. deployed" mismatch — caught the second time proactively, showing you actually learn from your own mistakes within the same project.

**"Describe your testing/QA approach."**
Day 58: a deliberate release-readiness audit conducted *when nothing was broken* — the harder, more valuable QA instinct. 14 test categories, including confirming a "SQL injection" attempt was harmless by design (because the app never executes generated SQL), turning a scope decision into a demonstrable security property.

**"How do you make design decisions, and how do you handle disagreement with your own earlier choices?"**
Day 57: built a full VS Code-style interface redesign, then reverted it cleanly via git when it wasn't the right direction, and rebuilt with a different visual language. Frame this as evidence that you treat design as iterative and reversible, not precious — and that clean version control made a full pivot low-risk.

## Short demo script (~90 seconds)

1. **(10s) Open with the problem:** "As a data analyst, I write SQL against schemas I don't fully know, constantly. This is QueryMind — it fixes that."
2. **(10s) Show the live URL** loading — point out it's a real, publicly deployed app, not a local demo.
3. **(20s) Paste a schema** (have a 2-3 table example ready), **type a real question** in plain English.
4. **(15s) Click Generate**, let the loading state play, show the SQL + explanation appearing.
5. **(15s) Click Copy SQL**, point out the explanation is written for a non-SQL audience too.
6. **(10s) Mention the safety net:** "If the AI ever references a table that isn't in your schema, it warns you — it never just trusts blindly."
7. **(10s) Close:** "Built solo in 10 days, full lifecycle from product discovery to a hardened, deployed v1.0.0 — and I can walk through any of those decisions."

## Suggested screenshots / demo media

- **Homepage (empty state)** — shows the clean input UI and the value proposition immediately
- **Result state** — schema + question filled in, SQL and explanation visible, ideally on a slightly complex multi-table example so it doesn't look trivial
- **Mobile view** — proves the responsive work from Day 57 wasn't skipped
- **The warning state** (deliberately trigger it with a contrived example) — shows the safety net is real, not just claimed
- **A short screen recording (15-20s)** of the actual generate → result flow, showing the loading spinner and reveal animation — more convincing than any static screenshot for showing the polish from Days 57-58

## Recommended GitHub repository metadata

**Repository description (160 char max):**
> AI-powered SQL query generator. Paste a schema, ask in plain English, get correct SQL + explanation. FastAPI + Groq. Built solo in a 10-day sprint.

**Topics to add** (GitHub repo page → gear icon next to "About" → Topics):
`sql` `ai` `fastapi` `python` `llm` `groq` `sql-generator` `data-analytics` `natural-language-processing` `render` `javascript` `claude-ai`

**Social preview image:** GitHub repo Settings → Social preview — upload one of the suggested screenshots above (the result-state one works best) so shared repo links look intentional, matching the Open Graph work already done on the live app itself (Day 59).

**Website field:** set to the live demo URL in the repo's "About" section, so it shows directly under the repo name on GitHub.
