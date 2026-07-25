---
field: fnd6_optprcwa
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.91
best_fitness: 0.77
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1413
ann_vol: 0.1
hit_rate: 0.4802
rolling_sharpe_min: -1.369
rolling_sharpe_max: 2.527
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 33
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.37
---
# fnd6_optprcwa (fundamental6)

*Options Exercisable - Weighted Avg Price*

## Signal Profile
- `rank(fnd6_optprcwa)`: S=0.40, F=0.25, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_optprcwa / close)`: S=0.91, F=0.77, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_optprcwa, 5))`: S=0.37, F=0.11, T=36.6%, INFERIOR (TOP500)
- `-rank(fnd6_optprcwa)`: S=-0.08, F=-0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcwa, 5))`: S=0.54, F=0.17, T=36.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optprcwa, 22)`: S=0.04, F=0.00, T=43.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optprcwa, 10)`: S=0.13, F=0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optprcwa, 22))`: S=0.19, F=0.05, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcwa)`: S=-0.40, F=-0.25, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcwa / close)`: S=-0.91, F=-0.77, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.89, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.24 (negative), ret=-1.8%
  - 2020: S=0.99 (moderate), ret=+13.3%
  - 2021: S=1.58 (strong), ret=+15.8%
  - 2022: S=2.07 (strong), ret=+16.7%
  - 2023: S=-0.05 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 14.13% over 470 days (recovered)
- Annualized: return +8.9%, volatility 10.0% (fraction of booksize)
- Hit rate: 48.0% positive days
- Tail shape: skew +0.89, excess kurtosis +4.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.37, max 2.53, latest 0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.87%; worst month: -4.53%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.17
- Sideways: S=-1.02
- Bear: S=1.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_optprcwa, 5))` S=0.54, F=0.17, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_optprcwa)`: S=-0.40, F=-0.25, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcwa / close)`: S=-0.91, F=-0.77, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcwa, 5))`: S=0.54, F=0.17, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optprcwa / close)` | TOP3000 | 0.89 | 0.77 | 14.1% | 60% | all-weather |
| `rank(fnd6_optprcwa / close)` | TOP500 | 0.75 | 0.65 | 15.7% | 80% | bull-only |
| `rank(fnd6_optprcwa / close)` | TOP1000 | 0.58 | 0.43 | 17.2% | 80% | bull-only |
| `rank(fnd6_optprcwa)` | TOP3000 | 0.39 | 0.25 | 34.6% | 60% | bull-only |
| `rank(fnd6_optprcwa / close)` | TOP200 | 0.37 | 0.25 | 21.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_optprcwa, 5))` | TOP500 | 0.38 | 0.11 | 14.8% | 80% | bull-only |
| `rank(fnd6_optprcwa)` | TOP1000 | 0.07 | 0.02 | 34.9% | 40% | bull-only |
| `rank(fnd6_optprcwa)` | TOP500 | 0.07 | 0.02 | 38.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_optprcby: 0.990 (strongly positively correlated)
- fn_comp_options_exercisable_weighted_avg_a: 0.965 (strongly positively correlated)
- fnd6_optprcey: 0.965 (strongly positively correlated)
- fnd6_optprcca: 0.954 (strongly positively correlated)
- fn_comp_options_out_weighted_avg_a: 0.921 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 1.83 | +0.66 | -0.46 | yes |
| rp_ess_revenue | news18 | -0.33 | 1.54 | +0.65 | -0.33 | yes |
| max_gross_income_guidance | analyst4 | -0.28 | 1.48 | +0.59 | -0.72 | yes |
| min_gross_income_guidance | analyst4 | -0.28 | 1.47 | +0.58 | -0.73 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.31 | 1.44 | +0.55 | -0.77 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
