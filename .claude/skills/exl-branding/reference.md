# Branding & Style Guide

> EXL-inspired design system for future builds. Modeled on the look of exlservice.com: modern, corporate, data and AI driven, with a confident orange accent on clean space.
>
> Light is the default theme. Dark is an optional secondary. Every component reads from CSS variables, so switching themes means swapping one token block.

---

## 1. Brand Essence

Personality: Confident, Clear, Data-driven.

The voice is enterprise grade but not stuffy. State big ideas plainly, leave lots of room, and use one decisive accent color (orange) sparingly so it always means "act here." Designs should feel built by people who trust the data: clean structure, honest hierarchy, no decoration for its own sake.

Two looks ship as themes:
- Light (default). Airy, EXL-faithful. Use it for marketing, dashboards, docs, and most pages.
- Dark (optional). High-contrast alternate for demos, storytelling, and hero-heavy pages when you specifically want it.

---

## 1.5 Voice and Writing Rules

These rules apply to the prose in this guide and to any copy written from it.

- No emojis. Use plain text labels instead (for example "Do" and "Avoid").
- No em dashes. Use a period, comma, colon, or split the sentence.
- No decorative dashes or arrow glyphs in copy. Write the word ("Get started", not "Get started ->").
- Avoid AI-slop tells. Do not write "in today's fast-paced world", "unleash", "elevate", "supercharge", "seamless", "robust", "delve", "navigate the landscape", or "it's not just X, it's Y". Drop filler intensifiers like "powerful", "cutting-edge", and "revolutionary" unless you can back them with a specific fact.
- Prefer short, concrete sentences. One idea per sentence.
- Make specific claims, not vague ones. "Ships in 3 weeks" beats "fast turnaround".
- Use sentence case for body copy and headings. Reserve all-caps for small eyebrow labels.
- Read it out loud. If it sounds like a brochure, cut it.

---

## 2. Color Tokens

Same variable names across both themes. Swap the token block to retheme a page. Light is the base. Dark is opt-in via a `[data-theme="dark"]` attribute on a parent element.

### Brand constants (shared)

| Token | Value | Use |
|---|---|---|
| `--brand-orange` | `#FF6633` | Primary CTA, active accent, focus ring |
| `--brand-orange-hover` | `#FF7D52` | Hover state of primary |
| `--brand-orange-dim` | `#E04E1F` | Pressed state, strong label text |
| `--brand-navy` | `#0B1B33` | Headlines on light, deep surfaces |
| `--orange-soft` | `rgba(255,102,51,0.08)` | Tinted fills, selected rows, icon wells |
| `--orange-glow` | `rgba(255,102,51,0.18)` | Shadow tint, selection, ring halo |
| `--danger` | `#E04545` | Reserved: critical-risk callout only |
| `--danger-soft` | `rgba(224,69,69,0.07)` | Critical-risk callout background |

No rainbow status palette. Do not use green, amber, and red together to grade metrics. Status is shown with orange plus neutral grays, not hue: a stronger value gets a longer orange bar and an orange label; a weaker value gets a shorter bar and a muted gray label. Reserve red (`--danger`) for one thing only: a single critical-risk callout. Never use red, green, or amber for ordinary metrics, badges, pills, or chart fills.

A three-tier status reads as: Strong uses `--accent`, Fair uses `--text-secondary`, Weak uses `--text-muted`. Convey the level through bar length and that one orange hue, not a traffic-light color shift.

### Theme A: Light (default)

```css
:root{
  /* surfaces */
  --bg-base:#F7F8FA;
  --bg-surface:#FFFFFF;
  --bg-card:#FFFFFF;
  --bg-card-hover:#FBFAF8;
  --border-subtle:#E7E9EE;
  --border-active:#D4D8E0;

  /* text */
  --text-primary:#0B1B33;
  --text-secondary:#5A6577;
  --text-muted:#9AA3B2;

  /* accent (from brand constants) */
  --accent:#FF6633;
  --accent-hover:#FF7D52;
  --accent-dim:#E04E1F;
  --accent-glow:rgba(255,102,51,0.18);

  /* elevation */
  --shadow-card:0 1px 2px rgba(11,27,51,.05), 0 8px 24px rgba(11,27,51,.06);
}
```

### Theme B: Dark (optional, secondary)

Apply by adding `data-theme="dark"` to a parent (for example the `html` or `body` element). It overrides the light tokens.

```css
[data-theme="dark"]{
  --bg-base:#0A0E1A;
  --bg-surface:#111827;
  --bg-card:#1A2235;
  --bg-card-hover:#202B42;
  --border-subtle:#1E2D45;
  --border-active:#33405C;

  --text-primary:#F1F5F9;
  --text-secondary:#9AA6B8;
  --text-muted:#5A6477;

  --accent:#FF6633;
  --accent-hover:#FF7D52;
  --accent-dim:#E04E1F;
  --accent-glow:rgba(255,102,51,0.22);

  --shadow-card:0 6px 24px rgba(0,0,0,.35), inset 0 1px 0 rgba(255,255,255,.04);
}
```

Rule: orange is the only hue that signals action. Never use it for body text or large fills, or it loses meaning. Aim for one primary orange element per viewport.

---

## 3. Typography

```css
--font-sans: "Inter", -apple-system, "Segoe UI", Roboto, system-ui, sans-serif;
```

The system stack is fine. Load Inter when you can for the corporate feel.

| Role | Size | Weight | Tracking | Line-height |
|---|---|---|---|---|
| Eyebrow | 11px | 700 | `.14em` UPPERCASE | 1 |
| Hero H1 | 48 to 64px (clamp) | 800 | `-.03em` | 1.05 |
| H2 / Section | 26 to 32px | 760 | `-.02em` | 1.15 |
| H3 / Sub | 18 to 20px | 700 | `-.01em` | 1.3 |
| Body / Lead | 15 to 16px | 400 to 500 | 0 | 1.65 |
| Caption / Meta | 12 to 13px | 600 | `.02em` | 1.5 |

```css
.eyebrow{font-size:11px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--accent);font-weight:700;}
.hero-h1{font-size:clamp(40px,6vw,64px);font-weight:800;letter-spacing:-.03em;
  line-height:1.05;color:var(--text-primary);}
.lead{font-size:16px;line-height:1.65;color:var(--text-secondary);}
```

Numbers such as metrics and scores should use `font-variant-numeric:tabular-nums;` for clean alignment.

---

## 4. Spacing & Layout

- Base unit: 4px. Use multiples: 4, 8, 12, 16, 24, 32, 48, 64.
- Container: `max-width:1100px; margin:0 auto; padding:0 20px;`. A hero may go full bleed.
- Card radius: 12px. Controls and pills 8 to 10px. Hero or large surfaces 16 to 20px.
- Section rhythm: 64 to 96px of vertical gap between major sections.

```css
--space-1:4px; --space-2:8px; --space-3:12px; --space-4:16px;
--space-6:24px; --space-8:32px; --space-12:48px; --space-16:64px;
--radius-sm:8px; --radius:12px; --radius-lg:20px;
```

Breakpoints are mobile first. Stack below `680px`, two or three columns above.

```css
.grid{display:grid;gap:16px;}
@media(min-width:680px){
  .grid-2{grid-template-columns:1fr 1fr;}
  .grid-3{grid-template-columns:repeat(3,1fr);}
}
```

---

## 5. Components

### Buttons

```css
.btn{font:inherit;font-weight:600;font-size:14px;border-radius:10px;
  padding:12px 24px;border:1px solid transparent;cursor:pointer;
  display:inline-flex;align-items:center;gap:8px;
  transition:all .18s cubic-bezier(.16,1,.3,1);}

.btn-primary{background:var(--accent);color:#fff;
  box-shadow:0 4px 14px var(--accent-glow);}
.btn-primary:hover{background:var(--accent-hover);transform:translateY(-2px);
  box-shadow:0 8px 22px var(--accent-glow);}

.btn-secondary{background:transparent;color:var(--text-primary);
  border-color:var(--border-active);}
.btn-secondary:hover{background:var(--bg-card-hover);transform:translateY(-2px);}

.btn-lg{font-size:15px;padding:14px 30px;}
.btn:disabled{opacity:.4;cursor:not-allowed;transform:none;box-shadow:none;}
```

### Card

```css
.card{background:var(--bg-card);border:1px solid var(--border-subtle);
  border-radius:var(--radius);padding:24px;box-shadow:var(--shadow-card);
  transition:.18s;}
.card:hover{border-color:var(--border-active);transform:translateY(-2px);}
```

### Pills & badges

```css
.pill{display:inline-flex;align-items:center;gap:5px;border-radius:999px;padding:4px 12px;
  font-size:12px;font-weight:600;background:var(--bg-surface);color:var(--text-primary);
  border:1px solid var(--border-subtle);}
.pill-accent{background:var(--orange-soft);color:var(--brand-orange-dim);
  border-color:var(--orange-glow);}
/* status reads through one hue, never a traffic light */
.badge-strong{color:var(--accent);} .badge-fair{color:var(--text-secondary);}
.badge-weak{color:var(--text-muted);}
```

### Inputs

```css
.input{width:100%;font:inherit;font-size:15px;padding:12px 14px;
  border-radius:10px;background:var(--bg-surface);color:var(--text-primary);
  border:1px solid var(--border-subtle);transition:.16s;}
.input:focus{outline:none;border-color:var(--accent);
  box-shadow:0 0 0 3px var(--accent-glow);}
```

---

## 5.5 Icons

Use [Lucide](https://lucide.dev) icons only. No emoji glyphs anywhere (this matches the humanizer skill rule). No decorative unicode arrows or check marks in markup either; use the icon component.

- Web build with a bundler: `import { ArrowRight } from "lucide-react"` and render `<ArrowRight size={16} />`.
- Single-file or offline build with no npm (React via CDN, no bundler): inline the same icons as SVG. Copy the path data from lucide.dev. They are the exact paths `lucide-react` ships, so the look is identical and nothing loads from the network.

Inline pattern:

```jsx
const iconBase = size => ({
  width:size, height:size, viewBox:"0 0 24 24", fill:"none",
  stroke:"currentColor", strokeWidth:2, strokeLinecap:"round", strokeLinejoin:"round",
  style:{display:"inline-block", verticalAlign:"-0.15em", flex:"none"}
});
const Svg = ({size=16, children}) => <svg {...iconBase(size)}>{children}</svg>;
const ArrowRight = ({size=16}) => <Svg size={size}><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></Svg>;
```

Rules:
- Icons inherit color from `currentColor`. Set the color on the parent so an icon next to orange text is orange, and an icon in a muted label is muted. Do not hardcode icon colors.
- Default size 16px inline with text, 14px for dense chips, 18 to 20px for headers and feature wells.
- Put an icon on every section header, every stat or fact tile, and primary buttons. One icon per item, not a row of them.
- Keep stroke width at 2. Do not mix filled and outlined icon styles on one page.

---

## 6. Hero Page Spec

The hero is the first impression, so make it decisive. EXL uses a bold full-width band, one strong headline, a clear CTA, and a supporting proof element such as a stat strip or visual.

### Anatomy (top to bottom)

1. Eyebrow. Small uppercase orange label, for example "AI-Powered Operations".
2. Headline. One line, eight words or fewer, the core promise.
3. Lead. One or two plain sentences of support, about 60 characters wide.
4. CTA pair. Primary orange button plus a secondary outline, for example "Get started" and "See how it works".
5. Proof strip. Three stat tiles or a product visual that backs the claim.

### Markup

```html
<section class="hero">
  <div class="hero-inner">
    <span class="eyebrow">AI-Powered Operations</span>
    <h1 class="hero-h1">Turn your data into decisions.</h1>
    <p class="lead hero-lead">
      We help enterprises move faster with clean models, clear metrics,
      and the people who know how to use them.
    </p>
    <div class="hero-cta">
      <button class="btn btn-primary btn-lg">Get started</button>
      <button class="btn btn-secondary btn-lg">See how it works</button>
    </div>
    <div class="hero-stats">
      <div class="stat"><b>3.2x</b><span>faster delivery</span></div>
      <div class="stat"><b>40%</b><span>lower cost</span></div>
      <div class="stat"><b>99.9%</b><span>uptime</span></div>
    </div>
  </div>
</section>
```

### CSS

```css
.hero{padding:96px 20px;background:var(--bg-base);}
.hero-inner{max-width:760px;margin:0 auto;text-align:center;}
.hero-lead{margin:18px auto 28px;max-width:56ch;}
.hero-cta{display:flex;gap:14px;justify-content:center;flex-wrap:wrap;}
.hero-stats{display:flex;gap:32px;justify-content:center;flex-wrap:wrap;
  margin-top:48px;}
.stat b{display:block;font-size:32px;font-weight:800;color:var(--accent);
  letter-spacing:-.02em;font-variant-numeric:tabular-nums;}
.stat span{font-size:13px;color:var(--text-muted);}

/* Optional accent: a soft orange aura behind the headline (use sparingly) */
.hero{position:relative;overflow:hidden;}
.hero::before{content:"";position:absolute;inset:0;
  background:radial-gradient(600px 300px at 50% 0%, var(--accent-glow), transparent 70%);
  pointer-events:none;}
```

### Do and Avoid

- Do: one headline, one primary CTA. Keep the lead near 60 characters wide. Use real, specific stats.
- Avoid: orange paragraphs or orange backgrounds. Two competing primary buttons. A headline longer than two lines on desktop.

### Responsive

- Below `680px`: stats stack to a column, CTA buttons go full width, the headline shrinks via `clamp()`.
- Keep `hero-inner` centered. Left-aligned text is fine for content-heavy variants.

### Marketing hero vs app header

The full 96px hero is for marketing and landing pages. Do not use it inside an app, tool, or dashboard. There the first screen is the product, and a tall hero just wastes vertical space. Use a slim app header instead: a small logo icon, the product name inline, and one short tagline pushed to the right. One row, a thin bottom border, about 48px tall.

```html
<header class="app-head">
  <div class="logo-dot"><!-- Lucide icon --></div>
  <h1>Product Name</h1>
  <div class="sub">One short line of context</div>
</header>
```

```css
.app-head{display:flex;align-items:center;gap:10px;padding:6px 2px 16px;
  border-bottom:1px solid var(--border-subtle);margin-bottom:20px;}
.logo-dot{width:30px;height:30px;border-radius:8px;background:var(--accent);color:#fff;
  display:flex;align-items:center;justify-content:center;flex:none;
  box-shadow:0 3px 10px var(--accent-glow);}
.app-head h1{font-size:15.5px;font-weight:700;letter-spacing:-.01em;}
.app-head .sub{font-size:12px;color:var(--text-muted);margin-left:auto;}
```

Keep app page padding tight too: about `18px` top, not `32px+`. Reserve large vertical rhythm for marketing pages.

---

## 7. Light (default) vs Dark (optional)

| | Light (default) | Dark (optional) |
|---|---|---|
| Canvas | `#F7F8FA` with white cards | `#0A0E1A` with `#1A2235` cards |
| Mood | Calm, trustworthy, corporate | Bold, high-contrast, demo |
| Contrast | Soft, low-noise | Punchy |
| Shadows | Light, diffuse | Deep with inset highlight |
| Accent use | Small and precise (CTA, links) | Slightly bolder (glow, auras) |
| Motion | Subtle, functional | More expressive (shimmer, lift) |
| Best for | Most pages: dashboards, docs, marketing | Landing heroes, storytelling, demos |

Both themes share the same orange, the same type scale, and the same components. Only the surface, text, and shadow tokens differ. Light is the standard. Reach for dark only when you specifically want it. To support both in one page, keep the light tokens in `:root` and the dark tokens under `[data-theme="dark"]`, then toggle the attribute.

```css
[data-theme="dark"]{ /* Theme B tokens from Section 2 */ }
```

---

## 8. Motion & States

```css
/* shared timing */
--ease:cubic-bezier(.16,1,.3,1);

/* hover lift on cards and buttons: translateY(-2px) on hover */
transition:all .18s var(--ease);

/* focus ring: always orange, always visible */
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:6px;}

/* selection */
::selection{background:var(--accent-glow);}

/* section entrance */
@keyframes enter{from{opacity:0;transform:translateY(12px) scale(.99);}to{opacity:1;transform:none;}}
.enter{animation:enter .28s var(--ease);}
```

- Durations: micro-interactions 160 to 200ms, entrances 280 to 400ms. Nothing slower than about 700ms except deliberate data animations such as bars and gauges.
- Dark-theme extras such as shimmer sweeps and radial auras stay off in light.
- Respect `@media (prefers-reduced-motion: reduce)` and disable transforms and animations.

---

## 9. Usage Checklist

When starting a new page:

1. Drop in the light tokens from Section 2 as `:root`, plus the brand constants.
2. Set the font stack and a reset (`*{box-sizing:border-box;margin:0;padding:0;}`).
3. Build the hero first (Section 6). It sets the tone for everything below.
4. Lay out sections on the 1100px container with 64 to 96px rhythm.
5. Use `.card`, `.btn`, and `.pill` from Section 5. Do not reinvent spacing or radius.
6. Keep one primary orange action per viewport. Audit before shipping.
7. For an app or dashboard, use the slim app header (Section 6), not the marketing hero, and keep top padding tight.
8. Add Lucide icons (Section 5.5) on section headers, fact tiles, and primary buttons. No emoji glyphs.
9. No rainbow status colors. Grade metrics with orange plus neutral grays. Reserve red for one critical-risk callout.
10. Check focus rings, reduced motion, and the layout below `680px`.
11. Follow the writing rules in Section 1.5 for all copy: no emojis, no em dashes, no AI slop.
12. To offer dark, add the `[data-theme="dark"]` block and a toggle. Light stays the default.
