---
field: fnd6_txc
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.67
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2241
ann_vol: 0.0982
hit_rate: 0.5004
rolling_sharpe_min: -2.712
rolling_sharpe_max: 2.436
redundancy_cluster: 13
negated_best_sharpe: 0.71
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: 0.04
---
# fnd6_txc (fundamental6)

*Income Taxes - Current*

## Signal Profile
- `rank(fnd6_txc)`: S=0.35, F=0.20, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_txc / close)`: S=0.53, F=0.34, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txc, 5))`: S=-0.02, F=0.00, T=33.2%, INFERIOR (TOP500)
- `-rank(fnd6_txc)`: S=-0.04, F=-0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txc, 5))`: S=0.71, F=0.41, T=41.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txc, 63)`: S=0.67, F=0.53, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txc, 10)`: S=-0.02, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txc, 22))`: S=-0.90, F=-0.65, T=20.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txc)`: S=-0.04, F=-0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txc / close)`: S=-0.14, F=-0.05, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.52, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.09 (weak), ret=+0.4%
  - 2020: S=-1.66 (negative), ret=-11.5%
  - 2021: S=1.17 (moderate), ret=+13.4%
  - 2022: S=1.50 (strong), ret=+21.4%
  - 2023: S=0.14 (weak), ret=+1.1%

## Risk & Drawdown
- Max drawdown: 22.41% over 770 days (recovered)
- Annualized: return +5.1%, volatility 9.8% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.04, excess kurtosis +1.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.71, max 2.44, latest -0.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.48%; worst month: -4.69%
Positive months: 46%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.85
- Sideways: S=0.90
- Bear: S=-2.99

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txc, 5))` S=0.71, F=0.41, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txc)`: S=-0.04, F=-0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txc / close)`: S=-0.14, F=-0.05, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txc, 5))`: S=0.71, F=0.41, T=41.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txc / close)` | TOP3000 | 0.52 | 0.34 | 22.4% | 80% | bull-only |
| `rank(fnd6_txc)` | TOP3000 | 0.34 | 0.20 | 35.4% | 60% | bull-only |
| `rank(fnd6_txc / close)` | TOP1000 | 0.12 | 0.05 | 26.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_curritxexp: 0.969 (strongly positively correlated)
- ebitda: 0.961 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.961 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.961 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.960 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
