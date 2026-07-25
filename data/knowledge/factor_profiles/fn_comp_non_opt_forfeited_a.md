---
field: fn_comp_non_opt_forfeited_a
dataset: fundamental2
best_template: rank_level
best_sharpe: 0.82
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.0571
ann_vol: 0.038
hit_rate: 0.515
rolling_sharpe_min: -1.23
rolling_sharpe_max: 3.082
top_merge_partner: implied_volatility_mean_skew_720
negated_best_sharpe: 0.46
negated_best_template: neg_rank_level
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.36
---
# fn_comp_non_opt_forfeited_a (fundamental2)

*The number of equity-based payment instruments, excluding stock (or unit) options, that were forfeited during the reporting period.*

## Signal Profile
- `rank(fn_comp_non_opt_forfeited_a)`: S=0.82, F=0.41, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_comp_non_opt_forfeited_a / close)`: S=0.56, F=0.32, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comp_non_opt_forfeited_a, 5))`: S=0.49, F=0.24, T=33.6%, INFERIOR (TOP500)
- `-rank(fn_comp_non_opt_forfeited_a)`: S=-0.10, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_forfeited_a, 5))`: S=0.14, F=0.04, T=30.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_comp_non_opt_forfeited_a, 22)`: S=0.36, F=0.20, T=23.7%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_non_opt_forfeited_a, 10)`: S=0.18, F=0.09, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_non_opt_forfeited_a, 22))`: S=-0.04, F=-0.01, T=14.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_forfeited_a)`: S=0.46, F=0.25, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_forfeited_a / close)`: S=0.22, F=0.08, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.84, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.42 (negative), ret=-1.1%
  - 2020: S=1.59 (strong), ret=+5.6%
  - 2021: S=1.26 (moderate), ret=+3.8%
  - 2022: S=0.56 (moderate), ret=+2.2%
  - 2023: S=1.02 (moderate), ret=+5.2%

## Risk & Drawdown
- Max drawdown: 5.71% over 461 days (recovered)
- Annualized: return +3.2%, volatility 3.8% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.18, excess kurtosis +1.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.23, max 3.08, latest 0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +3.64%; worst month: -2.11%
Positive months: 51%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.09
- Sideways: S=0.43
- Bear: S=1.03

## Negated Direction
Best negated: `rank(-1 * fn_comp_non_opt_forfeited_a)` S=0.46, F=0.25, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_non_opt_forfeited_a)`: S=0.46, F=0.25, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_non_opt_forfeited_a / close)`: S=0.22, F=0.08, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_non_opt_forfeited_a, 5))`: S=0.14, F=0.04, T=30.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_non_opt_forfeited_a)` | TOP3000 | 0.84 | 0.41 | 5.7% | 80% | all-weather |
| `rank(fn_comp_non_opt_forfeited_a / close)` | TOP3000 | 0.56 | 0.32 | 13.1% | 60% | mixed |
| `rank(ts_delta(fn_comp_non_opt_forfeited_a, 5))` | TOP500 | 0.49 | 0.24 | 27.0% | 100% | all-weather |
| `rank(fn_comp_non_opt_forfeited_a / close)` | TOP1000 | 0.25 | 0.09 | 14.2% | 60% | mixed |
| `rank(fn_comp_non_opt_forfeited_a / close)` | TOP500 | 0.16 | 0.04 | 10.3% | 20% | mixed |
| `rank(ts_delta(fn_comp_non_opt_forfeited_a, 5))` | TOP3000 | 0.12 | 0.02 | 38.3% | 60% | weak |

## Correlation Notes
Top correlates:
- fn_allocated_share_based_compensation_expense_a: 0.708 (strongly positively correlated)
- fn_comp_non_opt_nonvested_number_q: 0.689 (moderately positively correlated)
- fnd2_a_sbcpnatqsttotnsvdptfv: 0.676 (moderately positively correlated)
- fn_comp_not_rec_a: 0.671 (moderately positively correlated)
- fnd2_a_dfdtxava: 0.666 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_mean_skew_720 | option8 | -0.27 | 1.52 | +0.51 | -0.53 | yes |
| implied_volatility_mean_skew_1080 | option8 | -0.28 | 1.52 | +0.51 | -0.46 | yes |
| implied_volatility_mean_skew_360 | option8 | -0.26 | 1.56 | +0.46 | -0.80 | yes |
| cashflow_per_share_minimum | analyst4 | -0.15 | 1.29 | +0.44 | -0.78 | yes |
| implied_volatility_mean_skew_270 | option8 | -0.23 | 1.45 | +0.43 | -0.83 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
