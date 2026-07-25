---
field: fn_payments_to_acquire_businesses_net_of_cash_acquired_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 1.23
best_fitness: 1.12
best_universe: TOP200
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.2115
ann_vol: 0.1843
hit_rate: 0.5053
rolling_sharpe_min: -0.488
rolling_sharpe_max: 2.414
top_merge_partner: fnd6_idit
negated_best_sharpe: 0.27
negated_best_template: neg_rank_level
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.96
---
# fn_payments_to_acquire_businesses_net_of_cash_acquired_a (fundamental2)

*The cash outflow associated with the acquisition of a business, net of the cash acquired from the purchase.*

## Signal Profile
- `rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_a)`: S=0.25, F=0.07, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_a / close)`: S=0.41, F=0.14, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_a, 5))`: S=1.23, F=1.12, T=27.2%, AVERAGE (TOP200)
- `-rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_a)`: S=0.14, F=0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_a, 5))`: S=-0.98, F=-0.81, T=26.9%, INFERIOR (TOP3000)
- `-ts_zscore(fn_payments_to_acquire_businesses_net_of_cash_acquired_a, 63)`: S=0.48, F=0.33, T=14.8%, INFERIOR (TOP3000)
- `ts_mean(fn_payments_to_acquire_businesses_net_of_cash_acquired_a, 10)`: S=-0.03, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_a, 22))`: S=0.24, F=0.10, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_to_acquire_businesses_net_of_cash_acquired_a)`: S=0.27, F=0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_to_acquire_businesses_net_of_cash_acquired_a / close)`: S=0.23, F=0.08, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.22, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=2.50 (strong), ret=+36.6%
  - 2020: S=0.05 (weak), ret=+0.7%
  - 2021: S=0.23 (weak), ret=+5.2%
  - 2022: S=2.35 (strong), ret=+51.9%
  - 2023: S=1.14 (moderate), ret=+16.0%

## Risk & Drawdown
- Max drawdown: 21.15% over 269 days (recovered)
- Annualized: return +22.6%, volatility 18.4% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +1.04, excess kurtosis +11.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.49, max 2.41, latest 1.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +14.46%; worst month: -6.46%
Positive months: 70%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.87
- Sideways: S=0.82
- Bear: S=0.83

## Negated Direction
Best negated: `rank(-1 * fn_payments_to_acquire_businesses_net_of_cash_acquired_a)` S=0.27, F=0.10, INFERIOR
Direction gap: -0.96 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_payments_to_acquire_businesses_net_of_cash_acquired_a)`: S=0.27, F=0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_payments_to_acquire_businesses_net_of_cash_acquired_a / close)`: S=0.23, F=0.08, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_a, 5))`: S=-0.98, F=-0.81, T=26.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_a, 5))` | TOP200 | 1.22 | 1.12 | 21.1% | 100% | all-weather |
| `rank(ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_a, 5))` | TOP500 | 0.68 | 0.41 | 26.3% | 80% | mixed |
| `rank(ts_delta(fn_payments_to_acquire_businesses_net_of_cash_acquired_a, 5))` | TOP1000 | 0.43 | 0.20 | 19.8% | 100% | bull-only |
| `rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_a / close)` | TOP3000 | 0.41 | 0.14 | 4.3% | 80% | mixed |
| `rank(fn_payments_to_acquire_businesses_net_of_cash_acquired_a)` | TOP3000 | 0.24 | 0.07 | 10.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_finite_lived_intangible_assets_net_a: 0.442 (moderately positively correlated)
- fnd2_a_flintasamt1expyfour: 0.392 (weakly positively correlated)
- fn_avg_diluted_sharesout_adj_a: 0.269 (weakly positively correlated)
- fn_accum_oth_income_loss_fx_adj_net_of_tax_a: 0.261 (weakly positively correlated)
- fnd2_a_fedstyitxrt: 0.193 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_idit | fundamental6 | -0.06 | 1.68 | +0.45 | -0.73 | yes |
| fnd6_nopio | fundamental6 | +0.06 | 1.72 | +0.44 | -0.83 | yes |
| fnd6_mrc1 | fundamental6 | -0.03 | 1.79 | +0.52 | +0.05 | yes |
| news_mins_4_pct_dn | news12 | +0.01 | 1.77 | +0.47 | -0.21 | yes |
| implied_volatility_mean_10 | option8 | -0.03 | 1.71 | +0.48 | +0.17 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
