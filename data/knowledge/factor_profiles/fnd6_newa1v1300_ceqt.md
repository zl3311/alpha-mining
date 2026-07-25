---
field: fnd6_newa1v1300_ceqt
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.45
best_fitness: 0.17
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1175
ann_vol: 0.0399
hit_rate: 0.5166
rolling_sharpe_min: -2.168
rolling_sharpe_max: 3.4
negated_best_sharpe: 0.45
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.01
---
# fnd6_newa1v1300_ceqt (fundamental6)

*Common Equity - Tangible*

## Signal Profile
- `rank(fnd6_newa1v1300_ceqt)`: S=0.44, F=0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_ceqt / close)`: S=0.13, F=0.03, T=2.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa1v1300_ceqt, 5))`: S=0.00, F=0.00, T=30.6%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_ceqt)`: S=-0.35, F=-0.12, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ceqt, 5))`: S=0.45, F=0.17, T=39.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_ceqt, 63)`: S=0.14, F=0.05, T=20.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_ceqt, 10)`: S=0.04, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_ceqt, 22))`: S=-0.69, F=-0.42, T=18.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ceqt)`: S=-0.44, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ceqt / close)`: S=-0.02, F=0.00, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.44, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.2%
  - 2020: S=-1.59 (negative), ret=-7.2%
  - 2021: S=0.53 (moderate), ret=+2.5%
  - 2022: S=1.28 (moderate), ret=+4.8%
  - 2023: S=2.55 (strong), ret=+8.7%

## Risk & Drawdown
- Max drawdown: 11.75% over 1028 days (recovered)
- Annualized: return +1.8%, volatility 4.0% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.16, excess kurtosis +1.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.17, max 3.40, latest 2.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +2.36%; worst month: -4.08%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.48
- Sideways: S=1.18
- Bear: S=-1.28

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_ceqt, 5))` S=0.45, F=0.17, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_ceqt)`: S=-0.44, F=-0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_ceqt / close)`: S=-0.02, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_ceqt, 5))`: S=0.45, F=0.17, T=39.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_ceqt)` | TOP3000 | 0.44 | 0.16 | 11.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ceqt)` | TOP1000 | 0.35 | 0.12 | 9.9% | 60% | bull-only |
| `rank(fnd6_newa1v1300_ceqt)` | TOP500 | 0.26 | 0.08 | 11.8% | 60% | mixed |
| `rank(fnd6_newa1v1300_ceqt / close)` | TOP1000 | 0.12 | 0.03 | 7.3% | 60% | mixed |
| `rank(fnd6_newa1v1300_ceqt / close)` | TOP500 | 0.12 | 0.03 | 9.0% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_ivstq: 0.769 (strongly positively correlated)
- fnd6_newqv1300_wcapq: 0.739 (strongly positively correlated)
- working_capital: 0.739 (strongly positively correlated)
- fnd6_newa2v1300_wcap: 0.731 (strongly positively correlated)
- fnd6_tfva: 0.724 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
