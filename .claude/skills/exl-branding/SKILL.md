---
name: exl-branding
description: |
  EXL-inspired design system for building or restyling web pages, heroes,
  dashboards, and docs. Modeled on exlservice.com: modern, corporate, data and
  AI driven, with a single confident orange accent on clean space. Use when the
  user asks to build/restyle a page in "EXL style", apply EXL branding, or wants
  an on-brand hero, dashboard, card, or landing page. Full spec in reference.md.
license: MIT
compatibility: any-agent
allowed-tools:
  - Read
  - Write
  - Edit
---

# EXL Branding

Apply this whenever building or restyling a page to the EXL look. The complete
guide with every token, component, and rationale lives in `reference.md` next to
this file. Read it when you need the full detail; the rules below are the working
set.

## Brand essence

Confident, clear, data-driven. Enterprise grade but not stuffy. State big ideas
plainly, leave lots of room, and use one decisive accent (orange) sparingly so it
always means "act here." No decoration for its own sake.

- **Light is the default theme.** Dark is opt-in via `[data-theme="dark"]`.
- Every component reads from CSS variables. Retheme by swapping one token block.

## Writing rules (all copy)

- No emojis. Use plain labels ("Do", "Avoid").
- No em dashes. Use a period, comma, colon, or split the sentence.
- No decorative arrows or check glyphs in copy. Write the word.
- No AI slop: avoid "seamless", "robust", "unleash", "elevate", "supercharge",
  "cutting-edge", "in today's fast-paced world", "it's not just X, it's Y".
- Short, concrete sentences. Specific claims ("Ships in 3 weeks", not "fast").
- Sentence case for body and headings. All-caps only for small eyebrow labels.

## Color tokens

Orange is the only hue that signals action. Never use it for body text or large
fills. Aim for one primary orange element per viewport.

**No rainbow status.** Do not grade metrics with green/amber/red. Show status with
orange plus neutral grays: stronger value gets a longer orange bar and orange
label; weaker gets a shorter bar and a muted gray label. Reserve red (`--danger`)
for a single critical-risk callout only.

```css
:root{
  /* brand constants (shared across themes) */
  --brand-orange:#FF6633; --brand-orange-hover:#FF7D52; --brand-orange-dim:#E04E1F;
  --brand-navy:#0B1B33;
  --orange-soft:rgba(255,102,51,0.08); --orange-glow:rgba(255,102,51,0.18);
  --danger:#E04545; --danger-soft:rgba(224,69,69,0.07);

  /* light surfaces (default) */
  --bg-base:#F7F8FA; --bg-surface:#FFFFFF; --bg-card:#FFFFFF; --bg-card-hover:#FBFAF8;
  --border-subtle:#E7E9EE; --border-active:#D4D8E0;

  /* text */
  --text-primary:#0B1B33; --text-secondary:#5A6577; --text-muted:#9AA3B2;

  /* accent */
  --accent:#FF6633; --accent-hover:#FF7D52; --accent-dim:#E04E1F;
  --accent-glow:rgba(255,102,51,0.18);

  --shadow-card:0 1px 2px rgba(11,27,51,.05), 0 8px 24px rgba(11,27,51,.06);
}
[data-theme="dark"]{
  --bg-base:#0A0E1A; --bg-surface:#111827; --bg-card:#1A2235; --bg-card-hover:#202B42;
  --border-subtle:#1E2D45; --border-active:#33405C;
  --text-primary:#F1F5F9; --text-secondary:#9AA6B8; --text-muted:#5A6477;
  --accent:#FF6633; --accent-hover:#FF7D52; --accent-dim:#E04E1F;
  --accent-glow:rgba(255,102,51,0.22);
  --shadow-card:0 6px 24px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.04);
}
```

## Typography

```css
--font-sans:"Inter", -apple-system, "Segoe UI", Roboto, system-ui, sans-serif;
```

| Role | Size | Weight | Tracking | Line-height |
|---|---|---|---|---|
| Eyebrow | 11px | 700 | `.14em` UPPERCASE | 1 |
| Hero H1 | clamp(40–64px) | 800 | `-.03em` | 1.05 |
| H2 / Section | 26–32px | 760 | `-.02em` | 1.15 |
| H3 / Sub | 18–20px | 700 | `-.01em` | 1.3 |
| Body / Lead | 15–16px | 400–500 | 0 | 1.65 |
| Caption / Meta | 12–13px | 600 | `.02em` | 1.5 |

Metrics and scores use `font-variant-numeric:tabular-nums`.

## Spacing & layout

- Base unit 4px: `4, 8, 12, 16, 24, 32, 48, 64`.
- Container: `max-width:1100px; margin:0 auto; padding:0 20px`. Hero may go full bleed.
- Radius: cards 12px, controls/pills 8–10px, hero/large 16–20px.
- Section rhythm: 64–96px between major sections. Stack below `680px`.

## Components

Use `.btn` / `.btn-primary` / `.btn-secondary`, `.card`, `.pill` / `.pill-accent`,
`.input` from reference.md Section 5. Do not reinvent spacing or radius. Buttons
and cards lift `translateY(-2px)` on hover. Focus ring is always orange:
`:focus-visible{outline:2px solid var(--accent);outline-offset:2px;}`.

## Icons

Lucide only (lucide.dev). No emoji, no decorative unicode. Icons inherit
`currentColor` from the parent, do not hardcode colors. Default 16px inline, 18–20px
for headers. One icon per section header, fact tile, and primary button. Stroke
width 2, do not mix filled and outlined.

## Hero vs app header

- **Marketing hero** (Section 6): full-width band, eyebrow, one ≤8-word headline,
  1–2 line lead near 60ch, primary + secondary CTA, then a 3-stat proof strip.
  Optional soft orange radial aura behind the headline, used sparingly.
- **App / dashboard**: do NOT use the tall hero. Use a slim ~48px app header (logo
  dot, product name, one tagline pushed right, thin bottom border). Keep top
  padding tight (~18px).

## Ship checklist

1. Light tokens in `:root` + brand constants; font stack; reset.
2. Hero first (marketing) or slim header (app). It sets the tone.
3. 1100px container, 64–96px section rhythm.
4. Reuse `.card` / `.btn` / `.pill`. One primary orange action per viewport.
5. Lucide icons on headers, fact tiles, primary buttons. No emoji.
6. No rainbow status. Orange + grays. Red only for one critical callout.
7. Focus rings, `prefers-reduced-motion`, and layout below `680px`.
8. Copy follows the writing rules above.
9. Dark is opt-in only. Light stays default.
