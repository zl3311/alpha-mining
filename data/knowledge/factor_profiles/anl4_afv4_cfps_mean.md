---
field: anl4_afv4_cfps_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.88
best_fitness: 0.66
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1173
ann_vol: 0.0802
hit_rate: 0.5004
rolling_sharpe_min: -1.086
rolling_sharpe_max: 2.574
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.02
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.86
---
# anl4_afv4_cfps_mean (analyst4)

*Cash Flow Per Share - average of estimations for the annual frequency*

## Signal Profile
- `rank(anl4_afv4_cfps_mean)`: S=0.30, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_afv4_cfps_mean / close)`: S=0.88, F=0.66, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_afv4_cfps_mean, 5))`: S=0.29, F=0.05, T=36.2%, INFERIOR (TOP3000)
- `-rank(anl4_afv4_cfps_mean)`: S=-0.17, F=-0.06, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_cfps_mean, 5))`: S=0.05, F=0.00, T=36.7%, INFERIOR (TOP3000)
- `ts_zscore(anl4_afv4_cfps_mean, 22)`: S=0.33, F=0.09, T=33.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_cfps_mean, 10)`: S=-0.03, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_cfps_mean, 22))`: S=0.02, F=0.00, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_mean)`: S=0.02, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_mean / close)`: S=-0.16, F=-0.06, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.87, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+1.2%
  - 2020: S=0.40 (weak), ret=+4.5%
  - 2021: S=1.05 (moderate), ret=+8.1%
  - 2022: S=2.38 (strong), ret=+17.2%
  - 2023: S=0.65 (moderate), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 11.73% over 497 days (recovered)
- Annualized: return +7.0%, volatility 8.0% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.79, excess kurtosis +4.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 2.57, latest 0.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.07%; worst month: -5.13%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.62
- Sideways: S=-0.12
- Bear: S=-0.04

## Negated Direction
Best negated: `rank(-1 * anl4_afv4_cfps_mean)` S=0.02, F=0.00, INFERIOR
Direction gap: -0.86 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_afv4_cfps_mean)`: S=0.02, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_mean / close)`: S=-0.16, F=-0.06, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_cfps_mean, 5))`: S=0.05, F=0.00, T=36.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_cfps_mean / close)` | TOP3000 | 0.87 | 0.66 | 11.7% | 100% | mixed |
| `rank(anl4_afv4_cfps_mean / close)` | TOP1000 | 0.56 | 0.37 | 16.5% | 80% | bull-only |
| `rank(anl4_afv4_cfps_mean)` | TOP3000 | 0.29 | 0.14 | 30.6% | 80% | bull-only |
| `rank(anl4_afv4_cfps_mean / close)` | TOP200 | 0.17 | 0.08 | 43.9% | 40% | bull-only |
| `rank(anl4_afv4_cfps_mean)` | TOP200 | 0.14 | 0.06 | 34.5% | 60% | bull-only |
| `rank(anl4_afv4_cfps_mean / close)` | TOP500 | 0.15 | 0.06 | 27.7% | 60% | bull-only |
| `rank(anl4_afv4_cfps_mean)` | TOP1000 | 0.16 | 0.06 | 30.7% | 60% | bull-only |
| `rank(ts_delta(anl4_afv4_cfps_mean, 5))` | TOP3000 | 0.30 | 0.05 | 7.5% | 40% | mixed |

## Correlation Notes
Top correlates:
- anl4_afv4_cfps_median: 1.000 (strongly positively correlated)
- anl4_afv4_cfps_high: 0.997 (strongly positively correlated)
- anl4_afv4_cfps_low: 0.990 (strongly positively correlated)
- sales_ps: 0.865 (strongly positively correlated)
- anl4_afv4_eps_high: 0.849 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.53 | +0.64 | -0.36 | yes |
| fnd6_txtubadjust | fundamental6 | -0.21 | 1.37 | +0.49 | -0.87 | yes |
| max_gross_income_guidance | analyst4 | -0.29 | 1.45 | +0.57 | -0.90 | no |
| min_gross_income_guidance | analyst4 | -0.29 | 1.44 | +0.56 | -0.91 | no |
| anl4_epsr_flag | analyst4 | -0.34 | 1.79 | +0.61 | -0.27 | no |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
