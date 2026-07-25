---
field: "fnd6_pstkrv"
dataset: "fundamental6"
family: "preferred_stock_redemption_event"
discovery_session: "20260719-001"
best_sharpe: 2.32
best_fitness: 2.07
best_expression: "ts_decay_linear(rank(abs(ts_delta(fnd6_pstkrv / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)"
mechanism: "Discrete preferred-stock redemption-value swings are sparse capital-structure events; market underreacts to event magnitude"
status: "active"
redundancy_cluster: 81
---

# Factor: fnd6_pstkrv

## Economic Mechanism

`fnd6_pstkrv` is Preferred Stock — Redemption Value. Levels and signed deltas
are weak standalone predictors (profile best S≈0.63, INFERIOR). Large absolute
3-day changes, however, mark discrete capital-structure events (issuance,
call/refinance, conversion, remeasurement) whose size the market underreacts
to — the same event-magnitude logic that works for inventory, tax, PPE, and
fair-value anchors.

## Best Known Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_pstkrv / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_fcf_flag) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)`

→ [N1rlJ7mq](https://platform.worldquantbrain.com/alpha/N1rlJ7mq): EXCELLENT,
S=2.32, F=2.07, self-corr PASS 0.6903.

## Lessons

- Standalone rank/delta/zscore templates fail LOW_SHARPE — do not mine levels.
- Event-magnitude + dual stabilizer (`ivaco`+`drlt`) + FCF flag + buzz clears
  all gates; IV-spread hybrids on this anchor fail `LOW_SUB_UNIVERSE_SHARPE`.
- Omitting the leverage leg still reaches EXCELLENT on this anchor.
- Redundancy cluster #81 — relatively orthogonal to mega-clusters.
