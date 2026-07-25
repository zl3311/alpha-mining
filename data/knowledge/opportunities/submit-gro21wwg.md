---
type: "submit-candidate"
alpha_id: "Gro21wWG"
status: "ARCHIVED"
priority: "high"
grade: "SPECTACULAR"
sharpe: 2.59
fitness: 4.33
turnover: 0.0608
self_corr_max: 0.8802
neutralization: "MARKET"
decay: 10
family: "iv90_vol_regime_spread"
session: "20260614-003"
brain_url: "https://platform.worldquantbrain.com/alpha/Gro21wWG"
queued: "2026-06-14"
---

# Submit Gro21wWG (IV90 Volatility-Gated Spread)

> **Archived, never submitted.** The project ended while this candidate was still in the
> queue. Kept as a record of the submission-review format.

## Expression

`trade_when(ts_std_dev(returns, 20) > 0.02, zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), ts_std_dev(returns, 20) < 0.01)`

## Why Submittable

- BRAIN `/check` reports all computable checks PASS.
- BRAIN `SELF_CORRELATION` reports PASS at 0.8802. This relies on the
  Sharpe-premium escape because raw correlation is above 0.70.
- SPECTACULAR grade, S=2.59, F=4.33, turnover 6.08%.

## Risk Assessment

The full self-correlation peer breakdown timed out, so the exact top peer is not
recorded. Recheck BRAIN self-correlation immediately before official submission,
especially if another options or IV-spread alpha is activated first.

## Reviewer Action

Submit on the BRAIN platform if desired, then set `status: SUBMITTED` and flip
`data/book/Gro21wWG.md` to `status: ACTIVE`. If declined, set `status: REJECTED`.
