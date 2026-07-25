---
alpha_id: "le0gY6Ze"
name: "event_leverage_drlt_blend"
tags:
  - "event_magnitude"
  - "leverage"
  - "fundamental6"
  - "fnd6_itci"
  - "fnd6_drlt"
  - "equity_assets"
  - "abs_ts_delta"
  - "session_20260611-001"
  - "spectacular"
expression: "rank(abs(ts_delta(fnd6_itci / close, 5))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close)"
sharpe: 2.62
fitness: 2.74
turnover: 0.041
grade: "SPECTACULAR"
family: "event_leverage_fundamental"
mechanism: "Novel event detection via absolute inventory change magnitude combined with financial leverage premium and deferred revenue quality."
fields:
  - "fnd6_itci"
  - "equity"
  - "assets"
  - "fnd6_drlt"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_max: 0.5466
self_corr_peer: "MPbgqZ7o"
self_corr_verdict: "PASS"
brain_checks: "ALL_PASS"
status: "SUPERSEDED"
superseded_by: "0m8GV1Pp"
session: "20260611-001"
discovered: "2026-06-11"
brain_url: "https://platform.worldquantbrain.com/alpha/le0gY6Ze"
---

# le0gY6Ze — Event Magnitude + Leverage + Deferred Revenue

Superseded by 0m8GV1Pp (d=3 window variant, S=2.64, F=2.77).
