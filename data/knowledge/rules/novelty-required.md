---
category: "rule"
severity: "high"
updated: "2026-06-05"
---

# Structural Novelty Requirement

Cloud agent sessions MUST produce structurally novel expressions. The book is
near saturation with known pattern families; incremental variants of proven
templates have diminishing returns.

## Definition of "structurally novel"

An expression is structurally novel if its **operator tree shape** differs from
all expressions in `data/factors/` and `data/knowledge/patterns/`. Specifically:

**NOT novel (same tree shape, different leaves):**
- Changing the field: `zscore(ts_mean(X, 22))` → `zscore(ts_mean(Y, 22))`
- Changing the window: `ts_mean(X, 22)` → `ts_mean(X, 10)`
- Changing the decay: decay=5 → decay=10
- Changing neutralization: MARKET → SUBINDUSTRY

**Novel (different tree shape):**
- Adding conditional logic: `trade_when(cond, signal, exit)`
- Using inter-field ratios: `rank(F1 / F2)`
- Multi-horizon spreads: `ts_delta(F, 5) - ts_delta(F, 22)`
- Directional gating: `rank(F) * sign(ts_delta(G, d))`
- Dynamic correlation: `rank(ts_corr(F, returns, d))`
- Non-linear transforms: `rank(F) * rank(F)`, `rank(abs(...))`
- Cross-family interactions not yet in the factor catalog

## Budget allocation rule

At least **50% of each session's simulation budget** must be spent on
structurally novel templates. The remaining budget may be used for
refinement of promising novel discoveries within the same session.

## Known saturated patterns (do not repeat)

These template families are well-explored and have multiple entries in the book:

- `rank(field / close)` — fundamental value
- `zscore(ts_mean(IV_spread, d))` — options smoothing
- `rank(field / close) + zscore(ts_mean(IV_spread, d))` — IV-fundamental hybrid
- `rank(anl4_*_flag)` — analyst revision flags
- `ts_decay_linear(rank(field), d)` — smoothed rank

The agent should NOT generate more than 2-3 expressions from these families
per session unless combining them in a genuinely novel structure.
