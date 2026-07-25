---
pattern: "directional-gating-by-fundamental-trend"
discovered: "20260713-001"
applicable_to: "leverage premium, fundamental value anchors, gated by the trend direction of a second SLOW fundamental (not price/volume)"
confidence: "high (authoritative BRAIN self-corr PASS confirmed)"
best_alpha_id: "QPVWnxKK"
best_sharpe: 2.53
best_fitness: 1.71
best_self_corr_brain: 0.5667
best_self_corr_result: "PASS"
---

# Pattern: Gate a Fundamental Anchor by the Sign of Another SLOW Fundamental's Trend

## The finding

`data/knowledge/dead_zones/template-directional-gating-sign-delta.md` proved
that gating a fundamental by `sign(ts_delta(close/volume, d))` (a FAST
price/volume proxy) is dead (uniformly negative Sharpe, high turnover) and
explicitly suggested the untested alternative: gate by another SLOW-moving
signal instead. This session confirms that alternative works — structurally
novel (genuinely different operator tree from any additive/product blend in
the book) and produces a **BRAIN-confirmed self-correlation PASS at 0.5667**,
comfortably below the 0.70 threshold.

## Template

```
ts_decay_linear(rank(-1 * equity / assets) * sign(ts_delta(GATE_FIELD, 20)) + rank(STABILIZER / close) [+ rank(ts_mean(scl12_buzz, 5) * (-1 * returns))], 5)
```

| Parameter | Recommended | Notes |
|-----------|-------------|-------|
| GATE_FIELD | `fnd6_newqv1300_msaq` (or another fresh slow fundamental) | Window sweep d=10/20/40 all land in the same AVERAGE-GOOD band; d=20 marginally best |
| STABILIZER | `fnd6_ivaco` | Critical for fitness; `fnd6_drlt` also works, slightly lower |
| Buzz 5th leg | optional | Lifts AVERAGE -> GOOD (F 1.32 -> 1.71-1.88) at negligible correlation cost |
| Neutralization | SUBINDUSTRY | |
| Platform decay | 6 (default) or 10 | decay=10 does not meaningfully change fitness (turnover only drops 22.7% -> 19.9%) |

## Best result

`QPVWnxKK`: GOOD, S=2.53, F=1.71, T=22.7%. BRAIN `/check` (via
`/correlations/self` fallback) confirmed `SelfCorr=0.5667, Result=PASS`.

## Mechanism

The leverage-premium signal (`rank(-1*equity/assets)`) is a slow, persistent
cross-sectional tilt. Gating it by the direction of a SECOND slow fundamental's
recent trend (here, whether OCI marketable-security adjustments are rising or
falling over 20 days) turns the leverage tilt on/off in a way that is
economically coherent (leverage matters differently depending on whether the
firm's mark-to-market asset base is expanding or contracting) without the
whipsaw problem of gating by fast price/volume signals — the gate flips far
less often because both series are quarterly/slow-moving fundamentals.

## Ceiling

Despite tuning (window sweep 10/20/40, decay sweep 5/8/10, stabilizer swap
ivaco/drlt, adding ffo_flag/current_ratio as a 4th leg, swapping which
component is gated vs additive), fitness plateaued at F=1.65-1.88 (GOOD) across
7+ variants this session — turnover stays structurally in the 17-27% band
because the `sign()` gate still flips more often than the underlying fitness
math rewards. This appears to be a genuine ceiling for the 2-3 leg form of this
template, not a tuning artifact.

## When to use

- Need a genuinely novel (per `novelty-required.md`) operator-tree shape with
  confirmed-safe self-correlation.
- Acceptable to submit at GOOD grade rather than holding out for EXCELLENT —
  this is a legitimate low-corr filler, not (yet) a breakthrough.
- Future work: try gating a DIFFERENT anchor (not leverage) by this same
  mechanism, or try a 3-way gate (product of two sign() gates) to see if
  fitness can clear the GOOD ceiling without re-introducing turnover.
