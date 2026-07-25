---
field: anl4_ptpr_median
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.37
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.2803
ann_vol: 0.1081
hit_rate: 0.5077
rolling_sharpe_min: -3.397
rolling_sharpe_max: 2.164
negated_best_sharpe: 0.37
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: 0.01
---
# anl4_ptpr_median (analyst4)

*Reported pretax income - Median of estimations*

## Signal Profile
- `rank(anl4_ptpr_median)`: S=0.17, F=0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_ptpr_median / close)`: S=0.36, F=0.20, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ptpr_median, 5))`: S=0.06, F=0.01, T=36.8%, INFERIOR (TOP1000)
- `-rank(anl4_ptpr_median)`: S=0.07, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptpr_median, 5))`: S=0.13, F=0.02, T=36.7%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ptpr_median, 22)`: S=-0.06, F=-0.01, T=34.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptpr_median, 10)`: S=-0.08, F=-0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ptpr_median, 22))`: S=-0.07, F=-0.01, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_median)`: S=0.32, F=0.18, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_median / close)`: S=0.37, F=0.22, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.35, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.06 (weak), ret=+0.3%
  - 2020: S=-2.55 (negative), ret=-17.6%
  - 2021: S=0.91 (moderate), ret=+10.9%
  - 2022: S=1.57 (strong), ret=+24.3%
  - 2023: S=0.05 (weak), ret=+0.5%

## Risk & Drawdown
- Max drawdown: 28.03% over 821 days (recovered)
- Annualized: return +3.8%, volatility 10.8% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.13, excess kurtosis +1.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.40, max 2.16, latest -0.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.57%; worst month: -6.33%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.09
- Sideways: S=0.74
- Bear: S=-3.54

## Negated Direction
Best negated: `rank(-1 * anl4_ptpr_median / close)` S=0.37, F=0.22, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_ptpr_median)`: S=0.32, F=0.18, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_median / close)`: S=0.37, F=0.22, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptpr_median, 5))`: S=0.13, F=0.02, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ptpr_median / close)` | TOP3000 | 0.35 | 0.20 | 28.0% | 80% | bull-only |
| `rank(anl4_ptpr_median)` | TOP3000 | 0.16 | 0.07 | 42.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ptpr_mean: 1.000 (strongly positively correlated)
- anl4_ptpr_low: 0.998 (strongly positively correlated)
- est_ptpr: 0.975 (strongly positively correlated)
- anl4_ptp_low: 0.948 (strongly positively correlated)
- anl4_netprofit_low: 0.946 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
