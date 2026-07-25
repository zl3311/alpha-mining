---
field: "fnd6_cld2"
dataset: "fundamental6"
family: "capitalized_lease_fopo_leverage_free_blend"
discovery_session: "20260716-001"
best_sharpe: 2.29
best_fitness: 2.26
best_expression: "ts_decay_linear(rank(fnd6_cld2 / close) + rank(fnd6_fopo / close) + 2 * rank(fnd6_ivaco / close) + 2 * rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)"
mechanism: "Capitalized (finance) lease obligation due in year 2 -- a balance-sheet financing commitment; firms taking on more near-term finance-lease burden are systematically mispriced relative to peers."
status: "active"
---

# Factor: fnd6_cld2

## Economic Mechanism

`fnd6_cld2` is the disclosed amount of capitalized (finance) lease payments
due in the second fiscal year following the balance sheet date. Unlike
operating leases (off-balance-sheet historically, now ASC 842 right-of-use
assets), capitalized/finance leases represent debt-like obligations already
on the balance sheet. Standalone (`rank(fnd6_cld2 / close)`), it shows S=1.29,
F=0.96, T=2.3%, with 100% positive-year consistency 2019-2023 (per
`data/knowledge/factor_profiles/fnd6_cld2.md`) — an unusually clean,
low-turnover signal for a single fundamental field. It sits in redundancy
cluster #14 with only one other member (`fnd6_cld3`), meaning it is
essentially unrepresented anywhere in the 47-alpha submitted book — the
freshest anchor tested this session by redundancy-cluster criteria.

## Best Known Expression

```
ts_decay_linear(rank(fnd6_cld2 / close) + rank(fnd6_fopo / close) + 2 * rank(fnd6_ivaco / close) + 2 * rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)
```
EXCELLENT, S=2.29, F=2.26, T=11.9%. See `data/book/aknmG1M6.md`.

## Lessons

- Standalone (`rank(fnd6_cld2/close)`, no transform) already beats the
  `abs(ts_delta(...))` event-magnitude transform used throughout the
  saturated event-magnitude family for this field — event-magnitude form
  reached only F=2.00-2.13 combined with the full stabilizer stack, vs the
  plain ratio form reaching F=2.26 with a leaner, leverage-free stack. Not
  every fresh anchor benefits from the event-magnitude wrapper; test both.
- Novel structural transforms (multi-horizon spread `ts_delta(F,5)-ts_delta(F,22)`,
  MA crossover `ts_mean(F,5)-ts_mean(F,22)`, `ts_zscore` regime divergence)
  all produced near-zero signal on this field (S=-0.21 to 0.13, T=17-21%) —
  see dead zone `template-multi-horizon-ma-crossover-regime-divergence.md`.
  The plain ratio form is the correct building block, not a fancier
  transform.
- Combined with `fnd6_fopo` (another fresh fundamental6 field) plus
  double-weighted `fnd6_ivaco` and double-weighted buzz-reversal, but
  WITHOUT the leverage leg (`-1*equity/assets`) or `fnd6_drlt`, which were
  believed at the time to jointly drive the event-magnitude family's
  self-corr to 0.775-0.926 regardless of anchor (see pattern
  `leverage-free-fresh-anchor-decorrelation.md`). Dropping `drlt` turned out
  not to be necessary: `N1rlJ7mq` keeps it (with the analyst flag) and still
  reaches 0.6903 PASS. Leverage is the leg that has to go.
