---
type: "submit-candidate"
alpha_id: "N1rY5ZJg"
status: "SUBMITTED"
priority: "resolved"
submitted: "2026-07-17"
grade: "EXCELLENT"
sharpe: 2.23
fitness: 2.20
turnover: 0.078
self_corr_max: 0.6638
neutralization: "SUBINDUSTRY"
decay: 6
family: "fair_val_liab_event_magnitude_sales_densify"
session: "20260717-001"
brain_url: "https://platform.worldquantbrain.com/alpha/N1rY5ZJg"
queued: "2026-07-17"
---

# Submit N1rY5ZJg (Annual Liab Fair-Value Event-Magnitude + FFO + OC + Sales Densify)

## Expression

`ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_a / close, 3))) + rank(-1 * equity / assets) + rank(anl4_ffo_flag) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(open / close - 1) + rank(sales_estimate_count_quarterly), 5)`

## Why submittable

- **All 8 BRAIN checks PASS**, including authoritative
  `SELF_CORRELATION: PASS value=0.6638` via `/alphas/N1rY5ZJg/check`
  (peer `rKlo39p1`, S=2.13) — below 0.70, no Sharpe-premium escape needed.
- Grade **EXCELLENT**, S=2.23, F=2.20, T=7.8%. SUBINDUSTRY, decay=6.
- Fresh annual liability fair-value anchor (`fn_liab_fair_val_a`) distinct from
  the already-ACTIVE quarterly L2 sibling (`YP0bLdzA` / `fn_liab_fair_val_l2_q`).
- `sales_estimate_count_quarterly` densifier was necessary: OC-only variant
  `XgndlqrX` hit F=2.00 GOOD but FAILED self-corr at 0.725.

## Platform URL

https://platform.worldquantbrain.com/alpha/N1rY5ZJg

## Submission

Submitted by human **2026-07-17**. BRAIN status **ACTIVE**.
