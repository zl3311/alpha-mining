---
category: "dead_zone"
entity_type: "template"
template: "ts_delta(F,5)-ts_delta(F,22) | ts_mean(F,5)-ts_mean(F,22) | ts_zscore(F,10)-ts_zscore(F,60)"
discovered: "20260716-001"
expressions_tested: 8
best_sharpe: 0.13
status: "dead_end"
confidence: "high"
---

# Templates: Multi-Horizon Spread, MA Crossover, and ts_zscore Regime Divergence

Three genuinely novel operator-tree shapes from `novelty-required.md`'s
"Multi-horizon spreads" section, tested on two fresh fundamental6 anchors
(`fnd6_cld2`, `fnd6_fopo`, both close-normalized) to isolate whether the
STRUCTURE (not field freshness) could produce signal. All failed.

## Evidence (session 20260716-001)

| Template | Expression | S | F | T |
|----------|-----------|---|---|---|
| Multi-horizon spread | `rank(ts_delta(fnd6_cld2/close,5)-ts_delta(fnd6_cld2/close,22))` | -0.21 | -0.06 | 19.2% |
| Multi-horizon spread | `rank(ts_delta(fn_op_lease_min_pay_due_in_5y_a/close,5)-ts_delta(...,22))` | -0.11 | -0.02 | 17.5% |
| MA crossover | `rank(ts_mean(fnd6_cld2/close,5)-ts_mean(fnd6_cld2/close,22))` | 0.13 | 0.03 | 16.9% |
| MA crossover | `rank(ts_mean(fnd6_fopo/close,5)-ts_mean(fnd6_fopo/close,22))` | -0.08 | -0.01 | 15.0% |
| Regime divergence | `rank(ts_zscore(fnd6_cld2/close,10)-ts_zscore(fnd6_cld2/close,60))` | -0.11 | -0.02 | 21.2% |
| Regime divergence | `rank(ts_zscore(fnd6_fopo/close,10)-ts_zscore(fnd6_fopo/close,60))` | 0.07 | 0.01 | 20.0% |

All six near-zero Sharpe, 15-21% turnover (vs 2-3% for the plain ratio form
of the same fields). Two additional variants tested on
`unsystematic_risk_last_360_days` (a model51 field, see
`dataset-model51-high-turnover.md`) showed the same pattern.

## Why they fail

These transforms all effectively difference TWO overlapping windowed
statistics of the SAME slow-moving quarterly fundamental. Since the field
updates discretely (once per quarter) and is flat between updates, both the
short and long window statistics move together except right at the update
event — the difference is dominated by noise around the (rare) update days,
producing a high-turnover, near-zero-Sharpe signal. This generalizes the
existing `signal-to-noise-ratio` dead zone's diagnosis (a `ts_delta/ts_std_dev`
ratio) to differencing-based multi-horizon structures more broadly: **any
transform that subtracts two windowed statistics of a low-frequency
fundamental field is unlikely to produce signal**, regardless of which
specific windowed statistic (delta, mean, or zscore) is used.

## Rule

Do not apply multi-horizon spread (`ts_delta(F,5)-ts_delta(F,22)`), MA
crossover (`ts_mean(F,5)-ts_mean(F,22)`), or `ts_zscore` regime divergence
(`ts_zscore(F,10)-ts_zscore(F,60)`) to fundamental2/fundamental6 fields. If
these structures are revisited, they may still work on DENSE, continuously-
updated series (price, volume, IV) where the windows are not dominated by a
handful of discrete update days — untested in this session.
