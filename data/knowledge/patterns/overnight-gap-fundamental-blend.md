---
category: "pattern"
discovered: "20260625-002"
applicable_to: "fundamental6, analyst4, non-IV blends"
best_alpha_id: "3q7lm2p6"
best_sharpe: 2.95
best_fitness: 3.44
---

# Overnight Gap + Fundamental + Analyst Blend

## Template

```
ts_decay_linear(rank(F1 / close) + rank(open / close - 1) + rank(analyst_flag) + rank(F2 / close), 5)
```

Use SUBINDUSTRY neutralization and platform decay 6.

## When to Use

Use this template when:
- The self-corr wall blocks IV-based expressions (all IV60/90/270 paths saturated)
- You need SPECTACULAR grade without any options data
- You want guaranteed low self-corr (< 0.7) against IV-dominated book

## Field Selection

Best performing combinations (sorted by Sharpe):
1. F1=fnd6_acdo, analyst=anl4_ptpr_flag, F2=fnd6_itci → S=3.02
2. F1=fnd6_acdo, analyst=anl4_netdebt_flag, F2=fnd6_itci → S=2.95
3. F1=fnd6_acdo, analyst=anl4_bvps_flag, F2=fnd6_itci → S=2.53 (fails SUB_UNIVERSE)

The `anl4_ptpr_flag` (pre-tax profit revision) is the strongest analyst complement.
Avoid `anl4_bvps_flag` — it fails LOW_SUB_UNIVERSE_SHARPE with this template.

## Key Constraints

- Turnover is 13-15% (moderate-high) due to the daily `open/close` component
- Requires fundamental6 fields with reasonable coverage (>50% of TOP3000)
- The `open/close - 1` leg is essential — removing it drops Sharpe from 3.0 to ~2.0

## Anti-Patterns

- Do NOT use MARKET neutralization with this template (drops S from 3.0 to ~2.2)
- Do NOT combine with IV60 (creates self-corr > 0.7 against IV60 book entries)
- The `bvps_flag` variant fails SUB_UNIVERSE check — use ptpr_flag or netdebt_flag
- Mutual correlation between analyst-flag variants is very high (~0.85-0.95); only
  ONE variant from this template is submittable at a time. After submitting one,
  other variants will be blocked by self-correlation.
