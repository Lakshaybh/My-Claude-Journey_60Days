# Day 58 — Testing, Debugging & Production Optimization (QueryMind Capstone)

Part of the 10-day QueryMind capstone (Days 51-60) in the 60 Days of Claude AI Challenge by AB Talks.
All project code lives in `Day 52/querymind/` — this file documents what Day 58's session built there.

**Live demo:** https://querymind-3msv.onrender.com
**Repo:** github.com/Lakshaybh/My-Claude-Journey_60Days

## What we did today

Today was a release-readiness review, not new feature work: reviewed the whole codebase like a QA engineer, security reviewer, and performance engineer would, found real gaps, fixed them, then tested aggressively until confident enough to approve a public launch.

**Issues found and fixed:**

1. **No rate limiting.** `/api/generate` is public and unauthenticated, and every call costs real AI API usage. Anyone (or a bot) could hammer it and burn through the free quota. Fixed with `app/core/rate_limit.py` — a simple per-IP sliding-window limiter (15 requests/minute), no new dependency needed.

2. **Narrow error handling.** Only one specific error type from the AI service was being caught; anything else (a timeout, a network blip, an unexpected bug) would produce a generic, non-JSON error that the frontend couldn't parse — so the user would see a misleading "could not reach server" message even when the actual problem was something else. Fixed by broadening the catch and adding a global exception handler that always returns a proper, honest error message.

3. **No request timeout.** The AI client had no explicit timeout, so a hung network connection could block a request indefinitely. Fixed with a 30-second timeout and a single retry.

4. **No server-side logging.** If something broke in production, there was no way to see what happened. Added basic logging so real errors are recorded on the server (not shown to users, just kept for debugging).

5. **Missing favicon.** Caused a small console error on every single page load. Fixed with a tiny inline icon, no extra image file needed.

6. **No basic security headers.** Added headers that block clickjacking attempts and prevent browsers from misinterpreting file types — standard, low-effort protections appropriate for a public site.

**Testing performed — 14 categories, all passed:**
- Normal valid request (baseline)
- Empty schema and question
- Missing fields entirely
- Malformed JSON body
- Oversized input (over the 8,000/500 character limits)
- Wrong content-type header
- Wrong HTTP method (GET instead of POST)
- Non-existent routes
- Security headers present on every response
- Favicon loads without error
- SQL-injection-style text in the question (confirmed harmless, since QueryMind never executes SQL by design)
- Unicode and emoji in input
- Rate limiting actually triggers after repeated rapid requests
- Malformed/broken AI responses fail gracefully instead of crashing

**Deployed and verified live:** committed, pushed, confirmed Render redeployed automatically, then re-ran the full verification (health check, footer, security headers, favicon, real AI generation, validation errors) directly against the live public URL, not just localhost.

## Key learnings from today

1. **"It hasn't broken yet" is not the same as "it's production-ready."** Nothing in the app was actually broken before today — all the fixes were about handling situations that simply hadn't come up yet: abuse, network hiccups, unexpected AI responses. A real QA pass means deliberately trying to cause the failures that haven't happened by accident.

2. **A confusing error message is its own kind of bug.** The app never crashed on unexpected errors before today, but it did show the *wrong* explanation to the user (blaming the network when the real problem was something else). Fixing that required understanding not just "did it fail" but "does the error message actually tell the truth."

3. **Free and public means somebody, eventually, will misuse it.** Since QueryMind has no login and calls a real (if free) AI service, rate limiting isn't a hypothetical extra — it's the one thing standing between "free tool anyone can try" and "free tool a bot could quietly break for everyone."

4. **A feature designed narrowly on purpose (no SQL execution) turned out to double as a security boundary.** Testing with SQL-injection-style input confirmed there's nothing to actually inject into, since the app never runs the generated SQL against a real database. A decision made for simplicity back on Day 51 turned out to also be a safety decision.

## What's next
Day 59 (Blueprint Day 8 continued / prep for launch): final documentation pass, README polish for the live repo, and preparing the demo walkthrough and pitch materials ahead of Day 60's final submission and reflection.
