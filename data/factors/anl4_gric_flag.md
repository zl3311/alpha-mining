---
field: "anl4_gric_flag"
dataset: "analyst4"
family: "analyst_revision"
discovery_session: "20260711-001"
best_sharpe: 2.32
best_fitness: 2.22
best_expression: "ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_gric_flag) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
mechanism: "Gross-income forecast-type revision flag; used here as a decorrelated sub-universe densifier rather than a primary revision signal"
status: "active"
---

# Factor: anl4_gric_flag

*Gross Income — forecast type (revision/new/...)*

## Economic Mechanism

`anl4_gric_flag` flags when an analyst issues a revised or new gross-income
estimate. Standalone it behaves like a typical sparse analyst-revision flag:
weak in raw `rank()` form (S=0.84) but reaches AVERAGE grade (S=1.31, F=1.28)
via `ts_mean(F, 10)` smoothing, consistent with the `zscore-accumulated-revision`
pattern's general finding that sparse event-driven analyst flags need temporal
smoothing to extract signal. Moderately correlated (0.40-0.42) with other
analyst4 flags (`cfi_flag`, `cff_flag`, `cfo_flag`, `totassets_flag`,
`capex_flag`) as expected for the same dataset family.

## Best Known Expression

`ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_gric_flag) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

EXCELLENT, S=2.32, F=2.22, T=10.66%, SUBINDUSTRY, decay=6, TOP3000, USA. Used in
raw `rank()` form here (not the `ts_mean`-smoothed standalone-optimal form) — in
this blend it functions as a `LOW_SUB_UNIVERSE_SHARPE` densifier/stabilizer
rather than the primary signal.

## Lessons

- **Never used in the book before this session** — this is precisely why it
  decorrelates well: swapping the standard `fnd6_drlt`/`fnd6_ivaco`-only
  stabilizer combo in the `event-magnitude-abs-ts-delta` family template for
  one that includes `anl4_gric_flag` instead of a second fundamental6 field
  dropped the family's peer-max correlation from ~0.70 to 0.67, while also
  improving fitness. See `fn_liab_fair_val_l2_q.md` factor entry and pattern
  `data/knowledge/patterns/event-magnitude-fresh-stabilizer.md` for the full
  discovery path.
- Direction gap is -0.70 (positive direction dominant); do not use the negated
  form.
- Best standalone template is `ts_mean(F, 10)`, not `rank(F)` — but in a blend
  context the raw `rank(F)` form (as used here) still contributes usefully as a
  breadth/densifier leg even without the smoothing.
