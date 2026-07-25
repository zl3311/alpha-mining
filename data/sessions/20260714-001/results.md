---
id: "20260714-001-results"
session: "20260714-001"
total_expressions: 0
gate_passers: 1
best_sharpe: 2.83
best_fitness: 2.49
best_alpha_id: "KP9V7YLz"
---

# Results: Session 20260714-001

## Summary

This validation session did not submit new simulations. It recovered one
non-submitted EXCELLENT result from session `20260713-001` and verified it
against BRAIN's authoritative self-correlation endpoint after the asynchronous
calculation had resolved.

## Validated Candidate

| Alpha ID | Sharpe | Fitness | Turnover | Grade | Max Self-Corr | Peer | Verdict |
| --- | ---: | ---: | ---: | --- | ---: | --- | --- |
| KP9V7YLz | 2.83 | 2.49 | 15.63% | EXCELLENT | 0.8015 | O0Z6NE0b | SAFE via Sharpe premium (0.8015 is over the 0.70 gate; clears only because S=2.83 >= 1.10x the peer's Sharpe) |

## Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_msaq / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_ffo_flag) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

## BRAIN Check Results

All eight BRAIN checks passed on 2026-07-14. The decisive check was
`SELF_CORRELATION`: BRAIN measured 0.8015 against the ACTIVE
`O0Z6NE0b` and returned `PASS`. The candidate Sharpe of 2.83 exceeds
`1.10 × 2.10 = 2.31`, qualifying for BRAIN's Sharpe-premium override.

## Interpretation

The candidate is technically submittable, but its self-correlation is high.
It should be considered after lower-correlation EXCELLENT+ candidates because
it consumes more of the future correlation budget.
