---
category: "dead_zone"
entity_type: "template"
template: "rank(ts_delta(IV_call_T - IV_put_T, d))"
discovered: "20260715-002"
expressions_tested: 2
best_sharpe: 0.30
status: "dead_end"
confidence: "medium"
---

# Template: IV Call-Put Spread MOMENTUM (delta of the spread, not the level)

`iv270-spread-family.md`'s "still viable" section flagged "IV rank/momentum
(ts_delta of IV) rather than cross-sectional level" as unknown territory.
Tested at two non-270 tenors to also avoid the confirmed IV270 correlation
block:

| Expression | S | F | T | Grade |
|-----------|---|---|---|-------|
| `ts_decay_linear(rank(ts_delta(implied_volatility_call_60 - implied_volatility_put_60, 5)), 8)` | 0.30 | 0.05 | 46.0% | INFERIOR |
| `ts_decay_linear(rank(ts_delta(implied_volatility_call_180 - implied_volatility_put_180, 10)), 8)` | -0.24 | -0.04 | 35.3% | INFERIOR |

Both dead: near-zero-to-negative Sharpe with very high turnover (35-46%).
Taking the day-over-day CHANGE in the call-put spread (rather than its
smoothed level, as in the proven `iv-spread-zscore-tsmean` pattern) produces
noise, not signal — the spread's LEVEL carries the informative skew signal;
its short-horizon delta does not.

## Rule

Do not pursue `ts_delta(IV_call_T - IV_put_T, d)` as a standalone signal at
any tenor. The proven form remains `zscore(ts_mean(IV_call_T - IV_put_T, 22))`
(level, smoothed) per `iv-spread-zscore-tsmean.md`.
