---
field: fnd6_optprcca
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.85
best_fitness: 0.72
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.2006
ann_vol: 0.1063
hit_rate: 0.4874
rolling_sharpe_min: -1.531
rolling_sharpe_max: 2.722
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 33
negated_best_sharpe: 0.2
negated_best_template: neg_rank_level
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.65
---
# fnd6_optprcca (fundamental6)

*Options Cancelled - Price*

## Signal Profile
- `rank(fnd6_optprcca)`: S=0.42, F=0.27, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_optprcca / close)`: S=0.85, F=0.72, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_optprcca, 5))`: S=0.55, F=0.21, T=36.1%, INFERIOR (TOP500)
- `-rank(fnd6_optprcca)`: S=-0.02, F=0.00, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcca, 5))`: S=0.08, F=0.02, T=33.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optprcca, 22)`: S=0.38, F=0.14, T=41.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optprcca, 10)`: S=-0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optprcca, 22))`: S=0.30, F=0.11, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcca)`: S=0.20, F=0.10, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcca / close)`: S=-0.03, F=-0.01, T=4.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/25P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.84, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.45 (negative), ret=-3.5%
  - 2020: S=0.97 (moderate), ret=+12.8%
  - 2021: S=1.94 (strong), ret=+19.8%
  - 2022: S=1.84 (strong), ret=+16.2%
  - 2023: S=-0.15 (negative), ret=-1.7%

## Risk & Drawdown
- Max drawdown: 20.06% over 330 days (not yet recovered, ongoing at window end)
- Annualized: return +8.9%, volatility 10.6% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.81, excess kurtosis +2.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.53, max 2.72, latest 0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.99%; worst month: -4.83%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.74
- Sideways: S=-0.92
- Bear: S=1.51

## Negated Direction
Best negated: `rank(-1 * fnd6_optprcca)` S=0.20, F=0.10, INFERIOR
Direction gap: -0.65 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_optprcca)`: S=0.20, F=0.10, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optprcca / close)`: S=-0.03, F=-0.01, T=4.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optprcca, 5))`: S=0.08, F=0.02, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optprcca / close)` | TOP3000 | 0.84 | 0.72 | 20.1% | 60% | all-weather |
| `rank(fnd6_optprcca / close)` | TOP500 | 0.52 | 0.38 | 22.6% | 80% | mixed |
| `rank(fnd6_optprcca)` | TOP3000 | 0.41 | 0.27 | 37.0% | 60% | bull-only |
| `rank(fnd6_optprcca / close)` | TOP1000 | 0.39 | 0.24 | 17.2% | 80% | mixed |
| `rank(ts_delta(fnd6_optprcca, 5))` | TOP500 | 0.56 | 0.21 | 20.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_optprcca, 5))` | TOP1000 | 0.49 | 0.16 | 16.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_optprcey: 0.974 (strongly positively correlated)
- fnd6_optprcby: 0.962 (strongly positively correlated)
- fnd6_optprcwa: 0.954 (strongly positively correlated)
- fn_comp_options_out_weighted_avg_a: 0.944 (strongly positively correlated)
- fn_comp_options_exercisable_weighted_avg_a: 0.940 (strongly positively correlated)

Redundancy cluster #33: 12 similar fields, mean |rho| 0.787 (representative: anl4_afv4_eps_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.75 | +0.58 | -0.56 | yes |
| rp_ess_revenue | news18 | -0.28 | 1.44 | +0.55 | -0.42 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.25 | 1.34 | +0.50 | -0.85 | yes |
| min_gross_income_guidance | analyst4 | -0.24 | 1.39 | +0.52 | -0.64 | yes |
| max_gross_income_guidance | analyst4 | -0.24 | 1.40 | +0.51 | -0.63 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
