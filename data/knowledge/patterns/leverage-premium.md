---
category: "pattern"
discovered: "20260609"
---

# Leverage Premium: rank(-1 * equity / assets)

Financial leverage (low equity/assets ratio = high debt) produces S=1.55
standalone, boosted to S=1.87-2.37 when combined with fundamental quality fields.

## Template

```
rank(-1 * equity / assets) + rank(QUALITY_FIELD / close)
```

Best quality fields: fnd6_itci (S=2.37, fails SUB_UNIVERSE), fnd6_drlt (S=1.87,
ALL PASS), fnd6_ivaco, fnd6_acdo, fnd6_fatl, fnd6_dlto.

Wrap with `ts_decay_linear(..., 5)` for marginal fitness improvement.

## Critical constraints

- **SUBINDUSTRY neut only** — MARKET neut kills the signal (S drops from 1.55 to 0.72)
- **itci combination is permanently blocked** by LOW_SUB_UNIVERSE_SHARPE
- **zscore(-1*equity/assets)** fixes itci sub-universe issue but lower S (1.72 vs 2.37)
- After submitting ONE leverage alpha, all others will be blocked by mutual self-corr
