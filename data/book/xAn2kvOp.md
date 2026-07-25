---
alpha_id: "xAn2kvOp"
name: "event3d_leverage_netprofit"
tags:
  - "event_magnitude"
  - "leverage"
  - "analyst4"
  - "netprofit"
  - "fundamental6"
  - "fnd6_itci"
  - "fnd6_fatl"
  - "equity_assets"
  - "abs_ts_delta"
  - "session_20260612-001"
  - "excellent"
expression: "rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close) + zscore(ts_sum(anl4_netprofit_flag, 22))"
sharpe: 1.75
fitness: 2.21
turnover: 0.065
grade: "EXCELLENT"
family: "event_leverage_analyst_revision"
mechanism: "Inventory event magnitude and financial leverage premium, stabilized by fixed assets and accumulated net profit estimate revisions. Analyst confirmation and the fatl stabilizer keep self-correlation below the raw 0.70 threshold."
fields:
  - "fnd6_itci"
  - "equity"
  - "assets"
  - "fnd6_fatl"
  - "anl4_netprofit_flag"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.5963
self_corr_peer: "xAn1LqXm"
self_corr_verdict: "PASS"
brain_checks: "ALL_PASS"
status: "ACTIVE"
session: "20260612-001"
discovered: "2026-06-12"
submitted: "2026-06-14"
brain_url: "https://platform.worldquantbrain.com/alpha/xAn2kvOp"
---

# xAn2kvOp — Event Magnitude + Leverage + FATL + Net Profit Revision

## Expression

`rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close) + zscore(ts_sum(anl4_netprofit_flag, 22))`

## Mechanism

The expression combines the inventory event-magnitude template with the leverage
premium, fixed assets, and sparse analyst net profit revision confirmation. It
tests whether a capital-intensity stabilizer plus earnings-revision agreement
can preserve lower self-correlation versus the deferred revenue event family.

## Why Submittable

- Self-corr 0.5963 vs `xAn1LqXm`, below the raw 0.70 threshold.
- All computable BRAIN checks PASS.
- EXCELLENT grade, S=1.75, F=2.21.
- Cleaner self-correlation profile than the higher-Sharpe event variants blocked
  against `0m8GV1Pp`.

## Risk Assessment

This shares `anl4_netprofit_flag` with the pending leverage-revision candidate
`xAn1LqXm`; if that alpha is officially activated before this one, recheck
self-correlation and submission ordering.

## Post-Submission

Submitted on BRAIN on 2026-06-14 and marked ACTIVE locally.
