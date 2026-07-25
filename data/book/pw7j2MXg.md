---
alpha_id: "pw7j2MXg"
name: "zscore_leverage_double_itci"
tags:
  - "leverage"
  - "fundamental6"
  - "fnd6_itci"
  - "equity_assets"
  - "session_20260609-001"
  - "excellent"
expression: "zscore(-1 * equity / assets) + rank(fnd6_itci / close) + rank(fnd6_itci / close)"
sharpe: 1.98
fitness: 2.01
turnover: 0.030
grade: "EXCELLENT"
family: "leverage_fundamental"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.7414
self_corr_verdict: "FAIL"
status: "REJECTED"
session: "20260609-001"
brain_url: "https://platform.worldquantbrain.com/alpha/pw7j2MXg"
---

# pw7j2MXg

zscore leverage premium + double-weighted cost-to-income quality. First
leverage-family alpha in the book. EXCELLENT grade.

## Expression

```
zscore(-1 * equity / assets) + rank(fnd6_itci / close) + rank(fnd6_itci / close)
```

## Simulation Settings

| Setting | Value |
|---------|-------|
| Region | USA |
| Universe | TOP3000 |
| Delay | 1 |
| Decay | 6 |
| Neutralization | SUBINDUSTRY |
| Truncation | 0.08 |

## Pre-Submission Checks (2026-06-09)

| Check | Result |
|-------|--------|
| Sharpe | 1.98 (PASS, limit 1.25) |
| Fitness | 2.01 (PASS, limit 1.0) |
| Turnover | 3.0% (PASS) |
| LOW_SUB_UNIVERSE_SHARPE | PASS |
| CONCENTRATED_WEIGHT | PASS |
| All 8 BRAIN checks | PASS |
| Self-corr vs book (BRAIN) | 0.412 SAFE |

## Mechanism

The expression combines two orthogonal signals:

1. **Leverage premium** (`zscore(-1 * equity / assets)`): Within the same
   subindustry, firms with higher financial leverage (lower equity/assets ratio)
   tend to outperform. This is the capital structure risk premium — higher leverage
   represents greater financial risk that is compensated with higher returns.
   Using zscore (not rank) is critical: it normalizes the leverage distribution
   in a way that passes the LOW_SUB_UNIVERSE_SHARPE check, which rank fails.

2. **Cost-to-income quality** (`rank(fnd6_itci / close)`): Tax-related income on
   continuing operations relative to price captures operational efficiency and
   earnings quality. Double-weighting this factor (adding it twice) tilts the
   blend toward the quality signal, which provides consistent returns across
   subindustries and pushes the grade from GOOD to EXCELLENT.

The 1:2 leverage:quality weighting is the key structural insight — equal weighting
produces GOOD S=1.72; quality-tilted achieves EXCELLENT S=1.98.

## Self-Correlation Profile

| Book Alpha | Family | Corr |
|------------|--------|------|
| MPbgqZ7o | fundamental_sentiment | 0.412 |

Novel mechanism family at original discovery time. NOTE (2026-06-17): after the
event/leverage family (`0m8GV1Pp`, `d5Q3ZmWv`, `xAn1LqXm`) was activated, the
authoritative BRAIN `/check` now returns SELF_CORRELATION FAIL at 0.7414 vs
`0m8GV1Pp` (Sharpe premium not met). Status changed to REJECTED — the leverage +
itci structure is now redundant with the active book.

## Discovery Path

1. Round 1: `rank(equity/assets)` tested as novel cross-cluster ratio → S=-1.55
2. Round 2: Negated → `rank(-1*equity/assets)` → S=+1.55 standalone (AVERAGE)
3. Round 3: `rank(-1*equity/assets) + rank(fnd6_itci/close)` → EXCELLENT S=2.37
   but FAILS LOW_SUB_UNIVERSE_SHARPE (structural, unfixable with rank)
4. Round 8: `zscore(-1*equity/assets) + rank(fnd6_itci/close)` → GOOD S=1.72
   (zscore fixes sub-universe but reduces Sharpe)
5. Round 13: `zscore(-1*equity/assets) + 2×rank(fnd6_itci/close)` → EXCELLENT
   S=1.98 ALL PASS! Double-weighting itci recovers the EXCELLENT grade.
