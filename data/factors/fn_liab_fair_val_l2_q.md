---
field: "fn_liab_fair_val_l2_q"
dataset: "fundamental2"
family: "fair_value_liability"
discovery_session: "20260711-001"
best_sharpe: 2.32
best_fitness: 2.22
best_expression: "ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_gric_flag) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
mechanism: "Event-magnitude of Level-2 (model-priced) fair-value liability changes signals a re-marking event (rate/credit shock, hedge restructuring) that the market underreacts to, regardless of direction"
status: "active"
---

# Factor: fn_liab_fair_val_l2_q

*Liabilities Fair Value, Recurring, Level 2 (Quarterly)*

## Economic Mechanism

Level-2 fair-value liabilities are financial instruments (derivatives,
structured notes, hedges) priced by internal models using observable market
inputs rather than a quoted market price. Because they are not marked by an
external market, large quarter-over-quarter revaluations reflect either a
genuine change in the underlying risk exposure (rate/credit-spread shock) or a
valuation-model/assumption change — both of which are opaque to most market
participants and get underreacted to. The `abs(ts_delta(F/close, 3))` transform
captures the SIZE of this re-marking event regardless of direction, following
the same logic as the proven `event-magnitude-abs-ts-delta` template (originally
validated on `fnd6_itci` inventory events).

## Best Known Expression

`ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_gric_flag) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

EXCELLENT, S=2.32, F=2.22, T=10.66%, SUBINDUSTRY, decay=6, TOP3000, USA.

## Lessons

- **Standalone is LOW_FITNESS-blocked**: best solo form `rank(F / close)`
  reaches S=1.41 but F=0.86 (INFERIOR by fitness gate). The `abs(ts_delta(...))`
  event-magnitude transform is what makes it usable in a blend.
- **Correlation with the itci/ppegtq/tlcf/txw event-magnitude family is
  field-dependent, not template-dependent**: `fnd6_dltis` (also tested this
  session on the identical 5-leg template) correlated 0.94 with `WjGVJ7bN`
  (txw-anchored) — both are debt/tax flow items and economically adjacent. This
  field correlates a much lower 0.67-0.71 against the same peer set, likely
  because fair-value-liability re-marking is a distinct economic driver from
  inventory/PPE/tax-loss/excise-tax events.
- **Stabilizer-leg choice materially changes correlation, not just fitness**:
  swapping the standard `fnd6_drlt` sub-universe-fixer leg for `fnd6_fatl` or
  `fnd6_dlto` (both also used elsewhere in the book) still left correlation at
  0.69-0.70 vs `rKlo39p1`. Swapping instead to `anl4_gric_flag` (a field with
  zero prior usage in this family) dropped the same peer's correlation to 0.67
  while simultaneously improving Sharpe/Fitness (S=2.16→2.32, F=2.33→2.22).
  Prefer swapping in a genuinely unused stabilizer leg over tuning windows/decay
  when the goal is decorrelation, not just fitness.
- **`trade_when` realized-vol gating failed with a permanent BRAIN unit-type
  error** (`Incompatible unit for input of "greater"`) on this specific
  expression shape (event-magnitude inner term + `ts_decay_linear` outer wrap +
  `trade_when` gate). Not resolved; avoid this exact combination until the root
  cause is understood.
