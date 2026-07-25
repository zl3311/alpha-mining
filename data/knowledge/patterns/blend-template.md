---
category: "pattern"
---

# Multi-Factor Blend Template

```
rank(factor_A) + rank(factor_B) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns))
```

Wrap with `ts_decay_linear(..., 5)` for fitness boost (F=1.91->2.86).
Weight heavier on low-turnover factors (`ptp*2`, `ptp*3`).
Decay values: 5 (default), 6, 8, 10.
