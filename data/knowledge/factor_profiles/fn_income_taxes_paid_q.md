---
field: fn_income_taxes_paid_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.91
best_fitness: 0.53
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2165
ann_vol: 0.14
hit_rate: 0.5093
rolling_sharpe_min: -1.092
rolling_sharpe_max: 2.767
top_merge_partner: fnd6_txbco
negated_best_sharpe: 0.47
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: -0.44
---
# fn_income_taxes_paid_q (fundamental2)

*The amount of cash paid during the current period to foreign, federal, state, and local authorities as taxes on income.*

## Signal Profile
- `rank(fn_income_taxes_paid_q)`: S=0.31, F=0.15, T=2.2%, INFERIOR (TOP3000)
- `rank(fn_income_taxes_paid_q / close)`: S=0.61, F=0.37, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_income_taxes_paid_q, 5))`: S=0.91, F=0.53, T=37.5%, INFERIOR (TOP500)
- `-rank(fn_income_taxes_paid_q)`: S=0.02, F=0.00, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_income_taxes_paid_q, 5))`: S=-0.20, F=-0.07, T=37.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_income_taxes_paid_q, 22)`: S=-0.14, F=-0.04, T=34.4%, INFERIOR (TOP3000)
- `ts_mean(fn_income_taxes_paid_q, 10)`: S=-0.15, F=-0.05, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_income_taxes_paid_q, 22))`: S=-0.11, F=-0.02, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_taxes_paid_q)`: S=0.42, F=0.33, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_taxes_paid_q / close)`: S=0.47, F=0.37, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.92, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+7.8%
  - 2020: S=1.24 (moderate), ret=+18.4%
  - 2021: S=1.09 (moderate), ret=+15.3%
  - 2022: S=-0.02 (negative), ret=-0.4%
  - 2023: S=2.00 (strong), ret=+21.9%

## Risk & Drawdown
- Max drawdown: 21.65% over 540 days (recovered)
- Annualized: return +12.9%, volatility 14.0% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.23, excess kurtosis +3.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 2.77, latest 1.98

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +11.97%; worst month: -7.57%
Positive months: 70%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.24
- Sideways: S=1.48
- Bear: S=0.04

## Negated Direction
Best negated: `rank(-1 * fn_income_taxes_paid_q / close)` S=0.47, F=0.37, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_income_taxes_paid_q)`: S=0.42, F=0.33, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_taxes_paid_q / close)`: S=0.47, F=0.37, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_income_taxes_paid_q, 5))`: S=-0.20, F=-0.07, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_income_taxes_paid_q, 5))` | TOP500 | 0.92 | 0.53 | 21.6% | 80% | mixed |
| `rank(fn_income_taxes_paid_q / close)` | TOP3000 | 0.60 | 0.37 | 18.2% | 60% | bull-only |
| `rank(fn_income_taxes_paid_q)` | TOP3000 | 0.30 | 0.15 | 30.6% | 60% | bull-only |
| `rank(fn_income_taxes_paid_q / close)` | TOP1000 | 0.15 | 0.06 | 20.7% | 60% | bull-only |
| `rank(ts_delta(fn_income_taxes_paid_q, 5))` | TOP3000 | 0.23 | 0.04 | 19.3% | 60% | weak |
| `rank(ts_delta(fn_income_taxes_paid_q, 5))` | TOP200 | 0.10 | 0.02 | 50.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_oth_income_loss_fx_transaction_and_tax_translation_adj_q: 0.138 (weakly positively correlated)
- news_mins_20_pct_up: 0.132 (weakly positively correlated)
- news_mins_20_chg: 0.132 (weakly positively correlated)
- fn_comp_options_out_weighted_avg_q: 0.131 (weakly positively correlated)
- implied_volatility_put_360: 0.119 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_txbco | fundamental6 | -0.05 | 1.40 | +0.39 | -0.93 | yes |
| fnd6_invrm | fundamental6 | -0.07 | 1.36 | +0.41 | -0.60 | yes |
| fnd6_optosby | fundamental6 | -0.04 | 1.40 | +0.38 | -0.77 | yes |
| max_net_debt_guidance | company_guidance | -0.06 | 1.42 | +0.39 | -0.51 | yes |
| min_net_debt_guidance | company_guidance | -0.06 | 1.42 | +0.39 | -0.51 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
