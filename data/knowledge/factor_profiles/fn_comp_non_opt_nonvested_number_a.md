---
field: fn_comp_non_opt_nonvested_number_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.56
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2118
ann_vol: 0.1154
hit_rate: 0.4834
rolling_sharpe_min: -1.461
rolling_sharpe_max: 2.239
negated_best_sharpe: 0.32
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.24
---
# fn_comp_non_opt_nonvested_number_a (fundamental2)

*The number of non-vested equity-based payment instruments, excluding stock (or unit) options, that validly exist and are outstanding as of the balance sheet date.*

## Signal Profile
- `rank(fn_comp_non_opt_nonvested_number_a)`: S=0.40, F=0.15, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_comp_non_opt_nonvested_number_a / close)`: S=0.29, F=0.13, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comp_non_opt_nonvested_number_a, 5))`: S=0.56, F=0.24, T=34.9%, INFERIOR (TOP3000)
- `-rank(fn_comp_non_opt_nonvested_number_a)`: S=0.07, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_nonvested_number_a, 5))`: S=0.21, F=0.07, T=31.8%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_non_opt_nonvested_number_a, 63)`: S=-0.01, F=0.00, T=17.4%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_non_opt_nonvested_number_a, 10)`: S=-0.08, F=-0.03, T=0.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_non_opt_nonvested_number_a, 22))`: S=0.05, F=0.01, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_nonvested_number_a)`: S=0.32, F=0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_nonvested_number_a / close)`: S=0.15, F=0.05, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.57, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.82 (negative), ret=-8.3%
  - 2020: S=1.26 (moderate), ret=+14.8%
  - 2021: S=1.86 (strong), ret=+23.7%
  - 2022: S=0.51 (moderate), ret=+5.6%
  - 2023: S=-0.33 (negative), ret=-3.6%

## Risk & Drawdown
- Max drawdown: 21.18% over 700 days (not yet recovered, ongoing at window end)
- Annualized: return +6.6%, volatility 11.5% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +1.03, excess kurtosis +8.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.46, max 2.24, latest -0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +15.24%; worst month: -5.29%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.81
- Sideways: S=-0.48
- Bear: S=0.26

## Negated Direction
Best negated: `rank(-1 * fn_comp_non_opt_nonvested_number_a)` S=0.32, F=0.15, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_non_opt_nonvested_number_a)`: S=0.32, F=0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_nonvested_number_a / close)`: S=0.15, F=0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_nonvested_number_a, 5))`: S=0.21, F=0.07, T=31.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_comp_non_opt_nonvested_number_a, 5))` | TOP1000 | 0.53 | 0.24 | 27.2% | 60% | mixed |
| `rank(ts_delta(fn_comp_non_opt_nonvested_number_a, 5))` | TOP3000 | 0.57 | 0.24 | 21.2% | 60% | mixed |
| `rank(fn_comp_non_opt_nonvested_number_a)` | TOP3000 | 0.41 | 0.15 | 9.2% | 80% | mixed |
| `rank(fn_comp_non_opt_nonvested_number_a / close)` | TOP3000 | 0.29 | 0.13 | 20.8% | 60% | bear-only |
| `rank(fn_comp_non_opt_nonvested_number_a / close)` | TOP500 | 0.15 | 0.04 | 9.0% | 40% | all-weather |
| `rank(ts_delta(fn_comp_non_opt_nonvested_number_a, 5))` | TOP500 | 0.10 | 0.02 | 39.4% | 80% | weak |

## Correlation Notes
Top correlates:
- fnd6_dlcch: 0.140 (weakly positively correlated)
- fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q: 0.133 (weakly positively correlated)
- fnd6_acdo: 0.111 (weakly positively correlated)
- fn_oth_income_loss_available_for_sale_securities_adj_of_tax_a: 0.097 (weakly positively correlated)
- fnd6_currencya_curcd: 0.093 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
