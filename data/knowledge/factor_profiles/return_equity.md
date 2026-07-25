---
field: return_equity
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.53
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1949
ann_vol: 0.0722
hit_rate: 0.5142
rolling_sharpe_min: -3.17
rolling_sharpe_max: 3.527
redundancy_cluster: 13
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.03
---
# return_equity (fundamental6)

*Return on Equity*

## Signal Profile
- `rank(return_equity)`: S=0.47, F=0.27, T=2.7%, INFERIOR (TOP3000)
- `rank(return_equity / close)`: S=0.53, F=0.29, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(return_equity, 5))`: S=-0.48, F=-0.12, T=37.6%, INFERIOR (TOP3000)
- `ts_decay_linear(rank(return_equity), 5)`: S=0.48, F=0.28, T=2.6%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(return_equity), ts_std_dev(returns,20)<0.01)`: S=0.48, F=0.28, T=3.2%, INFERIOR (TOP3000)
- `-rank(return_equity)`: S=-0.32, F=-0.15, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(return_equity, 5))`: S=0.50, F=0.16, T=37.6%, INFERIOR (TOP3000)
- `ts_zscore(return_equity, 22)`: S=0.45, F=0.15, T=37.8%, INFERIOR (TOP3000)
- `ts_mean(return_equity, 10)`: S=0.44, F=0.27, T=4.1%, INFERIOR (TOP3000)
- `rank(ts_rank(return_equity, 22))`: S=0.18, F=0.04, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * return_equity)`: S=-0.32, F=-0.15, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * return_equity / close)`: S=-0.41, F=-0.20, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/27P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/19P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.53, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.20 (negative), ret=-0.6%
  - 2020: S=-2.44 (negative), ret=-11.4%
  - 2021: S=1.98 (strong), ret=+14.1%
  - 2022: S=1.66 (strong), ret=+17.9%
  - 2023: S=-0.16 (negative), ret=-1.2%

## Risk & Drawdown
- Max drawdown: 19.49% over 642 days (recovered)
- Annualized: return +3.8%, volatility 7.2% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew -0.32, excess kurtosis +1.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.17, max 3.53, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.87%; worst month: -4.77%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.96
- Sideways: S=0.72
- Bear: S=-2.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(return_equity, 5))` S=0.50, F=0.16, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * return_equity)`: S=-0.32, F=-0.15, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * return_equity / close)`: S=-0.41, F=-0.20, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(return_equity, 5))`: S=0.50, F=0.16, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(return_equity / close)` | TOP3000 | 0.53 | 0.29 | 19.5% | 40% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(return_equity), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.48 | 0.28 | 27.9% | 40% | bull-only |
| `ts_decay_linear(rank(return_equity), 5)` | TOP3000 | 0.48 | 0.28 | 27.3% | 60% | bull-only |
| `rank(return_equity)` | TOP3000 | 0.47 | 0.27 | 27.3% | 60% | bull-only |
| `rank(return_equity / close)` | TOP1000 | 0.40 | 0.20 | 18.6% | 60% | bull-only |
| `rank(return_equity)` | TOP1000 | 0.31 | 0.15 | 27.6% | 60% | bull-only |
| `rank(return_equity / close)` | TOP200 | 0.09 | 0.03 | 29.1% | 60% | bull-only |
| `rank(return_equity)` | TOP200 | 0.08 | 0.02 | 30.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- return_assets: 0.953 (strongly positively correlated)
- eps: 0.944 (strongly positively correlated)
- fnd6_newqv1300_epspiq: 0.944 (strongly positively correlated)
- fnd6_newqv1300_epsfiq: 0.944 (strongly positively correlated)
- fnd6_newqv1300_epspxq: 0.943 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
