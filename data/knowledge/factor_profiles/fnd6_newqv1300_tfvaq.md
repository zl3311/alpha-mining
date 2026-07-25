---
field: fnd6_newqv1300_tfvaq
dataset: fundamental6
best_template: ts_mean
best_sharpe: 0.58
best_fitness: 0.34
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.0623
ann_vol: 0.0631
hit_rate: 0.4899
rolling_sharpe_min: -0.882
rolling_sharpe_max: 1.999
negated_best_sharpe: 0.09
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.49
---
# fnd6_newqv1300_tfvaq (fundamental6)

*Total Fair Value Assets*

## Signal Profile
- `rank(fnd6_newqv1300_tfvaq)`: S=0.53, F=0.27, T=6.4%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_tfvaq / close)`: S=0.56, F=0.30, T=8.2%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_tfvaq, 5))`: S=0.41, F=0.14, T=60.5%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_tfvaq)`: S=-0.52, F=-0.27, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_tfvaq, 5))`: S=0.12, F=0.03, T=63.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_tfvaq, 63)`: S=0.17, F=0.03, T=21.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_tfvaq, 10)`: S=0.58, F=0.34, T=4.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_tfvaq, 22))`: S=0.53, F=0.20, T=23.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tfvaq)`: S=0.09, F=0.03, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tfvaq / close)`: S=-0.11, F=-0.03, T=9.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+1.1%
  - 2020: S=0.60 (moderate), ret=+3.6%
  - 2021: S=1.04 (moderate), ret=+6.7%
  - 2022: S=0.02 (weak), ret=+0.2%
  - 2023: S=0.99 (moderate), ret=+5.6%

## Risk & Drawdown
- Max drawdown: 6.23% over 91 days (recovered)
- Annualized: return +3.5%, volatility 6.3% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.27, excess kurtosis +2.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.88, max 2.00, latest 1.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +3.89%; worst month: -2.72%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.77
- Sideways: S=0.73
- Bear: S=0.21

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_tfvaq)` S=0.09, F=0.03, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_tfvaq)`: S=0.09, F=0.03, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_tfvaq / close)`: S=-0.11, F=-0.03, T=9.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_tfvaq, 5))`: S=0.12, F=0.03, T=63.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_tfvaq / close)` | TOP1000 | 0.56 | 0.30 | 6.2% | 100% | mixed |
| `rank(fnd6_newqv1300_tfvaq)` | TOP3000 | 0.54 | 0.27 | 19.8% | 80% | bull-only |
| `rank(fnd6_newqv1300_tfvaq)` | TOP1000 | 0.52 | 0.27 | 18.7% | 80% | bull-only |
| `rank(fnd6_newqv1300_tfvaq / close)` | TOP3000 | 0.40 | 0.17 | 9.4% | 60% | mixed |
| `rank(fnd6_newqv1300_tfvaq / close)` | TOP500 | 0.36 | 0.16 | 11.0% | 40% | mixed |
| `rank(ts_delta(fnd6_newqv1300_tfvaq, 5))` | TOP500 | 0.40 | 0.14 | 34.8% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_tfvaq, 5))` | TOP1000 | 0.37 | 0.11 | 26.9% | 60% | mixed |
| `rank(ts_delta(fnd6_newqv1300_tfvaq, 5))` | TOP3000 | 0.43 | 0.10 | 21.3% | 60% | all-weather |
| `rank(fnd6_newqv1300_tfvaq)` | TOP500 | 0.17 | 0.06 | 22.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_tfvaq / close)` | TOP200 | 0.12 | 0.03 | 21.6% | 40% | mixed |

## Correlation Notes
Top correlates:
- fn_allocated_share_based_compensation_expense_a: 0.606 (moderately positively correlated)
- fn_comp_not_rec_a: 0.594 (moderately positively correlated)
- fnd6_newqv1300_stkcoq: 0.576 (moderately positively correlated)
- fn_oth_comp_fair_value_a: 0.573 (moderately positively correlated)
- fn_op_lease_min_pay_due_in_5y_a: 0.571 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
