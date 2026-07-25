---
id: "20260625-002-learnings"
session: "20260625-002"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260625-002

## What Worked

- **`rank(open / close - 1)` as Sharpe booster**: The overnight gap component elevates fundamental blends from EXCELLENT (S~2.5) to SPECTACULAR (S~3.0). It captures informed overnight trading before market open, providing a fast-changing signal complementary to slow-moving fundamentals.
- **`anl4_ptpr_flag` as optimal analyst complement**: Pre-tax profit revision flag (ptpr) outperforms bvps_flag and netdebt_flag when combined with acdo+itci fundamental core (S=3.02 vs 2.53 vs 2.95).
- **4-factor additive blend structure fixes SUB_UNIVERSE**: Adding diverse legs ensures signal breadth across sectors, passing the sub-universe consistency check.
- **Non-IV blends can decorrelate below 0.7**: By avoiding IV60/90/270 entirely, the fundamental+intraday blend achieves max self-corr of 0.63 — well below the 0.7 auto-pass threshold.

## What Didn't Work

- **IV60 4-factor blends**: Despite passing all IS checks (S=2.82, F=5.04), self-corr is 0.81-0.83 against 88z7MM37. Premium escape requires S>=3.06 which is unachievable with 4 factors (3-factor reaches 3.09 but fails sub-universe).
- **Pure fundamental blends without intraday/analyst**: `dpactq+epsr+dlto+acdo` only reaches S=1.35 (AVERAGE). The overnight gap and analyst revision legs are essential for grade.
- **MARKET neutralization on IV60**: Reduces Sharpe from 3.09 to 1.93-2.73 without meaningfully reducing self-correlation.
- **`bvps_flag` with acdo+itci**: Inferior to ptpr_flag (S=2.53 vs 3.02) and fails SUB_UNIVERSE.

## New Patterns

- **Overnight gap + fundamental + analyst template**: `ts_decay_linear(rank(F1/close) + rank(open/close - 1) + rank(analyst_flag) + rank(F2/close), 5)` with SUBINDUSTRY neutralization and decay=6. Achieves SPECTACULAR with low self-corr.
- **ptpr_flag dominance**: Among analyst revision flags, `anl4_ptpr_flag` provides the highest marginal Sharpe when combined with fundamental acdo+itci core.

## Mechanism Insights

The winning alpha exploits four independent information channels:

1. **Balance sheet value (fnd6_acdo/close, fnd6_itci/close)**: Slow-moving quarterly fundamentals capturing capital intensity and asset maturity — firms with high accumulated depreciation and inventory relative to price are undervalued.
2. **Overnight gap (open/close - 1)**: Captures informed after-hours trading. Large positive gaps (open > previous close) signal institutional conviction from overnight news/analysis processing.
3. **Analyst information flow (anl4_ptpr_flag)**: Pre-tax profit revision direction captures sell-side consensus shifts before they fully propagate to market prices.

The combination works because each channel has distinct information content and temporal characteristics (quarterly/daily/event-driven), providing natural diversification.
