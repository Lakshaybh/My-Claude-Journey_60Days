# Design

## Visual Theme

Consulting-report register on the EXL brand system: white/pale-gray surfaces, navy ink, a single decisive orange accent used only for action and status emphasis. Light is the default and primary theme (this page is built to be printed, so dark mode is a secondary on-screen convenience, not the design target). Structure reads like a bound deliverable: a cover/title block, numbered report sections, a running header, tabular data treated with real rules and tabular-nums, not card soup.

## Color Palette

```css
:root{
  --brand-orange:#FF6633; --brand-orange-hover:#FF7D52; --brand-orange-dim:#E04E1F;
  --brand-navy:#0B1B33;
  --orange-soft:rgba(255,102,51,0.08); --orange-glow:rgba(255,102,51,0.18);
  --danger:#E04545; --danger-soft:rgba(224,69,69,0.07);

  --bg-base:#F7F8FA; --bg-surface:#FFFFFF; --bg-card:#FFFFFF; --bg-card-hover:#FBFAF8;
  --border-subtle:#E7E9EE; --border-active:#D4D8E0;

  --text-primary:#0B1B33; --text-secondary:#5A6577; --text-muted:#9AA3B2;

  --accent:#FF6633; --accent-hover:#FF7D52; --accent-dim:#E04E1F;
  --accent-glow:rgba(255,102,51,0.18);

  --shadow-card:0 1px 2px rgba(11,27,51,.05), 0 8px 24px rgba(11,27,51,.06);
}
```

Status/score bars: no red/amber/green rainbow. Weaker scores get a shorter bar in a muted gray-navy tone; stronger scores get a longer bar in brand orange. Reserve `--danger` for the one flagged critical gap (the blank Experience entry) only.

## Typography

- `--font-sans: "Inter", -apple-system, "Segoe UI", Roboto, system-ui, sans-serif` for all UI and body text.
- A serif is not used; the consulting-report feel comes from rule lines, numbered sections, and a running header/footer, not from a display serif.
- Eyebrow 11px/700/uppercase/.14em tracking. H1 clamp(32–44px)/800/-.03em. H2 24–28px/760/-.02em. H3 16–18px/700. Body 15px/1.65. Caption/meta 12–13px/600.
- Scores, dates, and percentages use `font-variant-numeric: tabular-nums`.

## Layout

- Container max-width 1100px, 20px side padding.
- Slim running header (report title, page/section indicator) rather than a tall marketing hero.
- Section rhythm 64–80px between major report sections; sections are numbered (I, II, III...) because the report genuinely is a sequence a reader/printer moves through top to bottom.
- Base spacing unit 4px: 4/8/12/16/24/32/48/64.
- Radius: cards 12px, controls/pills 8–10px.

## Components

- `.btn` / `.btn-primary` (solid orange, white text) / `.btn-secondary` (outline navy).
- `.card` white surface, 1px `--border-subtle`, `--shadow-card`.
- `.pill` / `.pill-accent` for score badges and status tags.
- Print button is a `.btn-primary` fixed in the report header, using `window.print()` with a dedicated print stylesheet that unrolls every tab into one continuous document.

## Motion

Restrained: 150–250ms ease-out transitions on tabs, toggles, and score-bar fills. No bounce/elastic. All motion respects `prefers-reduced-motion`.

## Print / PDF Output

A dedicated `@media print` stylesheet: hides the tab bar, day-nav, copy buttons, and interactive chrome; forces every panel and day-plan section visible and stacked in document order; adds print-only running headers/footers and page-break rules between major sections so "Print to PDF" produces a clean, complete, correctly-paginated report.
