---
pattern: "direction-diversification"
discovered: "20260705 (full-corpus PnL spectral analysis, 31k alphas)"
applicable_to: "book construction, EXPLORE/RECOMBINE strategy, portfolio diversification"
confidence: "high (PCA on 1,645 fields with 1,234 daily observations)"
---

# Pattern: Negation Direction Adds 5x Independent Signal Dimensions

## The finding

PCA eigenvalue decomposition on 1,645 field-level daily PnL return series shows:

| Metric | Positive-only (Jun 2026) | With negation (Jul 2026) |
|--------|--------------------------|--------------------------|
| PCs for 50% variance | 7 | **34** |
| PCs for 75% variance | 95 | **162** |
| PCs for 90% variance | 253 | **353** |
| PC1 explained | 31.7% | **21.1%** |
| Correlated pairs (>0.5) | 197,224 | **73,901** |
| Singleton fields | 332 | **516** |

The factor space has **5x more independent dimensions** when negation direction
is included. This means the book can be diversified far beyond what
positive-direction-only analysis suggests.

## Mechanism

Negation creates temporal diversification because:
1. The PnL of `rank(-1 * F)` is NOT simply `-1 * PnL(rank(F))` (see rule:
   `no-negated-duplicates.md` and pattern: `negation-asymmetry-fundamentals.md`). The neutralization-induced asymmetry creates genuinely
   different return patterns.
2. Fields where positive and negated directions are both strong but temporally
   decorrelated provide "self-blending" opportunities.
3. The dominant PC1 cluster (fundamental value + analyst revision, 918 fields)
   shrinks in weight because negated variants pull orthogonal directions.

## Implication for book construction

- **Untapped diversification**: 516 fields are singletons (not correlated >0.5 with
  anything). These represent independent signal sources for the book.
- **Self-corr escape**: A field's negated version often has LOW correlation with
  book alphas that use the positive version. This provides a self-corr escape route.
- **Set-cover result**: 10 optimally selected factors combine to S=6.08 (65% positive
  days). The greedy algorithm naturally picks a mix of positive and negated fields.

## How to exploit

1. When self-corr is blocking a field's positive version, try the negated version
2. For EXPLORE mode, prioritize the 516 singleton fields as seeds
3. For RECOMBINE mode, blend a field's positive and negated versions from different
   clusters (they're independent by construction)
