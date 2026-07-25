---
alpha_id: "vRm07LP3"
name: "iv_spread_zscore_tsmean22_market"
tags:
  - "options"
  - "iv_spread"
  - "option8"
  - "H-006"
  - "session_20260604-001"
  - "excellent"
expression: "ts_decay_linear(zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)), 10)"
sharpe: 1.82
fitness: 2.35
turnover: 0.046
grade: "EXCELLENT"
family: "options_iv_spread"
neutralization: "MARKET"
decay: 10
universe: "TOP3000"
region: "USA"
self_corr_max: 0.309
status: "ACTIVE"
session: "20260604-001"
brain_url: "https://platform.worldquantbrain.com/alpha/vRm07LP3"
---

# vRm07LP3

Pure options IV spread alpha. Ready for manual submission.

## Expression

```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)), 10)
```

## Simulation Settings

| Setting | Value |
|---------|-------|
| Region | USA |
| Universe | TOP3000 |
| Delay | 1 |
| Decay | 10 |
| Neutralization | MARKET |
| Truncation | 0.08 |

## Pre-Submission Checks (2026-06-04)

| Check | Result |
|-------|--------|
| Sharpe | 1.82 (PASS, limit 1.25) |
| Fitness | 2.35 (PASS, limit 1.0) |
| Turnover | 4.6% (PASS) |
| CONCENTRATED_WEIGHT | PASS |
| LOW_SUB_UNIVERSE_SHARPE | PASS (1.02 vs 0.79) |
| Self-corr vs book (local) | 0.309 SAFE (max vs vR56vdYd analyst_revision) |

## Mechanism

Call-put implied volatility spread (270-day) captures forward-looking options market sentiment. When call IV exceeds put IV, informed options traders price upside above downside. Smoothing with `ts_mean(..., 22)` reduces noise; cross-sectional `zscore` and `ts_decay_linear(..., 10)` improve fitness and pass BRAIN weight-distribution checks. MARKET neutralization keeps self-correlation low vs the fundamental-heavy book.

## Self-Correlation Profile

| Book Alpha | Family | Corr |
|------------|--------|------|
| vR56vdYd | analyst_revision | 0.309 |
| xAR9Ybjp | relationships_market | 0.234 |
| 6Xzm6PQP | guidance_fundamental | 0.146 |

Uniquely uncorrelated — first pure options family in the book.

## Post-Submission

After submitting on BRAIN, update `status` to `ACTIVE` and record submission date.
