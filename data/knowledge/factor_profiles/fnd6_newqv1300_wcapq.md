---
field: fnd6_newqv1300_wcapq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.53
best_fitness: 0.28
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2391
ann_vol: 0.0664
hit_rate: 0.515
rolling_sharpe_min: -3.261
rolling_sharpe_max: 3.275
redundancy_cluster: 17
negated_best_sharpe: 0.2
negated_best_template: neg_rank_level
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.33
---
# fnd6_newqv1300_wcapq (fundamental6)

*Working Capital (Balance Sheet)*

## Signal Profile
- `rank(fnd6_newqv1300_wcapq)`: S=0.53, F=0.28, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_wcapq / close)`: S=0.50, F=0.25, T=3.0%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_wcapq, 5))`: S=0.56, F=0.22, T=36.9%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_wcapq)`: S=-0.13, F=-0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_wcapq, 5))`: S=-0.05, F=-0.01, T=37.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_wcapq, 22)`: S=0.66, F=0.27, T=38.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_wcapq, 10)`: S=0.31, F=0.14, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_wcapq, 22))`: S=-0.10, F=-0.02, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_wcapq)`: S=0.20, F=0.08, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_wcapq / close)`: S=0.09, F=0.02, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.57 (moderate), ret=+2.0%
  - 2020: S=-1.60 (negative), ret=-9.3%
  - 2021: S=0.34 (weak), ret=+3.5%
  - 2022: S=1.98 (strong), ret=+11.3%
  - 2023: S=1.80 (strong), ret=+9.6%

## Risk & Drawdown
- Max drawdown: 23.91% over 917 days (recovered)
- Annualized: return +3.5%, volatility 6.6% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.05, excess kurtosis +2.56

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.26, max 3.27, latest 1.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.06%; worst month: -6.41%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.80
- Sideways: S=1.23
- Bear: S=-2.70

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_wcapq)` S=0.20, F=0.08, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_wcapq)`: S=0.20, F=0.08, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_wcapq / close)`: S=0.09, F=0.02, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_wcapq, 5))`: S=-0.05, F=-0.01, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_wcapq)` | TOP3000 | 0.53 | 0.28 | 23.9% | 80% | bull-only |
| `rank(fnd6_newqv1300_wcapq / close)` | TOP500 | 0.50 | 0.25 | 7.8% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_wcapq, 5))` | TOP500 | 0.58 | 0.22 | 23.3% | 80% | mixed |
| `rank(fnd6_newqv1300_wcapq)` | TOP500 | 0.30 | 0.12 | 16.7% | 40% | bull-only |
| `rank(fnd6_newqv1300_wcapq / close)` | TOP3000 | 0.26 | 0.11 | 13.6% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_wcapq, 5))` | TOP3000 | 0.26 | 0.05 | 14.9% | 60% | mixed |
| `rank(fnd6_newqv1300_wcapq / close)` | TOP1000 | 0.12 | 0.03 | 11.7% | 60% | mixed |
| `rank(fnd6_newqv1300_wcapq)` | TOP1000 | 0.12 | 0.03 | 17.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- working_capital: 1.000 (strongly positively correlated)
- fnd6_newa2v1300_wcap: 0.967 (strongly positively correlated)
- cash: 0.950 (strongly positively correlated)
- fnd6_cptnewqv1300_actq: 0.914 (strongly positively correlated)
- assets_curr: 0.914 (strongly positively correlated)

Redundancy cluster #17: 12 similar fields, mean |rho| 0.768 (representative: fnd6_newqv1300_aol2q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
