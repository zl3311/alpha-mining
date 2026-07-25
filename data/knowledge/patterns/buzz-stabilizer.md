---
category: "pattern"
---

# Buzz Stabilizer

Expression: `rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`

100% coverage. Fixes SUB_UNIVERSE_SHARPE check.
`ts_mean(5)` balances turnover vs Sharpe.
