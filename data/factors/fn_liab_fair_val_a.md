---
field: "fn_liab_fair_val_a"
dataset: "fundamental2"
family: "fair_value_liability"
discovery_session: "20260717-001"
best_sharpe: 2.23
best_fitness: 2.20
best_expression: "ts_decay_linear(rank(abs(ts_delta(fn_liab_fair_val_a / close, 3))) + rank(-1 * equity / assets) + rank(anl4_ffo_flag) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(open / close - 1) + rank(sales_estimate_count_quarterly), 5)"
mechanism: "Annual liability fair-value MTM / reclassification event magnitude predicts subsequent returns"
status: "active"
---

# Factor: fn_liab_fair_val_a

## Economic Mechanism

Annual (period-end) liability fair-value aggregates jump when firms remeasure
Level 1–3 liabilities or reclassify instruments. Markets underreact to the
*magnitude* of those balance-sheet events; combining with leverage premium and
dense coverage legs yields a tradable, decorrelated signal relative to the
quarterly L2 sibling already in the book.

## Best Known Expression

`N1rY5ZJg` — EXCELLENT S=2.23 F=2.20, self-corr PASS 0.6638.

## Lessons

- Bare event-magnitude + leverage + ffo + ivaco + drlt is GOOD (F≈1.58) with
  comfortable self-corr (~0.66).
- Adding `open/close - 1` alone lifts fitness to the EXCELLENT border but
  raises self-corr above 0.70.
- Adding `sales_estimate_count_quarterly` on top restores self-corr PASS while
  clearing F>2.0.
