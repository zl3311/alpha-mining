---
field: fn_accum_oth_income_loss_fx_adj_net_of_tax_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.67
best_fitness: 0.46
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.2338
ann_vol: 0.1932
hit_rate: 0.4794
rolling_sharpe_min: -0.781
rolling_sharpe_max: 1.967
negated_best_sharpe: 0.15
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.52
---
# fn_accum_oth_income_loss_fx_adj_net_of_tax_a (fundamental2)

*Accumulated adjustment, net of tax, that results from the process of translating subsidiary financial statements and foreign equity investments into the reporting currency from the functional currency of the reporting entity, net of reclassification of realized foreign currency translation gains or losses.*

## Signal Profile
- `rank(fn_accum_oth_income_loss_fx_adj_net_of_tax_a)`: S=0.31, F=0.12, T=1.0%, INFERIOR (TOP1000)
- `rank(fn_accum_oth_income_loss_fx_adj_net_of_tax_a / close)`: S=0.31, F=0.13, T=1.5%, INFERIOR (TOP500)
- `rank(ts_delta(fn_accum_oth_income_loss_fx_adj_net_of_tax_a, 5))`: S=0.67, F=0.46, T=28.0%, INFERIOR (TOP200)
- `-rank(fn_accum_oth_income_loss_fx_adj_net_of_tax_a)`: S=-0.31, F=-0.12, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accum_oth_income_loss_fx_adj_net_of_tax_a, 5))`: S=0.11, F=0.02, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(fn_accum_oth_income_loss_fx_adj_net_of_tax_a, 22)`: S=-0.10, F=-0.03, T=19.7%, INFERIOR (TOP3000)
- `ts_mean(fn_accum_oth_income_loss_fx_adj_net_of_tax_a, 10)`: S=0.58, F=0.31, T=0.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_accum_oth_income_loss_fx_adj_net_of_tax_a, 22))`: S=0.69, F=0.46, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_oth_income_loss_fx_adj_net_of_tax_a)`: S=-0.16, F=-0.04, T=0.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_oth_income_loss_fx_adj_net_of_tax_a / close)`: S=0.15, F=0.03, T=0.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 9F/23P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.68, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.87 (moderate), ret=+14.7%
  - 2020: S=1.29 (moderate), ret=+24.7%
  - 2021: S=0.20 (weak), ret=+4.6%
  - 2022: S=0.68 (moderate), ret=+14.1%
  - 2023: S=0.41 (weak), ret=+5.9%

## Risk & Drawdown
- Max drawdown: 23.38% over 500 days (not yet recovered, ongoing at window end)
- Annualized: return +13.0%, volatility 19.3% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.97, excess kurtosis +12.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.78, max 1.97, latest 0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +17.76%; worst month: -8.01%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.52
- Sideways: S=0.23
- Bear: S=1.21

## Negated Direction
Best negated: `rank(-1 * fn_accum_oth_income_loss_fx_adj_net_of_tax_a / close)` S=0.15, F=0.03, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_accum_oth_income_loss_fx_adj_net_of_tax_a)`: S=-0.16, F=-0.04, T=0.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_accum_oth_income_loss_fx_adj_net_of_tax_a / close)`: S=0.15, F=0.03, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_accum_oth_income_loss_fx_adj_net_of_tax_a, 5))`: S=0.11, F=0.02, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_accum_oth_income_loss_fx_adj_net_of_tax_a, 5))` | TOP200 | 0.68 | 0.46 | 23.4% | 100% | all-weather |
| `rank(ts_delta(fn_accum_oth_income_loss_fx_adj_net_of_tax_a, 5))` | TOP1000 | 0.46 | 0.19 | 23.7% | 80% | mixed |
| `rank(fn_accum_oth_income_loss_fx_adj_net_of_tax_a / close)` | TOP500 | 0.32 | 0.13 | 20.8% | 60% | bear-only |
| `rank(fn_accum_oth_income_loss_fx_adj_net_of_tax_a)` | TOP1000 | 0.32 | 0.12 | 13.2% | 60% | bear-only |
| `rank(fn_accum_oth_income_loss_fx_adj_net_of_tax_a)` | TOP500 | 0.30 | 0.11 | 20.1% | 60% | bear-only |
| `rank(fn_accum_oth_income_loss_fx_adj_net_of_tax_a / close)` | TOP1000 | 0.25 | 0.07 | 12.7% | 60% | bear-only |
| `rank(ts_delta(fn_accum_oth_income_loss_fx_adj_net_of_tax_a, 5))` | TOP500 | 0.18 | 0.04 | 32.3% | 40% | mixed |
| `rank(fn_accum_oth_income_loss_fx_adj_net_of_tax_a)` | TOP3000 | 0.16 | 0.04 | 13.6% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fn_finite_lived_intangible_assets_net_a: 0.292 (weakly positively correlated)
- fn_payments_to_acquire_businesses_net_of_cash_acquired_a: 0.261 (weakly positively correlated)
- fnd2_a_flintasamt1expyfour: 0.212 (weakly positively correlated)
- fn_avg_diluted_sharesout_adj_a: 0.210 (weakly positively correlated)
- fnd2_ebitfr: 0.202 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
