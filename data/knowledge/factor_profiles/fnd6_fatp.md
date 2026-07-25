---
field: fnd6_fatp
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.71
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2483
ann_vol: 0.116
hit_rate: 0.5004
rolling_sharpe_min: -2.388
rolling_sharpe_max: 2.827
redundancy_cluster: 13
negated_best_sharpe: 0.44
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.27
---
# fnd6_fatp (fundamental6)

*Plant, Property and Equipment at Cost - Land & Improvements*

## Signal Profile
- `rank(fnd6_fatp)`: S=0.55, F=0.41, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_fatp / close)`: S=0.66, F=0.51, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_fatp, 5))`: S=0.11, F=0.03, T=28.5%, INFERIOR (TOP500)
- `-rank(fnd6_fatp)`: S=-0.33, F=-0.20, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fatp, 5))`: S=0.44, F=0.20, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_fatp, 22)`: S=0.71, F=0.58, T=14.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_fatp, 10)`: S=0.46, F=0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fatp, 22))`: S=-0.23, F=-0.09, T=21.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatp)`: S=-0.33, F=-0.20, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatp / close)`: S=-0.32, F=-0.19, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.65, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.32 (negative), ret=-1.6%
  - 2020: S=-1.79 (negative), ret=-13.8%
  - 2021: S=1.76 (strong), ret=+26.1%
  - 2022: S=1.33 (moderate), ret=+22.2%
  - 2023: S=0.48 (weak), ret=+3.9%

## Risk & Drawdown
- Max drawdown: 24.83% over 666 days (recovered)
- Annualized: return +7.5%, volatility 11.6% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.04, excess kurtosis +2.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.39, max 2.83, latest 0.30

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +8.79%; worst month: -3.41%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.86
- Sideways: S=0.82
- Bear: S=-2.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_fatp, 5))` S=0.44, F=0.20, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_fatp)`: S=-0.33, F=-0.20, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fatp / close)`: S=-0.32, F=-0.19, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fatp, 5))`: S=0.44, F=0.20, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_fatp / close)` | TOP3000 | 0.65 | 0.51 | 24.8% | 60% | bull-only |
| `rank(fnd6_fatp)` | TOP3000 | 0.54 | 0.41 | 35.0% | 80% | bull-only |
| `rank(fnd6_fatp)` | TOP1000 | 0.32 | 0.20 | 38.4% | 40% | bull-only |
| `rank(fnd6_fatp / close)` | TOP1000 | 0.31 | 0.19 | 31.7% | 40% | bull-only |
| `rank(fnd6_fatp / close)` | TOP500 | 0.24 | 0.14 | 41.3% | 40% | bull-only |
| `rank(fnd6_fatp)` | TOP500 | 0.24 | 0.13 | 51.8% | 40% | bull-only |
| `rank(ts_delta(fnd6_fatp, 5))` | TOP500 | 0.11 | 0.03 | 31.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_fatb: 0.962 (strongly positively correlated)
- fnd6_txtubxintbs: 0.939 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.933 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.933 (strongly positively correlated)
- ebitda: 0.932 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
