---
field: fnd6_cptnewqv1300_nopiq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.5
best_fitness: 0.18
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1729
ann_vol: 0.0983
hit_rate: 0.4972
rolling_sharpe_min: -1.16
rolling_sharpe_max: 2.588
negated_best_sharpe: 0.19
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.31
---
# fnd6_cptnewqv1300_nopiq (fundamental6)

*Non-Operating Income (Expense) - Total*

## Signal Profile
- `rank(fnd6_cptnewqv1300_nopiq)`: S=0.43, F=0.15, T=3.2%, INFERIOR (TOP3000)
- `rank(fnd6_cptnewqv1300_nopiq / close)`: S=0.44, F=0.15, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cptnewqv1300_nopiq, 5))`: S=0.50, F=0.18, T=39.4%, INFERIOR (TOP500)
- `-rank(fnd6_cptnewqv1300_nopiq)`: S=0.01, F=0.00, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_nopiq, 5))`: S=0.19, F=0.03, T=38.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cptnewqv1300_nopiq, 63)`: S=-0.16, F=-0.03, T=18.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cptnewqv1300_nopiq, 10)`: S=0.10, F=0.02, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cptnewqv1300_nopiq, 22))`: S=-0.33, F=-0.10, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_nopiq)`: S=-0.43, F=-0.15, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_nopiq / close)`: S=-0.44, F=-0.15, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.49, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.76 (moderate), ret=+6.1%
  - 2020: S=-0.62 (negative), ret=-6.1%
  - 2021: S=0.17 (weak), ret=+1.9%
  - 2022: S=2.56 (strong), ret=+26.1%
  - 2023: S=-0.56 (negative), ret=-4.6%

## Risk & Drawdown
- Max drawdown: 17.29% over 1088 days (recovered)
- Annualized: return +4.8%, volatility 9.8% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew +0.67, excess kurtosis +5.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 2.59, latest -0.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.78%; worst month: -5.10%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.89
- Sideways: S=0.74
- Bear: S=-0.16

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cptnewqv1300_nopiq, 5))` S=0.19, F=0.03, INFERIOR
Direction gap: -0.31 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cptnewqv1300_nopiq)`: S=-0.43, F=-0.15, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cptnewqv1300_nopiq / close)`: S=-0.44, F=-0.15, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cptnewqv1300_nopiq, 5))`: S=0.19, F=0.03, T=38.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_cptnewqv1300_nopiq, 5))` | TOP500 | 0.49 | 0.18 | 17.3% | 60% | mixed |
| `rank(fnd6_cptnewqv1300_nopiq)` | TOP3000 | 0.44 | 0.15 | 11.8% | 80% | bull-only |
| `rank(fnd6_cptnewqv1300_nopiq / close)` | TOP3000 | 0.45 | 0.15 | 6.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_cptnewqv1300_nopiq, 5))` | TOP200 | 0.37 | 0.13 | 27.7% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_ciq: 0.181 (weakly positively correlated)
- fnd6_newqv1300_citotalq: 0.180 (weakly positively correlated)
- rp_ess_credit_ratings: 0.177 (weakly positively correlated)
- news_mins_20_pct_up: 0.124 (weakly positively correlated)
- news_mins_20_chg: 0.124 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
