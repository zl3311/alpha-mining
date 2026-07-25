---
field: pcr_oi_all
dataset: option9
best_template: ts_zscore
best_sharpe: 0.58
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1663
ann_vol: 0.0516
hit_rate: 0.5053
rolling_sharpe_min: -2.865
rolling_sharpe_max: 2.288
negated_best_sharpe: 0.03
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.55
---
# pcr_oi_all (option9)

*Ratio of total put option open interest to call option open interest aggregated across all option maturities for the stock*

## Signal Profile
- `rank(pcr_oi_all)`: S=0.33, F=0.12, T=6.3%, INFERIOR (TOP3000)
- `rank(pcr_oi_all / close)`: S=0.03, F=0.00, T=5.5%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_oi_all, 5))`: S=0.11, F=0.01, T=37.2%, INFERIOR (TOP500)
- `-rank(pcr_oi_all)`: S=-0.13, F=-0.03, T=7.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_all, 5))`: S=0.04, F=0.00, T=35.0%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_oi_all, 63)`: S=0.58, F=0.22, T=15.1%, INFERIOR (TOP3000)
- `ts_mean(pcr_oi_all, 10)`: S=0.18, F=0.05, T=5.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_oi_all, 22))`: S=-0.34, F=-0.08, T=23.4%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_all)`: S=-0.33, F=-0.12, T=6.3%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_all / close)`: S=0.03, F=0.00, T=5.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.33, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.20 (moderate), ret=+2.5%
  - 2020: S=-2.27 (negative), ret=-9.8%
  - 2021: S=0.88 (moderate), ret=+5.5%
  - 2022: S=1.33 (moderate), ret=+9.1%
  - 2023: S=0.21 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 16.63% over 817 days (recovered)
- Annualized: return +1.7%, volatility 5.2% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.12, excess kurtosis +0.97

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.87, max 2.29, latest -0.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.63%; worst month: -3.06%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.13
- Sideways: S=0.83
- Bear: S=-2.22

## Negated Direction
Best negated: `rank(-1 * pcr_oi_all / close)` S=0.03, F=0.00, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_oi_all)`: S=-0.33, F=-0.12, T=6.3%, INFERIOR (TOP3000)
- `rank(-1 * pcr_oi_all / close)`: S=0.03, F=0.00, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_oi_all, 5))`: S=0.04, F=0.00, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_oi_all)` | TOP3000 | 0.33 | 0.12 | 16.6% | 80% | bull-only |
| `rank(pcr_oi_all)` | TOP500 | 0.18 | 0.05 | 9.5% | 40% | bull-only |
| `rank(pcr_oi_all)` | TOP1000 | 0.12 | 0.03 | 11.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pcr_oi_10: 0.910 (strongly positively correlated)
- pcr_oi_20: 0.905 (strongly positively correlated)
- pcr_oi_30: 0.891 (strongly positively correlated)
- pcr_oi_360: 0.881 (strongly positively correlated)
- pcr_oi_720: 0.869 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
