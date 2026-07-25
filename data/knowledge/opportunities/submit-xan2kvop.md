---
type: "submit-candidate"
alpha_id: "xAn2kvOp"
status: "SUBMITTED"
priority: "medium"
grade: "EXCELLENT"
sharpe: 1.75
fitness: 2.21
turnover: 0.065
self_corr_max: 0.5963
neutralization: "SUBINDUSTRY"
decay: 6
family: "event_leverage_analyst_revision"
session: "20260612-001"
brain_url: "https://platform.worldquantbrain.com/alpha/xAn2kvOp"
queued: "2026-06-12"
submitted: "2026-06-14"
---

# Submit xAn2kvOp (Event + Leverage + FATL + Net Profit Revision)

## Expression

`rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close) + zscore(ts_sum(anl4_netprofit_flag, 22))`

## Why Submittable

- Self-corr 0.5963 vs current book, below the raw 0.70 threshold.
- All computable BRAIN checks PASS.
- EXCELLENT grade, S=1.75, F=2.21.

## Risk Assessment

This shares analyst net profit revision exposure with `xAn1LqXm`; recheck if that
candidate is activated first. It is lower priority than `6XEo91jO` because its
grade and Sharpe are lower.

## Reviewer Action

Submitted on the BRAIN platform on 2026-06-14. `data/book/xAn2kvOp.md` has been
flipped to `status: ACTIVE`.
