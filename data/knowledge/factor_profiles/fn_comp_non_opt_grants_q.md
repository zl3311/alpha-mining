---
field: fn_comp_non_opt_grants_q
dataset: fundamental2
best_template: ts_mean
best_sharpe: 0.49
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0506
ann_vol: 0.0416
hit_rate: 0.5287
rolling_sharpe_min: -0.599
rolling_sharpe_max: 2.505
negated_best_sharpe: 0.7
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: 0.21
---
# fn_comp_non_opt_grants_q (fundamental2)

*The number of grants made during the period on other than stock (or unit) option plans (for example, phantom stock or unit plan, stock or unit appreciation rights plan, performance target plan).*

## Signal Profile
- `rank(fn_comp_non_opt_grants_q)`: S=0.67, F=0.32, T=1.4%, INFERIOR (TOP3000)
- `rank(fn_comp_non_opt_grants_q / close)`: S=0.46, F=0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comp_non_opt_grants_q, 5))`: S=0.58, F=0.30, T=36.9%, INFERIOR (TOP1000)
- `-rank(fn_comp_non_opt_grants_q)`: S=-0.61, F=-0.29, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_grants_q, 5))`: S=0.70, F=0.34, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_non_opt_grants_q, 63)`: S=0.53, F=0.37, T=15.6%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_non_opt_grants_q, 10)`: S=0.49, F=0.50, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_non_opt_grants_q, 22))`: S=0.46, F=0.25, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_grants_q)`: S=-0.67, F=-0.32, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_grants_q / close)`: S=-0.46, F=-0.24, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.68, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.31 (weak), ret=+0.9%
  - 2020: S=1.84 (strong), ret=+6.9%
  - 2021: S=1.03 (moderate), ret=+3.5%
  - 2022: S=-0.13 (negative), ret=-0.7%
  - 2023: S=0.72 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 5.06% over 163 days (not yet recovered, ongoing at window end)
- Annualized: return +2.8%, volatility 4.2% (fraction of booksize)
- Hit rate: 52.9% positive days
- Tail shape: skew -0.05, excess kurtosis +1.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.60, max 2.50, latest 0.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +2.83%; worst month: -3.63%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.19
- Sideways: S=0.36
- Bear: S=1.49

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_non_opt_grants_q, 5))` S=0.70, F=0.34, INFERIOR
Direction gap: +0.21 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_comp_non_opt_grants_q)`: S=-0.67, F=-0.32, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_grants_q / close)`: S=-0.46, F=-0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_grants_q, 5))`: S=0.70, F=0.34, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_non_opt_grants_q)` | TOP3000 | 0.68 | 0.32 | 5.1% | 80% | mixed |
| `rank(ts_delta(fn_comp_non_opt_grants_q, 5))` | TOP1000 | 0.57 | 0.30 | 42.1% | 80% | bull-only |
| `rank(fn_comp_non_opt_grants_q)` | TOP1000 | 0.62 | 0.29 | 10.2% | 80% | mixed |
| `rank(ts_delta(fn_comp_non_opt_grants_q, 5))` | TOP500 | 0.49 | 0.27 | 53.3% | 40% | mixed |
| `rank(fn_comp_non_opt_grants_q / close)` | TOP3000 | 0.47 | 0.24 | 17.0% | 80% | bear-only |
| `rank(fn_comp_non_opt_grants_q / close)` | TOP1000 | 0.43 | 0.20 | 13.2% | 60% | mixed |
| `rank(fn_comp_non_opt_grants_q / close)` | TOP500 | 0.42 | 0.19 | 13.6% | 60% | all-weather |
| `rank(fn_comp_non_opt_grants_q)` | TOP500 | 0.19 | 0.05 | 11.9% | 60% | bull-only |
| `rank(fn_comp_non_opt_grants_q / close)` | TOP200 | 0.15 | 0.03 | 14.2% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_comp_non_opt_nonvested_number_q: 0.737 (strongly positively correlated)
- fnd2_a_dfdtxava: 0.667 (moderately positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.667 (moderately positively correlated)
- fnd6_tlcf: 0.660 (moderately positively correlated)
- fn_comp_not_rec_a: 0.654 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
