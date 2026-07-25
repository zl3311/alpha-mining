---
category: "dead_zone"
entity_type: "family"
family: "fundamental2_sparse_ts_zscore"
discovered: "20260614-001"
expressions_tested: 22
best_sharpe: 1.39
best_fitness: 3.06
blocking_check: "CONCENTRATED_WEIGHT"
status: "blocked"
---

# Fundamental2 Sparse ts_zscore Family

Sparse fundamental2 fields can show spectacular aggregate metrics under
`ts_zscore`, but the resulting alphas are structurally blocked by BRAIN's
`CONCENTRATED_WEIGHT` check.

## Evidence

Session `20260614-001` tested the fresh HF tax-benefit anomaly anchored on:

`ts_zscore(fn_excess_tax_benefit_from_share_based_comp_fin_activities_a, 22)`

The raw annual anchor `RRroP5ra` reached S=4.10 and F=10.75 but failed:

- `CONCENTRATED_WEIGHT`: 0.50 vs 0.10
- `LOW_SUB_UNIVERSE_SHARPE`: -1.95 vs 2.17

The best repaired quarterly variants (`JjdJxrnx`, `pw7e5w06`) reached S=1.39 and
F=3.06 and passed sub-universe, but both still failed `CONCENTRATED_WEIGHT` at
0.50 vs 0.10.

## Tried Fixes

- `rank(ts_zscore(...))`
- `group_rank(ts_zscore(...), subindustry)`
- `ts_decay_linear(...)`
- Additive blends with `rank(-1 * equity / assets)`, `rank(fnd6_drlt / close)`,
  and buzz-reversal stabilizers
- `ts_backfill(...)` and `group_backfill(...)`
- Longer backfill windows, winsorization, and smoothed backfilled inputs

## Rule

Do not mine additional sparse fundamental2 `ts_zscore` variants unless the plan
includes a genuinely new coverage repair mechanism and explicitly checks
`CONCENTRATED_WEIGHT` before treating aggregate metrics as actionable.
