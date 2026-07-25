---
type: "submit-candidate"
alpha_id: "xAn1LqXm"
status: "SUBMITTED"
priority: "high"
grade: "EXCELLENT"
sharpe: 2.00
fitness: 2.12
turnover: 0.039
self_corr_max: 0.5022
self_corr_result: "PASS"
neutralization: "SUBINDUSTRY"
decay: 6
family: "leverage_analyst_revision"
session: "20260610-001"
brain_url: "https://platform.worldquantbrain.com/alpha/xAn1LqXm"
queued: "2026-06-10"
---

# Submit xAn1LqXm (vol-gated leverage + netprofit revision)

## Expression

`trade_when(ts_std_dev(returns, 30) > 0.025, zscore(-1 * equity / assets) + zscore(ts_sum(anl4_netprofit_flag, 22)), ts_std_dev(returns, 30) < 0.012)`

## Why Submittable

- Self-corr 0.5022 vs current book by authoritative BRAIN `/check` endpoint.
- All computable BRAIN checks PASS.
- EXCELLENT grade, S=2.00, F=2.12, turnover 3.9%.
- Improves on prior leverage + analyst recombinations by using a 30-day volatility
  regime gate.

## Risk Assessment

Top correlated peer from `/check`/`correlations/self` output was `vRmlGnkv`
(corr 0.502, S=1.72), safely below the 0.70 threshold. After submission, closely
related leverage + netprofit variants will likely become redundant.

## Reviewer Action

BRAIN check reported this alpha as ACTIVE on 2026-06-17. `data/book/xAn1LqXm.md`
has been flipped to `status: ACTIVE`.

