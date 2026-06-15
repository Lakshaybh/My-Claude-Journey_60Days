# Day 16 — Custom Skill: stock-fundamental-research

## What I Built Today

Created a reusable Claude Code **Custom Skill** called `stock-fundamental-research` that performs evidence-based fundamental analysis of Indian and global listed stocks without ever giving buy/sell/hold advice.

---

## Skill Details

| Field | Value |
|-------|-------|
| **Skill Name** | `stock-fundamental-research` |
| **Trigger** | `/stock-fundamental-research` or mentioning the skill name |
| **Scope** | Indian NSE/BSE stocks, global listed companies |
| **Output Modes** | Quick Take, Deep Dive, Compare, Pros & Cons, Portfolio Fit |

### Description
Analyze Indian and global listed companies using fundamentals, financial statements, business quality, competitive advantages, valuation, risks, and growth prospects. Generate evidence-based research reports and investor-friendly summaries. Never provides direct buy, sell, or hold recommendations.

---

## How to Create the Skill (Step-by-Step)

1. Open **Claude Code** (Desktop App or VSCode Extension)
2. Click your **profile icon → Settings**
3. Navigate to **Custom Skills** section
4. Click **+ New Skill**
5. Enter **Skill Name**: `stock-fundamental-research`
6. Paste the **Description** (above)
7. Paste the **Instructions** (the full prompt with modes, rules, research checklist)
8. Click **Save**
9. Use via `/stock-fundamental-research` in any conversation

---

## Test Report: TCS (Tata Consultancy Services)

### Quick Take

**TCS (NSE: TCS)** is India's largest IT services company with ₹8.42 Lakh Crore market cap.

| Metric | Value | Verdict |
|--------|-------|---------|
| CMP | ~₹3,240 | 52W Low zone |
| P/E | 22.5x | Cheap vs sector (30x median) |
| EV/EBITDA | 15.8x | Below 5Y avg (20x) |
| ROE | 51.2% | Excellent |
| ROCE | 54.9% | Excellent |
| D/E | 0.00 | Debt-free |
| Dividend Yield | ~3.9% | Attractive |
| Revenue FY25 | ₹2,55,324 Cr | $30Bn milestone crossed |
| Net Profit FY25 | ₹48,797 Cr | NPM: 19.1% |
| Promoter Holding | 71.77% | 0% pledged — Very Healthy |

### 3 Strengths
1. **Moat & Scale** — Largest Indian IT company, mission-critical enterprise systems, high switching costs
2. **Capital Efficiency** — ROE 51%, ROCE 55% with ZERO debt; returned ₹45,588 Cr to shareholders in FY25
3. **Governance** — Tata Sons backing, zero pledging, 25+ years of profitability

### 2 Watch Points
1. **Growth Slowdown** — 3Y revenue CAGR ~4.3% vs 5Y CAGR ~9.2%; BFSI discretionary spend cuts
2. **FII Outflow** — FII holding declined for 8 consecutive quarters; stock down -25% YTD

**Fundamental Quality: STRONG**

---

## Files Generated

| File | Description |
|------|-------------|
| `TCS_Deep_Dive_Report.html` | Full interactive Deep Dive report with 8 tabs |
| `day16.md` | This learning document |

---

## Key Features of the Skill

### Research Checklist Covered
- [x] CMP, Market Cap, Face Value, 52W High/Low
- [x] P/E, P/B, EV/EBITDA vs sector and 5Y average
- [x] Revenue, Profit, EPS CAGR (3Y/5Y)
- [x] EBITDA Margin & NPM (5Y trend)
- [x] EPS last 8 quarters
- [x] D/E, Interest Coverage, Current Ratio
- [x] ROE & ROCE (current, 3Y avg, 5Y avg)
- [x] Dividend history & payout
- [x] Promoter holding trend and pledging
- [x] FII/DII trends (8 quarters)
- [x] Moat analysis
- [x] Peer comparison (TCS vs Infosys vs Wipro vs HCL)

### Output Modes Available
| Mode | When to Use |
|------|-------------|
| **Quick Take** | Just the stock name → 150-220 word snapshot |
| **Deep Dive** | "Full analysis" → 8-tab HTML report |
| **Compare** | "TCS vs Infosys" → side-by-side table |
| **Pros & Cons** | "Strengths and risks of TCS" |
| **Portfolio Fit** | "How does TCS fit my portfolio?" |

---

## Why This Skill Is Powerful

1. **Reusable** — Once saved, use `/stock-fundamental-research` for any stock without re-entering the prompt
2. **Structured** — Forces Claude to follow a consistent research framework every time
3. **Safe** — Never gives buy/sell recommendations — purely educational
4. **Live Data** — Prioritizes Screener → Tickertape → Moneycontrol → NSE for real-time figures
5. **Comparable** — Same template across stocks enables easy investor-style comparisons

---



## Key Learnings

1. **Custom Skills in Claude Code** act as reusable prompt templates — define once, invoke many times
2. Skills support **modes** (Quick/Deep/Compare) — the AI selects the right output format based on context
3. A well-structured skill with a **research checklist** ensures consistent, comprehensive analysis
4. **Mandatory rules** (no buy/sell advice, cite sources, flag missing data) make the skill trustworthy
5. The skill enforces **source hierarchy** (Screener > Tickertape > Moneycontrol > NSE) for data quality
6. **Peer comparison** is automatically included — helps contextualize individual stock metrics
7. Ownership trends (FII/DII over 8 quarters) reveal institutional sentiment shifts
8. A **disclaimer is hardcoded** in the closing — important for financial tools

---

> *This is a view of the fundamentals for educational purposes only. It is not investment advice and not a buy/sell/hold recommendation. Verify all figures independently. The final decision is yours.*

**Challenge Progress: Day 16 / 60 ✅**
