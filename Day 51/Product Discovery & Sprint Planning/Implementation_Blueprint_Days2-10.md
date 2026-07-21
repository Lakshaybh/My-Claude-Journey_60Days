# Implementation Blueprint — QueryMind (Days 2–10)

**Single source of truth for the rest of this capstone.** Each day assumes a fresh AI conversation — paste the relevant day's section (plus the PRD) to continue building without re-deciding architecture.

**Project:** AI-Powered SQL Query Generator for Data Analysts
**Builder availability:** ~1 focused hour/day
**Core flow (locked, do not change):** paste schema (`CREATE TABLE` text) → ask plain-English question → receive generated SQL + plain-English explanation. Single-shot. No login. No execution. No file upload.

---

## Day 2 — Tech Stack Decision + Project Setup

🎯 **Objective:** Choose the simplest tech stack that fits a 1-hour/day, no-new-learning-curve constraint, and get a running skeleton project.

📖 **What I'll learn:** How to make a fast, low-risk architecture decision and scaffold a project cleanly.

🛠 **Features to build:** Empty but running app — one page that loads, nothing functional yet.

📝 **Step-by-step plan:**
1. Decide stack. Recommended default (builder already knows Python + a web framework): **Streamlit** for fastest single-day build (Python only, minimal frontend code) OR a simple **HTML/CSS/JS frontend + Python (Flask/FastAPI) backend** if more UI control is wanted for the "polished UI" priority. Given UI polish is the top success criterion, lean toward **Flask/FastAPI backend + hand-built HTML/CSS/JS frontend** for full styling control — but confirm based on comfort level.
2. Create project folder structure (see below).
3. Initialize git repo, first commit.
4. Set up a virtual environment and install base dependencies (framework of choice + `anthropic` SDK for Claude API).
5. Get a Claude API key and store it in a `.env` file (never commit it).
6. Build a minimal "hello world" page to confirm the server runs locally.

📂 **Files/folders to create:**
```
querymind/
  backend/
    app.py
    .env
    requirements.txt
  frontend/
    index.html
    style.css
    script.js
  .gitignore
  README.md
```

🔗 **Tools to integrate:** Anthropic Claude API (get API key), chosen web framework, git/GitHub for version control.

🧪 **Testing tasks:** Confirm local server starts without errors; confirm `.env` is git-ignored (no secrets committed).

🐞 **Common issues:** Port already in use; missing `.env` causing crash on startup — add a clear error message instead of a stack trace.

✅ **End-of-day checklist:**
- [ ] Tech stack decided and documented in README
- [ ] Project folder structure created
- [ ] Git repo initialized with first commit
- [ ] Local server runs and shows a blank/hello page
- [ ] Claude API key obtained and stored safely in `.env`

📸 **Expected state/screenshot:** Terminal showing server running + browser showing a blank placeholder page.

➡️ **Handoff notes:** Stack is locked — Day 3 builds the backend logic that calls Claude with schema + question and returns SQL + explanation. Do not revisit stack choice after today.

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

📂 **Files to create/modify:** `backend/app.py` (add route), `backend/prompts.py` (prompt template), `backend/requirements.txt` (update if needed).

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

📂 **Files to modify:** `frontend/index.html`, `frontend/script.js`.

🔗 **Tools:** Fetch API (or equivalent) to call backend; CORS setup if frontend/backend run on different ports.

🧪 **Testing tasks:** Full manual end-to-end test with 3+ schema/question combos; test loading state appears; test error messages show correctly for empty inputs.

🐞 **Common issues:** CORS errors (enable CORS on backend for local dev); button submitting multiple times if clicked repeatedly (disable button while loading).

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

📂 **Files to modify:** `backend/prompts.py`, `backend/app.py` (add validation logic), `frontend/index.html` (disclaimer text).

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

📂 **Files to modify:** `frontend/style.css` (full rewrite/expansion), `frontend/index.html` (structural/class updates if needed).

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

📂 **Files to modify:** `frontend/style.css` (transitions/animations), `frontend/script.js` (copy-to-clipboard logic, class toggling for animations).

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

📂 **Files to modify:** Whichever files bugs are found in (likely `script.js`, `app.py`, minor `style.css` fixes).

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
1. Choose a free hosting platform appropriate to the chosen stack (e.g., Render/Railway free tier for a Flask/FastAPI backend, or a static host + serverless function if applicable). Confirm this fits "no paid tools" constraint.
2. Set up environment variables (Claude API key) securely on the hosting platform — never hard-code or commit the key.
3. Deploy backend; verify the API endpoint works via the live URL.
4. Deploy/connect frontend (same host or a static hosting service) pointing to the live backend URL.
5. Do a full end-to-end test on the live deployed link (not localhost).
6. Update `README.md` with the live link and setup instructions.

📂 **Files to modify:** Add hosting config files as required by chosen platform (e.g., `Procfile`, `render.yaml`, or platform-specific config); update `README.md`.

🔗 **Tools:** Free-tier hosting platform (to be selected based on stack), environment variable management on that platform.

🧪 **Testing tasks:** Full manual test on the live URL: paste schema, ask question, confirm SQL + explanation returned correctly; test on mobile via the live link too.

🐞 **Common issues:** API key not set correctly in production causing 500 errors; CORS misconfiguration between deployed frontend and backend domains; cold-start delays on free-tier hosting (add a loading message if the first request is slow).

✅ **End-of-day checklist:**
- [ ] Backend deployed and reachable via public URL
- [ ] Frontend deployed and correctly calling the live backend
- [ ] Full flow tested successfully on the live link
- [ ] README updated with live link + setup instructions
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
