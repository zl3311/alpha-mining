---
field: fnd6_newa1v1300_aoloch
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.72
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1616
ann_vol: 0.0948
hit_rate: 0.502
rolling_sharpe_min: -1.209
rolling_sharpe_max: 2.473
redundancy_cluster: 67
negated_best_sharpe: 0.72
negated_best_template: rank_neg_delta
negated_best_fitness: 0.49
n_negated_sims: 10
direction_gap: -0.03
---
# fnd6_newa1v1300_aoloch (fundamental6)

*Assets and Liabilities - Other - Net Change*

## Signal Profile
- `rank(fnd6_newa1v1300_aoloch)`: S=0.39, F=0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_aoloch / close)`: S=0.18, F=0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_aoloch, 5))`: S=0.75, F=0.33, T=36.4%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_aoloch)`: S=0.21, F=0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aoloch, 5))`: S=0.72, F=0.49, T=33.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_aoloch, 22)`: S=0.42, F=0.23, T=28.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_aoloch, 10)`: S=0.16, F=0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_aoloch, 22))`: S=0.37, F=0.17, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aoloch)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aoloch / close)`: S=-0.04, F=-0.01, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.75, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.17 (weak), ret=+1.3%
  - 2020: S=-0.06 (negative), ret=-0.6%
  - 2021: S=1.11 (moderate), ret=+11.4%
  - 2022: S=0.77 (moderate), ret=+7.1%
  - 2023: S=1.73 (strong), ret=+15.8%

## Risk & Drawdown
- Max drawdown: 16.16% over 856 days (recovered)
- Annualized: return +7.1%, volatility 9.5% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.61, excess kurtosis +5.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.21, max 2.47, latest 1.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +9.39%; worst month: -5.85%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.79
- Sideways: S=1.22
- Bear: S=0.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_aoloch, 5))` S=0.72, F=0.49, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_aoloch)`: S=0.01, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_aoloch / close)`: S=-0.04, F=-0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_aoloch, 5))`: S=0.72, F=0.49, T=33.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_aoloch, 5))` | TOP3000 | 0.75 | 0.33 | 16.2% | 80% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_aoloch, 5))` | TOP1000 | 0.54 | 0.23 | 20.7% | 60% | all-weather |
| `rank(ts_delta(fnd6_newa1v1300_aoloch, 5))` | TOP500 | 0.45 | 0.22 | 41.8% | 80% | weak |
| `rank(fnd6_newa1v1300_aoloch)` | TOP3000 | 0.40 | 0.11 | 4.4% | 60% | weak |
| `rank(fnd6_newa1v1300_aoloch / close)` | TOP3000 | 0.18 | 0.04 | 6.4% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_mfma1_aoloch: 0.997 (strongly positively correlated)
- fnd6_cimii: -0.168 (weakly negatively correlated)
- fnd2_a_eplsbvdcpcstnrgprg: 0.115 (weakly positively correlated)
- fnd2_q_flintasamt1expytwo: 0.097 (weakly positively correlated)
- fnd6_aqc: 0.096 (weakly positively correlated)

Redundancy cluster #67: 2 similar fields, mean |rho| 0.997 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
