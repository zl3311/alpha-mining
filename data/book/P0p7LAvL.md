---
alpha_id: "P0p7LAvL"
name: "acdo_overnight_ptpr_itci_blend"
tags:
  - "fundamental6"
  - "analyst4"
  - "intraday"
  - "fnd6_acdo"
  - "fnd6_itci"
  - "anl4_ptpr_flag"
  - "overnight_gap"
  - "session_20260625-002"
  - "spectacular"
submitted: null
session: "20260625-002"
grade: "SPECTACULAR"
sharpe: 3.02
fitness: 3.48
turnover: 0.137
returns: 0.182
expression: "ts_decay_linear(rank(fnd6_acdo / close) + rank(open / close - 1) + rank(anl4_ptpr_flag) + rank(fnd6_itci / close), 5)"
family: "fundamental_intraday_analyst_blend"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.6318
self_corr_peer: "LLR0n261"
self_corr_result: "STALE — sibling 3q7lm2p6 now ACTIVE; recompute before submitting"
status: "PENDING"
brain_url: "https://platform.worldquantbrain.com/alpha/P0p7LAvL"
---

# Alpha P0p7LAvL: Fundamental + Overnight Gap + Analyst Revision Blend

## Expression

```
ts_decay_linear(rank(fnd6_acdo / close) + rank(open / close - 1) + rank(anl4_ptpr_flag) + rank(fnd6_itci / close), 5)
```

Settings: SUBINDUSTRY neutralization, decay=6, USA TOP3000, truncation=0.08

## Mechanism

4-factor additive blend combining three independent information channels:

1. **rank(fnd6_acdo / close)** — Accumulated depreciation relative to price. High values
   indicate established firms with substantial fixed asset bases trading at low valuations.
   Captures capital-intensive value (accounting quality signal).

2. **rank(open / close - 1)** — Overnight gap: ratio of today's open to yesterday's close
   minus 1. Positive values indicate upward overnight gaps driven by after-hours news,
   institutional overnight analysis, and pre-market order flow. Fast-changing daily signal
   complementing slow-moving fundamentals.

3. **rank(anl4_ptpr_flag)** — Pre-tax profit revision direction flag. Upward revisions
   to pre-tax profit estimates signal improving profitability before reported earnings.
   Captures sell-side information flow ahead of market consensus adjustment.

4. **rank(fnd6_itci / close)** — Inventory to total capital investment relative to price.
   High inventory-to-capital ratios at low prices indicate firms with large working capital
   positions being undervalued by the market (supply chain/operational intensity value).

## Why It Works

The alpha exploits the market's inability to simultaneously process four orthogonal
information dimensions with different update frequencies:
- **Quarterly** (fnd6_acdo, fnd6_itci): Balance sheet signals updated quarterly, slow to
  be incorporated into prices
- **Daily** (open/close): Overnight information gaps that create short-term momentum
- **Event-driven** (anl4_ptpr_flag): Analyst revision events that precede full price adjustment

The independence of these information sources produces natural decorrelation from the
existing book (max self-corr 0.63), which is dominated by options volatility signals.

## Self-Correlation Profile

| Peer | Correlation | Peer Sharpe | Status |
|------|-------------|-------------|--------|
| LLR0n261 (acdo+sentiment) | 0.6318 | 2.51 | auto-PASS (< 0.7) |
| omnopQ9k (itci+acdo+sentiment) | 0.6187 | 2.64 | auto-PASS (< 0.7) |
| Jjnr7VOl (itci+acdo+netdebt) | 0.6156 | 3.08 | auto-PASS (< 0.7) |
| omVpwdqk (guidance+analyst) | 0.6144 | 2.55 | auto-PASS (< 0.7) |
| vR56vdYd (ptp+bvps+sentiment) | 0.6087 | 2.86 | auto-PASS (< 0.7) |

All peers below 0.7 → automatic PASS without needing Sharpe premium escape.

## Post-Submission

PENDING: awaiting human submission on BRAIN platform. After submission, flip status
to ACTIVE and set submitted date.

**Warning**: Sibling `3q7lm2p6` (same template, netdebt_flag variant) is already
ACTIVE. Self-correlation between P0p7LAvL and 3q7lm2p6 is likely >0.85 given
identical template structure. Verify via `pnl_correlation.py` before submitting.
