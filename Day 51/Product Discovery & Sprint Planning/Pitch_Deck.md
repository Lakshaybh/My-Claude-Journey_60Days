# Pitch Deck — QueryMind
*AI-Powered SQL Query Generator for Data Analysts*

---

## Slide 1 — Title
**QueryMind**
Ask your data a question. Get the SQL instantly.

*(Built during the AB Talks 60-Day Claude AI Challenge — Capstone Project)*

---

## Slide 2 — Problem
- Data analysts spend a large chunk of their day writing SQL queries by hand.
- The hard part isn't creativity — it's **translating a business question into correct query logic** and **remembering exact syntax** across unfamiliar schemas.
- This is slow, repetitive, and error-prone — especially for interns and analysts working across many different databases.

---

## Slide 3 — Target Users
- **Primary:** Data analyst interns and students who work with varied, unfamiliar schemas daily.
- **Secondary:** Junior analysts and BI trainees who understand the business question but not the exact SQL syntax.
- **Relatable insight:** the builder *is* the target user — this tool solves a problem experienced firsthand during a real data analyst internship.

---

## Slide 4 — Solution
A simple, focused web tool:
1. Paste your database schema (`CREATE TABLE` statements).
2. Ask your question in plain English.
3. Get back a correct, ready-to-use SQL query — plus a plain-English explanation of what it does.

No login. No setup. No execution risk. Just a fast, reliable bridge between "what I want to know" and "the query that gets it."

---

## Slide 5 — Key Features
- ✅ Schema-aware SQL generation (grounded only in the tables/columns provided)
- ✅ Plain-English explanation of every generated query
- ✅ Clean, copy-ready SQL output
- ✅ Built-in validation warning if the AI references anything outside the given schema
- ✅ Polished, professional, distraction-free interface

---

## Slide 6 — Technical Approach
- **AI Engine:** Claude API, with a schema-grounded prompt design that constrains output to valid, structured SQL + explanation.
- **Architecture:** Lightweight web app — a clean frontend interface calling a backend API that handles the Claude integration.
- **Design philosophy:** Minimalist, professional UI (informed by structured branding and minimalist design principles) — because trust in a data tool starts with how credible it looks.
- **Deployment:** Live, publicly accessible, free-tier hosting — no login friction for anyone trying it.

---

## Slide 7 — Future Scope
- DAX / Power BI query generation (natural extension of the same engine)
- Live query execution against a connected sample database
- Multi-turn conversational refinement ("now filter by last month")
- Schema file upload support (`.sql`, `.csv`)
- Saved query history (with lightweight accounts)
- Auto-suggested example questions generated from any pasted schema

---

## Slide 8 — Vision
Every data analyst — student, intern, or professional — should be able to go from *"I know what I want to ask"* to *"I have the correct query"* in seconds, without wrestling with syntax. QueryMind is the first step toward an AI-native workflow where data analysts spend their time on **insight**, not **syntax**.

---

## Slide 9 — Close
**QueryMind** — built in 10 days, solving a problem experienced firsthand.
Live demo: *[link added at deployment on Day 9]*
