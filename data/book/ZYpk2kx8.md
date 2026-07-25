---
alpha_id: "ZYpk2kx8"
status: "ACTIVE"
grade: "SPECTACULAR"
sharpe: 1.71
fitness: 2.52
turnover: 0.046
returns: null
name: "iv60_operating_income_blend"
family: "iv60_fundamental_blend"
neutralization: "MARKET"
decay: 5
self_corr_max: 0.6358
self_corr_peer: "Gro21wWG"
self_corr_result: "PASS"
expression: "ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(operating_income / close), 5)"
brain_url: "https://platform.worldquantbrain.com/alpha/ZYpk2kx8"
session: "20260619-001"
tags:
  - "iv60"
  - "operating_income"
  - "market_neutral"
  - "spectacular"
---

# ZYpk2kx8 — IV60 + Operating Income Blend

## Expression

```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(operating_income / close), 5)
```

## Settings

- Region: USA
- Universe: TOP3000
- Neutralization: MARKET
- Decay: 5
- Delay: 1

## Mechanism

Short-term (60-day) implied volatility call-put spread captures options market
sentiment about near-term directional risk. The 44-day smoothing window filters
noise while preserving the structural skew signal. The `operating_income / close`
leg acts as a quality anchor, directing capital toward profitable firms within the
vol-skew signal. MARKET neutralization resolves the CONCENTRATED_WEIGHT failure
inherent to sparse IV60 coverage by removing broad market exposure.

## Self-Correlation Profile

Max correlation 0.6358 vs `Gro21wWG` (iv90_vol_gated_spread, S=2.59). All 5
correlated peers are IV-family alphas; none exceed 0.70. The 44-day smoothing
window provides better decorrelation than the 22-day window (which hit 0.6743).

## Discovery Path

Session 20260619-001:
- R1: IV60 standalone MARKET → SPECTACULAR S=2.56 but CONCENTRATED_WEIGHT FAIL
- R2: IV60 + operating_income MARKET → EXCELLENT S=1.55, BRAIN ALL PASS + self-corr 0.6743 PASS
- R3: IV60 44-day window + operating_income MARKET → SPECTACULAR S=1.71, BRAIN ALL PASS + self-corr 0.6358 PASS
