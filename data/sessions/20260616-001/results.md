---
id: "20260616-001-results"
session: "20260616-001"
total_expressions: 58
gate_passers: 31
best_sharpe: 2.21
best_fitness: 2.73
best_alpha_id: "GrwrVP5G"
---

# Results: Session 20260616-001

## Summary Metrics

| Metric | Value |
|--------|-------|
| Expressions tested | 58 |
| Gate-passers (S>=1.25, F>=1.0, turnover 1%-70%) | 31 |
| Best Sharpe | 2.21 (`j2Z2QV8e`) |
| Best Fitness | 2.73 (`j2Z2QV8e`) |
| Submittable candidates | 2 (`YPpjReEW`, `GrwrVP5G`) |
| Budget used | 58 |

## Gate-Passers

| # | Alpha ID | Expression | Sharpe | Fitness | Turnover | Family | Verdict |
|---|----------|------------|--------|---------|----------|--------|---------|
| 1 | YPpjReEW | `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) * rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.01)` | 1.74 | 1.09 | 18.38% | options_news_volatility_regime | QUEUED |
| 2 | RRpJgbVn | `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.01)` | 1.70 | 1.03 | 19.32% | options_news_volatility_regime | BLOCKED_LOW_SUB_UNIVERSE |
| 3 | akdr52L9 | `trade_when(ts_std_dev(returns, 30) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 30) < 0.01)` | 1.66 | 1.00 | 19.07% | options_news_volatility_regime | BLOCKED_LOW_SUB_UNIVERSE |

## Continuation Gate-Passers

| Alpha ID | Expression Summary | Grade | Sharpe | Fitness | Turnover | Local Self-Corr | Verdict |
|----------|--------------------|-------|--------|---------|----------|-----------------|---------|
| GrwrVP5G | MARKET event + leverage × `fatl` product | EXCELLENT | 2.04 | 2.29 | 2.89% | 0.517 | QUEUED_RISKY |
| j2Z2QV8e | MARKET event + leverage + netdebt flag | SPECTACULAR | 2.21 | 2.73 | 2.90% | 0.712 | BLOCKED_LOCAL |
| YPpPXl6q | MARKET event × intraday + `fatl` | SPECTACULAR | 2.05 | 2.58 | 7.91% | 0.641 | BLOCKED_LOCAL |
| 1Y7Y5W5J | MARKET event + leverage + intraday | SPECTACULAR | 2.20 | 2.66 | 12.71% | 0.673 | BLOCKED_LOCAL |
| WjpjkEzx | MARKET event + `fatl` + intraday | SPECTACULAR | 2.07 | 2.72 | 11.34% | 0.673 | BLOCKED_LOCAL |

## All Expressions Tested

| # | Alpha ID | Expression Summary | Sharpe | Fitness | Turnover | Status |
|---|----------|--------------------|--------|---------|----------|--------|
| 1 | rKo1qVbj | additive raw news blend | 1.94 | 0.53 | 129.48% | BELOW_GATE_HIGH_TURNOVER |
| 2 | 0m7bVZlr | 1080 skew + smoothed news | 1.30 | 0.62 | 24.46% | BELOW_GATE |
| 3 | 1Y7qMkG6 | 720 skew + smoothed news | 1.31 | 0.62 | 24.39% | BELOW_GATE |
| 4 | pw6q227b | 360 skew/news product | 1.53 | 0.80 | 21.88% | BELOW_GATE |
| 5 | QPa18Xng | 1080 skew/news product | 1.23 | 0.57 | 23.31% | BELOW_GATE |
| 6 | npg1EM6q | rank-ratio skew/news | 0.71 | 0.27 | 37.44% | BELOW_GATE |
| 7 | 9qwznRKd | multi-horizon skew + smoothed news | 0.42 | 0.15 | 17.62% | BELOW_GATE |
| 8 | wpR8renY | skew + news acceleration | 0.92 | 0.33 | 38.09% | BELOW_GATE |
| 9 | WjpE5aKZ | dynamic skew/news correlation | -0.50 | -0.12 | 18.25% | BELOW_GATE |
| 10 | RRpJgbVn | volatility-gated additive blend | 1.70 | 1.03 | 19.32% | GATE_PASS_BLOCKED |
| 11 | leVLmKA7 | drawdown-gated additive blend | 1.55 | 0.49 | 86.53% | BELOW_GATE_HIGH_TURNOVER |
| 12 | VkpvWzlw | skew/news + `fnd6_cshtr` | 1.19 | 0.69 | 17.51% | BELOW_GATE |
| 13 | omK1xpWl | broader 20d vol gate 0.015 | 1.69 | 0.96 | 21.35% | BELOW_GATE |
| 14 | omK1xvvv | broader 20d vol gate 0.018 | 1.64 | 0.93 | 20.32% | BELOW_GATE |
| 15 | leVLo7bO | 30d vol gate 0.018 | 1.65 | 0.96 | 19.88% | BELOW_GATE |
| 16 | akdr52L9 | 30d vol gate 0.020 | 1.66 | 1.00 | 19.07% | GATE_PASS_BLOCKED |
| 17 | 1Y7qrwj6 | 44d smoothed news | 1.62 | 0.99 | 18.59% | BELOW_GATE |
| 18 | 2r713AMZ | add `scl12_buzz` stabilizer | 0.87 | 0.40 | 19.06% | BELOW_GATE |
| 19 | pw6q9vXq | add `fnd6_cshtr` stabilizer | 1.24 | 0.84 | 14.08% | BELOW_GATE |
| 20 | null | 1080 skew volatility gate | null | null | null | FAILED |
| 21 | leVLow6e | 720 skew volatility gate | 1.41 | 0.80 | 19.96% | BELOW_GATE |
| 22 | YPpjReEW | volatility-gated skew/news product | 1.74 | 1.09 | 18.38% | QUEUED |

## BRAIN Check Results

| Alpha ID | Computable Checks | Self-Correlation | Verdict |
|----------|-------------------|------------------|---------|
| YPpjReEW | ALL PASS | PASS, 0.4613 | QUEUED |
| GrwrVP5G | ALL PASS | local PnL 0.517; BRAIN endpoint pending | QUEUED_RISKY |
| RRpJgbVn | `LOW_SUB_UNIVERSE_SHARPE` FAIL 0.71 vs 0.74 | not checked | BLOCKED |
| akdr52L9 | `LOW_SUB_UNIVERSE_SHARPE` FAIL 0.66 vs 0.72 | not checked | BLOCKED |
