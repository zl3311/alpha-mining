---
field: ebitda
dataset: fundamental6
cluster: fundamental6_income_earnings
coverage: 0.5
community_alphas: 20319
best_template: rank_value_norm
best_sharpe: 0.59
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.2366
ann_vol: 0.1208
hit_rate: 0.502
rolling_sharpe_min: -2.14
rolling_sharpe_max: 2.424
redundancy_cluster: 13
negated_best_sharpe: 0.22
negated_best_template: neg_rank_level
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.37
---
# ebitda (fundamental6)

*Earnings Before Interest*

## Signal Profile
- `rank(ebitda)`: S=0.32, F=0.19, T=1.1%, INFERIOR (TOP3000)
- `rank(ebitda / close)`: S=0.59, F=0.45, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(ebitda, 5))`: S=0.69, F=0.42, T=34.7%, INFERIOR (TOP200)
- `ts_decay_linear(rank(ebitda), 5)`: S=0.32, F=0.19, T=1.0%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(ebitda), ts_std_dev(returns,20)<0.01)`: S=0.27, F=0.15, T=2.0%, INFERIOR (TOP3000)
- `-rank(ebitda)`: S=-0.12, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(ebitda, 5))`: S=-0.71, F=-0.44, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(ebitda, 63)`: S=-0.06, F=-0.01, T=19.6%, INFERIOR (TOP3000)
- `ts_mean(ebitda, 10)`: S=0.14, F=0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(ebitda, 22))`: S=0.13, F=0.03, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * ebitda)`: S=0.22, F=0.12, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ebitda / close)`: S=0.17, F=0.08, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/25P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.07 (weak), ret=+0.4%
  - 2020: S=-1.19 (negative), ret=-10.8%
  - 2021: S=1.22 (moderate), ret=+18.2%
  - 2022: S=1.47 (moderate), ret=+24.9%
  - 2023: S=0.19 (weak), ret=+1.7%

## Risk & Drawdown
- Max drawdown: 23.66% over 770 days (recovered)
- Annualized: return +7.0%, volatility 12.1% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.02, excess kurtosis +1.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.14, max 2.42, latest 0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.20%; worst month: -5.00%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.13
- Sideways: S=0.72
- Bear: S=-2.94

## Negated Direction
Best negated: `rank(-1 * ebitda)` S=0.22, F=0.12, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * ebitda)`: S=0.22, F=0.12, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ebitda / close)`: S=0.17, F=0.08, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(ebitda, 5))`: S=-0.71, F=-0.44, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ebitda / close)` | TOP3000 | 0.58 | 0.45 | 23.7% | 80% | bull-only |
| `rank(ts_delta(ebitda, 5))` | TOP200 | 0.68 | 0.42 | 25.5% | 80% | mixed |
| `rank(ts_delta(ebitda, 5))` | TOP1000 | 0.67 | 0.30 | 14.0% | 80% | mixed |
| `rank(ebitda)` | TOP3000 | 0.30 | 0.19 | 40.9% | 60% | bull-only |
| `ts_decay_linear(rank(ebitda), 5)` | TOP3000 | 0.31 | 0.19 | 40.9% | 60% | bull-only |
| `rank(ebitda / close)` | TOP1000 | 0.29 | 0.18 | 28.4% | 60% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(ebitda), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.26 | 0.15 | 39.5% | 60% | bull-only |
| `rank(ts_delta(ebitda, 5))` | TOP500 | 0.32 | 0.12 | 18.7% | 80% | mixed |
| `rank(ts_delta(ebitda, 5))` | TOP3000 | 0.31 | 0.09 | 10.6% | 80% | mixed |
| `rank(ebitda)` | TOP1000 | 0.11 | 0.05 | 45.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ebitda: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 1.000 (strongly positively correlated)
- fnd6_mfma2_oancf: 0.987 (strongly positively correlated)
- cashflow_op: 0.987 (strongly positively correlated)
- fnd6_newa2v1300_oancf: 0.987 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
