---
id: "20260608-001-learnings"
session: "20260608-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260608-001

## What Worked

- **zscore normalization on sparse analyst flags**: The single most impactful
  discovery. `zscore(ts_sum(anl4_netprofit_flag, 22))` reaches EXCELLENT (S=1.72,
  F=2.21) from a field previously rated INFERIOR (S=0.72 with rank). The same
  pattern works for epsr_flag (AVERAGE) and capex_flag (AVERAGE).
- **ts_sum accumulation over 22 days**: Captures persistent revision trends.
  Both 10-day and 44-day windows also work but 22 is optimal.
- **Platform decay=6 (default)**: All EXCELLENT candidates pass self-corr at
  decay=6. Platform decay=10 causes self-corr failure (0.713 vs 0.593).
- **MARKET neutralization for epsr_flag**: Upgrades from AVERAGE to GOOD grade
  (F=1.25 → 1.51), suggesting MARKET neut may help weaker signals.

## What Didn't Work

- **rank() normalization**: Produces wrong-sign (negative Sharpe) results for
  these sparse analyst flags at TOP3000. The zero-dominated distribution causes
  rank to compress all zero-valued stocks, losing the signal.
- **Novel template structures (trade_when, ts_corr, multi-horizon, directional
  gating)**: ALL produced negative Sharpe for these fields. The simple
  zscore(ts_sum()) pattern dominates everything else.
- **Multi-flag blends with rank()**: Additive and multiplicative rank-based
  blends destroyed signal (S=-0.19 to -0.89).
- **Platform decay=10**: Causes self-corr failure due to PnL profile compression.

## New Patterns Discovered

### zscore + ts_sum Accumulated Revision (HIGH confidence)
- **Pattern**: `ts_decay_linear(zscore(ts_sum(anl4_*_flag, D)), W)`
- **Best D=22, W=3-5, platform decay=6, SUBINDUSTRY neut**
- Promoted to: `data/knowledge/patterns/zscore-accumulated-revision.md`
- Applicable to all sparse, event-driven analyst4 flags

## New Rules Discovered

### rank() fails on sparse analyst flags (HIGH confidence)
- `rank(ts_sum(anl4_*_flag, d))` produces wrong-sign signals at TOP3000
- Always use `zscore()` for analyst revision flags
- (Not promoted to rules/ — captured in the pattern file instead)

### Platform decay=10 inflates self-corr (MEDIUM confidence)
- Same expression with platform decay=10 has self-corr 0.713 vs 0.593 at decay=6
- Higher platform decay compresses PnL differences, increasing apparent correlation
- Confirmed on one candidate (78d1MV28 vs GroLXj95)

## Mechanism Insights

The economic mechanism: analyst net profit revision flags capture persistent
upward/downward revision trends in analyst earnings estimates. When multiple
analysts revise net profit forecasts in the same direction over ~22 trading days,
it signals a durable change in market consensus that hasn't fully priced in.

The `zscore` normalization is critical because revision events are rare (most
stocks have zero revisions on any given day). Cross-sectional zscore normalizes
by the standard deviation, giving higher weight to stocks with unusual revision
activity relative to the cross-section — exactly the signal we want.
