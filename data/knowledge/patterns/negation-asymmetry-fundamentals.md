---
pattern: "negation-asymmetry-fundamentals"
discovered: "20260705 (negation sweep v1+v2, 4,900 sims)"
applicable_to: "fundamental6, fundamental2, analyst4 single-factor building blocks"
confidence: "high (verified across 1,634 fields)"
---

# Pattern: Fundamental Fields Are Often Stronger Negated

## The finding

17 fields have Sharpe significantly higher in the negated direction (`rank(-1 * F)`)
than positive (`rank(F)`), with direction gap > 0.3. All are fundamental balance
sheet or analyst guidance fields.

## Top negated building blocks (GOOD+ grade, F >= 1.0)

| Field | Negated Expr | S | F | T% | Mechanism |
|-------|-------------|---|---|----|-----------|
| fnd6_txw | `rank(-1 * fnd6_txw)` | 0.89 | 1.66 | 5.9% | Low tax expense = undervalued |
| fnd6_txdbca | `rank(-1 * fnd6_txdbca)` | 1.06 | 1.63 | 6.1% | Low deferred tax = cash quality |
| fnd6_acqgdwl | `rank(-1 * ts_delta(fnd6_acqgdwl, 5))` | 1.17 | 1.54 | 14.7% | Declining goodwill = disciplined M&A |
| fnd6_intc | `rank(-1 * fnd6_intc / close)` | 1.32 | 1.47 | 3.5% | Low capitalized interest = low capex burden |
| fnd6_dcvsub | `rank(-1 * ts_delta(fnd6_dcvsub, 5))` | 1.16 | 1.41 | 9.6% | Declining convertible subs |

## Economic mechanism

Fundamental fields (balance sheet items) have right-skewed distributions: a few
companies have very large values (mega-cap debt, massive goodwill), while most
have moderate values. Under SUBINDUSTRY neutralization:

- **Positive rank** (`rank(F)`): longs the few extreme outliers within each
  subindustry. Signal is noisy because outliers are idiosyncratic.
- **Negated rank** (`rank(-1 * F)`): shorts the outliers, longs the "normal"
  companies. Signal is cleaner because the majority cluster is more predictable.

The asymmetry is strongest for:
- Balance sheet stock items (not flow): tax, debt, goodwill, inventory
- Fields with high cross-sectional skewness
- Low-turnover templates (rank_level, rank_value_norm)

## When to use

- Building single-factor components for multi-factor blends
- When a positive-direction fundamental has S < 1.0 but the field seems economically
  meaningful — try the negated version
- Factor profiles now include `negated_best_sharpe` and `direction_gap` in frontmatter
  for quick lookup

## When NOT to use

- High-turnover fields (pv13, news): negation is symmetric (T > 30%)
- Fields where positive S is already strong (> 1.5): negation won't help
- Submission-ready alphas: negated single-factor still needs blending for fitness
