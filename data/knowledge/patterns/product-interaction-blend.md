---
pattern: "product-interaction-blend"
discovered: "20260629-001"
applicable_to: "fundamental6 + analyst4 + intraday blends"
confidence: "high"
best_alpha_id: "JjpzQAze"
best_sharpe: 2.30
best_fitness: 2.05
---

# Pattern: Product Interaction Blend (Multiplicative)

## Template

```
ts_decay_linear(rank(F / close) * rank(open / close - 1) * rank(anl4_FLAG), 5)
```

Use SUBINDUSTRY neutralization and platform decay 6.

## When to Use

Use when additive blends (`rank(A) + rank(B) + rank(C)`) are saturated or
produce high self-corr. Product interactions create a fundamentally different
position profile because they require ALL factors to agree — stocks must rank
high on every dimension simultaneously.

## Key Findings

| Field (F) | Sharpe | Fitness | Self-Corr | Status |
|-----------|--------|---------|-----------|--------|
| fnd6_ivaco | 2.30 | 2.05 | 0.681 | **SUBMITTABLE** |
| fnd6_acdo | 2.28 | 2.10 | 0.822 | BLOCKED (LLR0n261) |
| fnd6_fate | 1.71 | 1.88 | — | GOOD grade |
| fnd6_drlt | 2.05 | 2.15 | — | FAIL SUB_UNIVERSE |

## Self-Corr Decorrelation

The product template produces ~0.05-0.15 LOWER self-corr than additive blends
using the same fields. Reason: multiplicative interaction creates sparser,
more selective positions that share less PnL overlap with dense additive blends.

fnd6_ivaco specifically decorrelates well because investment-in-associates
captures a different economic dimension (conglomerate capital allocation) than
the accrual/depreciation/debt themes dominating the book.

## Caution

- Product of 3 ranks concentrates signal in a smaller stock set; check
  CONCENTRATED_WEIGHT if using sparse fields.
- 2-way products (`rank(A) * rank(B) + rank(C)`) can reach higher Sharpe but
  trade off self-corr advantage. Prefer pure 3-way products for decorrelation.
