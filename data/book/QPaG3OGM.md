---
alpha_id: "QPaG3OGM"
grade: "SPECTACULAR"
status: "PENDING"
sharpe: 3.09
fitness: 5.14
turnover: 0.079
returns: null
family: "iv60_guidance_revision"
mechanism: "Cross-dataset 3-factor blend: 22-day smoothed IV60 call-put spread zscore captures directional options market sentiment; max adjusted net income guidance rank captures forward-looking earnings quality; analyst BVPS revision flag captures balance sheet revaluation. The shorter IV smoothing window (22d vs 44d) increases responsiveness to recent sentiment shifts."
expression: "ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 22)) + rank(max_adjusted_net_income_guidance) + rank(anl4_bvps_flag), 5)"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_value: 0.8206
self_corr_result: "PASS"
self_corr_method: "sharpe_premium_escape"
top_corr_peer: "Gro21wWG"
top_corr_peer_sharpe: 2.59
brain_checks_pass: true
session: "20260625-001"
discovered: "2026-06-25"
platform_url: "https://platform.worldquantbrain.com/alpha/QPaG3OGM"
---

# QPaG3OGM — IV60 22d Guidance + BVPS Revision

SPECTACULAR alpha discovered in session 20260625-001. Passes all 8 BRAIN
submission checks and self-correlation via Sharpe premium escape (S=3.09 vs
1.10×2.59=2.849 threshold).

## Key Metrics

| Metric | Value |
|--------|-------|
| Grade | SPECTACULAR |
| Sharpe | 3.09 |
| Fitness | 5.14 |
| Turnover | 7.9% |
| Self-Corr | 0.8206 (PASS via premium) |
| Top Corr Peer | Gro21wWG (IV90 vol-gated, S=2.59) |

## Self-Correlation Peers

| Peer | Corr | Sharpe | Premium Needed | Status |
|------|------|--------|----------------|--------|
| Gro21wWG | 0.821 | 2.59 | 2.849 | PASS (3.09 > 2.849) |
| omY3pZq2 | 0.755 | 2.13 | 2.343 | PASS (3.09 > 2.343) |
| vRm07LP3 | 0.703 | 1.82 | 2.002 | PASS (3.09 > 2.002) |
| ZYpk2kx8 | 0.624 | 1.71 | — | AUTO PASS (< 0.70) |
| kq33Gjqk | 0.592 | 2.63 | — | AUTO PASS (< 0.70) |

## Discovery Process

Round 4 of session 20260625-001. Derived from WjpV8AxO (S=2.96) by simplifying
to 3 factors and changing IV60 smoothing window from 44 to 22 days. The 22-day
window fixed LOW_SUB_UNIVERSE_SHARPE (the 44-day version failed by 0.02) while
maintaining S=3.09.
