---
field: "anl4_epsr_flag"
dataset: "analyst4"
family: "eps_revision"
discovery_session: "20260626-001"
best_sharpe: 2.08
best_fitness: 2.36
best_expression: "ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close) + rank(open / close - 1), 5)"
mechanism: "Accumulated EPS revision momentum captures analyst sentiment shifts that the market slowly incorporates"
status: "active"
---

# Factor: anl4_epsr_flag

## Economic Mechanism

EPS revision flags signal discrete changes in analyst earnings-per-share estimates.
Accumulated over 22 days via ts_sum, they capture the momentum of analyst sentiment.
The market underreacts to these revisions, creating a drift effect where stocks with
positive EPS revisions continue to outperform. The zscore normalization is critical
because the flag distribution is heavily zero-dominated (most stocks have no revision
on any given day).

## Best Known Expression

```
ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)) + rank(fnd6_newqv1300_dpactq / close) + rank(open / close - 1), 5)
```

XgpJGaL0: EXCELLENT S=2.08, F=2.36, self-corr=0.604 PASS

## Lessons

- zscore+ts_sum is mandatory for this sparse flag (rank produces wrong-sign signals)
- Window=22 is the sweet spot; 10 drops to GOOD, 44 also GOOD
- Standalone with zscore+ts_sum: AVERAGE S=1.31 (from prior sessions)
- Works best in SUBINDUSTRY neutralization; MARKET kills the signal
- Pairs well with depreciation value (negative PnL correlation, rho ~ -0.35)
- Multiplicative combination kills the signal (concentrates too much)
