---
type: "submit-candidate"
alpha_id: "YPpjReEW"
status: "ARCHIVED"
priority: "medium"
grade: "AVERAGE"
sharpe: 1.74
fitness: 1.09
turnover: 0.1838
self_corr_max: 0.4613
neutralization: "SUBINDUSTRY"
decay: 6
family: "options_news_volatility_regime"
session: "20260616-001"
brain_url: "https://platform.worldquantbrain.com/alpha/YPpjReEW"
queued: "2026-06-16"
---

# Submit YPpjReEW (Options News Volatility Regime)

> **Archived, never submitted.** The project ended while this candidate was still in the
> queue. Kept as a record of the submission-review format.

## Expression

`trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) * rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.01)`

## Why Submittable

- BRAIN self-correlation check PASS at 0.4613, below the 0.70 threshold.
- All computable BRAIN checks PASS.
- AVERAGE grade, S=1.74, F=1.09, turnover 18.38%.

## Risk Assessment

This is a decorrelated filler rather than a high-grade submission. The main risk
is low marginal point value from AVERAGE grade, not self-correlation or BRAIN
checks. Its value is that it introduces an underrepresented option-skew/news-flow
regime leg with substantially cleaner self-corr than most recent book-saturation
candidates.

## Reviewer Action

Submit on the BRAIN platform if desired, then set `status: SUBMITTED` and flip
`data/book/YPpjReEW.md` to `status: ACTIVE`. If declined, set `status: REJECTED`.
