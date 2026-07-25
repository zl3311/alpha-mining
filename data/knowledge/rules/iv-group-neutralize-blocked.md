---
category: "rule"
severity: "high"
discovered: "20260604-001"
---

# group_neutralize(IV spread) is Structurally Blocked

`ts_decay_linear(group_neutralize(implied_volatility_call_270 - implied_volatility_put_270, <group>), d)`
reaches EXCELLENT metrics (S~2.0-2.2, F~2.1-2.5) but ALWAYS fails BRAIN
`CONCENTRATED_WEIGHT` AND `LOW_SUB_UNIVERSE_SHARPE` across every variant tested
(subindustry/industry/market groups, decay 5-15, scale/rank/zscore wrappers,
buzz multiplier). This is a structural block, not a tuning problem — do not keep
mutating this family.

## Fix: use the zscore + ts_mean template instead

```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)), 10)
```

MARKET neut, decay=10. This passes all 8 checks at EXCELLENT (vRm07LP3:
S=1.82, F=2.35, self-corr 0.309). See pattern
`data/knowledge/patterns/iv-spread-zscore-tsmean.md`.

## Related

- Adding `+ rank(buzz)` to a `group_neutralize(...)` output is a UNIT ERROR
  (BRAIN status WARNING). Use a multiplier `* (1 + rank(buzz))` instead.
- Stop condition: 3+ variants with the same BRAIN check failure → pivot family.
