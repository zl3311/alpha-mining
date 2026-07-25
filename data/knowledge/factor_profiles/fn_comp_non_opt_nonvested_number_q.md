---
field: fn_comp_non_opt_nonvested_number_q
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.98
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1795
ann_vol: 0.061
hit_rate: 0.5215
rolling_sharpe_min: -1.698
rolling_sharpe_max: 3.121
negated_best_sharpe: 0.98
negated_best_template: rank_neg_delta
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: 0.61
---
# fn_comp_non_opt_nonvested_number_q (fundamental2)

*The number of non-vested equity-based payment instruments, excluding stock (or unit) options, that validly exist and are outstanding as of the balance sheet date.*

## Signal Profile
- `rank(fn_comp_non_opt_nonvested_number_q)`: S=0.36, F=0.15, T=1.1%, INFERIOR (TOP3000)
- `rank(fn_comp_non_opt_nonvested_number_q / close)`: S=0.19, F=0.09, T=2.6%, INFERIOR (TOP200)
- `rank(ts_delta(fn_comp_non_opt_nonvested_number_q, 5))`: S=-0.52, F=-0.27, T=37.0%, INFERIOR (TOP500)
- `-rank(fn_comp_non_opt_nonvested_number_q)`: S=-0.06, F=-0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_nonvested_number_q, 5))`: S=0.98, F=0.58, T=36.5%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_non_opt_nonvested_number_q, 63)`: S=0.37, F=0.18, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_non_opt_nonvested_number_q, 10)`: S=-0.29, F=-0.21, T=0.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_non_opt_nonvested_number_q, 22))`: S=-0.14, F=-0.04, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_nonvested_number_q)`: S=-0.36, F=-0.15, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_nonvested_number_q / close)`: S=-0.09, F=-0.02, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.36, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.99 (moderate), ret=+3.3%
  - 2020: S=1.81 (strong), ret=+8.4%
  - 2021: S=1.02 (moderate), ret=+4.2%
  - 2022: S=-1.37 (negative), ret=-12.0%
  - 2023: S=0.97 (moderate), ret=+7.0%

## Risk & Drawdown
- Max drawdown: 17.95% over 795 days (not yet recovered, ongoing at window end)
- Annualized: return +2.2%, volatility 6.1% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.12, excess kurtosis +2.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.70, max 3.12, latest 1.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +3.89%; worst month: -4.55%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.41
- Sideways: S=0.10
- Bear: S=1.45

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_non_opt_nonvested_number_q, 5))` S=0.98, F=0.58, INFERIOR
Direction gap: +0.61 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fn_comp_non_opt_nonvested_number_q)`: S=-0.36, F=-0.15, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_nonvested_number_q / close)`: S=-0.09, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_nonvested_number_q, 5))`: S=0.98, F=0.58, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_non_opt_nonvested_number_q)` | TOP3000 | 0.36 | 0.15 | 17.9% | 80% | mixed |
| `rank(fn_comp_non_opt_nonvested_number_q / close)` | TOP200 | 0.21 | 0.09 | 34.5% | 60% | bear-only |
| `rank(fn_comp_non_opt_nonvested_number_q / close)` | TOP500 | 0.22 | 0.08 | 19.6% | 60% | bear-only |
| `rank(fn_comp_non_opt_nonvested_number_q / close)` | TOP1000 | 0.15 | 0.05 | 27.0% | 60% | bear-only |
| `rank(fn_comp_non_opt_nonvested_number_q / close)` | TOP3000 | 0.09 | 0.02 | 34.4% | 80% | bear-only |

## Correlation Notes
Top correlates:
- fn_allocated_share_based_compensation_expense_a: 0.769 (strongly positively correlated)
- fn_comp_not_rec_a: 0.749 (strongly positively correlated)
- fn_comp_non_opt_grants_q: 0.737 (strongly positively correlated)
- fn_comp_non_opt_grants_a: 0.706 (strongly positively correlated)
- fnd6_cshtr: 0.697 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
