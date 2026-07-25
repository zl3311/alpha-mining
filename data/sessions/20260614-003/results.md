---
id: "20260614-003-results"
session: "20260614-003"
total_expressions: 10
gate_passers: 10
best_sharpe: 2.75
best_fitness: 4.63
best_alpha_id: "RRrOjRdn"
submittable_alpha_id: "Gro21wWG"
---

# Results: Session 20260614-003

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 10 |
| Gate-passers | 10 |
| Submittable candidates | 1 |
| Official submissions | 0 |
| Best aggregate Sharpe | 2.75 (`RRrOjRdn`, blocked) |
| Best aggregate fitness | 4.63 (`RRrOjRdn`, blocked) |
| Best submittable | `Gro21wWG` |

## Gate-Passers

| Alpha ID | Expression | Sharpe | Fitness | Turnover | BRAIN Checks | Self-Corr | Verdict |
|----------|------------|--------|---------|----------|--------------|-----------|---------|
| `RRrOjRdn` | `ts_decay_linear(zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 40)), 10)` | 2.75 | 4.63 | 4.09% | `CONCENTRATED_WEIGHT` FAIL | not checked | BLOCKED |
| `WjgZ1Evd` | `ts_decay_linear(zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 60)), 10)` | 2.68 | 4.51 | 3.30% | `CONCENTRATED_WEIGHT` FAIL | not checked | BLOCKED |
| `Gro21wWG` | `trade_when(ts_std_dev(returns, 20) > 0.02, zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), ts_std_dev(returns, 20) < 0.01)` | 2.59 | 4.33 | 6.08% | ALL PASS | PASS 0.8802 | SUBMITTABLE |
| `pw72Yqeq` | `ts_decay_linear(zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)), 10)` | 2.57 | 4.14 | 5.52% | `CONCENTRATED_WEIGHT` FAIL | not checked | BLOCKED |
| `qMXa9XlP` | `ts_decay_linear(zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)) + rank(ts_mean(scl12_buzz, 5)), 5)` | 2.57 | 3.80 | 9.20% | ALL PASS | timed out | FOLLOW-UP |
| `pw72YJ8v` | `ts_decay_linear(zscore(ts_mean(implied_volatility_call_180 - implied_volatility_put_180, 60)), 10)` | 2.35 | 3.56 | 2.64% | ALL PASS | timed out | FOLLOW-UP |
| `LLRvV6V1` | `ts_decay_linear(zscore(ts_mean(implied_volatility_call_180 - implied_volatility_put_180, 40)), 10)` | 2.34 | 3.53 | 3.33% | ALL PASS | timed out | FOLLOW-UP |
| `mLXGw2R2` | `ts_decay_linear(zscore(ts_mean(implied_volatility_call_180 - implied_volatility_put_180, 22)), 10)` | 2.10 | 2.96 | 4.57% | ALL PASS | timed out / rate limited | FOLLOW-UP |
| `qMXa90ev` | `ts_decay_linear(zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22)) + rank(historical_volatility_180), 5)` | 1.83 | 2.69 | 5.80% | `CONCENTRATED_WEIGHT` FAIL | not checked | BLOCKED |
| `O09LQAKv` | `ts_decay_linear(zscore(ts_mean(implied_volatility_call_180 - implied_volatility_put_180, 22)) + rank(historical_volatility_180), 5)` | 1.58 | 2.13 | 5.15% | `CONCENTRATED_WEIGHT` FAIL | not checked | BLOCKED |

## Final Candidate

`Gro21wWG` passed all required checks and was recorded for manual review:

- BRAIN URL: https://platform.worldquantbrain.com/alpha/Gro21wWG
- Grade: SPECTACULAR
- Sharpe: 2.59
- Fitness: 4.33
- Turnover: 6.08%
- Self-correlation: PASS at 0.8802 via Sharpe-premium escape.

## Notes

The full `/correlations/self` peer breakdown timed out for `Gro21wWG`, but the
`/check` endpoint returned the authoritative self-correlation PASS verdict.
