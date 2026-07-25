---
category: "rule"
severity: "high"
supersedes: "original claim that rank(-1*F) = -Sharpe(rank(F))"
discovered: "20260705 (negation sweep: 11,645 sims across 1,294 fields)"
---

# Negation Is NOT Symmetric Under Neutralization

## The rule

`rank(-1 * F)` does NOT always produce `Sharpe = -1 * Sharpe(rank(F))`.
Under SUBINDUSTRY neutralization + 8% truncation, the long and short sides
experience different effective exposures. Always test both directions explicitly.

## Evidence (negation sweep, 2026-07-05)

| Field | `rank(F)` Sharpe | `rank(-1 * F)` Sharpe | Ratio |
|-------|------------------|-----------------------|-------|
| fnd6_intc | 0.83 | 1.32 | 1.59x better negated |
| fnd6_txw | 0.45 | 0.89 | 1.98x better negated |
| fnd6_txdbca | 0.52 | 1.06 | 2.04x better negated |
| fnd6_acqgdwl | 0.62 | 1.17 | 1.89x better negated |
| pv13_custretsig_retsig | -1.90 | 1.90 | symmetric (high turnover) |

17 fields are significantly better negated (direction gap > 0.3).

## Why negation is asymmetric

1. **SUBINDUSTRY neutralization** removes the subindustry mean from both sides,
   but the long-tail distribution of fundamentals is skewed — a few stocks with
   very high values dominate the top rank, while the bottom rank is more evenly
   distributed.
2. **Truncation (8%)** clips extreme positions asymmetrically when the underlying
   field distribution is skewed.
3. The net effect: the "short expensive" side often produces a cleaner signal than
   the "long cheap" side for fields with right-skewed distributions (most
   fundamental balance sheet items).

## Implication for mining

- Do NOT assume negated Sharpe from positive direction. Test explicitly.
- The negation sweep (tag `negation-sweep-v1`) has real PnL for both directions
  across 1,634 fields — use `data/knowledge/factor_profiles/` which includes
  `negated_best_sharpe` and `direction_gap` in frontmatter.
- For blend design, consider that a field's negated version may be a stronger
  building block than its positive version.
