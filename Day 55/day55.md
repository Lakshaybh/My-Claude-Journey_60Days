# Day 55 — Continue Core Feature Development (QueryMind Capstone)

Part of the 10-day QueryMind capstone (Days 51-60) in the 60 Days of Claude AI Challenge by AB Talks.
All project code lives in `Day 52/querymind/` (kept in one place across the capstone) — this file documents what Day 55's session built there.

## What we did today

Today's blueprint milestone was the "reliability pass" — making sure the AI feature holds up against messier, harder, real-world input, not just clean textbook examples.

**1. Built a safety-net validator (`app/prompts/validator.py`, new file)**
Checks whether the SQL the AI generates actually references tables that exist in the schema you pasted. If the AI ever "hallucinates" a table that isn't really there, the app now catches it and shows a warning instead of silently trusting bad output.

**2. Wired the validator into the API (`app/api/generate.py`, updated)**
Every generated query now automatically gets checked before being sent back to the user.

**3. Found and fixed a gap: the frontend didn't actually exist yet**
While reviewing everything built so far, it turned out the actual input form (schema box, question box, Generate button) had never been built — only a placeholder "hello world" page existed. That had to be built first before today's disclaimer/warning display had anywhere to go. Built:
- A working schema input box and question input box
- A "Generate SQL" button that calls the backend
- A results area showing the generated SQL, a Copy button, and the explanation
- A warning message area (only appears if the validator catches something suspicious)
- The disclaimer: "AI-generated — please review before using it."

**4. Tested extensively — 11 total test cases**
- 8 varied real requests through the running server: a 5-table schema with foreign keys, ambiguous column names across tables, a vague one-word question ("show me the good stuff"), a question completely unrelated to the schema, a 7-table schema, typos and informal language, and special characters in the question.
- 3 direct tests of the validator logic itself: a valid query (no warning), a deliberately fake table name (warning correctly shown), and a case-sensitivity check (no false alarm).
- Every single test passed. No crashes, no bad SQL, no false warnings.

**Confirmed today:** still using Groq's free API (no Anthropic key, no cost, no card) — same setup from Day 54.

## Key learnings from today

1. **"Review what's already built" is not a formality — it catches real gaps.** Before writing any new code, going back over the existing codebase surfaced a missing piece (the frontend form) that would have caused today's actual assigned task to make no sense. Skipping that review step would have meant building a feature with nowhere to display it.

2. **A good safety check has to avoid crying wolf.** The first version of the validator idea included checking column names, not just table names. Column-checking turned out to be much riskier: things like renamed results (`AS total_sales`) or table aliases would have triggered false warnings on perfectly correct SQL. Choosing the simpler, more reliable check (tables only) was a better decision than trying to cover everything.

3. **Testing on purpose, not just testing until it works once.** Instead of trying one schema and calling it done, deliberately picking hard cases (ambiguous names, vague questions, irrelevant questions, typos) is what actually builds confidence that the feature will hold up when a real user tries something unexpected.

4. **Environment problems are usually about *where* you are, not *what* you typed.** Two setup hiccups today (a bad path, then a missing command) both traced back to the same root cause: the virtual environment wasn't actually active in that terminal. Running commands through the environment's own Python directly, instead of relying on activation working perfectly, turned out to be the more reliable fix.

## What's next
Day 56 (Blueprint Day 6): visual design direction — colors, typography, and layout — turning today's plain, functional page into something that actually looks like a polished product.
