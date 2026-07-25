---
field: fnd6_newqv1300_txdbaq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.79
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2221
ann_vol: 0.0829
hit_rate: 0.5045
rolling_sharpe_min: -3.044
rolling_sharpe_max: 2.632
redundancy_cluster: 13
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.21
---
# fnd6_newqv1300_txdbaq (fundamental6)

*Deferred Tax Asset - Long Term*

## Signal Profile
- `rank(fnd6_newqv1300_txdbaq)`: S=0.49, F=0.29, T=3.7%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_txdbaq / close)`: S=0.53, F=0.31, T=3.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_txdbaq, 5))`: S=0.27, F=0.06, T=38.8%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_txdbaq)`: S=-0.32, F=-0.17, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txdbaq, 5))`: S=0.58, F=0.23, T=39.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_txdbaq, 22)`: S=0.79, F=0.52, T=39.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_txdbaq, 10)`: S=-0.16, F=-0.06, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_txdbaq, 22))`: S=0.32, F=0.10, T=17.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txdbaq)`: S=-0.32, F=-0.17, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txdbaq / close)`: S=-0.40, F=-0.23, T=5.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.53, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.12 (negative), ret=-0.4%
  - 2020: S=-2.25 (negative), ret=-13.5%
  - 2021: S=1.56 (strong), ret=+17.0%
  - 2022: S=1.73 (strong), ret=+19.0%
  - 2023: S=-0.11 (negative), ret=-0.7%

## Risk & Drawdown
- Max drawdown: 22.21% over 776 days (recovered)
- Annualized: return +4.4%, volatility 8.3% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.02, excess kurtosis +2.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.04, max 2.63, latest -0.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.88%; worst month: -3.57%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.34
- Sideways: S=0.38
- Bear: S=-3.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_txdbaq, 5))` S=0.58, F=0.23, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_txdbaq)`: S=-0.32, F=-0.17, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_txdbaq / close)`: S=-0.40, F=-0.23, T=5.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_txdbaq, 5))`: S=0.58, F=0.23, T=39.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_txdbaq / close)` | TOP3000 | 0.53 | 0.31 | 22.2% | 40% | bull-only |
| `rank(fnd6_newqv1300_txdbaq)` | TOP3000 | 0.48 | 0.29 | 27.3% | 60% | bull-only |
| `rank(fnd6_newqv1300_txdbaq / close)` | TOP1000 | 0.39 | 0.23 | 26.8% | 40% | bull-only |
| `rank(fnd6_newqv1300_txdbaq)` | TOP1000 | 0.31 | 0.17 | 33.9% | 40% | bull-only |
| `rank(fnd6_newqv1300_txdbaq / close)` | TOP500 | 0.19 | 0.08 | 48.4% | 60% | bull-only |
| `rank(fnd6_newqv1300_txdbaq)` | TOP500 | 0.17 | 0.07 | 54.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_txdbaq, 5))` | TOP3000 | 0.25 | 0.06 | 16.4% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_txdbaq, 5))` | TOP200 | 0.16 | 0.05 | 41.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txdba: 0.984 (strongly positively correlated)
- fnd6_mfma2_oancf: 0.940 (strongly positively correlated)
- cashflow_op: 0.940 (strongly positively correlated)
- fnd6_newa2v1300_oancf: 0.939 (strongly positively correlated)
- ebitda: 0.935 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
