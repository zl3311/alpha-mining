---
category: "dead_zone"
entity_type: "template"
template: "rank(F) * sign(ts_delta(price_or_volume, d))"
discovered: "20260709-001"
expressions_tested: 5
best_sharpe: -0.16
status: "dead_end"
confidence: "high"
---

# Template: Directional Gating via `sign(ts_delta(close/volume, d))`

`rank(FUNDAMENTAL) * sign(ts_delta(close, d))` or `* sign(ts_delta(volume, d))`
— gating a slow-moving fundamental anchor by the discrete sign of recent
price/volume momentum — produces uniformly negative Sharpe and very high
turnover (40-60%) regardless of the fundamental field or window used.

## Evidence (session 20260709-001, 5 variants across fnd6_mrct/dcvsub/acqgdwl/tlcf/fn_prepaid_expense_q)

| Expression | S | F | T |
|-----------|---|---|---|
| `rank(fnd6_mrct/close) * sign(ts_delta(close,5))` | -1.10 | -0.52 | 40% |
| `rank(-1*fnd6_acqgdwl/close) * sign(ts_delta(close,5))` | -0.80 | -0.31 | 40% |
| `rank(-1*fnd6_dcvsub/close) * sign(ts_delta(close,10))` | -0.68 | -0.29 | 31% |
| `rank(fnd6_tlcf/close) * sign(ts_delta(volume,5))` | -0.16 | -0.02 | 61% |
| `rank(fn_prepaid_expense_q/close) * sign(ts_delta(volume,10))` | -0.35 | -0.07 | 48% |

## Why it fails

The binary `sign()` gate flips daily as price/volume momentum crosses zero,
causing the position to whipsaw between full-exposure and zero/inverted-exposure
on a fundamental signal that itself changes slowly. This maximizes turnover
(gate churns daily) while adding no informational content (the gate is a noisy,
mean-reverting coin-flip at short horizons, uncorrelated with whether the slow
fundamental's signal is currently "valid"). Continuous-weight alternatives
(`rank(F) * rank(ts_delta(close, 20))`, tested same session on `fnd6_ivaco`,
`rel_num_all`, `enterprise_value`, `fnd6_mrct`) also failed to produce signal
(all Sharpe -0.03 to -0.23), suggesting momentum-gating of slow fundamentals is
not a fruitful direction generally, not just the binary-sign variant.

## Rule

Do not gate a fundamental6/fundamental2 signal by the sign or rank of
`ts_delta(close, d)` or `ts_delta(volume, d)` at any window tested (5, 10, 20).
If directional gating is attempted again, gate by another SLOW-moving signal
(e.g. another fundamental's own trend direction), not a fast price/volume proxy.
