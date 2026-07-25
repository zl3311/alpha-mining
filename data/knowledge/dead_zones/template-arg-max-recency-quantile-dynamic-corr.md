---
category: "dead_zone"
entity_type: "template"
template: "ts_arg_max recency-of-extreme | quantile() bucketing | ts_corr(F1,F2,d) non-return | zscore(F,10)-zscore(F,60) multi-horizon spread | cross-dataset ratio F/IV_field"
discovered: "20260713-001"
expressions_tested: 8
best_sharpe: 1.02
best_fitness: 0.64
status: "dead_end"
confidence: "medium"
---

# Templates: `ts_arg_max` Recency, `quantile()`, Non-Return Dynamic Correlation, Multi-Horizon Spread, Cross-Dataset Ratio — All Weak on Fresh Fundamentals

Five genuinely novel operator-tree shapes from `novelty-required.md`'s
"non-linear combinations" / "inter-field ratios" / "dynamic correlation" /
"multi-horizon spreads" sections, tested on two fresh fundamental6/pv1 fields
(`fnd6_newqv1300_msaq`, `current_ratio`) to isolate whether the STRUCTURE
(independent of field freshness) could produce signal. All failed to clear
even GOOD grade.

## Evidence (session 20260713-001, round 1)

| Template | Expression | S | F |
|----------|-----------|---|---|
| `ts_arg_max` recency | `rank(-1 * ts_arg_max(abs(ts_delta(fnd6_newqv1300_msaq / close, 1)), 20))` | 0.77 | 0.36 |
| `ts_arg_max` recency | `rank(-1 * ts_arg_max(abs(ts_delta(current_ratio, 1)), 20))` | -0.80 | -0.40 |
| Multi-horizon spread | `ts_decay_linear(rank(ts_mean(F/close,5) - ts_mean(F/close,40)), 5)` on `msaq` | 0.53 | 0.22 |
| `quantile()` bucketing | `ts_decay_linear(quantile(fnd6_newqv1300_msaq/close) + rank(-1*equity/assets), 5)` | 1.02 | 0.64 |
| Non-return dynamic corr | `rank(ts_corr(fnd6_newqv1300_msaq, fnd6_ivaco, 40))` | 0.10 | 0.04 |
| Non-return dynamic corr | `rank(ts_corr(fnd6_ivaco, implied_volatility_mean_skew_180, 40))` | -0.98 | -0.98 |
| Cross-dataset ratio | `rank(fnd6_newqv1300_msaq / implied_volatility_mean_skew_180)` | -0.18 | -0.09 |
| Directional gating (own field, self-gated by longer window) | `ts_decay_linear(rank(ts_delta(current_ratio,5)) * sign(ts_delta(current_ratio,60)), 5)` | -0.34 | -0.09 |

## Why they fail

- **`ts_arg_max` recency-of-extreme**: the day-index-of-max/min within a short
  window (20 days) is itself a noisy, near-uniformly-distributed statistic for
  slow quarterly fundamentals — most values simply haven't had a large jump
  recently, so the signal is dominated by rare large moves with little
  persistence, similar in spirit to why raw `rank(anl4_flag)` fails for sparse
  event flags (needs `zscore(ts_sum(...))`-style normalization instead, per
  `zscore-accumulated-revision.md`).
- **`quantile()` bucketing**: discretizing into buckets loses the fine-grained
  cross-sectional ordering that `rank()` preserves, without adding robustness
  benefit for these particular fields (which are not extreme-outlier-dominated
  enough to need quantile's coarser buckets).
- **Non-return dynamic correlation between two fundamentals/an option field**:
  extends the already-dead `ts_corr(fundamental, returns, d)` dead zone
  (`template-dynamic-correlation.md`) — time-varying correlation between two
  slow-moving or heterogeneous series (fundamental-fundamental,
  fundamental-option) is noise at the tested 40-day horizon, just as it was
  for fundamental-returns at 20-day.
- **Cross-dataset ratio (fundamental / option field)**: extends the
  same-dataset ratio dead zone (`template-inter-field-ratio.md`) to
  cross-dataset pairs — numerator/denominator scale mismatches (dollar-value
  fundamental vs percentage-point IV skew) produce a ratio with no stable
  cross-sectional interpretation.
- **Self-gating by a longer window of the SAME field**: unlike gating by a
  DIFFERENT slow fundamental (which works — see
  `patterns/directional-gating-by-fundamental-trend.md`), gating a field's
  short-window delta by the SIGN of its own long-window delta produces a
  mean-reversion-vs-momentum ambiguity that nets to noise for `current_ratio`.

## Rule

Do not pursue `ts_arg_max`/`ts_arg_min` recency-of-extreme, `quantile()` as a
drop-in `rank()` replacement, `ts_corr()` between any two non-return series
(fundamental-fundamental or fundamental-option), cross-dataset ratios crossing
a fundamental with an option/IV field, or self-referential directional gating
(a field gated by its own longer-window trend) as standalone signals on fresh
fundamental/pv1 fields. If any of these structures is revisited, it needs a
field with a genuinely different distributional character (e.g. a rare-event
sparse field for `ts_arg_max`, or two fields with a documented strong
theoretical co-movement relationship for `ts_corr`), not just another
fundamental swapped in.
