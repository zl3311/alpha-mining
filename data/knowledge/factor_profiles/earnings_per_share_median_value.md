---
field: earnings_per_share_median_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.74
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1089
ann_vol: 0.042
hit_rate: 0.5174
rolling_sharpe_min: -1.214
rolling_sharpe_max: 2.25
negated_best_sharpe: 0.2
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.7
---
# earnings_per_share_median_value (analyst4)

*Earnings per share - median of estimations*

## Signal Profile
- `rank(earnings_per_share_median_value)`: S=0.40, F=0.25, T=1.2%, INFERIOR (TOP3000)
- `rank(earnings_per_share_median_value / close)`: S=0.90, F=0.74, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(earnings_per_share_median_value, 5))`: S=0.21, F=0.03, T=36.1%, INFERIOR (TOP1000)
- `-rank(earnings_per_share_median_value)`: S=-0.16, F=-0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_median_value, 5))`: S=0.20, F=0.03, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(earnings_per_share_median_value, 22)`: S=0.24, F=0.05, T=33.5%, INFERIOR (TOP3000)
- `ts_mean(earnings_per_share_median_value, 10)`: S=-0.10, F=-0.03, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(earnings_per_share_median_value, 22))`: S=0.09, F=0.01, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_median_value)`: S=-0.08, F=-0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_median_value / close)`: S=-0.14, F=-0.05, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.21, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.07 (weak), ret=+0.2%
  - 2020: S=-0.68 (negative), ret=-2.9%
  - 2021: S=1.47 (moderate), ret=+7.0%
  - 2022: S=0.24 (weak), ret=+1.1%
  - 2023: S=-0.29 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 10.89% over 662 days (recovered)
- Annualized: return +0.9%, volatility 4.2% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.20, excess kurtosis +1.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.21, max 2.25, latest -0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +2.83%; worst month: -2.99%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.79
- Sideways: S=-0.43
- Bear: S=-0.80

## Negated Direction
Best negated: `rank(-1 * ts_delta(earnings_per_share_median_value, 5))` S=0.20, F=0.03, INFERIOR
Direction gap: -0.70 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * earnings_per_share_median_value)`: S=-0.08, F=-0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * earnings_per_share_median_value / close)`: S=-0.14, F=-0.05, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(earnings_per_share_median_value, 5))`: S=0.20, F=0.03, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(earnings_per_share_median_value, 5))` | TOP1000 | 0.21 | 0.03 | 10.9% | 60% | bull-only |
| `rank(ts_delta(earnings_per_share_median_value, 5))` | TOP3000 | 0.17 | 0.02 | 11.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- earnings_per_share_maximum: 0.585 (moderately positively correlated)
- earnings_per_share_minimum: 0.579 (moderately positively correlated)
- income: 0.481 (moderately positively correlated)
- fnd6_mfmq_ibcomq: 0.481 (moderately positively correlated)
- put_breakeven_1080: 0.480 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
