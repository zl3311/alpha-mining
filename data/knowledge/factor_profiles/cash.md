---
field: cash
dataset: fundamental6
cluster: fundamental6_other
coverage: 0.5
community_alphas: 11756
best_template: rank_level
best_sharpe: 0.51
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 39
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.3073
ann_vol: 0.0912
hit_rate: 0.5134
rolling_sharpe_min: -3.009
rolling_sharpe_max: 2.526
redundancy_cluster: 13
negated_best_sharpe: 0.4
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 12
direction_gap: -0.11
---
# cash (fundamental6)

*Cash*

## Signal Profile
- `rank(cash)`: S=0.51, F=0.31, T=2.2%, INFERIOR (TOP3000)
- `rank(cash / close)`: S=0.47, F=0.27, T=3.5%, INFERIOR (TOP500)
- `rank(ts_delta(cash, 5))`: S=0.26, F=0.08, T=38.2%, INFERIOR (TOP200)
- `ts_decay_linear(rank(cash), 5)`: S=0.51, F=0.31, T=2.2%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(cash), ts_std_dev(returns,20)<0.01)`: S=0.44, F=0.25, T=2.6%, INFERIOR (TOP3000)
- `-rank(cash)`: S=-0.24, F=-0.10, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash, 5))`: S=0.40, F=0.13, T=38.3%, INFERIOR (TOP3000)
- `-ts_zscore(cash, 63)`: S=0.27, F=0.07, T=18.0%, INFERIOR (TOP3000)
- `ts_mean(cash, 10)`: S=0.35, F=0.20, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(cash, 22))`: S=-0.30, F=-0.09, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * cash)`: S=-0.17, F=-0.07, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * cash / close)`: S=-0.47, F=-0.27, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/30P
- LOW_FITNESS: 39F/0P
- LOW_SHARPE: 39F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/26P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.51, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.76 (moderate), ret=+4.0%
  - 2020: S=-1.52 (negative), ret=-11.9%
  - 2021: S=0.69 (moderate), ret=+9.8%
  - 2022: S=1.68 (strong), ret=+13.1%
  - 2023: S=1.09 (moderate), ret=+7.9%

## Risk & Drawdown
- Max drawdown: 30.73% over 653 days (recovered)
- Annualized: return +4.7%, volatility 9.1% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.01, excess kurtosis +2.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.01, max 2.53, latest 0.89

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.61%; worst month: -6.34%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.79
- Sideways: S=1.33
- Bear: S=-2.80

## Negated Direction
Best negated: `rank(-1 * ts_delta(cash, 5))` S=0.40, F=0.13, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cash)`: S=-0.17, F=-0.07, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * cash / close)`: S=-0.47, F=-0.27, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash, 5))`: S=0.40, F=0.13, T=38.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cash)` | TOP3000 | 0.51 | 0.31 | 30.7% | 80% | bull-only |
| `ts_decay_linear(rank(cash), 5)` | TOP3000 | 0.51 | 0.31 | 30.7% | 80% | bull-only |
| `rank(cash / close)` | TOP500 | 0.47 | 0.27 | 11.9% | 60% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(cash), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.44 | 0.25 | 30.0% | 80% | bull-only |
| `rank(cash / close)` | TOP3000 | 0.44 | 0.24 | 13.5% | 80% | mixed |
| `rank(cash / close)` | TOP1000 | 0.34 | 0.17 | 9.8% | 80% | bull-only |
| `rank(cash)` | TOP1000 | 0.23 | 0.10 | 30.0% | 60% | bull-only |
| `rank(ts_delta(cash, 5))` | TOP200 | 0.26 | 0.08 | 33.5% | 60% | mixed |
| `rank(cash)` | TOP500 | 0.17 | 0.07 | 36.3% | 40% | bull-only |
| `rank(ts_delta(cash, 5))` | TOP3000 | 0.18 | 0.03 | 11.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- assets_curr: 0.959 (strongly positively correlated)
- fnd6_cptnewqv1300_actq: 0.959 (strongly positively correlated)
- fnd6_cptmfmq_actq: 0.958 (strongly positively correlated)
- fnd6_newqv1300_wcapq: 0.950 (strongly positively correlated)
- working_capital: 0.950 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
