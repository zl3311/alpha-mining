---
field: fnd6_optprcby
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.01
best_fitness: 0.9
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.1341
ann_vol: 0.0994
hit_rate: 0.4899
rolling_sharpe_min: -1.457
rolling_sharpe_max: 2.709
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 33
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.52
---
# fnd6_optprcby (fundamental6)

*Options Outstanding Beginning of Year - Price*

## Signal Profile
- `rank(fnd6_optprcby)`: S=0.46, F=0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_optprcby / close)`: S=1.01, F=0.90, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_optprcby, 5))`: S=0.25, F=0.06, T=36.7%, INFERIOR (TOP500)
- `-rank(fnd6_optprcby)`: S=-0.10, F=-0.03, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcby, 5))`: S=0.49, F=0.14, T=36.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optprcby, 22)`: S=0.85, F=0.41, T=43.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optprcby, 10)`: S=0.16, F=0.06, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optprcby, 22))`: S=0.10, F=0.02, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcby)`: S=-0.46, F=-0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcby / close)`: S=-1.01, F=-0.90, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.00, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.26 (negative), ret=-1.8%
  - 2020: S=1.02 (moderate), ret=+13.6%
  - 2021: S=1.62 (strong), ret=+15.9%
  - 2022: S=2.29 (strong), ret=+18.3%
  - 2023: S=0.28 (weak), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 13.41% over 470 days (recovered)
- Annualized: return +9.9%, volatility 9.9% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.85, excess kurtosis +3.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.46, max 2.71, latest 0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +8.03%; worst month: -4.50%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.25
- Sideways: S=-0.88
- Bear: S=1.35

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_optprcby, 5))` S=0.49, F=0.14, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_optprcby)`: S=-0.46, F=-0.30, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcby / close)`: S=-1.01, F=-0.90, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcby, 5))`: S=0.49, F=0.14, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optprcby / close)` | TOP3000 | 1.00 | 0.90 | 13.4% | 80% | all-weather |
| `rank(fnd6_optprcby / close)` | TOP500 | 0.85 | 0.77 | 18.5% | 80% | bull-only |
| `rank(fnd6_optprcby / close)` | TOP1000 | 0.58 | 0.43 | 18.8% | 100% | mixed |
| `rank(fnd6_optprcby / close)` | TOP200 | 0.50 | 0.40 | 21.1% | 80% | bull-only |
| `rank(fnd6_optprcby)` | TOP3000 | 0.45 | 0.30 | 35.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_optprcby, 5))` | TOP500 | 0.24 | 0.06 | 16.9% | 60% | bull-only |
| `rank(fnd6_optprcby)` | TOP500 | 0.12 | 0.05 | 38.1% | 60% | bull-only |
| `rank(fnd6_optprcby)` | TOP1000 | 0.09 | 0.03 | 34.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_optprcwa: 0.990 (strongly positively correlated)
- fnd6_optprcey: 0.967 (strongly positively correlated)
- fn_comp_options_exercisable_weighted_avg_a: 0.963 (strongly positively correlated)
- fnd6_optprcca: 0.962 (strongly positively correlated)
- fn_comp_options_out_weighted_avg_a: 0.925 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.37 | 1.93 | +0.75 | -0.39 | yes |
| max_gross_income_guidance | analyst4 | -0.29 | 1.58 | +0.58 | -0.81 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.62 | +0.62 | -0.32 | yes |
| min_gross_income_guidance | analyst4 | -0.29 | 1.56 | +0.57 | -0.82 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.31 | 1.53 | +0.53 | -0.80 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
