---
field: fnd6_newa2v1300_wcap
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.77
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2273
ann_vol: 0.066
hit_rate: 0.5166
rolling_sharpe_min: -3.155
rolling_sharpe_max: 3.048
redundancy_cluster: 17
negated_best_sharpe: 0.22
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.55
---
# fnd6_newa2v1300_wcap (fundamental6)

*Working Capital (Balance Sheet)*

## Signal Profile
- `rank(fnd6_newa2v1300_wcap)`: S=0.72, F=0.44, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_wcap / close)`: S=0.63, F=0.34, T=2.0%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa2v1300_wcap, 5))`: S=0.25, F=0.07, T=35.5%, INFERIOR (TOP3000)
- `-rank(fnd6_newa2v1300_wcap)`: S=-0.30, F=-0.12, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_wcap, 5))`: S=0.22, F=0.07, T=33.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_wcap, 22)`: S=0.77, F=0.58, T=26.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_wcap, 10)`: S=0.40, F=0.21, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_wcap, 22))`: S=-0.59, F=-0.34, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_wcap)`: S=-0.41, F=-0.19, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_wcap / close)`: S=-0.63, F=-0.34, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.73, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.90 (moderate), ret=+3.2%
  - 2020: S=-1.76 (negative), ret=-10.0%
  - 2021: S=0.83 (moderate), ret=+8.6%
  - 2022: S=2.01 (strong), ret=+11.8%
  - 2023: S=2.09 (strong), ret=+10.0%

## Risk & Drawdown
- Max drawdown: 22.73% over 792 days (recovered)
- Annualized: return +4.8%, volatility 6.6% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.07, excess kurtosis +2.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.15, max 3.05, latest 1.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +5.03%; worst month: -4.95%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.85
- Sideways: S=1.36
- Bear: S=-2.36

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_wcap, 5))` S=0.22, F=0.07, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_wcap)`: S=-0.41, F=-0.19, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_wcap / close)`: S=-0.63, F=-0.34, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_wcap, 5))`: S=0.22, F=0.07, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_wcap)` | TOP3000 | 0.73 | 0.44 | 22.7% | 80% | bull-only |
| `rank(fnd6_newa2v1300_wcap / close)` | TOP500 | 0.63 | 0.34 | 6.5% | 80% | mixed |
| `rank(fnd6_newa2v1300_wcap / close)` | TOP3000 | 0.52 | 0.29 | 10.6% | 80% | all-weather |
| `rank(fnd6_newa2v1300_wcap)` | TOP500 | 0.41 | 0.19 | 16.7% | 40% | bull-only |
| `rank(fnd6_newa2v1300_wcap)` | TOP1000 | 0.30 | 0.12 | 15.4% | 60% | bull-only |
| `rank(fnd6_newa2v1300_wcap / close)` | TOP1000 | 0.27 | 0.10 | 7.6% | 80% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_wcap, 5))` | TOP3000 | 0.25 | 0.07 | 32.6% | 80% | weak |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_wcapq: 0.967 (strongly positively correlated)
- working_capital: 0.967 (strongly positively correlated)
- cash: 0.941 (strongly positively correlated)
- fnd6_newa1v1300_act: 0.920 (strongly positively correlated)
- fnd6_cptnewqv1300_actq: 0.916 (strongly positively correlated)

Redundancy cluster #17: 12 similar fields, mean |rho| 0.768 (representative: fnd6_newqv1300_aol2q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
