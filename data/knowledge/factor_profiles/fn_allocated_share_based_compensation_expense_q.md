---
field: fn_allocated_share_based_compensation_expense_q
dataset: fundamental2
cluster: fundamental2_balance_sheet_equity
coverage: 0.6541
community_alphas: 1144
best_template: rank_level
best_sharpe: 0.47
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1762
ann_vol: 0.0684
hit_rate: 0.5255
rolling_sharpe_min: -1.792
rolling_sharpe_max: 2.295
negated_best_sharpe: 0.33
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.14
---
# fn_allocated_share_based_compensation_expense_q (fundamental2)

*Represents the expense recognized during the period arising from equity-based compensation arrangements (for example, shares of stock, units, stock options, or other equity instruments) with employees, directors, and certain consultants qualifying for treatment as employees.*

## Signal Profile
- `rank(fn_allocated_share_based_compensation_expense_q)`: S=0.47, F=0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(fn_allocated_share_based_compensation_expense_q / close)`: S=0.43, F=0.22, T=2.4%, INFERIOR (TOP500)
- `rank(ts_delta(fn_allocated_share_based_compensation_expense_q, 5))`: S=0.44, F=0.14, T=36.1%, INFERIOR (TOP1000)
- `-rank(fn_allocated_share_based_compensation_expense_q)`: S=-0.05, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_allocated_share_based_compensation_expense_q, 5))`: S=0.33, F=0.08, T=36.7%, INFERIOR (TOP3000)
- `ts_zscore(fn_allocated_share_based_compensation_expense_q, 22)`: S=0.08, F=0.01, T=35.4%, INFERIOR (TOP3000)
- `ts_mean(fn_allocated_share_based_compensation_expense_q, 10)`: S=0.30, F=0.15, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_allocated_share_based_compensation_expense_q, 22))`: S=-0.21, F=-0.05, T=16.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_allocated_share_based_compensation_expense_q)`: S=-0.47, F=-0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_allocated_share_based_compensation_expense_q / close)`: S=-0.35, F=-0.17, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.47, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.85 (moderate), ret=+3.9%
  - 2020: S=-0.30 (negative), ret=-2.0%
  - 2021: S=0.49 (weak), ret=+4.9%
  - 2022: S=0.57 (moderate), ret=+3.2%
  - 2023: S=1.06 (moderate), ret=+5.8%

## Risk & Drawdown
- Max drawdown: 17.62% over 642 days (recovered)
- Annualized: return +3.2%, volatility 6.8% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew -0.13, excess kurtosis +1.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.79, max 2.29, latest 1.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +3.74%; worst month: -4.15%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.61
- Sideways: S=1.43
- Bear: S=-1.46

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_allocated_share_based_compensation_expense_q, 5))` S=0.33, F=0.08, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_allocated_share_based_compensation_expense_q)`: S=-0.47, F=-0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_allocated_share_based_compensation_expense_q / close)`: S=-0.35, F=-0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_allocated_share_based_compensation_expense_q, 5))`: S=0.33, F=0.08, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_allocated_share_based_compensation_expense_q)` | TOP3000 | 0.47 | 0.24 | 17.6% | 80% | bull-only |
| `rank(fn_allocated_share_based_compensation_expense_q / close)` | TOP500 | 0.44 | 0.22 | 7.6% | 80% | mixed |
| `rank(fn_allocated_share_based_compensation_expense_q / close)` | TOP3000 | 0.35 | 0.17 | 23.9% | 80% | mixed |
| `rank(ts_delta(fn_allocated_share_based_compensation_expense_q, 5))` | TOP1000 | 0.45 | 0.14 | 13.4% | 60% | weak |
| `rank(fn_allocated_share_based_compensation_expense_q / close)` | TOP1000 | 0.32 | 0.13 | 12.7% | 60% | all-weather |
| `rank(fn_allocated_share_based_compensation_expense_q / close)` | TOP200 | 0.18 | 0.06 | 16.7% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_comp_not_rec_q: 0.876 (strongly positively correlated)
- cash: 0.842 (strongly positively correlated)
- fnd6_tfva: 0.829 (strongly positively correlated)
- fnd6_fopox: 0.828 (strongly positively correlated)
- fnd6_newqv1300_xrdq: 0.825 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
