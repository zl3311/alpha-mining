---
id: "20260629-001-results"
session: "20260629-001"
total_expressions: 25
gate_passers: 17
best_sharpe: 2.49
best_fitness: 2.63
best_alpha_id: "9qwMj8kd"
---

# Results: Session 20260629-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 25 |
| Gate-passers (S>=1.25, F>=1.0) | 17 |
| Failed expressions | 2 |
| SPECTACULAR | 1 |
| EXCELLENT | 5 |
| GOOD | 6 |
| AVERAGE | 5 |
| Best Sharpe | 2.49 (9qwMj8kd) |
| Best Fitness | 2.63 (9qwMj8kd) |
| Submittable (all checks PASS) | 1 (JjpzQAze) |

## Gate-Passers

| # | Alpha ID | Expression (truncated) | S | F | T% | Template Family | BRAIN | Self-Corr | Verdict |
|---|----------|----------------------|-----|------|------|-----------------|-------|-----------|---------|
| 1 | 9qwMj8kd | rank(drlt/close/ts_std_dev(ret,20))+... | 2.49 | 2.63 | 13.7 | vol-adjusted value | ALL PASS | 0.759 FAIL | BLOCKED |
| 2 | npgqPYKq | rank(dlto/close)*rank(dlto/close)+... | 2.14 | 2.41 | 12.7 | rank-squared convex | ALL PASS | 0.798 FAIL | BLOCKED |
| 3 | zq9G81pG | rank(acdo/close)*rank(open/close-1)*... | 2.28 | 2.10 | 18.0 | 3-way product | ALL PASS | 0.822 FAIL | BLOCKED |
| 4 | JjpzQAze | rank(ivaco/close)*rank(open/close-1)*... | 2.30 | 2.05 | 11.7 | 3-way product | ALL PASS | 0.681 PASS | **SAFE** |
| 5 | rKoGeARo | rank(acdo/close)*rank(bvps_flag)+... | 2.47 | 2.04 | 28.5 | 2-way product | ALL PASS | 0.782 FAIL | BLOCKED |
| 6 | 88zJPP5V | rank(drlt/close)*rank(open/close-1)+... | 2.05 | 2.15 | 9.9 | product + additive | f=1 (SUB_UNIV) | — | BLOCKED |
| 7 | O0pzN3r1 | rank(ts_delta(acdo,5)-ts_delta(acdo,22))+... | 2.24 | 2.00 | 19.1 | multi-horizon spread | — | — | GOOD |
| 8 | kq3GgNzg | rank(txdbca/close)+rank(open/close-1)+... | 2.23 | 1.98 | 19.6 | additive (txdbca) | — | — | GOOD |
| 9 | pw6G5vW3 | rank(abs(ts_delta(acdo,5)))*rank(bvps)+... | 2.40 | 1.95 | 28.5 | event-magnitude product | — | — | GOOD |
| 10 | ZYpzAoVY | rank(ts_rank(acdo,22))*rank(bvps)+... | 2.36 | 1.90 | 28.7 | ts_rank product | — | — | GOOD |
| 11 | omKGLVgm | rank(fate/close)*rank(bvps)*rank(o/c-1) | 1.71 | 1.88 | 14.6 | 3-way product | — | — | GOOD |
| 12 | QPazKpvX | rank(ts_mean(fate,5)-ts_mean(fate,22))+... | 1.77 | 1.61 | 18.1 | MA crossover | — | — | GOOD |

## BRAIN Check Results (top 6)

| Alpha ID | LOW_SHARPE | LOW_FITNESS | LOW_TURNOVER | HIGH_TURNOVER | CONCENTRATED_WEIGHT | LOW_SUB_UNIVERSE_SHARPE | SELF_CORRELATION | MATCHES_COMPETITION |
|----------|------------|-------------|--------------|---------------|---------------------|-------------------------|------------------|---------------------|
| 9qwMj8kd | PASS | PASS | PASS | PASS | PASS | PASS | FAIL (0.759) | PASS |
| npgqPYKq | PASS | PASS | PASS | PASS | PASS | PASS | FAIL (0.798) | PASS |
| zq9G81pG | PASS | PASS | PASS | PASS | PASS | PASS | FAIL (0.822) | PASS |
| JjpzQAze | PASS | PASS | PASS | PASS | PASS | PASS | PASS (0.681) | PASS |
| rKoGeARo | PASS | PASS | PASS | PASS | PASS | PASS | FAIL (0.782) | PASS |
| 88zJPP5V | PASS | PASS | PASS | PASS | PASS | FAIL (0.81<0.89) | PENDING | PASS |
