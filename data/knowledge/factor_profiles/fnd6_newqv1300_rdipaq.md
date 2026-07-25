---
field: fnd6_newqv1300_rdipaq
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.52
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.423
ann_vol: 0.2056
hit_rate: 0.4866
rolling_sharpe_min: -1.091
rolling_sharpe_max: 1.761
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.43
n_negated_sims: 10
direction_gap: 0.34
---
# fnd6_newqv1300_rdipaq (fundamental6)

*In Process R&D Expense After-tax*

## Signal Profile
- `rank(fnd6_newqv1300_rdipaq)`: S=-0.20, F=-0.11, T=4.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_rdipaq / close)`: S=-0.19, F=-0.10, T=4.2%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_rdipaq, 5))`: S=0.18, F=0.08, T=24.9%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_rdipaq)`: S=0.26, F=0.15, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rdipaq, 5))`: S=-0.07, F=-0.02, T=20.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_rdipaq, 63)`: S=-0.10, F=-0.05, T=11.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_rdipaq, 10)`: S=-0.43, F=-0.34, T=3.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_rdipaq, 22))`: S=0.10, F=0.04, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipaq)`: S=0.52, F=0.43, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipaq / close)`: S=0.51, F=0.42, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 30F/2P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.20, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+7.6%
  - 2020: S=-0.20 (negative), ret=-5.6%
  - 2021: S=0.55 (moderate), ret=+11.7%
  - 2022: S=0.49 (weak), ret=+10.8%
  - 2023: S=-0.51 (negative), ret=-4.7%

## Risk & Drawdown
- Max drawdown: 42.30% over 673 days (recovered)
- Annualized: return +4.0%, volatility 20.6% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew -1.33, excess kurtosis +53.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 1.76, latest -0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +18.21%; worst month: -36.15%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.11
- Sideways: S=0.52
- Bear: S=-0.79

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_rdipaq)` S=0.52, F=0.43, INFERIOR
Direction gap: +0.34 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_rdipaq)`: S=0.52, F=0.43, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_rdipaq / close)`: S=0.51, F=0.42, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_rdipaq, 5))`: S=-0.07, F=-0.02, T=20.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_rdipaq, 5))` | TOP500 | 0.20 | 0.08 | 42.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_rdipaq, 5))` | TOP3000 | 0.18 | 0.08 | 58.3% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_rdipaq, 5))` | TOP200 | 0.15 | 0.06 | 45.5% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_rdipepsq: 0.856 (strongly positively correlated)
- fnd6_newqv1300_rdipq: 0.555 (moderately positively correlated)
- fnd6_newqv1300_rdipdq: 0.481 (moderately positively correlated)
- fnd6_mkvaltq: -0.170 (weakly negatively correlated)
- fnd6_txdbcl: 0.156 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
