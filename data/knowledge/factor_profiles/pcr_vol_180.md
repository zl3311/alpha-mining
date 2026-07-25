---
field: pcr_vol_180
dataset: option9
best_template: ts_zscore
best_sharpe: 0.93
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.0633
ann_vol: 0.043
hit_rate: 0.5093
rolling_sharpe_min: -1.289
rolling_sharpe_max: 2.063
redundancy_cluster: 79
negated_best_sharpe: 0.12
negated_best_template: neg_rank
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.81
---
# pcr_vol_180 (option9)

*Ratio of total put option volume to call option volume for options expiring in 180 days, capturing short-term options flow sentiment*

## Signal Profile
- `rank(pcr_vol_180)`: S=0.51, F=0.10, T=57.1%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_vol_180, 5))`: S=-0.07, F=0.00, T=85.9%, INFERIOR (TOP3000)
- `-rank(pcr_vol_180)`: S=0.12, F=0.01, T=49.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_180, 5))`: S=0.07, F=0.00, T=85.9%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_vol_180, 63)`: S=0.93, F=0.24, T=56.2%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_180, 10)`: S=0.06, F=0.01, T=18.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_180, 22))`: S=-1.00, F=-0.22, T=65.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_180)`: S=-0.51, F=-0.10, T=57.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_180 / close)`: S=-0.30, F=-0.05, T=59.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 7F/13P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/5P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.50, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.62 (moderate), ret=+1.9%
  - 2020: S=0.69 (moderate), ret=+3.5%
  - 2021: S=0.34 (weak), ret=+1.5%
  - 2022: S=-0.63 (negative), ret=-2.5%
  - 2023: S=1.47 (moderate), ret=+6.1%

## Risk & Drawdown
- Max drawdown: 6.33% over 1008 days (recovered)
- Annualized: return +2.2%, volatility 4.3% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.04, excess kurtosis +1.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 2.06, latest 1.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +3.07%; worst month: -3.26%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.64
- Sideways: S=1.27
- Bear: S=-0.25

## Negated Direction
Best negated: `-rank(pcr_vol_180)` S=0.12, F=0.01, INFERIOR
Direction gap: -0.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_180)`: S=-0.51, F=-0.10, T=57.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_180 / close)`: S=-0.30, F=-0.05, T=59.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_180, 5))`: S=0.07, F=0.00, T=85.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_vol_180)` | TOP3000 | 0.50 | 0.10 | 6.3% | 80% | mixed |

## Correlation Notes
Top correlates:
- pcr_vol_150: 0.987 (strongly positively correlated)
- pcr_vol_270: 0.972 (strongly positively correlated)
- pcr_vol_1080: 0.893 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_q: 0.532 (moderately positively correlated)
- fn_assets_fair_val_q: 0.523 (moderately positively correlated)

Redundancy cluster #79: 2 similar fields, mean |rho| 0.893 (representative: pcr_vol_1080). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
