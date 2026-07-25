---
id: "20260715-002-results"
session: "20260715-002"
total_expressions: 46
gate_passers: 13
best_sharpe: 2.55
best_fitness: 2.55
best_alpha_id: "oml0kV52"
---

# Results: Session 20260715-002

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 46 |
| Gate-passers (S>=1.25, F>=1.0) | 13 |
| Best Sharpe | 2.55 (`oml0kV52`) |
| Best Fitness | 2.55 (`oml0kV52`) |
| Budget used | 46 / unlimited |

## Gate-Passers

| # | Alpha ID | Expression | Sharpe | Fitness | Turnover | Family | Verdict |
|---|----------|-----------|--------|---------|----------|--------|---------|
| 1 | `oml0kV52` | `guidance + cfi_flag + buzz + ivaco + drlt` | 2.55 | 2.55 | 12.8% | guidance_analyst_ivaco_drlt_blend | DEPRIORITIZED (est. self-corr 0.796) |
| 2 | `kq06YLrd` | `guidance + cfi_flag + buzz + fatl` | 1.99 | 2.06 | 16.4% | guidance_analyst_fatl_blend | DEPRIORITIZED (est. self-corr 0.813) |
| 3 | `N1rlJ7mq` | `pstkrv event-mag + ivaco + drlt + fcf_flag + buzz` | 2.32 | 2.07 | 11.1% | pstkrv_event_magnitude_ivaco_drlt_blend | **PRIMARY CANDIDATE** (self-corr 0.691, RISKY/unconfirmed) |
| 4 | `np25eXrE` | `mibnq event-mag + ivaco + drlt + fcf_flag + buzz` | 2.19 | 2.00 | 10.4% | mibnq_event_magnitude_ivaco_drlt_blend | NOT PURSUED (borderline GOOD/EXCELLENT) |
| 5 | `np25lW8a` | `guidance + cfi_flag + drlt + fatl` | 1.81 | 1.99 | 3.49% | guidance_analyst_drlt_fatl_blend | NOT PURSUED (GOOD, est. self-corr 0.803) |
| 6 | `9qrO8OZV` | `mibnq event-mag + ivaco + drlt + fcf_flag + buzz` (variant) | 1.88 | 1.87 | 9.6% | mibnq_event_magnitude_ivaco_drlt_blend | GOOD, not checked |
| 7 | `kq06vjGP` | `pstkrv event-mag` variant | 1.82 | 1.94 | 11.2% | pstkrv_event_magnitude_ivaco_drlt_blend | GOOD, not checked |
| 8 | `xAkpVdVm` | `pstkrv event-mag` variant | 1.89 | 1.74 | 10.5% | pstkrv_event_magnitude_ivaco_drlt_blend | GOOD, not checked |
| 9 | `d50r3d5j` | `pstkrv event-mag + fatl` variant | 1.46 | 1.78 | 9.3% | pstkrv_event_magnitude_ivaco_drlt_blend | GOOD, not checked |
| 10 | `E5EPNppm` | `pstkrv event-mag + leverage` variant | 1.48 | 1.72 | 8.6% | pstkrv_event_magnitude_ivaco_drlt_blend | GOOD, not checked |
| 11 | `781R32aQ` | `pstkrv event-mag` variant (decay=8) | 1.57 | 1.61 | 11.2% | pstkrv_event_magnitude_ivaco_drlt_blend | GOOD, not checked |
| 12 | `9qrOl0o2` | `pstkrv event-mag + ivaco+drlt+capex_flag+buzz` MARKET | 1.60 | 1.65 | 10.2% | pstkrv_event_magnitude_ivaco_drlt_blend | GOOD, superseded by N1rlJ7mq |
| 13 | `88QxNeKW` | `mibnq event-mag` MARKET | 1.41 | 1.53 | 9.2% | mibnq_event_magnitude_ivaco_drlt_blend | GOOD, superseded |

## BRAIN Check Results

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|------------------|---------------------|
| `N1rlJ7mq` | PASS | PASS | PASS | PASS | PASS | PASS | **PENDING** (never resolved; local est. 0.691 RISKY) | PASS |
| `kq06YLrd` | PASS | PASS | PASS | PASS | PASS | PASS | PENDING (local est. 0.813 BLOCKED) | PASS |
| `oml0kV52` | PASS | PASS | PASS | PASS | PASS | PASS | PENDING (local est. 0.796 BLOCKED) | PASS |

## Dead Ends / Errors This Session

| Expression shape | Result | Note |
|---|---|---|
| `rank(ts_delta(IV_call_T - IV_put_T, d))` (spread momentum, T=60,180) | INFERIOR (S=0.30, -0.24) | New dead zone: `template-iv-spread-momentum.md` |
| `rank(scl12_buzz) * rank(IV_call_60 - IV_put_60)` | INFERIOR (S=0.66, F=0.19) | Sentiment x options interaction, dead |
| `rank(IV_call_60 - IV_put_60) * rank(-1*returns)` | AVERAGE (S=1.46, F=1.03) | Options x reversal, weak but not fully dead |
| `rank(abs(ts_delta(guidance_field/close,3))) + ...` | INFERIOR (S=0.72, F=0.62) | Event-magnitude transform does not transfer to guidance-dataset fields |
| `zscore(fn_derivative_notional_amount_q/close,10) - zscore(...,60)` | ERROR | `zscore()` is cross-sectional single-input; needed `ts_zscore()` |
| `trade_when(ts_std_dev(returns,20) > 0.02, <event-mag blend>, ...)` | WARNING/error | Unit mismatch on this specific leg combination (works elsewhere per `volatility-gate-fixes-sub-universe.md`, but failed here — not fully diagnosed) |
