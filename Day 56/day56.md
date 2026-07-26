# Day 56 — Complete the MVP & Deliver a Working Demo (QueryMind Capstone)

Part of the 10-day QueryMind capstone (Days 51-60) in the 60 Days of Claude AI Challenge by AB Talks.
All project code lives in `Day 52/querymind/` — this file documents what Day 56's session built there.

**Live demo:** https://querymind-3msv.onrender.com

## What we did today

Today's goal was a complete working MVP with a real, shareable live demo — a bigger ask than the original blueprint's Day 6 (which only planned visual design direction, no deployment). Rather than stall on that mismatch, it was treated as a deliberate scope compression: do lighter styling now, deploy early, and push the full branding pass to Day 7.

**1. Presentable styling pass (not final branding — that's Day 7)**
Rewrote `app/static/index.html` and `app/static/css/style.css`: a clean card-based layout, readable spacing, a styled dark code block for the generated SQL, a proper warning banner style, and a responsive breakpoint for smaller screens. No JavaScript changes were needed — all existing element IDs stayed the same, so the working logic from Day 55 kept functioning without modification.

**2. Required footer added**
Added: *"Built with Claude as part of the AB Talks 60-Day Claude AI Challenge."* — visible at the bottom of every page load, confirmed on both the local version and the live deployed version.

**3. Deployed to Render (free tier)**
Walked through creating a Render account, connecting the GitHub repo, and configuring the service to build from a subfolder (`Day 52/querymind`) inside the larger challenge-journal repo, since the whole capstone lives in one repo rather than its own. Set the `GROQ_API_KEY` environment variable directly in Render's dashboard — the key itself never touches GitHub or the codebase.

**4. Caught and fixed a real deployment mistake**
The first deploy check showed the live site was still running the *old* unstyled version. The cause: today's code changes had been tested locally but never actually committed and pushed to GitHub before deployment — and Render only ever deploys what's in the repo, not what's on a local machine. Committing and pushing triggered Render's auto-deploy, and the fresh version went live within about a minute.

**5. Verified the live app end-to-end**
Checked the actual public URL, not just localhost: homepage loads with the new styling, `/api/health` returns healthy, the footer text is present, and a real AI-generated SQL query came back correctly through the live server — confirming the Groq integration works in production, not just locally.

## Key learnings from today

1. **"It works on my machine" and "it works live" are two different claims.** Everything had been tested and confirmed working locally, but the live site was still serving old code, because local testing never touches what's actually deployed. The only way to be sure is to check the real public URL directly.

2. **Deployment only reflects what's committed and pushed — nothing else.** Hosting platforms like Render build directly from the GitHub repo. Code sitting unpushed on a local machine, no matter how well it works, is invisible to the deployed app until it's actually pushed.

3. **A request to "put a secret key on GitHub so people can see the project" is a red flag worth catching.** The real goal (letting other people use the live app) doesn't require exposing an API key at all — the key stays private in the hosting platform's environment settings, and the public only ever sees the live URL, not the credentials behind it.

4. **When a day's instructions don't match the existing plan, name the conflict and keep moving instead of stalling.** Today's prompt asked for a full MVP and live deployment earlier than originally scheduled. Rather than refuse or silently redesign everything, the right move was to flag the mismatch briefly, propose a reasonable compromise (lighter styling now, full branding later), and continue — while writing the change down clearly in the project docs so it isn't forgotten.

## What's next
Day 57 (now absorbing the original Day 6 + Day 7 blueprint scope): the full visual branding pass (color system, typography, layout refinement) plus motion/micro-interaction polish, applied on top of today's working MVP. Day 9 becomes a lighter "final deploy refresh" instead of a first-time deployment, since the app is already live.
