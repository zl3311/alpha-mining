---
id: "20260608-001-results"
session: "20260608-001"
total_expressions: 48
gate_passers: 20
best_sharpe: 1.72
best_fitness: 2.21
best_alpha_id: "vRmlGnkv"
---

# Results: Session 20260608-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 48 |
| Gate-passers (S>=1.25, F>=1.0) | 20 |
| Best Sharpe | 1.72 |
| Best Fitness | 2.21 |
| Budget used | 48 / unlimited (manual) |
| Hit rate | 42% |

## Gate-Passers (ranked by fitness)

| # | Alpha ID | Expression | Sharpe | Fitness | Turnover | Grade | Verdict |
|---|----------|-----------|--------|---------|----------|-------|---------|
| 1 | vRmlGnkv | `ts_decay_linear(zscore(ts_sum(anl4_netprofit_flag, 22)), 3)` | 1.72 | 2.21 | 8.1% | EXCELLENT | SUBMITTABLE |
| 2 | E5KEzxzR | `zscore(ts_sum(anl4_netprofit_flag, 22))` | 1.72 | 2.21 | 8.2% | EXCELLENT | REDUNDANT |
| 3 | GroLXj95 | `ts_decay_linear(zscore(ts_sum(anl4_netprofit_flag, 22)), 5)` | 1.71 | 2.20 | 8.0% | EXCELLENT | REDUNDANT |
| 4 | 78d1MV28 | same expr, platform decay=10 | 1.63 | 2.20 | 4.6% | EXCELLENT | BLOCKED (self-corr 0.713) |
| 5 | P013zpWL | `ts_decay_linear(zscore(ts_sum(anl4_netprofit_flag, 22)), 10)` | 1.70 | 2.18 | 7.7% | EXCELLENT | REDUNDANT |
| 6 | 2rKL6jp6 | `ts_decay_linear(zscore(ts_sum(anl4_netprofit_flag, 44)), 5)` | 1.66 | 2.05 | 5.7% | EXCELLENT | REDUNDANT |
| 7 | rKWlGMmJ | netprofit + capex zscore blend | 1.74 | 1.92 | 8.3% | GOOD | REDUNDANT |
| 8 | d5Q0z0Pj | `ts_decay_linear(zscore(ts_sum(anl4_netprofit_flag, 10)), 5)` | 1.50 | 1.87 | 10.7% | GOOD | REDUNDANT |
| 9 | QPQVzpVw | netprofit + epsr zscore blend | 1.43 | 1.56 | 8.3% | GOOD | REDUNDANT |
| 10 | zqWm2nAO | `ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)), 5)` MARKET | 1.36 | 1.51 | 5.7% | GOOD | REDUNDANT |
| 11 | 6XE9oGdK | epsr + fcf zscore blend | 1.50 | 1.47 | 8.8% | AVERAGE | REDUNDANT |
| 12 | XgKnvkKb | `ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 44)), 5)` | 1.41 | 1.37 | 6.1% | AVERAGE | REDUNDANT |
| 13 | O09ZMJQ1 | epsr + capex zscore blend | 1.41 | 1.32 | 8.4% | AVERAGE | REDUNDANT |
| 14 | 9qRr8NO9 | `ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)), 3)` | 1.31 | 1.26 | 8.9% | AVERAGE | REDUNDANT |
| 15 | LLR1mXa9 | `zscore(ts_sum(anl4_epsr_flag, 22))` | 1.31 | 1.26 | 9.0% | AVERAGE | REDUNDANT |
| 16 | rKWl7Xpj | `ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)), 5)` | 1.30 | 1.25 | 8.8% | AVERAGE | REDUNDANT |
| 17 | WjgGo6PQ | `ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)), 10)` | 1.30 | 1.25 | 8.4% | AVERAGE | REDUNDANT |
| 18 | j2g0P77Z | `ts_decay_linear(zscore(ts_sum(anl4_epsr_flag, 22)), 5)` | 1.30 | 1.25 | 8.5% | AVERAGE | REDUNDANT |
| 19 | j2g0P77Z | duplicate | 1.30 | 1.25 | 8.5% | AVERAGE | REDUNDANT |
| 20 | 6XE9ZGaK | `ts_decay_linear(zscore(ts_sum(anl4_capex_flag, 22)), 5)` | 1.39 | 1.17 | 8.6% | AVERAGE | REDUNDANT |

## BRAIN Check Results (top 7 candidates)

| Alpha ID | Grade | Sharpe | Fitness | Self-Corr | Self-Corr Result | All 7 Computable |
|----------|-------|--------|---------|-----------|------------------|-----------------|
| vRmlGnkv | EXCELLENT | 1.72 | 2.21 | 0.593 | PASS | ALL PASS |
| E5KEzxzR | EXCELLENT | 1.72 | 2.21 | 0.594 | PASS | ALL PASS |
| GroLXj95 | EXCELLENT | 1.71 | 2.20 | 0.593 | PASS | ALL PASS |
| 78d1MV28 | EXCELLENT | 1.63 | 2.20 | 0.713 | FAIL | ALL PASS |
| P013zpWL | EXCELLENT | 1.70 | 2.18 | 0.593 | PASS | ALL PASS |
| 2rKL6jp6 | EXCELLENT | 1.66 | 2.05 | 0.589 | PASS | ALL PASS |
| rKWlGMmJ | GOOD | 1.74 | 1.92 | 0.668 | PASS | ALL PASS |
