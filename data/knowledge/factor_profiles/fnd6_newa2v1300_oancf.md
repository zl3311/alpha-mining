---
field: fnd6_newa2v1300_oancf
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.62
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.2374
ann_vol: 0.1061
hit_rate: 0.5061
rolling_sharpe_min: -2.66
rolling_sharpe_max: 2.544
redundancy_cluster: 13
negated_best_sharpe: 0.09
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.53
---
# fnd6_newa2v1300_oancf (fundamental6)

*Operating Activities - Net Cash Flow*

## Signal Profile
- `rank(fnd6_newa2v1300_oancf)`: S=0.35, F=0.20, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_oancf / close)`: S=0.62, F=0.45, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_oancf, 5))`: S=0.59, F=0.28, T=34.5%, INFERIOR (TOP1000)
- `-rank(fnd6_newa2v1300_oancf)`: S=-0.20, F=-0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_oancf, 5))`: S=-0.01, F=0.00, T=32.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_oancf, 22)`: S=0.38, F=0.20, T=27.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_oancf, 10)`: S=0.31, F=0.16, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_oancf, 22))`: S=-0.35, F=-0.15, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_oancf)`: S=0.09, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_oancf / close)`: S=0.05, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/2P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.61, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.3%
  - 2020: S=-1.55 (negative), ret=-11.6%
  - 2021: S=1.23 (moderate), ret=+16.7%
  - 2022: S=1.73 (strong), ret=+25.3%
  - 2023: S=0.22 (weak), ret=+1.9%

## Risk & Drawdown
- Max drawdown: 23.74% over 772 days (recovered)
- Annualized: return +6.5%, volatility 10.6% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.05, excess kurtosis +1.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.66, max 2.54, latest 0.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.30%; worst month: -5.00%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.23
- Sideways: S=0.90
- Bear: S=-3.14

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_oancf)` S=0.09, F=0.03, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_oancf)`: S=0.09, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_oancf / close)`: S=0.05, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_oancf, 5))`: S=-0.01, F=0.00, T=32.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_oancf / close)` | TOP3000 | 0.61 | 0.45 | 23.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_oancf, 5))` | TOP1000 | 0.61 | 0.28 | 22.9% | 80% | bull-only |
| `rank(fnd6_newa2v1300_oancf / close)` | TOP1000 | 0.35 | 0.22 | 26.2% | 60% | bull-only |
| `rank(fnd6_newa2v1300_oancf)` | TOP3000 | 0.34 | 0.20 | 38.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_oancf, 5))` | TOP500 | 0.39 | 0.18 | 50.3% | 80% | weak |
| `rank(ts_delta(fnd6_newa2v1300_oancf, 5))` | TOP3000 | 0.45 | 0.15 | 20.9% | 80% | bull-only |
| `rank(fnd6_newa2v1300_oancf / close)` | TOP500 | 0.19 | 0.10 | 42.5% | 40% | bull-only |
| `rank(fnd6_newa2v1300_oancf)` | TOP1000 | 0.19 | 0.09 | 40.5% | 60% | bull-only |
| `rank(fnd6_newa2v1300_oancf)` | TOP500 | 0.10 | 0.04 | 51.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_oancf, 5))` | TOP200 | 0.10 | 0.02 | 44.4% | 20% | weak |

## Correlation Notes
Top correlates:
- cashflow_op: 1.000 (strongly positively correlated)
- fnd6_mfma2_oancf: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.987 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.987 (strongly positively correlated)
- ebitda: 0.987 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
