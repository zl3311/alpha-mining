---
id: "20260629-001-learnings"
session: "20260629-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260629-001

## What Worked

- **3-way product interactions with fnd6_ivaco** produced EXCELLENT S=2.30 F=2.05
  with self-corr 0.68 (auto-PASS). The multiplicative template
  `rank(A) * rank(B) * rank(C)` is structurally novel vs the additive
  `rank(A) + rank(B) + rank(C)` that dominates the book.
- **Volatility-adjusted value** `rank(F / close / ts_std_dev(returns, 20))`
  produced SPECTACULAR S=2.49 F=2.63. The template is valid but needs
  self-corr reduction (MARKET neut or different field pairing).
- **Rank-squared convex weighting** `rank(F) * rank(F)` with dlto reached
  EXCELLENT S=2.14 F=2.41. The convex template works but shares too much
  correlation with existing guidance-fundamental entries.
- 68% gate-pass rate (17/25) across all novel templates — far above the
  typical 30-40% for EXPLORE sessions. Product interactions are a rich
  structural family.

## What Didn't Work

- **MA crossover on fundamentals** (`ts_mean(F,5) - ts_mean(F,22)`) peaked at
  GOOD grade (S=1.77 F=1.61). Fundamental fields update too slowly (quarterly)
  for short vs long MA to generate meaningful signal differentiation.
- **Signal-to-noise ratio** (`ts_delta(F,5) / ts_std_dev(F,22)`) reached only
  AVERAGE F=1.11. Division by volatility destabilizes the signal when ts_std_dev
  approaches zero on stable fundamentals.
- **Group z-score** (`group_zscore(F, subindustry)`) reached only AVERAGE F=1.45.
  Industry-relative normalization doesn't add enough vs simple rank().
- **fnd6_acdo and fnd6_dlto product interactions** all failed self-corr (0.78-0.82)
  due to high correlation with LLR0n261. These fundamental6 fields share too much
  signal with the accrual_intraday_analyst_revision family.
- **Trade_when regime gates** — both candidates produced 0 results (failed),
  likely due to FASTEXPR syntax issues or sparse condition coverage.

## New Patterns

- **Product interaction blend** (`rank(A) * rank(B) * rank(C)`) — promoted to
  `data/knowledge/patterns/product-interaction-blend.md`. Key finding: ivaco
  decorrelates well; acdo/dlto/drlt do not. See pattern file for template.

## Mechanism Insights

- fnd6_ivaco (investment in associated companies) captures cross-entity capital
  allocation decisions that are orthogonal to the accrual/depreciation themes
  dominating the book. Companies with high ivaco/close invest heavily in
  subsidiaries — a signal of management confidence and growth strategy that
  doesn't share the same PnL dynamics as intraday reversal or analyst revision.
- LLR0n261 is the primary correlation gatekeeper for any alpha using
  `open/close - 1` (intraday) + `anl4_bvps_flag` components. Future novel
  templates should consider alternative stabilizers to escape this peer.
