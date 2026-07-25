---
category: "rule"
severity: "critical"
updated: "20260705"
---

# Submitted Book Saturation

The submitted book spans 47+ mechanism families (run
`uv run python3 scripts/parse_frontmatter.py --dir data/book --field status,grade,family`
for live counts). Self-corr check uses a **0.7 correlation threshold** with a
**1.10x Sharpe premium escape** (see `self-corr-threshold` rule).

**Positive-direction** field exploration is effectively complete — all high-value
clusters in fundamental6, analyst4, options, sentiment, and guidance datasets have
been mined. However, **negation direction** opens significant new territory
(see pattern: `direction-diversification.md`): 516 singleton fields, 34 independent
PCA dimensions vs 7 for positive-only.

EXCELLENT + decorrelated is still difficult with existing positive-direction fields.

Realistic paths forward:

1. **Negated-direction building blocks** — 17 fundamental fields are significantly
   stronger negated (see pattern: `negation-asymmetry-fundamentals.md`). These are
   decorrelated from the positive-direction book.
2. **High-Sharpe variants within correlated families** — if candidate Sharpe
   exceeds 1.10x the max correlated peer, self-corr check passes even at
   corr > 0.7
3. **Cross-cluster combinations** — novel ratios/interactions between
   known-good fields, including positive x negated blends
4. **Tier/capability upgrade** — multi-region, PYTHON expressions, consultant
   datasets (not available on free tier)
