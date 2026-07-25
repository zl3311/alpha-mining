---
id: "20260719-001-results"
session: "20260719-001"
total_expressions: 0
gate_passers: 1
best_sharpe: 2.32
best_fitness: 2.07
best_alpha_id: "N1rlJ7mq"
---

# Results: Session 20260719-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| New expressions simulated | 0 |
| Existing candidates validated | 12 |
| Submittable (SAFE) | 1 (`N1rlJ7mq`) |
| Best Sharpe | 2.32 |
| Best Fitness | 2.07 |
| Budget used | 0 (unlimited) |

## Submission Candidate

| Alpha ID | Expression (abbrev) | S | F | T | Self-Corr | Verdict |
|----------|---------------------|---|---|---|-----------|---------|
| N1rlJ7mq | `ts_decay_linear(rank(abs(ts_delta(fnd6_pstkrv/close,3))) + ivaco + drlt + anl4_fcf_flag + buzz10*(-ret), 5)` | 2.32 | 2.07 | 11.1% | **PASS 0.6903** | **SAFE** |

## Validated But Blocked

| Alpha ID | Grade | S | F | Blocker |
|----------|-------|---|---|---------|
| xAd6K9Np | EXCELLENT | 1.91 | 2.02 | Already SUBMITTED on BRAIN |
| d50Jdpg2 | SPECTACULAR | 2.15 | 3.06 | Self-corr FAIL 0.849 |
| 9qrEVpMV | SPECTACULAR | 2.33 | 2.96 | Self-corr FAIL 0.939 |
| LL15dWke | SPECTACULAR | 2.68 | 2.71 | Self-corr FAIL 0.982 |
| oml0kV52 | SPECTACULAR | 2.55 | 2.55 | Self-corr FAIL 0.796 |
| WjGL7GPj | EXCELLENT | 2.06 | 2.47 | Self-corr FAIL 0.885 |
| GrLjgZrx | EXCELLENT | 2.16 | 2.21 | Self-corr FAIL 0.926 |
| oml00Kx2 | EXCELLENT | 1.98 | 2.09 | Self-corr FAIL 0.875 |
| pwKXqJEb | EXCELLENT | 2.31 | 2.08 | LOW_SUB_UNIVERSE_SHARPE FAIL |
| KP9V7YLz | EXCELLENT | 2.83 | 2.49 | Already ACTIVE |
| aknmG1M6 | EXCELLENT | 2.29 | 2.26 | Already ACTIVE |

## BRAIN Checks — N1rlJ7mq

| Check | Result | Value | Limit |
|-------|--------|-------|-------|
| LOW_SHARPE | PASS | 2.32 | 1.25 |
| LOW_FITNESS | PASS | 2.07 | 1.0 |
| LOW_TURNOVER | PASS | 0.1109 | 0.01 |
| HIGH_TURNOVER | PASS | 0.1109 | 0.7 |
| CONCENTRATED_WEIGHT | PASS | — | — |
| LOW_SUB_UNIVERSE_SHARPE | PASS | 1.87 | 1.0 |
| SELF_CORRELATION | PASS | 0.6903 | 0.7 |
| MATCHES_COMPETITION | PASS | — | — |
