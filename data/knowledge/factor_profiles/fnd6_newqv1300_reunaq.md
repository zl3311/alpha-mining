---
field: fnd6_newqv1300_reunaq
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 0.45
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1926
ann_vol: 0.1581
hit_rate: 0.4915
rolling_sharpe_min: -1.8
rolling_sharpe_max: 2.203
negated_best_sharpe: 0.45
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.14
---
# fnd6_newqv1300_reunaq (fundamental6)

*Unadjusted Retained Earnings*

## Signal Profile
- `rank(fnd6_newqv1300_reunaq)`: S=0.08, F=0.02, T=2.8%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_reunaq / close)`: S=0.22, F=0.10, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_reunaq, 5))`: S=0.46, F=0.19, T=41.8%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_reunaq)`: S=0.01, F=0.00, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_reunaq, 5))`: S=-0.39, F=-0.15, T=41.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_reunaq, 22)`: S=0.59, F=0.26, T=42.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_reunaq, 10)`: S=-0.03, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_reunaq, 22))`: S=0.40, F=0.16, T=18.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_reunaq)`: S=0.40, F=0.26, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_reunaq / close)`: S=0.45, F=0.32, T=5.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.47, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.61 (negative), ret=-16.3%
  - 2020: S=1.30 (moderate), ret=+19.9%
  - 2021: S=0.03 (weak), ret=+0.6%
  - 2022: S=1.98 (strong), ret=+37.2%
  - 2023: S=-0.38 (negative), ret=-5.3%

## Risk & Drawdown
- Max drawdown: 19.26% over 458 days (recovered)
- Annualized: return +7.4%, volatility 15.8% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.28, excess kurtosis +3.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.80, max 2.20, latest -0.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +9.44%; worst month: -7.30%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.11
- Sideways: S=-0.02
- Bear: S=0.25

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_reunaq / close)` S=0.45, F=0.32, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_reunaq)`: S=0.40, F=0.26, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_reunaq / close)`: S=0.45, F=0.32, T=5.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_reunaq, 5))`: S=-0.39, F=-0.15, T=41.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_reunaq, 5))` | TOP200 | 0.47 | 0.19 | 19.3% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_reunaq, 5))` | TOP500 | 0.40 | 0.14 | 21.2% | 40% | mixed |
| `rank(fnd6_newqv1300_reunaq / close)` | TOP3000 | 0.21 | 0.10 | 37.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_reunaq, 5))` | TOP3000 | 0.26 | 0.06 | 22.9% | 40% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_reunaq, 5))` | TOP1000 | 0.21 | 0.05 | 23.8% | 60% | bull-only |
| `rank(fnd6_newqv1300_reunaq)` | TOP3000 | 0.07 | 0.02 | 38.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- retained_earnings: 0.451 (moderately positively correlated)
- fnd6_cptnewqv1300_req: 0.451 (moderately positively correlated)
- fnd6_cptnewqv1300_epsx12: 0.400 (weakly positively correlated)
- fnd6_cptnewqv1300_epsf12: 0.352 (weakly positively correlated)
- fnd6_newa2v1300_re: 0.274 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
