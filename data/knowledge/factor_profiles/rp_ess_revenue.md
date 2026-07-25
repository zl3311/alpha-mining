---
field: rp_ess_revenue
dataset: news18
best_template: rank_level
best_sharpe: 0.88
best_fitness: 0.26
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.136
ann_vol: 0.1001
hit_rate: 0.5215
rolling_sharpe_min: -0.292
rolling_sharpe_max: 2.498
top_merge_partner: fnd6_dpvieb
negated_best_sharpe: 0.27
negated_best_template: neg_rank_level
negated_best_fitness: 0.03
n_negated_sims: 4
direction_gap: -0.61
---
# rp_ess_revenue (news18)

*Event sentiment score of revenue news*

## Signal Profile
- `rank(rp_ess_revenue)`: S=0.88, F=0.26, T=100.7%, INFERIOR (TOP200)
- `rank(ts_delta(rp_ess_revenue, 5))`: S=0.82, F=0.20, T=133.1%, INFERIOR (TOP200)
- `-rank(rp_ess_revenue)`: S=0.18, F=0.02, T=123.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_revenue, 5))`: S=-0.49, F=-0.07, T=163.3%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_revenue, 63)`: S=0.10, F=0.01, T=129.2%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_revenue, 10)`: S=-0.13, F=-0.03, T=14.2%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_revenue, 22))`: S=-0.08, F=0.00, T=136.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_revenue)`: S=0.27, F=0.03, T=140.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_revenue / close)`: S=0.08, F=0.00, T=141.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/14P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.89, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.94 (moderate), ret=+7.4%
  - 2020: S=1.30 (moderate), ret=+16.0%
  - 2021: S=0.50 (moderate), ret=+5.8%
  - 2022: S=0.87 (moderate), ret=+8.4%
  - 2023: S=0.97 (moderate), ret=+6.2%

## Risk & Drawdown
- Max drawdown: 13.60% over 383 days (recovered)
- Annualized: return +8.9%, volatility 10.0% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew -0.01, excess kurtosis +1.49

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.29, max 2.50, latest 0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +7.63%; worst month: -4.47%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.00
- Sideways: S=0.63
- Bear: S=2.07

## Negated Direction
Best negated: `rank(-1 * rp_ess_revenue)` S=0.27, F=0.03, INFERIOR
Direction gap: -0.61 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_ess_revenue)`: S=0.27, F=0.03, T=140.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_revenue / close)`: S=0.08, F=0.00, T=141.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_revenue, 5))`: S=-0.49, F=-0.07, T=163.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_ess_revenue)` | TOP200 | 0.89 | 0.26 | 13.6% | 100% | mixed |
| `rank(ts_delta(rp_ess_revenue, 5))` | TOP200 | 0.82 | 0.20 | 17.9% | 60% | all-weather |
| `rank(ts_delta(rp_ess_revenue, 5))` | TOP500 | 0.88 | 0.20 | 9.1% | 60% | all-weather |
| `rank(ts_delta(rp_ess_revenue, 5))` | TOP1000 | 0.75 | 0.14 | 8.9% | 80% | all-weather |
| `rank(rp_ess_revenue)` | TOP500 | 0.51 | 0.09 | 7.3% | 40% | mixed |
| `rank(ts_delta(rp_ess_revenue, 5))` | TOP3000 | 0.50 | 0.07 | 15.6% | 100% | weak |

## Correlation Notes
Top correlates:
- fn_accum_depr_depletion_and_amortization_ppne_a: -0.393 (weakly negatively correlated)
- fn_mne_a: -0.393 (weakly negatively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_q: -0.385 (weakly negatively correlated)
- fnd6_dpvieb: -0.383 (weakly negatively correlated)
- fnd6_optprcex: -0.382 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_dpvieb | fundamental6 | -0.38 | 1.73 | +0.69 | -0.79 | yes |
| fnd6_newa1v1300_dpact | fundamental6 | -0.38 | 1.72 | +0.69 | -0.79 | yes |
| fn_accum_depr_depletion_and_amortization_ppne_q | fundamental2 | -0.39 | 1.68 | +0.69 | -0.77 | yes |
| fnd6_optprcex | fundamental6 | -0.38 | 1.61 | +0.71 | -0.51 | yes |
| sales_ps | fundamental_value | -0.38 | 1.75 | +0.69 | -0.67 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
