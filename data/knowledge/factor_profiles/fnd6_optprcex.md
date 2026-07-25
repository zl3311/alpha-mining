---
field: fnd6_optprcex
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.93
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.1154
ann_vol: 0.0978
hit_rate: 0.4761
rolling_sharpe_min: -1.34
rolling_sharpe_max: 2.872
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.13
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.8
---
# fnd6_optprcex (fundamental6)

*Options Exercised - Price*

## Signal Profile
- `rank(fnd6_optprcex)`: S=0.43, F=0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_optprcex / close)`: S=0.93, F=0.79, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_optprcex, 5))`: S=0.66, F=0.27, T=36.6%, INFERIOR (TOP500)
- `-rank(fnd6_optprcex)`: S=-0.14, F=-0.05, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcex, 5))`: S=0.13, F=0.02, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optprcex, 22)`: S=0.65, F=0.29, T=43.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optprcex, 10)`: S=0.32, F=0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optprcex, 22))`: S=0.34, F=0.13, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcex)`: S=-0.43, F=-0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcex / close)`: S=-0.93, F=-0.79, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.90, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.24 (negative), ret=-1.5%
  - 2020: S=0.22 (weak), ret=+2.9%
  - 2021: S=1.55 (strong), ret=+17.2%
  - 2022: S=2.54 (strong), ret=+22.4%
  - 2023: S=0.35 (weak), ret=+2.4%

## Risk & Drawdown
- Max drawdown: 11.54% over 259 days (recovered)
- Annualized: return +8.8%, volatility 9.8% (fraction of booksize)
- Hit rate: 47.6% positive days
- Tail shape: skew +0.93, excess kurtosis +5.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.34, max 2.87, latest 0.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +8.91%; worst month: -3.50%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.93
- Sideways: S=-0.83
- Bear: S=0.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_optprcex, 5))` S=0.13, F=0.02, INFERIOR
Direction gap: -0.80 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_optprcex)`: S=-0.43, F=-0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcex / close)`: S=-0.93, F=-0.79, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcex, 5))`: S=0.13, F=0.02, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optprcex / close)` | TOP3000 | 0.90 | 0.79 | 11.5% | 80% | mixed |
| `rank(fnd6_optprcex / close)` | TOP500 | 0.59 | 0.48 | 21.0% | 60% | bull-only |
| `rank(fnd6_optprcex / close)` | TOP1000 | 0.48 | 0.35 | 19.2% | 40% | bull-only |
| `rank(fnd6_optprcex)` | TOP3000 | 0.42 | 0.30 | 44.9% | 80% | bull-only |
| `rank(ts_delta(fnd6_optprcex, 5))` | TOP500 | 0.66 | 0.27 | 14.1% | 80% | mixed |
| `rank(fnd6_optprcex / close)` | TOP200 | 0.22 | 0.13 | 37.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_optprcex, 5))` | TOP1000 | 0.25 | 0.06 | 16.6% | 60% | bull-only |
| `rank(fnd6_optprcex)` | TOP1000 | 0.13 | 0.05 | 41.0% | 60% | bull-only |
| `rank(fnd6_optprcex)` | TOP500 | 0.05 | 0.02 | 52.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_comp_options_exercises_weighted_avg_a: 0.955 (strongly positively correlated)
- fnd6_optprcwa: 0.915 (strongly positively correlated)
- fnd6_optprcby: 0.907 (strongly positively correlated)
- fnd6_optprcey: 0.876 (strongly positively correlated)
- fn_comp_options_exercisable_weighted_avg_a: 0.875 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.38 | 1.61 | +0.71 | -0.51 | yes |
| anl4_epsr_flag | analyst4 | -0.39 | 1.88 | +0.70 | -0.47 | yes |
| max_gross_income_guidance | analyst4 | -0.30 | 1.51 | +0.61 | -0.85 | yes |
| min_gross_income_guidance | analyst4 | -0.30 | 1.50 | +0.60 | -0.86 | yes |
| anl4_rd_exp_flag | analyst4 | -0.32 | 1.66 | +0.63 | -0.45 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
