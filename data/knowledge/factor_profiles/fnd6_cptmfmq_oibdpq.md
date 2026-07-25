---
field: fnd6_cptmfmq_oibdpq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.6
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.292
ann_vol: 0.1179
hit_rate: 0.4996
rolling_sharpe_min: -3.46
rolling_sharpe_max: 2.861
redundancy_cluster: 13
negated_best_sharpe: 0.67
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: 0.07
---
# fnd6_cptmfmq_oibdpq (fundamental6)

*Operating Income Before Depreciation - Quarterly*

## Signal Profile
- `rank(fnd6_cptmfmq_oibdpq)`: S=0.40, F=0.26, T=2.4%, INFERIOR (TOP3000)
- `rank(fnd6_cptmfmq_oibdpq / close)`: S=0.60, F=0.45, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptmfmq_oibdpq, 5))`: S=-0.09, F=-0.02, T=39.6%, INFERIOR (TOP200)
- `-rank(fnd6_cptmfmq_oibdpq)`: S=-0.18, F=-0.08, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_oibdpq, 5))`: S=0.67, F=0.20, T=38.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cptmfmq_oibdpq, 22)`: S=0.51, F=0.19, T=38.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptmfmq_oibdpq, 10)`: S=0.25, F=0.12, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptmfmq_oibdpq, 22))`: S=0.24, F=0.06, T=17.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_oibdpq)`: S=-0.40, F=-0.26, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_oibdpq / close)`: S=-0.60, F=-0.45, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.18 (weak), ret=+0.8%
  - 2020: S=-2.43 (negative), ret=-17.0%
  - 2021: S=1.51 (strong), ret=+21.8%
  - 2022: S=1.63 (strong), ret=+28.2%
  - 2023: S=0.03 (weak), ret=+0.3%

## Risk & Drawdown
- Max drawdown: 29.20% over 779 days (recovered)
- Annualized: return +7.0%, volatility 11.8% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.06, excess kurtosis +1.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.46, max 2.86, latest -0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +11.43%; worst month: -5.75%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.37
- Sideways: S=0.67
- Bear: S=-3.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptmfmq_oibdpq, 5))` S=0.67, F=0.20, INFERIOR
Direction gap: +0.07 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptmfmq_oibdpq)`: S=-0.40, F=-0.26, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptmfmq_oibdpq / close)`: S=-0.60, F=-0.45, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptmfmq_oibdpq, 5))`: S=0.67, F=0.20, T=38.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cptmfmq_oibdpq / close)` | TOP3000 | 0.59 | 0.45 | 29.2% | 80% | bull-only |
| `rank(fnd6_cptmfmq_oibdpq)` | TOP3000 | 0.39 | 0.26 | 41.9% | 60% | bull-only |
| `rank(fnd6_cptmfmq_oibdpq / close)` | TOP1000 | 0.22 | 0.11 | 35.3% | 60% | bull-only |
| `rank(fnd6_cptmfmq_oibdpq)` | TOP1000 | 0.17 | 0.08 | 45.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_oibdpq: 1.000 (strongly positively correlated)
- anl4_ebitda_value: 0.983 (strongly positively correlated)
- ebitda_reported_value: 0.983 (strongly positively correlated)
- fnd6_cptnewqv1300_oiadpq: 0.977 (strongly positively correlated)
- operating_income: 0.977 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
