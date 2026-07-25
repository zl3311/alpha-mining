---
category: "pattern"
discovered: "20260604-001"
applicable_to: "options_iv_spread, option8"
---

# IV Spread zscore + ts_mean Template

Submittable template for call-put IV spread (H-006). Passes CONCENTRATED_WEIGHT where `group_neutralize` fails.

## Template

```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, D)), W)
```

| Parameter | Recommended | Notes |
|-----------|-------------|-------|
| D (ts_mean window) | 22 | d=5 → GOOD; d=22 → EXCELLENT |
| W (decay_linear) | 10 | Outer wrap window |
| Platform decay | 10 | HF/BRAIN sim setting |
| Neutralization | MARKET | Required for low self-corr |
| Universe | TOP3000 | TOP1000 kills signal |

## When to Use

- Testing option8 IV spread fields
- Need uncorrelated signal vs fundamental book
- Avoid fundamentals in expression (blends fail CONCENTRATED_WEIGHT)

## Example (submittable)

Alpha vRm07LP3: EXCELLENT S=1.82 F=2.35, ALL PASS, self-corr 0.309.

```
ts_decay_linear(zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)), 10)
```

Settings: USA TOP3000, decay=10, MARKET neut.

## Anti-patterns

- Do NOT use `group_neutralize(IV spread, subindustry)` — EXCELLENT but blocked on CONCENTRATED_WEIGHT
- Do NOT add `+ rank(buzz)` to group_neutralize output — unit incompatibility
- Do NOT blend with fundamentals — CONCENTRATED_WEIGHT failure
