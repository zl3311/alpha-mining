---
field: fnd6_newqv1300_lol2q
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.73
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1
ann_vol: 0.0625
hit_rate: 0.5045
rolling_sharpe_min: -1.509
rolling_sharpe_max: 2.543
redundancy_cluster: 13
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.17
---
# fnd6_newqv1300_lol2q (fundamental6)

*Liabilities Level 2 (Observable)*

## Signal Profile
- `rank(fnd6_newqv1300_lol2q)`: S=0.67, F=0.41, T=6.8%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_lol2q / close)`: S=0.73, F=0.44, T=6.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_lol2q, 5))`: S=0.30, F=0.07, T=51.2%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_lol2q)`: S=-0.25, F=-0.10, T=8.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lol2q, 5))`: S=0.56, F=0.23, T=59.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_lol2q, 22)`: S=0.04, F=0.01, T=39.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_lol2q, 10)`: S=0.02, F=0.00, T=6.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_lol2q, 22))`: S=-1.05, F=-0.55, T=23.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lol2q)`: S=0.09, F=0.02, T=9.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lol2q / close)`: S=0.05, F=0.01, T=9.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.73, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.72 (moderate), ret=+2.6%
  - 2020: S=-0.89 (negative), ret=-4.3%
  - 2021: S=1.50 (strong), ret=+11.9%
  - 2022: S=0.99 (moderate), ret=+8.1%
  - 2023: S=0.88 (moderate), ret=+4.1%

## Risk & Drawdown
- Max drawdown: 10.00% over 533 days (recovered)
- Annualized: return +4.6%, volatility 6.2% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.05, excess kurtosis +2.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.51, max 2.54, latest 0.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.19%; worst month: -2.60%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.92
- Sideways: S=1.29
- Bear: S=-2.74

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_lol2q, 5))` S=0.56, F=0.23, INFERIOR
Direction gap: -0.17 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_lol2q)`: S=0.09, F=0.02, T=9.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_lol2q / close)`: S=0.05, F=0.01, T=9.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_lol2q, 5))`: S=0.56, F=0.23, T=59.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_lol2q / close)` | TOP3000 | 0.73 | 0.44 | 10.0% | 80% | bull-only |
| `rank(fnd6_newqv1300_lol2q)` | TOP3000 | 0.67 | 0.41 | 15.5% | 80% | bull-only |
| `rank(fnd6_newqv1300_lol2q / close)` | TOP1000 | 0.25 | 0.10 | 17.6% | 40% | bull-only |
| `rank(fnd6_newqv1300_lol2q)` | TOP1000 | 0.24 | 0.10 | 21.6% | 40% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_lol2q, 5))` | TOP3000 | 0.33 | 0.07 | 15.8% | 60% | bear-only |

## Correlation Notes
Top correlates:
- ebitda: 0.892 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.892 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.892 (strongly positively correlated)
- operating_profit_before_depr_amort: 0.891 (strongly positively correlated)
- fnd6_newa2v1300_txdb: 0.887 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
