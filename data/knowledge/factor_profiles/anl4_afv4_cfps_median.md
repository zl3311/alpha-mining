---
field: anl4_afv4_cfps_median
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.89
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 11
max_drawdown: 0.117
ann_vol: 0.0802
hit_rate: 0.4996
rolling_sharpe_min: -1.068
rolling_sharpe_max: 2.577
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.02
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.87
---
# anl4_afv4_cfps_median (analyst4)

*Cash Flow Per Share - Median value among forecasts for the annual frequency*

## Signal Profile
- `rank(anl4_afv4_cfps_median)`: S=0.30, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_afv4_cfps_median / close)`: S=0.89, F=0.67, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_afv4_cfps_median, 5))`: S=0.39, F=0.13, T=35.5%, INFERIOR (TOP200)
- `-rank(anl4_afv4_cfps_median)`: S=-0.17, F=-0.06, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_cfps_median, 5))`: S=-0.18, F=-0.03, T=36.8%, INFERIOR (TOP3000)
- `ts_zscore(anl4_afv4_cfps_median, 22)`: S=0.13, F=0.02, T=34.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_cfps_median, 10)`: S=-0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_cfps_median, 22))`: S=0.09, F=0.01, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_median)`: S=0.02, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_median / close)`: S=-0.16, F=-0.06, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.88, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.21 (weak), ret=+1.3%
  - 2020: S=0.41 (weak), ret=+4.6%
  - 2021: S=1.07 (moderate), ret=+8.2%
  - 2022: S=2.39 (strong), ret=+17.2%
  - 2023: S=0.67 (moderate), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 11.70% over 497 days (recovered)
- Annualized: return +7.1%, volatility 8.0% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.79, excess kurtosis +4.33

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.07, max 2.58, latest 0.71

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.03%; worst month: -5.18%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.63
- Sideways: S=-0.11
- Bear: S=-0.03

## Negated Direction
Best negated: `rank(-1 * anl4_afv4_cfps_median)` S=0.02, F=0.00, INFERIOR
Direction gap: -0.87 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_afv4_cfps_median)`: S=0.02, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_median / close)`: S=-0.16, F=-0.06, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_cfps_median, 5))`: S=-0.18, F=-0.03, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_cfps_median / close)` | TOP3000 | 0.88 | 0.67 | 11.7% | 100% | mixed |
| `rank(anl4_afv4_cfps_median / close)` | TOP1000 | 0.57 | 0.39 | 16.4% | 80% | bull-only |
| `rank(anl4_afv4_cfps_median)` | TOP3000 | 0.29 | 0.14 | 30.5% | 80% | bull-only |
| `rank(ts_delta(anl4_afv4_cfps_median, 5))` | TOP200 | 0.40 | 0.13 | 19.2% | 60% | weak |
| `rank(ts_delta(anl4_afv4_cfps_median, 5))` | TOP3000 | 0.47 | 0.10 | 6.6% | 60% | weak |
| `rank(anl4_afv4_cfps_median)` | TOP200 | 0.16 | 0.07 | 34.8% | 60% | bull-only |
| `rank(anl4_afv4_cfps_median / close)` | TOP200 | 0.16 | 0.07 | 43.9% | 40% | bull-only |
| `rank(anl4_afv4_cfps_median / close)` | TOP500 | 0.15 | 0.06 | 27.7% | 60% | bull-only |
| `rank(anl4_afv4_cfps_median)` | TOP1000 | 0.16 | 0.06 | 30.7% | 60% | bull-only |
| `rank(ts_delta(anl4_afv4_cfps_median, 5))` | TOP1000 | 0.21 | 0.03 | 7.7% | 60% | weak |
| `rank(ts_delta(anl4_afv4_cfps_median, 5))` | TOP500 | 0.19 | 0.03 | 10.0% | 40% | mixed |

## Correlation Notes
Top correlates:
- anl4_afv4_cfps_mean: 1.000 (strongly positively correlated)
- anl4_afv4_cfps_high: 0.997 (strongly positively correlated)
- anl4_afv4_cfps_low: 0.990 (strongly positively correlated)
- sales_ps: 0.865 (strongly positively correlated)
- anl4_afv4_eps_high: 0.849 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.54 | +0.65 | -0.36 | yes |
| fnd6_txtubadjust | fundamental6 | -0.21 | 1.38 | +0.49 | -0.87 | yes |
| max_gross_income_guidance | analyst4 | -0.29 | 1.46 | +0.58 | -0.90 | no |
| min_gross_income_guidance | analyst4 | -0.29 | 1.45 | +0.56 | -0.91 | no |
| anl4_epsr_flag | analyst4 | -0.34 | 1.80 | +0.62 | -0.27 | no |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
