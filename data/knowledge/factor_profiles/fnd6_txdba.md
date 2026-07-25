---
field: fnd6_txdba
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.56
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2012
ann_vol: 0.0779
hit_rate: 0.5109
rolling_sharpe_min: -2.911
rolling_sharpe_max: 2.542
redundancy_cluster: 13
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: 0.02
---
# fnd6_txdba (fundamental6)

*Deferred Tax Asset - Long Term*

## Signal Profile
- `rank(fnd6_txdba)`: S=0.44, F=0.24, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_txdba / close)`: S=0.54, F=0.31, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txdba, 5))`: S=0.40, F=0.15, T=35.7%, INFERIOR (TOP3000)
- `-rank(fnd6_txdba)`: S=-0.35, F=-0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdba, 5))`: S=0.56, F=0.37, T=27.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txdba, 63)`: S=-0.19, F=-0.08, T=18.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txdba, 10)`: S=-0.05, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txdba, 22))`: S=-0.63, F=-0.39, T=16.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdba)`: S=0.08, F=0.03, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdba / close)`: S=-0.04, F=-0.01, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.54, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-0.5%
  - 2020: S=-2.05 (negative), ret=-11.2%
  - 2021: S=1.38 (moderate), ret=+14.2%
  - 2022: S=1.68 (strong), ret=+17.5%
  - 2023: S=0.10 (weak), ret=+0.6%

## Risk & Drawdown
- Max drawdown: 20.12% over 785 days (recovered)
- Annualized: return +4.2%, volatility 7.8% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.04, excess kurtosis +2.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.91, max 2.54, latest -0.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.34%; worst month: -3.41%
Positive months: 44%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.27
- Sideways: S=0.48
- Bear: S=-3.03

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txdba, 5))` S=0.56, F=0.37, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txdba)`: S=0.08, F=0.03, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdba / close)`: S=-0.04, F=-0.01, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdba, 5))`: S=0.56, F=0.37, T=27.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txdba / close)` | TOP3000 | 0.54 | 0.31 | 20.1% | 60% | bull-only |
| `rank(fnd6_txdba / close)` | TOP1000 | 0.48 | 0.30 | 19.3% | 40% | bull-only |
| `rank(fnd6_txdba)` | TOP3000 | 0.43 | 0.24 | 26.9% | 80% | bull-only |
| `rank(fnd6_txdba)` | TOP1000 | 0.34 | 0.19 | 27.6% | 40% | bull-only |
| `rank(ts_delta(fnd6_txdba, 5))` | TOP3000 | 0.40 | 0.15 | 11.4% | 80% | weak |
| `rank(fnd6_txdba / close)` | TOP500 | 0.22 | 0.10 | 39.2% | 60% | bull-only |
| `rank(fnd6_txdba)` | TOP500 | 0.16 | 0.07 | 47.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_txdbaq: 0.984 (strongly positively correlated)
- fnd6_mfma2_oancf: 0.948 (strongly positively correlated)
- cashflow_op: 0.948 (strongly positively correlated)
- fnd6_newa2v1300_oancf: 0.948 (strongly positively correlated)
- ebitda: 0.947 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
