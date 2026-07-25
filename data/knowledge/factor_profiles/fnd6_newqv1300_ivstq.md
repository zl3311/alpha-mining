---
field: fnd6_newqv1300_ivstq
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 1.03
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1268
ann_vol: 0.0447
hit_rate: 0.5085
rolling_sharpe_min: -1.619
rolling_sharpe_max: 2.583
negated_best_sharpe: 0.18
negated_best_template: neg_rank_level
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.85
---
# fnd6_newqv1300_ivstq (fundamental6)

*Short-Term Investments - Total*

## Signal Profile
- `rank(fnd6_newqv1300_ivstq)`: S=0.44, F=0.17, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_ivstq / close)`: S=0.37, F=0.13, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_ivstq, 5))`: S=0.01, F=0.00, T=38.5%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_ivstq)`: S=-0.07, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ivstq, 5))`: S=-0.07, F=-0.01, T=39.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_ivstq, 22)`: S=-0.20, F=-0.06, T=39.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_ivstq, 10)`: S=0.44, F=0.25, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_ivstq, 22))`: S=1.03, F=0.58, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ivstq)`: S=0.18, F=0.07, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ivstq / close)`: S=-0.01, F=0.00, T=4.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.46, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.48 (negative), ret=-1.3%
  - 2020: S=-0.49 (negative), ret=-2.5%
  - 2021: S=0.46 (weak), ret=+2.5%
  - 2022: S=0.97 (moderate), ret=+4.3%
  - 2023: S=1.91 (strong), ret=+7.0%

## Risk & Drawdown
- Max drawdown: 12.68% over 1226 days (recovered)
- Annualized: return +2.0%, volatility 4.5% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.04, excess kurtosis +1.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.62, max 2.58, latest 1.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +2.92%; worst month: -3.06%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.51
- Sideways: S=1.06
- Bear: S=-1.03

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_ivstq)` S=0.18, F=0.07, INFERIOR
Direction gap: -0.85 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_ivstq)`: S=0.18, F=0.07, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_ivstq / close)`: S=-0.01, F=0.00, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_ivstq, 5))`: S=-0.07, F=-0.01, T=39.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_ivstq)` | TOP3000 | 0.46 | 0.17 | 12.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_ivstq / close)` | TOP3000 | 0.38 | 0.13 | 5.4% | 60% | weak |
| `rank(fnd6_newqv1300_ivstq / close)` | TOP500 | 0.29 | 0.10 | 13.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_ivstq / close)` | TOP1000 | 0.21 | 0.06 | 8.0% | 80% | bull-only |
| `rank(fnd6_newqv1300_ivstq)` | TOP500 | 0.12 | 0.03 | 20.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ceqt: 0.769 (strongly positively correlated)
- fnd6_tfva: 0.715 (strongly positively correlated)
- fnd6_newqv1300_wcapq: 0.706 (strongly positively correlated)
- working_capital: 0.706 (strongly positively correlated)
- cash: 0.700 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
