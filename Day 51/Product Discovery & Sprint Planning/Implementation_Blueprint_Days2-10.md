# Implementation Blueprint — QueryMind (Days 2–10)

**Single source of truth for the rest of this capstone.** Each day assumes a fresh AI conversation — paste the relevant day's section (plus the PRD) to continue building without re-deciding architecture.

**Project:** AI-Powered SQL Query Generator for Data Analysts
**Builder availability:** ~1 focused hour/day
**Core flow (locked, do not change):** paste schema (`CREATE TABLE` text) → ask plain-English question → receive generated SQL + plain-English explanation. Single-shot. No login. No execution. No file upload.

**Day 2 technical design docs (read these before starting Day 3):** `Day 52/ARCHITECTURE.md`, `Day 52/SCHEMA.md`, `Day 52/API.md`, `Day 52/UI-WIREFRAMES.md`, `Day 52/PROJECT-STRUCTURE.md`. All file paths referenced below (e.g. `app/api/generate.py`) live under `Day 52/querymind/`.

---

## Day 2 — Tech Stack Decision + Project Setup ✅ COMPLETED

🎯 **Objective:** Choose the simplest tech stack that fits a 1-hour/day, no-new-learning-curve constraint, and get a running skeleton project.

📖 **What I'll learn:** How to make a fast, low-risk architecture decision and scaffold a project cleanly.

🛠 **Features to build:** Empty but running app — one page that loads, nothing functional yet.

**FINALIZED STACK (see `ARCHITECTURE.md` for full rationale):**
- Frontend: hand-built HTML/CSS/JS, no framework, no build step
- Backend: Python + FastAPI + Uvicorn
- Database: none (stateless app, no accounts/history per PRD)
- Auth: none (per PRD)
- AI: Claude API (Anthropic Messages API, Sonnet model)
- Hosting: Render free Web Service tier
- **Key simplification:** FastAPI serves the frontend as static files directly (`StaticFiles` mount) — one deployed service, not two. This removes CORS entirely from the project (the original Day 2/Day 4/Day 9 CORS warnings below no longer apply).
- **Repo decision:** kept inside the existing `My-Claude-Journey_60Days` repo, under `Day 52/querymind/` (not a separate repo). Render will be configured on Day 9 with Root Directory = `Day 52/querymind`.

📂 **Actual folder structure created (see `PROJECT-STRUCTURE.md` for full detail):**
```
Day 52/querymind/
  app/
    main.py
    api/{generate.py, health.py}
    core/{config.py, claude_client.py}
    prompts/sql_prompt.py
    models/schemas.py
    static/{index.html, css/style.css, js/script.js}
  requirements.txt
  .env.example
  .gitignore
  README.md
```

🔗 **Tools to integrate:** Anthropic Claude API (get API key), FastAPI/Uvicorn, `anthropic` Python SDK, `python-dotenv`, git/GitHub (existing repo).

🧪 **Testing tasks:** Confirm local server starts without errors; confirm `.env` is git-ignored (no secrets committed).

🐞 **Common issues:** Port already in use; missing `.env` causing crash on startup — add a clear error message instead of a stack trace.

✅ **End-of-day checklist:**
- [x] Tech stack decided and documented (`ARCHITECTURE.md`)
- [x] Project folder structure created (empty scaffold, no production code yet)
- [ ] Git repo — commit pending at end of Day 2 session
- [ ] Local server runs and shows a blank/hello page — **this happens Day 3**, since FastAPI app code (`main.py`) is written then, not today
- [ ] Claude API key obtained and stored safely in `.env` — to confirm with builder before Day 3 starts

📸 **Expected state/screenshot:** Folder structure created; no running server yet (that's Day 3, since today was design-only per capstone rules).

➡️ **Handoff notes:** Stack is locked — Day 3 builds the backend logic that calls Claude with schema + question and returns SQL + explanation, using the exact file paths above (`app/main.py`, `app/api/generate.py`, `app/prompts/sql_prompt.py`, `app/models/schemas.py`). Full endpoint contract already specified in `API.md` — implement to that spec exactly, no redesign needed. Do not revisit stack choice after today.

---

## Day 3 — Backend: Core AI Query Generation Logic

🎯 **Objective:** Build the backend endpoint that takes schema + question and returns SQL + explanation from Claude.

📖 **What I'll learn:** Prompt engineering for structured, reliable AI output; basic API endpoint design.

🛠 **Features to build:** One backend endpoint (e.g. `POST /generate`) that accepts `{schema, question}` and returns `{sql, explanation}`.

📝 **Step-by-step plan:**
1. Write the core prompt template: instruct Claude to act as a SQL expert, given a schema and a question, output ONLY valid SQL plus a separate plain-English explanation — request structured output (e.g., JSON with `sql` and `explanation` keys) so the frontend can parse it reliably.
2. Implement the endpoint calling the Claude API with this prompt.
3. Add basic input validation (reject empty schema or empty question with a clear error).
4. Test with 3–4 sample schemas and questions manually (e.g., a simple `orders`/`customers` schema).
5. Add a system-level instruction reminding Claude to only use tables/columns present in the given schema, and to say so clearly if the question can't be answered from the schema.

📂 **Files to create/modify:** `app/api/generate.py` (route handler, per `API.md`), `app/prompts/sql_prompt.py` (prompt template + JSON parsing), `app/models/schemas.py` (Pydantic request/response models), `app/core/claude_client.py` (Claude API wrapper), `app/main.py` (wire the router in), `requirements.txt`.

🔗 **Tools:** Anthropic Claude API (Messages API), structured output via JSON instruction.

🧪 **Testing tasks:** Test with valid schema/question pairs; test with a nonsensical question; test with an empty schema; confirm JSON output parses correctly every time.

🐞 **Common issues:** Claude wrapping output in markdown code fences (strip them before parsing); inconsistent JSON formatting (add explicit "respond with ONLY valid JSON" instruction); API key not loading (double-check `.env` loading).

✅ **End-of-day checklist:**
- [ ] `/generate` endpoint works via a manual test (Postman, curl, or simple script)
- [ ] Returns clean `sql` and `explanation` fields
- [ ] Handles empty/invalid input gracefully
- [ ] Tested with at least 3 different schema/question pairs

📸 **Expected state:** Terminal or API client showing a successful JSON response with SQL + explanation for a test question.

➡️ **Handoff notes:** Backend logic works standalone. Day 4 builds the frontend UI (structure only, no styling polish yet) and wires it to this endpoint.

---

## Day 4 — Frontend: Core UI Structure + Wiring

🎯 **Objective:** Build the functional (unstyled) UI and connect it to the backend so the full flow works end-to-end.

📖 **What I'll learn:** Connecting a frontend form to a backend API; handling loading/error states in the UI.

🛠 **Features to build:** Schema textarea, question textarea, "Generate" button, output area showing SQL + explanation.

📝 **Step-by-step plan:**
1. Build basic HTML structure: schema input, question input, submit button, output section (split into "SQL" and "Explanation" blocks).
2. Write JS to call the `/generate` endpoint on submit, show a loading state, and render the response.
3. Handle and display errors (e.g., "Please paste a schema first").
4. Keep styling minimal/unstyled today — structure and function only.
5. Manually test the full flow in the browser: paste schema → ask question → see SQL + explanation appear.

📂 **Files to modify:** `app/static/index.html`, `app/static/js/script.js`.

🔗 **Tools:** Fetch API calling `/api/generate` on the same origin (no CORS needed — FastAPI serves the frontend itself, per the Day 2 architecture decision).

🧪 **Testing tasks:** Full manual end-to-end test with 3+ schema/question combos; test loading state appears; test error messages show correctly for empty inputs.

🐞 **Common issues:** Button submitting multiple times if clicked repeatedly (disable button while loading); forgetting to call `/api/generate` (not `/generate`) — check `API.md` for exact paths.

✅ **End-of-day checklist:**
- [ ] Full flow works in browser: input → generate → output displayed
- [ ] Loading state visible during generation
- [ ] Error states display clearly for bad input
- [ ] No CORS or console errors

📸 **Expected state/screenshot:** Browser screenshot showing schema pasted, question typed, and SQL + explanation displayed on screen (unstyled is fine).

➡️ **Handoff notes:** Core product works end-to-end but looks plain. Day 5 focuses on hardening the AI output quality and edge cases before we invest time in visual polish — don't polish UI yet.

---

## Day 5 — Reliability Pass: Prompt Refinement + Edge Cases

🎯 **Objective:** Make the AI output consistently correct and handle real-world messy input gracefully.

📖 **What I'll learn:** Iterative prompt refinement; defensive handling of unpredictable AI output.

🛠 **Features to build:** No new UI features — this is a quality/reliability day for the existing flow.

📝 **Step-by-step plan:**
1. Test with harder schemas: multiple tables with foreign keys, ambiguous column names, larger schemas (5+ tables).
2. Test with vague/unclear questions and confirm Claude either makes a reasonable assumption and states it, or asks for clarification within the explanation (not a chat — just a clear disclaimer in the explanation text).
3. Refine the prompt template based on failures observed (e.g., wrong joins, hallucinated columns not in schema).
4. Add a lightweight validation step: check the returned SQL references only table/column names present in the pasted schema; if not, flag a warning in the UI.
5. Add a clear on-screen disclaimer: "AI-generated — please review before running."

📂 **Files to modify:** `app/prompts/sql_prompt.py`, `app/api/generate.py` (add validation logic), `app/static/index.html` (disclaimer text).

🔗 **Tools:** None new — refinement of existing Claude integration.

🧪 **Testing tasks:** Run 8–10 varied schema/question tests; log which fail and why; confirm disclaimer displays; confirm validation warning triggers correctly on a deliberately bad case.

🐞 **Common issues:** Over-fitting the prompt to one test case and breaking another — keep a running list of test cases and re-run all of them after each prompt change.

✅ **End-of-day checklist:**
- [ ] 8+ test cases run, most producing correct/reasonable SQL
- [ ] Validation warning works for hallucinated table/column names
- [ ] Disclaimer visible in UI
- [ ] Prompt template finalized (documented in `prompts.py` comments)

📸 **Expected state:** Screenshot of a successful complex-schema test, and one showing the validation warning triggering correctly.

➡️ **Handoff notes:** Core logic is now trustworthy. Day 6 begins visual design direction — no more prompt changes unless a bug is found later.

---

## Day 6 — UI Design Direction + Branding

🎯 **Objective:** Establish the visual identity and layout direction before writing final CSS — avoid random styling decisions.

📖 **What I'll learn:** Applying a design system (branding, spacing, typography, color) consistently to a real product.

🛠 **Features to build:** Finalized visual design plan: color palette, typography, layout structure, component styling direction — applied using the `/exl-branding`, `/exl`, and `/minimalist-ui` design skills for a clean, professional, corporate-data-tool feel.

📝 **Step-by-step plan:**
1. Invoke `/minimalist-ui` and `/exl-branding` (or `/exl`) skill guidance to define: color palette (likely a confident single accent color on clean neutral space, per EXL-style branding), typography pairing, spacing scale.
2. Redesign the page layout: clear hero/header (product name + one-line value prop), two-panel or stacked layout for schema/question input, distinct visually-separated output card for SQL + explanation.
3. Apply base CSS: typography, spacing, color tokens, button and input styling.
4. Keep functionality untouched today — this is CSS/layout only, not logic changes.

📂 **Files to modify:** `app/static/css/style.css` (full rewrite/expansion), `app/static/index.html` (structural/class updates if needed).

🔗 **Tools/skills:** `/minimalist-ui`, `/exl-branding`, `/exl` design skills for palette, spacing, and layout guidance.

🧪 **Testing tasks:** Visual check across desktop width and mobile width (resize browser or use dev tools device toolbar); confirm text remains readable and buttons remain clickable at all sizes.

🐞 **Common issues:** Too many colors/fonts diluting the "professional" feel — stick to one accent color and one font pairing; overly cramped mobile layout — test responsiveness early, not at the end.

✅ **End-of-day checklist:**
- [ ] Color palette and typography finalized and applied
- [ ] Layout redesigned with clear visual hierarchy
- [ ] Responsive check done on at least 2 screen widths
- [ ] Core functionality still works after CSS changes

📸 **Expected state/screenshot:** Full-page screenshot of the redesigned tool on desktop, and one on mobile width.

➡️ **Handoff notes:** Visual foundation is set. Day 7 adds motion/micro-interaction polish and final UI refinement on top of this base — don't change the color/typography system again.

---

## Day 7 — Motion Polish + Final UI Refinement

🎯 **Objective:** Add subtle, professional micro-interactions and fix any remaining visual rough edges.

📖 **What I'll learn:** Using restrained animation to make a UI feel more premium without being distracting.

🛠 **Features to build:** Loading animation for the "Generate" button/output area, smooth transition when output appears, subtle hover states on interactive elements, copy-to-clipboard button with a confirmation micro-interaction.

📝 **Step-by-step plan:**
1. Invoke `/improve-animations` skill guidance to identify the highest-impact, lowest-risk motion additions for this specific UI (likely: button loading state, fade/slide-in for output, hover feedback).
2. Implement a proper loading indicator (spinner or animated dots) replacing any plain "Loading..." text.
3. Add a smooth fade/slide transition when the SQL + explanation output appears.
4. Add hover/focus states to buttons and inputs for clear interactivity feedback.
5. Add "Copy SQL" button with a brief "Copied!" confirmation animation.
6. Do a final visual QA pass: alignment, spacing consistency, font sizes, contrast/readability.

📂 **Files to modify:** `app/static/css/style.css` (transitions/animations), `app/static/js/script.js` (copy-to-clipboard logic, class toggling for animations).

🔗 **Tools/skills:** `/improve-animations` for motion guidance; native CSS transitions/keyframes (no animation libraries needed to keep it simple).

🧪 **Testing tasks:** Confirm animations run smoothly without jank; confirm copy-to-clipboard actually copies correct text; test on at least one non-primary browser if possible.

🐞 **Common issues:** Overusing animation making the UI feel busy — keep motion subtle and purposeful; copy-to-clipboard failing on some browsers due to permissions — use the standard Clipboard API with a fallback message.

✅ **End-of-day checklist:**
- [ ] Loading animation implemented
- [ ] Output appears with a smooth transition
- [ ] Hover/focus states present on all interactive elements
- [ ] Copy-to-clipboard works with confirmation feedback
- [ ] Final visual QA pass complete

📸 **Expected state/screenshot:** Short screen recording or before/after screenshots showing the loading and output-appear animations.

➡️ **Handoff notes:** UI is feature-and-polish complete. Day 8 is dedicated testing — no new features or styling should be added unless a bug is found.

---

## Day 8 — Testing Pass

🎯 **Objective:** Systematically test the full product for bugs, edge cases, and rough UX moments before deployment.

📖 **What I'll learn:** Structured manual QA — writing and executing a test plan like a real product team would.

🛠 **Features to build:** None — bug fixes only, based on findings.

📝 **Step-by-step plan:**
1. Write a simple test checklist covering: empty inputs, very long schema, very long question, schema with syntax typos, question unrelated to the schema, special characters in input, rapid repeated clicking of Generate, slow network (simulate via dev tools throttling).
2. Execute every test case and log pass/fail.
3. Fix any bugs found, re-test after each fix.
4. Test responsiveness again on mobile, tablet, and desktop widths.
5. Ask 1–2 people (classmates/colleagues) to try it and give quick feedback, if time allows.

📂 **Files to modify:** Whichever files bugs are found in (likely `app/static/js/script.js`, `app/api/generate.py`, minor `app/static/css/style.css` fixes).

🔗 **Tools:** Browser dev tools (network throttling, device toolbar).

🧪 **Testing tasks:** Full checklist execution (see step 1); regression check after each fix (re-run earlier passing tests).

🐞 **Common issues:** Fixing one bug introduces another — always re-run the full checklist after any fix, not just the failing case.

✅ **End-of-day checklist:**
- [ ] Full test checklist executed and documented
- [ ] All critical bugs fixed
- [ ] Responsiveness re-confirmed
- [ ] Outside feedback gathered (if possible)

📸 **Expected state:** Screenshot or note of the completed test checklist with pass/fail results.

➡️ **Handoff notes:** Product is stable and demo-ready. Day 9 is deployment — do not introduce new features during deployment.

---

## Day 9 — Deployment

🎯 **Objective:** Get the tool live on a public, shareable URL using a free hosting option.

📖 **What I'll learn:** Deploying a full-stack app (frontend + backend) to a live environment, and managing secrets safely in production.

🛠 **Features to build:** None — deployment configuration only.

📝 **Step-by-step plan:**
1. Deploy to **Render (free Web Service tier)** — already decided Day 2. Create the service pointing at the existing GitHub repo, with **Root Directory set to `Day 52/querymind`** (since the app lives inside the larger challenge-journal repo, not its own repo).
2. Set up the `ANTHROPIC_API_KEY` environment variable securely in the Render dashboard — never hard-code or commit the key.
3. Set Render's Start Command to run Uvicorn against `app.main:app`.
4. Deploy; verify both the frontend (`/`) and the API (`/api/generate`, `/api/health`) work via the live Render URL — this is a single service, so nothing extra to connect.
5. Do a full end-to-end test on the live deployed link (not localhost).
6. Update `querymind/README.md` with the live link and setup instructions.

📂 **Files to modify:** `requirements.txt` (confirm pinned versions), `querymind/README.md` (live link, setup instructions). No separate hosting config file needed if Render's dashboard build/start commands are used directly (simpler than maintaining a `render.yaml`).

🔗 **Tools:** Render (free tier), environment variable management in the Render dashboard.

🧪 **Testing tasks:** Full manual test on the live URL: paste schema, ask question, confirm SQL + explanation returned correctly; test on mobile via the live link too; hit `/api/health` to confirm the service is awake.

🐞 **Common issues:** API key not set correctly in production causing 500 errors; wrong Root Directory setting in Render (must be `Day 52/querymind`, not the repo root); cold-start delays on Render's free tier after inactivity (add a loading message if the first request is slow, and do a warm-up ping before any live demo).

✅ **End-of-day checklist:**
- [ ] Render service created with Root Directory = `Day 52/querymind`
- [ ] `ANTHROPIC_API_KEY` set in Render environment variables
- [ ] App deployed and reachable via public URL (frontend + API both work, single service)
- [ ] Full flow tested successfully on the live link
- [ ] `querymind/README.md` updated with live link + setup instructions
- [ ] No secrets committed to the repository

📸 **Expected state/screenshot:** Screenshot of the live deployed tool working, with the browser address bar showing the public URL.

➡️ **Handoff notes:** Product is live. Day 10 is final polish, documentation, and demo/pitch preparation — no structural changes unless something is broken.

---

## Day 10 — Final Polish, Documentation & Demo Prep

🎯 **Objective:** Ship a complete, professional v1.0 with full documentation and a rehearsed demo/pitch.

📖 **What I'll learn:** How to package and present a finished product like a real product launch, not just a finished codebase.

🛠 **Features to build:** None — final touches only (copy text, README, demo flow).

📝 **Step-by-step plan:**
1. Do a final full walkthrough of the live product as if seeing it for the first time; fix any last small copy/UI issues.
2. Finalize `README.md`: project description, problem/solution summary, live link, screenshots, tech stack, setup instructions, future scope.
3. Prepare a 2-minute demo script: problem → live demo of pasting schema + asking a question → explanation of output → close with future scope/vision (use the Pitch Deck as the script backbone).
4. Do a full rehearsal of the demo out loud, timed.
5. Take final polished screenshots/short screen recording for submission.
6. Submit/share the live link, repo, PRD, blueprint, and pitch deck as the capstone deliverables.

📂 **Files to modify:** `README.md` (finalize), no code changes unless a critical bug appears.

🔗 **Tools:** None new.

🧪 **Testing tasks:** One final full end-to-end test on the live link right before presenting/submitting, to catch any last-minute issue (e.g., expired API key, hosting downtime).

🐞 **Common issues:** Free-tier hosting "sleeping" after inactivity causing a slow first load during the live demo — do a warm-up request a few minutes before presenting.

✅ **End-of-day checklist:**
- [ ] Final walkthrough complete, no visible bugs
- [ ] README fully documented with live link and screenshots
- [ ] Demo script written and rehearsed
- [ ] All 3 deliverables (PRD, blueprint, pitch deck) finalized alongside the live product
- [ ] Live link double-checked working right before submission

📸 **Expected state/screenshot:** Final polished screenshots/recording of the complete product, ready for submission.

➡️ **Handoff notes:** Capstone complete — v1.0 shipped, documented, and demo-ready.
