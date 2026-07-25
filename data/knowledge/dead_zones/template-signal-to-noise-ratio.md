---
category: "dead_zone"
entity_type: "template"
template: "rank(ts_delta(F, 5) / ts_std_dev(F, 20))"
discovered: "20260715-001"
expressions_tested: 2
best_sharpe: -0.04
status: "dead_end"
confidence: "medium"
---

# Template: Signal-to-Noise Ratio (`ts_delta(F,5) / ts_std_dev(F,20)`)

Normalizing a fundamental field's recent change by its own trailing
volatility (a "z-scored momentum" transform, listed as an untested novel
structure in `novelty-required.md`/`signal-generation` skill) produces no
signal and extremely high turnover.

## Evidence (session 20260715-001)

| Expression | S | F | T |
|-----------|---|---|---|
| `rank(ts_delta(fnd6_dpvieb, 5) / ts_std_dev(fnd6_dpvieb, 20)) + rank(-1*equity/assets) + rank(fnd6_ivaco/close)` | -0.04 | -0.01 | 44.4% |
| `rank(ts_delta(fn_assets_fair_val_l2_q, 5) / ts_std_dev(fn_assets_fair_val_l2_q, 20)) + rank(-1*equity/assets) + rank(fnd6_drlt/close)` | -0.13 | -0.04 | 36.2% |

## Why it fails

Dividing a fundamental's short-horizon delta by its own trailing standard
deviation amplifies noise during low-volatility quarters (small denominator)
far more than it normalizes genuine signal during high-volatility
quarters — the opposite of the intended effect for a slow-moving,
sparsely-updated fundamental field (quarterly cadence means most of the
20-day trailing window is flat, so `ts_std_dev` is dominated by a handful of
update days and the ratio spikes unpredictably around them). Turnover is
2.5-3.5x higher than the standard `abs(ts_delta(F/close, d))` event-magnitude
form on the same fields, with negative/zero Sharpe.

## Rule

Do not use `ts_delta(F,d) / ts_std_dev(F,d2)` as a normalization for
low-frequency fundamental fields. If a signal-to-noise-style transform is
revisited, it may work for daily/dense fields (price, volume, IV) where the
trailing std-dev window is not dominated by a few discrete update events —
untested.
