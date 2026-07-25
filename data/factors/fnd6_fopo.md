---
field: "fnd6_fopo"
dataset: "fundamental6"
family: "capitalized_lease_fopo_leverage_free_blend"
discovery_session: "20260716-001"
best_sharpe: 2.29
best_fitness: 2.26
best_expression: "ts_decay_linear(rank(fnd6_cld2 / close) + rank(fnd6_fopo / close) + 2 * rank(fnd6_ivaco / close) + 2 * rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)"
mechanism: "Funds From Operations - Other (a residual FFO component beyond core operating cash flow); a fresh cash-quality anchor uncorrelated with the book's existing accrual/depreciation/debt-flow signals."
status: "active"
---

# Factor: fnd6_fopo

## Economic Mechanism

`fnd6_fopo` captures the "other" (residual, non-core) component of Funds
From Operations, a REIT/real-asset-style cash-flow metric. Standalone
(`rank(fnd6_fopo / close)`), S=1.06-1.09, F=0.69-0.73, T=1.5-2.3% (per
`data/knowledge/factor_profiles/fnd6_fopo.md`) — modest but genuinely
uncorrelated with the book's dominant debt/tax/depreciation/fair-value event-
magnitude cluster (redundancy cluster #31, 14 members, none used elsewhere
in the book).

## Best Known Expression

```
ts_decay_linear(rank(fnd6_cld2 / close) + rank(fnd6_fopo / close) + 2 * rank(fnd6_ivaco / close) + 2 * rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)
```
EXCELLENT, S=2.29, F=2.26, T=11.9%. See `data/book/aknmG1M6.md`.

## Lessons

- Alone, or with only ONE other fresh anchor, `fnd6_fopo` caps at AVERAGE
  (F<=1.2) — it needs the double-weighted `ivaco` + double-weighted buzz
  legs to reach EXCELLENT, per pattern
  `leverage-free-fresh-anchor-decorrelation.md`.
- The `abs(ts_delta(fnd6_fopo/close,3))` event-magnitude transform combined
  with the FULL classic stabilizer stack (leverage + ivaco + drlt + buzz)
  reached the highest raw fitness of the session (F=2.21, alpha `GrLjgZrx`)
  but was BLOCKED at local self-corr 0.926 vs the `tlcf_event_magnitude_buzz_blend`
  family (`rKlo39p1`) — the highest-risk candidate tested this session. Do
  not resurrect the event-magnitude form of this field with the classic
  stack; use the leverage-free ratio-form blend instead.
