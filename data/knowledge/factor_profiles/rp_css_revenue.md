---
field: rp_css_revenue
dataset: news18
cluster: news18_income_revenue
coverage: 0.5
community_alphas: 1177
best_template: rank_level
best_sharpe: 0.83
best_fitness: 0.21
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0873
ann_vol: 0.0859
hit_rate: 0.5198
rolling_sharpe_min: -0.594
rolling_sharpe_max: 2.26
top_merge_partner: parkinson_volatility_120
negated_best_sharpe: 0.34
negated_best_template: neg_rank_level
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: -0.49
---
# rp_css_revenue (news18)

*Composite sentiment score of revenue news*

## Signal Profile
- `rank(rp_css_revenue)`: S=0.83, F=0.21, T=108.1%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_revenue, 5))`: S=0.44, F=0.08, T=136.8%, INFERIOR (TOP200)
- `-rank(rp_css_revenue)`: S=-0.16, F=-0.01, T=131.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_revenue, 5))`: S=0.16, F=0.01, T=166.7%, INFERIOR (TOP3000)
- `ts_zscore(rp_css_revenue, 22)`: S=0.35, F=0.04, T=138.9%, INFERIOR (TOP3000)
- `ts_mean(rp_css_revenue, 10)`: S=-0.56, F=-0.22, T=19.7%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_revenue, 22))`: S=0.37, F=0.04, T=140.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_revenue)`: S=0.34, F=0.04, T=146.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_revenue / close)`: S=0.02, F=0.00, T=149.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/14P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.85, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.03 (weak), ret=+0.2%
  - 2020: S=1.32 (moderate), ret=+12.6%
  - 2021: S=0.57 (moderate), ret=+5.3%
  - 2022: S=1.55 (strong), ret=+14.1%
  - 2023: S=0.57 (moderate), ret=+3.6%

## Risk & Drawdown
- Max drawdown: 8.73% over 276 days (recovered)
- Annualized: return +7.3%, volatility 8.6% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.19, excess kurtosis +1.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.59, max 2.26, latest 0.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.69%; worst month: -4.19%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.23
- Sideways: S=0.36
- Bear: S=1.88

## Negated Direction
Best negated: `rank(-1 * rp_css_revenue)` S=0.34, F=0.04, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_revenue)`: S=0.34, F=0.04, T=146.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_revenue / close)`: S=0.02, F=0.00, T=149.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_revenue, 5))`: S=0.16, F=0.01, T=166.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_revenue)` | TOP200 | 0.85 | 0.21 | 8.7% | 100% | mixed |
| `rank(ts_delta(rp_css_revenue, 5))` | TOP200 | 0.45 | 0.08 | 9.9% | 80% | all-weather |
| `rank(rp_css_revenue)` | TOP500 | 0.33 | 0.04 | 11.4% | 60% | bear-only |
| `rank(ts_delta(rp_css_revenue, 5))` | TOP500 | 0.33 | 0.04 | 9.5% | 80% | mixed |

## Correlation Notes
Top correlates:
- rp_css_earnings: 0.498 (moderately positively correlated)
- rp_css_ptg: 0.436 (moderately positively correlated)
- anl4_qfd1_az_cfps_number: -0.296 (weakly negatively correlated)
- anl4_qf_az_cfps_number: -0.296 (weakly negatively correlated)
- anl4_afv4_cfps_number: -0.279 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| parkinson_volatility_120 | option8 | -0.20 | 1.37 | +0.48 | -0.79 | yes |
| fn_op_lease_min_pay_due_in_5y_a | fundamental2 | -0.27 | 1.42 | +0.52 | -0.20 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.21 | 1.47 | +0.47 | -0.24 | yes |
| fnd6_optprcwa | fundamental6 | -0.21 | 1.38 | +0.49 | +0.75 | yes |
| fn_op_lease_min_pay_due_after_5y_a | fundamental2 | -0.25 | 1.39 | +0.47 | -0.22 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
