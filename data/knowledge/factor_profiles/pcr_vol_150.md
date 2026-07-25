---
field: pcr_vol_150
dataset: option9
best_template: ts_zscore
best_sharpe: 0.79
best_fitness: 0.18
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.0619
ann_vol: 0.0425
hit_rate: 0.5117
rolling_sharpe_min: -1.204
rolling_sharpe_max: 2.02
negated_best_sharpe: 0.0
negated_best_template: neg_rank
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.79
---
# pcr_vol_150 (option9)

*Ratio of total put options volume to call options volume for options expiring in 150 days, reflecting short-term options flow sentiment*

## Signal Profile
- `rank(pcr_vol_150)`: S=0.46, F=0.08, T=58.0%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_vol_150, 5))`: S=0.23, F=0.02, T=86.0%, INFERIOR (TOP3000)
- `-rank(pcr_vol_150)`: S=0.00, F=0.00, T=50.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_150, 5))`: S=-0.23, F=-0.02, T=86.0%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_vol_150, 63)`: S=0.79, F=0.18, T=56.2%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_150, 10)`: S=0.19, F=0.05, T=18.5%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_150, 22))`: S=-0.71, F=-0.14, T=65.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_150)`: S=-0.46, F=-0.08, T=58.0%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_150 / close)`: S=-0.22, F=-0.04, T=59.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 7F/13P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.46, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+0.6%
  - 2020: S=0.70 (moderate), ret=+3.5%
  - 2021: S=0.45 (weak), ret=+2.0%
  - 2022: S=-0.54 (negative), ret=-2.1%
  - 2023: S=1.33 (moderate), ret=+5.5%

## Risk & Drawdown
- Max drawdown: 6.19% over 1087 days (recovered)
- Annualized: return +1.9%, volatility 4.2% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew -0.02, excess kurtosis +1.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.20, max 2.02, latest 1.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +2.46%; worst month: -3.27%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.77
- Sideways: S=1.10
- Bear: S=-0.34

## Negated Direction
Best negated: `-rank(pcr_vol_150)` S=0.00, F=0.00, INFERIOR
Direction gap: -0.79 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_150)`: S=-0.46, F=-0.08, T=58.0%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_150 / close)`: S=-0.22, F=-0.04, T=59.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_150, 5))`: S=-0.23, F=-0.02, T=86.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_vol_150)` | TOP3000 | 0.46 | 0.08 | 6.2% | 80% | mixed |
| `rank(ts_delta(pcr_vol_150, 5))` | TOP3000 | 0.23 | 0.02 | 7.0% | 80% | bull-only |

## Correlation Notes
Top correlates:
- pcr_vol_180: 0.987 (strongly positively correlated)
- pcr_vol_270: 0.955 (strongly positively correlated)
- pcr_vol_1080: 0.877 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_q: 0.569 (moderately positively correlated)
- fn_assets_fair_val_q: 0.547 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
