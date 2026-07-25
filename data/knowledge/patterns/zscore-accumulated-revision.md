---
category: "pattern"
discovered: "20260608-001"
applicable_to: "analyst4, sparse_flags"
---

# zscore + ts_sum Accumulated Revision Template

Critical normalization finding for sparse, event-driven analyst revision flags.

## Template

```
ts_decay_linear(zscore(ts_sum(anl4_*_flag, D)), W)
```

| Parameter | Recommended | Notes |
|-----------|-------------|-------|
| D (ts_sum window) | 22 | 10 → lower Sharpe; 44 → lower fitness |
| W (decay_linear) | 3-5 | 3 is marginally best; 10 also works |
| Platform decay | 6 | decay=10 FAILS self-corr (0.713 vs 0.593) |
| Neutralization | SUBINDUSTRY | MARKET boosts some flags (epsr AVERAGE→GOOD) |
| Universe | TOP3000 | |

## Why zscore, not rank

For sparse analyst revision flags (anl4_*_flag), the distribution is heavily
zero-dominated with discrete events. `rank()` compresses all zero-valued stocks
to the same rank, producing wrong-sign signals at TOP3000. `zscore()` normalizes
by standard deviation, better capturing the deviation of revised stocks from the
zero-dominated cross-sectional mean.

| Field | rank() Sharpe | zscore() Sharpe | Delta |
|-------|-------------|---------------|-------|
| anl4_netprofit_flag | -0.72 | +1.71 | **+2.43** |
| anl4_epsr_flag | -0.61 | +1.30 | **+1.91** |
| anl4_capex_flag | +1.28 | +1.39 | +0.11 |
| anl4_fcf_flag | +1.12 | +1.15 | +0.03 |

## Best Results

- anl4_netprofit_flag: EXCELLENT S=1.72 F=2.21, self-corr 0.593 (vRmlGnkv)
- anl4_epsr_flag: AVERAGE S=1.31, self-corr similar expected
- anl4_capex_flag: AVERAGE S=1.39
- anl4_fcf_flag: INFERIOR S=1.15

## When to Use

- Testing ANY analyst4 flag field (anl4_*_flag)
- The flag is sparse/event-driven (most values near zero)
- Previous testing with `rank()` showed INFERIOR/negative results

## When NOT to Use

- Fields with continuous distributions (fundamentals, price-volume)
- Fields where `rank()` already produces strong signals
