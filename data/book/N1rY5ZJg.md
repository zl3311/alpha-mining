---
alpha_id: "N1rY5ZJg"
name: "liab_fair_val_a_event_magnitude_ffo_ivaco_drlt_oc_sales"
status: "ACTIVE"
submitted: "2026-07-17"
grade: "EXCELLENT"
sharpe: 2.23
fitness: 2.20
turnover: 0.078
returns: 0.119
family: "fair_val_liab_event_magnitude_sales_densify"
mechanism: "Event-magnitude on annual liability fair-value changes, blended with leverage premium, FFO revision flag, investing-activities and deferred-revenue stabilizers, overnight gap, and sales-estimate-count densifier"
fields:
  - "fn_liab_fair_val_a"
  - "equity"
  - "assets"
  - "anl4_ffo_flag"
  - "fnd6_ivaco"
  - "fnd6_drlt"
  - "open"
  - "close"
  - "sales_estimate_count_quarterly"
expression: "ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_a / close, 3))) + rank(-1 * equity / assets) + rank(anl4_ffo_flag) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(open / close - 1) + rank(sales_estimate_count_quarterly), 5)"
neutralization: "SUBINDUSTRY"
decay: 6
delay: 1
truncation: 0.08
region: "USA"
universe: "TOP3000"
self_corr_max: 0.6638
self_corr_peer: "rKlo39p1"
self_corr_result: "PASS (AUTHORITATIVE — BRAIN /alphas/N1rY5ZJg/check: SELF_CORRELATION {result: PASS, value: 0.6638, limit: 0.7})"
self_corr_method: "brain_api_check_endpoint (authoritative). Confirmed stable on immediate re-poll."
session: "20260717-001"
brain_url: "https://platform.worldquantbrain.com/alpha/N1rY5ZJg"
tags:
  - "fn_liab_fair_val_a"
  - "anl4_ffo_flag"
  - "event_magnitude"
  - "fair_value_liability"
  - "sales_estimate_count"
  - "session_20260717-001"
---

# Alpha: N1rY5ZJg

## Expression

```
ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_a / close, 3))) + rank(-1 * equity / assets) + rank(anl4_ffo_flag) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(open / close - 1) + rank(sales_estimate_count_quarterly), 5)
```

## Mechanism

Annual Level-aggregate liability fair-value jumps (`fn_liab_fair_val_a`) are
sparse MTM / Level reclassification events. The event-magnitude transform
captures jump *size*; leverage premium, FFO revision, `ivaco`/`drlt`, overnight
gap, and analyst sales-coverage breadth densify the cross-section enough to
clear concentration / sub-universe gates while keeping self-corr below 0.70.

## Self-Correlation Profile

- Authoritative BRAIN `/check`: **PASS 0.6638** (limit 0.70)
- Closest peer: `rKlo39p1` (tlcf event-magnitude family, S=2.13)
- Note: the same structure *without* `sales_estimate_count_quarterly`
  (`XgndlqrX`, F=2.00) **FAILED** self-corr at 0.725 — the sales-count
  densifier both pushed grade to EXCELLENT and lowered correlation.

## Post-Submission

Submitted by human 2026-07-17. BRAIN confirms `status: ACTIVE`, remaining
computable checks PASS; `/check` returns `ALREADY_SUBMITTED` with peer corr
0.6638 vs `rKlo39p1` (matches pre-submission authoritative PASS).
