---
field: fn_comp_options_out_weighted_avg_q
dataset: fundamental2
best_template: rank_delta
best_sharpe: 1.21
best_fitness: 0.87
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.2364
ann_vol: 0.1596
hit_rate: 0.5215
rolling_sharpe_min: -0.536
rolling_sharpe_max: 3.365
top_merge_partner: news_mins_4_pct_dn
negated_best_sharpe: 0.33
negated_best_template: neg_rank_level
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.88
---
# fn_comp_options_out_weighted_avg_q (fundamental2)

*Weighted average price at which grantees can acquire the shares reserved for issuance under the stock option plan.*

## Signal Profile
- `rank(fn_comp_options_out_weighted_avg_q)`: S=0.51, F=0.33, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_comp_options_out_weighted_avg_q / close)`: S=0.55, F=0.40, T=2.8%, INFERIOR (TOP500)
- `rank(ts_delta(fn_comp_options_out_weighted_avg_q, 5))`: S=1.21, F=0.87, T=36.8%, INFERIOR (TOP3000)
- `-rank(fn_comp_options_out_weighted_avg_q)`: S=0.25, F=0.13, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_out_weighted_avg_q, 5))`: S=-0.28, F=-0.14, T=27.8%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_options_out_weighted_avg_q, 63)`: S=0.36, F=0.20, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_options_out_weighted_avg_q, 10)`: S=0.02, F=0.01, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_options_out_weighted_avg_q, 22))`: S=-0.06, F=-0.01, T=18.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_weighted_avg_q)`: S=0.33, F=0.24, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_weighted_avg_q / close)`: S=-0.29, F=-0.18, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.23, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+3.2%
  - 2020: S=0.57 (moderate), ret=+9.1%
  - 2021: S=1.62 (strong), ret=+24.2%
  - 2022: S=2.59 (strong), ret=+46.4%
  - 2023: S=0.79 (moderate), ret=+13.6%

## Risk & Drawdown
- Max drawdown: 23.64% over 263 days (recovered)
- Annualized: return +19.7%, volatility 16.0% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.47, excess kurtosis +3.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.54, max 3.37, latest 0.69

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +16.27%; worst month: -13.91%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.65
- Sideways: S=2.21
- Bear: S=-0.10

## Negated Direction
Best negated: `rank(-1 * fn_comp_options_out_weighted_avg_q)` S=0.33, F=0.24, INFERIOR
Direction gap: -0.88 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_comp_options_out_weighted_avg_q)`: S=0.33, F=0.24, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_options_out_weighted_avg_q / close)`: S=-0.29, F=-0.18, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_options_out_weighted_avg_q, 5))`: S=-0.28, F=-0.14, T=27.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_comp_options_out_weighted_avg_q, 5))` | TOP3000 | 1.23 | 0.87 | 23.6% | 100% | mixed |
| `rank(fn_comp_options_out_weighted_avg_q / close)` | TOP500 | 0.54 | 0.40 | 15.6% | 80% | bull-only |
| `rank(fn_comp_options_out_weighted_avg_q)` | TOP3000 | 0.51 | 0.33 | 34.2% | 60% | bull-only |
| `rank(fn_comp_options_out_weighted_avg_q / close)` | TOP3000 | 0.49 | 0.31 | 15.8% | 80% | all-weather |
| `rank(fn_comp_options_out_weighted_avg_q / close)` | TOP200 | 0.28 | 0.18 | 29.2% | 60% | bull-only |
| `rank(fn_comp_options_out_weighted_avg_q / close)` | TOP1000 | 0.30 | 0.16 | 22.9% | 80% | bull-only |
| `rank(ts_delta(fn_comp_options_out_weighted_avg_q, 5))` | TOP200 | 0.23 | 0.11 | 44.4% | 60% | bull-only |
| `rank(ts_delta(fn_comp_options_out_weighted_avg_q, 5))` | TOP1000 | 0.21 | 0.07 | 35.6% | 40% | bull-only |
| `rank(ts_delta(fn_comp_options_out_weighted_avg_q, 5))` | TOP500 | 0.14 | 0.04 | 44.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_propplteqmuflmblgland: -0.208 (weakly negatively correlated)
- anl4_afv4_div_number: -0.207 (weakly negatively correlated)
- anl4_qfd1_az_cfps_number: -0.202 (weakly negatively correlated)
- anl4_qf_az_cfps_number: -0.202 (weakly negatively correlated)
- anl4_afv4_cfps_number: -0.197 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_mins_4_pct_dn | news12 | +0.02 | 1.77 | +0.47 | -0.64 | yes |
| fnd6_fatl | fundamental_capital_intensity | -0.12 | 1.74 | +0.50 | -0.20 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.15 | 1.69 | +0.45 | -0.57 | yes |
| implied_volatility_mean_10 | option8 | -0.01 | 1.72 | +0.49 | -0.14 | yes |
| rp_css_technical | news18 | -0.03 | 1.74 | +0.50 | +0.69 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
