---
id: "20260626-001-learnings"
session: "20260626-001"
category: "discovery"
confidence: "high"
actionable: true
---

# Learnings: Session 20260626-001

## What Worked

- **anl4_epsr_flag as a novel decorrelating connector**: EPS revision flag is
  the first analyst4 flag field to reach EXCELLENT as a primary signal component.
  At session time, it was absent from book entries, keeping self-corr low (0.590-0.604).

- **fnd6_newqv1300_dpactq as a novel value anchor**: Depreciation (quarterly)
  at S=1.29 standalone combines well with analyst revision (negative PnL
  correlation, rho ~ -0.35). At session time, not yet a primary anchor in any book entry.

- **open/close-1 as the strongest 3rd factor for this family**: Adding the
  intraday gap to the 2-factor epsr+depreciation blend lifted Sharpe from 1.74
  to 2.08 (+20%) while only raising self-corr from 0.590 to 0.604.

- **zscore+ts_sum normalization confirmed essential for sparse flags**: The
  pattern from zscore-accumulated-revision holds. rank() would produce wrong-sign
  signals for zero-dominated distributions.

- **Event-magnitude on depreciation works**: abs(ts_delta(fnd6_newqv1300_dpactq/close, 3))
  produces EXCELLENT (S=1.95) when combined with epsr. The itci event-magnitude
  pattern generalizes to depreciation.

## What Didn't Work

- **Dynamic correlation (ts_corr) with fundamental fields**: All 4 candidates
  using `rank(ts_corr(field/close, returns, 22))` were INFERIOR (S=-0.37 to 1.00).
  Time-varying correlation between slow fundamentals and daily returns is noise.

- **Inter-field ratios (rank(F1/F2))**: All 4 ratio variants were INFERIOR
  (S=0.17 to 0.26). Within-dataset fundamental ratios produce no cross-sectional
  signal — the rank transform cannot rescue these.

- **Multiplicative combination**: `zscore(ts_sum(anl4_epsr_flag, 22)) * rank(fnd6_newqv1300_dpactq / close)`
  was INFERIOR (S=0.70). The product concentrates signal in stocks high on BOTH
  factors, destroying coverage.

- **MARKET neutralization on epsr+depreciation**: GOOD (S=1.34) vs EXCELLENT
  (S=1.74) under SUBINDUSTRY. Sparse analyst revision flags need within-industry
  context to be meaningful.

- **Novel fundamental6 fields (txs, dn, nopio, dpvieb, mrct)**: All blends
  using these fields stayed INFERIOR-AVERAGE (S=0.79 to 1.22). The novel
  field exploration for fundamental6 is exhausted.

## New Dead Zones

- **Dynamic correlation template**: `rank(ts_corr(field, returns, d))` is dead
  for fundamental6 fields. Do not test further.
- **Inter-field fundamental ratios**: `rank(F1/F2)` where F1, F2 are both
  fundamental6 fields is dead. Do not test further.
- **fnd6_txs, fnd6_dn, fnd6_nopio standalone**: Too weak (S < 1.25) for any
  blend to reach EXCELLENT.

## New Patterns

- **EPS revision + depreciation value**: `zscore(ts_sum(anl4_epsr_flag, 22)) +
  rank(fnd6_newqv1300_dpactq / close)` is a novel decorrelated 2-factor core
  reaching EXCELLENT (S=1.74) with self-corr=0.590.
- **+ open/close-1 stabilizer**: Adding `rank(open/close - 1)` as 3rd factor
  boosts Sharpe by 20% with minimal self-corr increase. This is the preferred
  3-factor variant.

## Mechanism Insights

The EPS revision + depreciation blend works because it combines two orthogonal
information sources: (1) analyst sentiment momentum (forward-looking, event-driven)
and (2) capital investment value (backward-looking, accounting-driven). Markets
underreact to both signals individually, and their negative PnL correlation means
the blend is diversified across market regimes (analyst revisions cluster around
earnings, depreciation value is persistent).
