---
field: fnd6_newa1v1300_ebitda
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.59
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2403
ann_vol: 0.1211
hit_rate: 0.4988
rolling_sharpe_min: -2.183
rolling_sharpe_max: 2.416
redundancy_cluster: 13
negated_best_sharpe: 0.22
negated_best_template: neg_rank_level
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.37
---
# fnd6_newa1v1300_ebitda (fundamental6)

*Earnings Before Interest*

## Signal Profile
- `rank(fnd6_newa1v1300_ebitda)`: S=0.31, F=0.18, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ebitda / close)`: S=0.59, F=0.44, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_ebitda, 5))`: S=0.65, F=0.39, T=34.6%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_ebitda)`: S=-0.13, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ebitda, 5))`: S=-0.69, F=-0.42, T=34.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_ebitda, 22)`: S=-0.05, F=-0.01, T=30.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ebitda, 10)`: S=0.16, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ebitda, 22))`: S=0.13, F=0.03, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ebitda)`: S=0.22, F=0.12, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ebitda / close)`: S=0.17, F=0.08, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.06 (weak), ret=+0.3%
  - 2020: S=-1.23 (negative), ret=-11.0%
  - 2021: S=1.21 (moderate), ret=+18.2%
  - 2022: S=1.48 (moderate), ret=+25.2%
  - 2023: S=0.17 (weak), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 24.03% over 770 days (recovered)
- Annualized: return +7.0%, volatility 12.1% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.02, excess kurtosis +1.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.18, max 2.42, latest -0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.24%; worst month: -5.01%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.13
- Sideways: S=0.71
- Bear: S=-2.96

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_ebitda)` S=0.22, F=0.12, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ebitda)`: S=0.22, F=0.12, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ebitda / close)`: S=0.17, F=0.08, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ebitda, 5))`: S=-0.69, F=-0.42, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_ebitda / close)` | TOP3000 | 0.58 | 0.44 | 24.0% | 80% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_ebitda, 5))` | TOP200 | 0.65 | 0.39 | 25.6% | 80% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_ebitda, 5))` | TOP1000 | 0.68 | 0.31 | 14.3% | 80% | mixed |
| `rank(fnd6_newa1v1300_ebitda / close)` | TOP1000 | 0.30 | 0.19 | 28.1% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ebitda)` | TOP3000 | 0.30 | 0.18 | 41.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_ebitda, 5))` | TOP500 | 0.27 | 0.10 | 19.4% | 80% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_ebitda, 5))` | TOP3000 | 0.29 | 0.08 | 10.2% | 80% | mixed |
| `rank(fnd6_newa1v1300_ebitda)` | TOP1000 | 0.12 | 0.05 | 44.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_oibdp: 1.000 (strongly positively correlated)
- ebitda: 1.000 (strongly positively correlated)
- fnd6_mfma2_oancf: 0.987 (strongly positively correlated)
- cashflow_op: 0.987 (strongly positively correlated)
- fnd6_newa2v1300_oancf: 0.987 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
