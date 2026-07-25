---
field: fn_avg_diluted_sharesout_adj_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.89
best_fitness: 0.67
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.2287
ann_vol: 0.1856
hit_rate: 0.5093
rolling_sharpe_min: -0.497
rolling_sharpe_max: 1.967
top_merge_partner: growth_potential_rank_derivative
negated_best_sharpe: 0.67
negated_best_template: neg_rank
negated_best_fitness: 0.33
n_negated_sims: 10
direction_gap: -0.22
---
# fn_avg_diluted_sharesout_adj_a (fundamental2)

*The sum of dilutive potential common shares or units used in the calculation of the diluted per-share or per-unit computation.*

## Signal Profile
- `rank(fn_avg_diluted_sharesout_adj_a)`: S=-0.08, F=-0.02, T=2.0%, INFERIOR (TOP200)
- `rank(fn_avg_diluted_sharesout_adj_a / close)`: S=0.20, F=0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_avg_diluted_sharesout_adj_a, 5))`: S=0.89, F=0.67, T=29.3%, INFERIOR (TOP200)
- `-rank(fn_avg_diluted_sharesout_adj_a)`: S=0.67, F=0.33, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_avg_diluted_sharesout_adj_a, 5))`: S=-0.67, F=-0.35, T=33.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_avg_diluted_sharesout_adj_a, 22)`: S=0.72, F=0.54, T=22.7%, INFERIOR (TOP3000)
- `ts_mean(fn_avg_diluted_sharesout_adj_a, 10)`: S=-0.30, F=-0.14, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_avg_diluted_sharesout_adj_a, 22))`: S=0.71, F=0.46, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_avg_diluted_sharesout_adj_a)`: S=0.67, F=0.33, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_avg_diluted_sharesout_adj_a / close)`: S=0.28, F=0.08, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.89, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.57 (strong), ret=+24.0%
  - 2020: S=-0.02 (negative), ret=-0.4%
  - 2021: S=0.95 (moderate), ret=+22.1%
  - 2022: S=1.02 (moderate), ret=+17.2%
  - 2023: S=1.46 (moderate), ret=+17.7%

## Risk & Drawdown
- Max drawdown: 22.87% over 272 days (recovered)
- Annualized: return +16.4%, volatility 18.6% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +1.36, excess kurtosis +15.48

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.50, max 1.97, latest 1.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +20.80%; worst month: -9.92%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.59
- Sideways: S=0.72
- Bear: S=1.32

## Negated Direction
Best negated: `-rank(fn_avg_diluted_sharesout_adj_a)` S=0.67, F=0.33, INFERIOR
Direction gap: -0.22 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_avg_diluted_sharesout_adj_a)`: S=0.67, F=0.33, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_avg_diluted_sharesout_adj_a / close)`: S=0.28, F=0.08, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_avg_diluted_sharesout_adj_a, 5))`: S=-0.67, F=-0.35, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_avg_diluted_sharesout_adj_a, 5))` | TOP200 | 0.89 | 0.67 | 22.9% | 80% | all-weather |
| `rank(ts_delta(fn_avg_diluted_sharesout_adj_a, 5))` | TOP1000 | 0.59 | 0.28 | 24.0% | 80% | mixed |
| `rank(ts_delta(fn_avg_diluted_sharesout_adj_a, 5))` | TOP500 | 0.47 | 0.21 | 20.7% | 80% | mixed |
| `rank(ts_delta(fn_avg_diluted_sharesout_adj_a, 5))` | TOP3000 | 0.39 | 0.13 | 24.1% | 60% | bear-only |
| `rank(fn_avg_diluted_sharesout_adj_a / close)` | TOP3000 | 0.19 | 0.04 | 5.2% | 60% | bull-only |
| `rank(fn_avg_diluted_sharesout_adj_a / close)` | TOP200 | 0.09 | 0.03 | 14.2% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_finite_lived_intangible_assets_net_a: 0.307 (weakly positively correlated)
- fn_payments_to_acquire_businesses_net_of_cash_acquired_a: 0.269 (weakly positively correlated)
- fnd2_unrgtxbnfinregfprtxps: 0.251 (weakly positively correlated)
- fn_incremental_shares_attributable_to_share_based_payment_a: 0.221 (weakly positively correlated)
- fn_accum_oth_income_loss_fx_adj_net_of_tax_a: 0.210 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| growth_potential_rank_derivative | model16 | -0.06 | 1.29 | +0.40 | -0.61 | yes |
| relative_valuation_rank_derivative | model16 | -0.06 | 1.33 | +0.40 | -0.53 | yes |
| earnings_certainty_rank_derivative | model16 | -0.06 | 1.33 | +0.40 | -0.53 | yes |
| analyst_revision_rank_derivative | model16 | -0.06 | 1.33 | +0.40 | -0.53 | yes |
| multi_factor_static_score_derivative | model16 | -0.06 | 1.26 | +0.37 | -0.67 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
