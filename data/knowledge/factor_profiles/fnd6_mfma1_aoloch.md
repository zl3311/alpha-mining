---
field: fnd6_mfma1_aoloch
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.65
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1606
ann_vol: 0.0946
hit_rate: 0.498
rolling_sharpe_min: -1.411
rolling_sharpe_max: 2.435
redundancy_cluster: 67
negated_best_sharpe: 0.65
negated_best_template: rank_neg_delta
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: -0.04
---
# fnd6_mfma1_aoloch (fundamental6)

*Assets and Liabilities - Other - Net Change*

## Signal Profile
- `rank(fnd6_mfma1_aoloch)`: S=0.40, F=0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_mfma1_aoloch / close)`: S=0.19, F=0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mfma1_aoloch, 5))`: S=0.69, F=0.29, T=36.4%, INFERIOR (TOP3000)
- `-rank(fnd6_mfma1_aoloch)`: S=0.22, F=0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_aoloch, 5))`: S=0.65, F=0.42, T=32.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_mfma1_aoloch, 22)`: S=0.40, F=0.21, T=28.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma1_aoloch, 10)`: S=0.15, F=0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma1_aoloch, 22))`: S=0.37, F=0.17, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_aoloch)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_aoloch / close)`: S=-0.03, F=0.00, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.69, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+1.7%
  - 2020: S=-0.28 (negative), ret=-2.8%
  - 2021: S=1.04 (moderate), ret=+10.8%
  - 2022: S=0.82 (moderate), ret=+7.6%
  - 2023: S=1.64 (strong), ret=+14.9%

## Risk & Drawdown
- Max drawdown: 16.06% over 877 days (recovered)
- Annualized: return +6.6%, volatility 9.5% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.61, excess kurtosis +5.30

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.41, max 2.44, latest 1.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +9.42%; worst month: -5.90%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.75
- Sideways: S=1.21
- Bear: S=0.19

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mfma1_aoloch, 5))` S=0.65, F=0.42, INFERIOR
Direction gap: -0.04 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_mfma1_aoloch)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_aoloch / close)`: S=-0.03, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_aoloch, 5))`: S=0.65, F=0.42, T=32.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_mfma1_aoloch, 5))` | TOP3000 | 0.69 | 0.29 | 16.1% | 80% | mixed |
| `rank(ts_delta(fnd6_mfma1_aoloch, 5))` | TOP500 | 0.49 | 0.25 | 43.3% | 80% | weak |
| `rank(ts_delta(fnd6_mfma1_aoloch, 5))` | TOP1000 | 0.55 | 0.24 | 20.7% | 40% | all-weather |
| `rank(fnd6_mfma1_aoloch)` | TOP3000 | 0.41 | 0.11 | 4.5% | 60% | weak |
| `rank(fnd6_mfma1_aoloch / close)` | TOP3000 | 0.19 | 0.04 | 6.5% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_aoloch: 0.997 (strongly positively correlated)
- fnd6_cimii: -0.168 (weakly negatively correlated)
- fnd2_a_eplsbvdcpcstnrgprg: 0.116 (weakly positively correlated)
- fnd6_aqc: 0.098 (weakly positively correlated)
- fnd2_q_flintasamt1expytwo: 0.096 (weakly positively correlated)

Redundancy cluster #67: 2 similar fields, mean |rho| 0.997 (representative: fnd6_newa1v1300_aoloch). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
