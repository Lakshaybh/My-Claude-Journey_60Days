# Daily Build Prompt — QueryMind 30-Day Growth Plan

Reusable prompt for each day of the 30-day growth plan. Copy this exactly, replacing only `[DAY NUMBER]`, and paste it to start that day's session.

---

Today is Day [DAY NUMBER] of the QueryMind 30-Day Growth Plan, continuing from the 10-day capstone (Days 51-60 of the AB Talks 60-Day Claude AI Challenge).

Read `Day 60/30-day-growth-plan.md` and find the entry for Day [DAY NUMBER]. Treat it as the source of truth for today. Do not redesign the project, do not skip ahead to a later day's work, and do not reopen decisions already made and documented in `Day 52/ARCHITECTURE.md`, `Day 52/API.md`, or `Day 60/challenge-retrospective.md` unless today's milestone explicitly requires it.

Before writing code, briefly review what was built in the most recent prior session so today's work builds on the real current state of the code, not an assumption about it.

Build only today's milestone. Assume I have the same experience level as throughout the original capstone — explain manual steps (installing anything new, configuring services, deploying) clearly and wait for my confirmation before assuming they're done. Prioritize working code over long explanations.

Use only free tools and services, consistent with every decision made throughout this project (Groq instead of a paid AI API, Render's free tier, no paid add-ons) unless I explicitly approve a cost.

When today's milestone is complete:
- Verify it works, including against the currently deployed live version where relevant.
- Update any documentation it affects (README, API.md, ARCHITECTURE.md, etc.) so the docs never drift from the real code.
- Help me commit and push with a clear, specific commit message.
- Give me a short summary of what changed today and confirm what tomorrow (Day [DAY NUMBER + 1]) will build, per the growth plan.

Treat this the same way the original 10-day capstone was run: real tradeoffs named out loud, real testing before calling something done, and no scope creep beyond what today's milestone actually asks for.
