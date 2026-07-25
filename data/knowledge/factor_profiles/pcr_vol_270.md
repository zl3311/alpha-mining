---
field: pcr_vol_270
dataset: option9
best_template: rank_level
best_sharpe: 0.48
best_fitness: 0.09
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0555
ann_vol: 0.0426
hit_rate: 0.5126
rolling_sharpe_min: -1.203
rolling_sharpe_max: 2.045
negated_best_sharpe: -0.29
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.05
n_negated_sims: 4
direction_gap: -0.77
---
# pcr_vol_270 (option9)

*Ratio of total put options volume to call options volume for contracts expiring 270 days in the future, indicating short-term options flow sentiment at longer tenor*

## Signal Profile
- `rank(pcr_vol_270)`: S=0.48, F=0.09, T=55.9%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_vol_270, 5))`: S=0.43, F=0.05, T=85.9%, INFERIOR (TOP3000)
- `-rank(pcr_vol_270)`: S=-0.35, F=-0.06, T=48.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_270, 5))`: S=-0.43, F=-0.05, T=85.9%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_vol_270, 63)`: S=0.20, F=0.02, T=56.5%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_270, 10)`: S=-0.02, F=0.00, T=18.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_270, 22))`: S=0.03, F=0.00, T=65.9%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_270)`: S=-0.48, F=-0.09, T=55.9%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_270 / close)`: S=-0.29, F=-0.05, T=58.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 7F/13P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.48, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.76 (moderate), ret=+2.4%
  - 2020: S=0.50 (weak), ret=+2.5%
  - 2021: S=0.36 (weak), ret=+1.6%
  - 2022: S=-0.81 (negative), ret=-3.1%
  - 2023: S=1.62 (strong), ret=+6.6%

## Risk & Drawdown
- Max drawdown: 5.55% over 1109 days (recovered)
- Annualized: return +2.0%, volatility 4.3% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.03, excess kurtosis +1.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.20, max 2.04, latest 1.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +3.28%; worst month: -3.09%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.59
- Sideways: S=1.19
- Bear: S=-0.22

## Negated Direction
Best negated: `rank(-1 * pcr_vol_270 / close)` S=-0.29, F=-0.05, INFERIOR
Direction gap: -0.77 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_270)`: S=-0.48, F=-0.09, T=55.9%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_270 / close)`: S=-0.29, F=-0.05, T=58.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_270, 5))`: S=-0.43, F=-0.05, T=85.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_vol_270)` | TOP3000 | 0.48 | 0.09 | 5.5% | 80% | mixed |
| `rank(pcr_vol_270)` | TOP1000 | 0.33 | 0.06 | 8.9% | 60% | bull-only |
| `rank(ts_delta(pcr_vol_270, 5))` | TOP3000 | 0.43 | 0.05 | 7.3% | 60% | mixed |
| `rank(pcr_vol_270)` | TOP500 | 0.15 | 0.02 | 11.3% | 40% | bull-only |

## Correlation Notes
Top correlates:
- pcr_vol_180: 0.972 (strongly positively correlated)
- pcr_vol_150: 0.955 (strongly positively correlated)
- pcr_vol_1080: 0.914 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_q: 0.530 (moderately positively correlated)
- fnd6_cptrank_gvkeymap: -0.525 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
