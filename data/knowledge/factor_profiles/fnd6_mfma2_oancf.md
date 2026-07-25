---
field: fnd6_mfma2_oancf
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.63
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.2329
ann_vol: 0.1062
hit_rate: 0.5101
rolling_sharpe_min: -2.603
rolling_sharpe_max: 2.549
redundancy_cluster: 13
negated_best_sharpe: 0.09
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.54
---
# fnd6_mfma2_oancf (fundamental6)

*Operating Activities - Net Cash Flow*

## Signal Profile
- `rank(fnd6_mfma2_oancf)`: S=0.35, F=0.21, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_mfma2_oancf / close)`: S=0.63, F=0.46, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mfma2_oancf, 5))`: S=0.60, F=0.28, T=34.4%, INFERIOR (TOP1000)
- `-rank(fnd6_mfma2_oancf)`: S=-0.19, F=-0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma2_oancf, 5))`: S=-0.03, F=0.00, T=32.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_mfma2_oancf, 22)`: S=0.37, F=0.20, T=27.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma2_oancf, 10)`: S=0.29, F=0.14, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma2_oancf, 22))`: S=-0.35, F=-0.15, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_oancf)`: S=0.09, F=0.03, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_oancf / close)`: S=0.07, F=0.02, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/2P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.62, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.05 (negative), ret=-0.2%
  - 2020: S=-1.50 (negative), ret=-11.3%
  - 2021: S=1.25 (moderate), ret=+16.9%
  - 2022: S=1.70 (strong), ret=+24.9%
  - 2023: S=0.23 (weak), ret=+1.9%

## Risk & Drawdown
- Max drawdown: 23.29% over 756 days (recovered)
- Annualized: return +6.6%, volatility 10.6% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.05, excess kurtosis +1.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.60, max 2.55, latest 0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.27%; worst month: -4.93%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.24
- Sideways: S=0.91
- Bear: S=-3.14

## Negated Direction
Best negated: `rank(-1 * fnd6_mfma2_oancf)` S=0.09, F=0.03, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_mfma2_oancf)`: S=0.09, F=0.03, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_oancf / close)`: S=0.07, F=0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma2_oancf, 5))`: S=-0.03, F=0.00, T=32.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfma2_oancf / close)` | TOP3000 | 0.62 | 0.46 | 23.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma2_oancf, 5))` | TOP1000 | 0.61 | 0.28 | 22.7% | 80% | bull-only |
| `rank(fnd6_mfma2_oancf)` | TOP3000 | 0.34 | 0.21 | 37.8% | 60% | bull-only |
| `rank(fnd6_mfma2_oancf / close)` | TOP1000 | 0.34 | 0.20 | 26.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma2_oancf, 5))` | TOP500 | 0.38 | 0.17 | 47.5% | 80% | mixed |
| `rank(ts_delta(fnd6_mfma2_oancf, 5))` | TOP3000 | 0.48 | 0.16 | 19.3% | 100% | bull-only |
| `rank(fnd6_mfma2_oancf / close)` | TOP500 | 0.18 | 0.09 | 42.6% | 40% | bull-only |
| `rank(fnd6_mfma2_oancf)` | TOP1000 | 0.17 | 0.09 | 40.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma2_oancf, 5))` | TOP200 | 0.15 | 0.05 | 41.5% | 20% | weak |
| `rank(fnd6_mfma2_oancf)` | TOP500 | 0.09 | 0.03 | 51.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cashflow_op: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_oancf: 1.000 (strongly positively correlated)
- ebitda: 0.987 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.987 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.987 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
