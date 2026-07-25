---
alpha_id: "ZYpVLGZj"
name: "PPE_Capital_ProfitRev_TaxCredit_OvernightGap"
tags:
  - "ppegtq"
  - "ptpr_flag"
  - "itci"
  - "overnight_gap"
  - "session_20260701-001"
submitted: "2026-07-02"
session: "20260701-001"
grade: "SPECTACULAR"
sharpe: 2.84
fitness: 3.21
turnover: 0.178
expression: "ts_decay_linear(rank(fnd6_newqv1300_ppegtq / close) + rank(anl4_ptpr_flag) + rank(fnd6_itci / close) + rank(open/close - 1), 5)"
family: "ppe_capital_intensity_revision"
neutralization: "SUBINDUSTRY"
decay: 8
self_corr_max: 0.7943
self_corr_peer: "MPbgqZ7o"
self_corr_result: "PASS"
status: "ACTIVE"
brain_url: "https://platform.worldquantbrain.com/alpha/ZYpVLGZj"
---

# Alpha: ZYpVLGZj

## Expression

```
ts_decay_linear(rank(fnd6_newqv1300_ppegtq / close) + rank(anl4_ptpr_flag) + rank(fnd6_itci / close) + rank(open/close - 1), 5)
```

Settings: SUBINDUSTRY, decay=8, USA TOP3000

## Mechanism

Four-factor cross-dataset blend capturing converging capital-intensity and information signals:

1. **PP&E gross / price** (`rank(fnd6_newqv1300_ppegtq / close)`): Firms with high gross property, plant & equipment relative to market cap are undervalued capital-intensive businesses. Replacement asset value exceeds market pricing — a deep value signal.

2. **Pre-tax profit revision** (`rank(anl4_ptpr_flag)`): Upward analyst revisions to pre-tax profit signal improving fundamentals before they appear in reported numbers. Captures the drift in prices following analyst reassessment.

3. **Investment tax credit / price** (`rank(fnd6_itci / close)`): Firms with large investment tax credits relative to market cap have made significant capital investments that generate tax benefits. Signals capital allocation quality and tax-efficient growth.

4. **Overnight gap** (`rank(open/close - 1)`): Captures institutional after-hours order flow. Positive overnight gaps indicate informed buying from institutions trading on non-public information after market close.

The combination works because capital-intensive value (PP&E), information revision (analyst profit), tax-efficient investment (tax credit), and institutional flow (overnight) are four distinct signal types that reinforce each other when converging.

## Self-Correlation Profile

BRAIN self-corr: 0.7943 vs MPbgqZ7o (EXCELLENT, S=2.58, family=fundamental_sentiment).
Passes via Sharpe premium escape: 2.84 >= 1.10 × 2.58 = 2.838 (margin: +0.002).

Key correlation breakdown:
| Peer | Family | Local PnL Corr | BRAIN Corr | Notes |
|------|--------|---------------|------------|-------|
| MPbgqZ7o | fundamental_sentiment | 0.675 | 0.794 | Shares itci → BRAIN inflation |
| 6Xzm6PQP | guidance_fundamental | 0.707 | — | No shared fields, natural PnL similarity |
| 3q7lm2p6 | fundamental_intraday | 0.554 | — | Shares ptpr, itci, gap but different anchor |

The tight premium margin means this alpha is sensitive to peer Sharpe fluctuations. If MPbgqZ7o's Sharpe increases above ~2.58, the premium escape would fail.

## Post-Submission

After submitting on BRAIN, flip `status: ACTIVE` and set `submitted: <date>`.
