---
id: "20260617-001-learnings"
session: "20260617-001"
category: "dead_end"
confidence: "medium"
actionable: true
---

# Learnings: Session 20260617-001

## What Worked

- The best relative result came from a product of options skew and R&D revision:
  `ts_decay_linear(rank(implied_volatility_mean_skew_180) * rank(anl4_rd_exp_flag), 5)`
  reached S=1.19 and F=0.67.
- Product structure outperformed additive and volatility-gated forms for the
  options-skew/R&D connector, suggesting confirmation logic is better than regime
  gating for this specific pair.

## What Didn't Work

- No expression reached aggregate gates. Best fitness was only 0.67, well below
  the 1.0 threshold.
- Volatility gates degraded the R&D-tax and R&D-debt connectors instead of
  repairing the weak standalone profile.
- Option9/deferred-tax wrappers remained too weak and too turnover-heavy:
  pcr/deferred-tax product reached only S=0.74, F=0.28, turnover 31.55%.
- Dynamic correlation between option flow and deferred-tax exposure inverted:
  S=-0.53, F=-0.41.
- The model16/options connector stayed weak, consistent with the existing
  model16 dead-zone rule.

## New Rules Discovered

None. This is not broad enough for a hard rule, but it is enough to avoid
retesting this exact connector branch without a new mechanism.

## New Dead Zones

Narrow dead-end candidate: R&D-tax / option9-deferred-tax connector wrappers
using simple additive, product, volatility-gated, or dynamic-correlation forms.

## Mechanism Insights

The factor-merge screen's negative correlations did not translate into live
BRAIN alphas for this connector branch. These fields diversify statistically, but
their standalone signal is too weak, so wrappers mostly combine weak legs rather
than unlock a new mechanism.

