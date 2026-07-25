---
field: pcr_vol_90
dataset: option9
best_template: rank_delta
best_sharpe: 0.61
best_fitness: 0.14
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.149
ann_vol: 0.0658
hit_rate: 0.5231
rolling_sharpe_min: -1.301
rolling_sharpe_max: 3.022
negated_best_sharpe: -0.07
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -0.68
---
# pcr_vol_90 (option9)

*Ratio of put options volume to call options volume for stock options expiring in 90 days, indicating short-term options flow sentiment*

## Signal Profile
- `rank(pcr_vol_90)`: S=0.35, F=0.05, T=59.4%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_vol_90, 5))`: S=0.61, F=0.14, T=71.1%, INFERIOR (TOP200)
- `-rank(pcr_vol_90)`: S=-0.15, F=-0.02, T=50.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_90, 5))`: S=-0.51, F=-0.06, T=85.7%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_vol_90, 63)`: S=-0.09, F=-0.01, T=55.9%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_90, 10)`: S=-0.35, F=-0.13, T=18.2%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_90, 22))`: S=-0.42, F=-0.06, T=63.8%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_90)`: S=-0.35, F=-0.05, T=59.4%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_90 / close)`: S=-0.07, F=-0.01, T=60.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 7F/13P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.62, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.24 (moderate), ret=+6.7%
  - 2020: S=-0.93 (negative), ret=-6.5%
  - 2021: S=-0.15 (negative), ret=-1.2%
  - 2022: S=1.90 (strong), ret=+13.2%
  - 2023: S=1.58 (strong), ret=+7.7%

## Risk & Drawdown
- Max drawdown: 14.90% over 752 days (recovered)
- Annualized: return +4.1%, volatility 6.6% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew -0.26, excess kurtosis +2.53

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.30, max 3.02, latest 1.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.24%; worst month: -4.54%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.17
- Sideways: S=1.27
- Bear: S=0.52

## Negated Direction
Best negated: `rank(-1 * pcr_vol_90 / close)` S=-0.07, F=-0.01, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_90)`: S=-0.35, F=-0.05, T=59.4%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_90 / close)`: S=-0.07, F=-0.01, T=60.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_90, 5))`: S=-0.51, F=-0.06, T=85.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pcr_vol_90, 5))` | TOP200 | 0.62 | 0.14 | 14.9% | 60% | mixed |
| `rank(ts_delta(pcr_vol_90, 5))` | TOP3000 | 0.52 | 0.06 | 5.6% | 60% | weak |
| `rank(pcr_vol_90)` | TOP3000 | 0.35 | 0.05 | 5.8% | 60% | bull-only |
| `rank(pcr_vol_90)` | TOP200 | 0.16 | 0.03 | 16.7% | 40% | mixed |

## Correlation Notes
Top correlates:
- pcr_vol_60: 0.542 (moderately positively correlated)
- pcr_vol_120: 0.147 (weakly positively correlated)
- fnd6_newa2v1300_prsho: 0.120 (weakly positively correlated)
- snt_buzz: 0.116 (weakly positively correlated)
- beta_last_360_days_spy: -0.102 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
