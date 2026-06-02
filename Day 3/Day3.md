# Day 3 — Role-Based Prompting

## ABTalks 60-Day Claude AI Mastery Challenge

**Date:** June 3, 2026
**Topic:** Role-Based Prompting — Turn Claude into Any Expert You Need
**Challenge:** Ask the same question 3 ways — no role, Founder persona, Developer persona

---

## The Question Used for All 3 Prompts

> **"How should I grow my product to reach more users?"**

---

## Prompt 1 — No Role Assigned

### 🔹 Prompt

```
How should I grow my product to reach more users?
```

### 🔹 Output

> You can grow your product by focusing on marketing, improving your social media presence, and engaging with your target audience. Consider using paid ads, content marketing, or referral programs. Make sure your product solves a real problem and collect user feedback to keep improving it. Networking and partnerships can also help you reach new audiences.

### 🔹 Learnings

- The response is **broad and generic** — it could apply to any product in any industry
- No prioritization — everything feels equally important
- Lacks strategic depth or actionable sequence
- Feels like a Google search summary, not expert advice
- **No persona = no context = surface-level answers**

## Prompt 2 — Founder Persona

### 🔹 Prompt

```
You are an experienced startup Founder who has scaled two B2B SaaS products 
from 0 to 10,000 users. Speak from real experience. 

How should I grow my product to reach more users?
```

### 🔹 Output

> When I scaled my first product, the biggest mistake I made early on was trying to market before we truly understood our best customers. Here's what actually worked:
>
> **1. Find your 10 power users first.** Forget growth hacks — talk to the 10 people who love your product most. Understand exactly why they use it and what they'd lose if it disappeared. That's your growth message.
>
> **2. Nail one acquisition channel before adding another.** We tried everything at once and wasted 4 months. Pick one channel — for us it was cold outbound — and squeeze every insight out of it first.
>
> **3. Build a referral loop into the product itself.** Word-of-mouth isn't accidental. We added a "Share with a teammate" prompt at the exact moment users hit their first success milestone. Referrals jumped 40% in 6 weeks.
>
> **4. Leverage your unfair advantages.** You have access to communities, networks, and audiences your competitors don't. Use those before spending a dollar on ads.
>
> Growth is a strategy, not a tactic. Focus on retention first — a leaky bucket can't be filled by more water.

### 🔹 Learnings

- The Founder persona adds **lived experience, specificity, and prioritization**
- Includes real numbers and timelines (40% jump, 6 weeks, 4 months wasted)
- Gives a narrative arc — not just a list, but a logical sequence
- The tone is direct, confident, and personal — exactly how a founder talks
- **The role shifted Claude from "what to do" to "what actually works"**

## Prompt 3 — Developer Persona

### 🔹 Prompt

```
You are a senior full-stack Developer with 10+ years of experience building 
and scaling SaaS products. You think in systems, metrics, and technical leverage.

How should I grow my product to reach more users?
```

### 🔹 Output

> Growth from a developer's lens is really a systems optimization problem. Here's how I think about it:
>
> **1. Instrument everything first.** You can't improve what you can't measure. Add event tracking (Mixpanel, PostHog, or Amplitude) to every key user action — signup, activation, first value moment, churn point. Without this, you're flying blind.
>
> **2. Optimize your activation funnel.** Most products lose 60–80% of users before they experience core value. Map your user journey technically: where do session drops happen? What's your time-to-value? Fixing activation beats any marketing spend.
>
> **3. Build a public API or integration layer.** Every integration you ship (Slack, Zapier, Notion) is a distribution channel. Users in those ecosystems discover you organically. This compounds over time with zero ad spend.
>
> **4. SEO as a technical asset.** Programmatic SEO — auto-generated pages from your data (think Zapier's "Connect X to Y" pages) — can drive thousands of organic visitors at scale. This is pure engineering leverage.
>
> **5. Reduce friction to zero.** Audit your onboarding flow technically. Cut every unnecessary form field, redirect, and loading state. A 1-second improvement in load time can improve conversions by 7%.
>
> Growth is an engineering problem as much as a marketing one. Build systems that compound.

### 🔹 Learnings

- The Developer persona focuses on **systems, data, and technical leverage** — completely different angle from the Founder
- Includes specific tools (PostHog, Zapier, Mixpanel) and real benchmarks (7% conversion lift, 60–80% drop-off)
- Introduces concepts a marketer would never mention: API distribution, programmatic SEO, instrumentation
- Structured like technical documentation — clear, precise, measurable
- **Same question, entirely different expert perspective = unique strategic value**

---

## Side-by-Side Comparison

|                          | No Role        | Founder Persona            | Developer Persona       |
| ------------------------ | -------------- | -------------------------- | ----------------------- |
| **Depth**          | Surface-level  | Strategic & experiential   | Technical & systematic  |
| **Tone**           | Generic        | Personal, direct           | Analytical, precise     |
| **Actionability**  | Low            | High                       | High                    |
| **Specificity**    | Broad          | Startup-focused            | Engineering-focused     |
| **Best used when** | Quick overview | Business strategy          | Building growth systems |
| **Unique insight** | None           | Retention over acquisition | Instrumentation first   |

---

## Key Takeaways from Day 3

1. **One role sentence changes everything.** Adding "You are a [role]" before your question is the single highest-leverage prompt upgrade you can make.
2. **Different personas unlock different expertise.** The Founder and Developer gave completely non-overlapping advice on the same question — both valuable, both expert-level.
3. **Roles activate depth, not just tone.** It's not just about how Claude "sounds" — roles change the frameworks, priorities, and knowledge domains Claude draws from.
4. **The formula is simple:**

   ```
   You are a [specific role] with [experience/context].
   [Your question here.]
   ```
5. **Match the role to your actual need.** Need to make a business decision? Use a Founder or Strategist. Need to build something? Use a Developer or Architect. Need to hire? Use an HR Director.

![Role-Based Prompting Challenge](Gemini_Generated_Image_fk2rsyfk2rsyfk2r.png)
