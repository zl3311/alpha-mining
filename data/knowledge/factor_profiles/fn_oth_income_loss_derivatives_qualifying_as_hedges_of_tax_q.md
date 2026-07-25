---
field: fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 1.14
best_fitness: 0.85
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.1342
ann_vol: 0.1381
hit_rate: 0.5231
rolling_sharpe_min: 0.035
rolling_sharpe_max: 3.515
top_merge_partner: anl4_netprofit_flag
negated_best_sharpe: 0.57
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.57
---
# fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q (fundamental2)

*Amount after tax and reclassification adjustments, of increase (decrease) in accumulated gain (loss) from derivative instruments designated and qualifying as the effective portion of cash flow hedges and an entity's share of an equity investee's increase (decrease) in deferred hedging gain (loss).*

## Signal Profile
- `rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q)`: S=0.48, F=0.18, T=1.8%, INFERIOR (TOP500)
- `rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q / close)`: S=0.51, F=0.19, T=1.9%, INFERIOR (TOP500)
- `rank(ts_delta(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q, 5))`: S=1.14, F=0.85, T=28.6%, INFERIOR (TOP1000)
- `-rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q)`: S=-0.25, F=-0.06, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q, 5))`: S=-0.66, F=-0.35, T=30.6%, INFERIOR (TOP3000)
- `ts_zscore(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q, 22)`: S=0.04, F=0.01, T=20.9%, INFERIOR (TOP3000)
- `ts_mean(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q, 10)`: S=0.65, F=0.32, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q, 22))`: S=0.73, F=0.56, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q)`: S=0.57, F=0.17, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q / close)`: S=0.45, F=0.13, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.15, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+4.7%
  - 2020: S=1.85 (strong), ret=+32.4%
  - 2021: S=2.12 (strong), ret=+32.7%
  - 2022: S=0.34 (weak), ret=+4.5%
  - 2023: S=0.30 (weak), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 13.42% over 303 days (recovered)
- Annualized: return +15.9%, volatility 13.8% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew +0.54, excess kurtosis +29.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.04, max 3.52, latest 0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +13.68%; worst month: -7.48%
Positive months: 58%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.04
- Sideways: S=1.38
- Bear: S=1.15

## Negated Direction
Best negated: `rank(-1 * fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q)` S=0.57, F=0.17, INFERIOR
Direction gap: -0.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q)`: S=0.57, F=0.17, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q / close)`: S=0.45, F=0.13, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q, 5))`: S=-0.66, F=-0.35, T=30.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q, 5))` | TOP1000 | 1.15 | 0.85 | 13.4% | 100% | all-weather |
| `rank(ts_delta(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q, 5))` | TOP3000 | 0.69 | 0.37 | 17.3% | 80% | mixed |
| `rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q / close)` | TOP500 | 0.51 | 0.19 | 6.2% | 60% | mixed |
| `rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q)` | TOP500 | 0.49 | 0.18 | 5.7% | 80% | mixed |
| `rank(ts_delta(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q, 5))` | TOP500 | 0.24 | 0.09 | 21.2% | 60% | bull-only |
| `rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q / close)` | TOP1000 | 0.33 | 0.09 | 3.8% | 60% | weak |
| `rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q)` | TOP1000 | 0.26 | 0.06 | 3.4% | 80% | mixed |
| `rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q / close)` | TOP200 | 0.19 | 0.05 | 14.9% | 80% | bear-only |
| `rank(fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q)` | TOP200 | 0.12 | 0.02 | 14.6% | 80% | bear-only |

## Correlation Notes
Top correlates:
- fn_oth_income_loss_net_of_tax_q: 0.176 (weakly positively correlated)
- fn_derivative_fair_value_of_derivative_liability_q: -0.161 (weakly negatively correlated)
- fnd6_newqv1300_reunaq: 0.152 (weakly positively correlated)
- fn_comp_non_opt_nonvested_number_a: 0.133 (weakly positively correlated)
- fn_avg_diluted_sharesout_adj_q: 0.128 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_netprofit_flag | analyst4 | -0.05 | 1.75 | +0.48 | -0.54 | yes |
| anl4_cfi_flag | analyst_revision | -0.03 | 1.62 | +0.45 | -0.76 | yes |
| anl4_epsr_flag | analyst4 | -0.04 | 1.65 | +0.47 | -0.46 | yes |
| implied_volatility_put_20 | option8 | -0.07 | 1.64 | +0.49 | -0.13 | yes |
| implied_volatility_mean_10 | option8 | -0.03 | 1.69 | +0.47 | -0.29 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
