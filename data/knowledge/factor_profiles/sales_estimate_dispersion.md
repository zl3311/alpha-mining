---
field: sales_estimate_dispersion
dataset: analyst4
best_template: rank_level
best_sharpe: 0.79
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1348
ann_vol: 0.0577
hit_rate: 0.5368
rolling_sharpe_min: -1.661
rolling_sharpe_max: 2.92
top_merge_partner: operating_profit_before_depr_amort_max_guidance_qtr
redundancy_cluster: 32
negated_best_sharpe: 0.64
negated_best_template: neg_rank_level
negated_best_fitness: 0.48
n_negated_sims: 10
direction_gap: -0.15
---
# sales_estimate_dispersion (analyst4)

*Standard deviation of Sales estimations for the annual period.*

## Signal Profile
- `rank(sales_estimate_dispersion)`: S=0.79, F=0.48, T=3.5%, INFERIOR (TOP3000)
- `rank(sales_estimate_dispersion / close)`: S=0.72, F=0.45, T=4.4%, INFERIOR (TOP1000)
- `rank(ts_delta(sales_estimate_dispersion, 5))`: S=0.00, F=0.00, T=37.5%, INFERIOR (TOP3000)
- `-rank(sales_estimate_dispersion)`: S=-0.72, F=-0.45, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_dispersion, 5))`: S=0.40, F=0.13, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(sales_estimate_dispersion, 22)`: S=-0.04, F=0.00, T=32.0%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_dispersion, 10)`: S=-0.04, F=-0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_dispersion, 22))`: S=-0.23, F=-0.05, T=16.9%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_dispersion)`: S=0.64, F=0.48, T=5.1%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_dispersion / close)`: S=-0.06, F=-0.01, T=4.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.01 (moderate), ret=+4.2%
  - 2020: S=-0.87 (negative), ret=-4.6%
  - 2021: S=0.52 (moderate), ret=+3.9%
  - 2022: S=2.25 (strong), ret=+13.0%
  - 2023: S=1.29 (moderate), ret=+6.3%

## Risk & Drawdown
- Max drawdown: 13.48% over 556 days (recovered)
- Annualized: return +4.7%, volatility 5.8% (fraction of booksize)
- Hit rate: 53.7% positive days
- Tail shape: skew +0.06, excess kurtosis +1.64

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.66, max 2.92, latest 1.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.65%; worst month: -4.29%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.05
- Sideways: S=1.62
- Bear: S=-2.33

## Negated Direction
Best negated: `rank(-1 * sales_estimate_dispersion)` S=0.64, F=0.48, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sales_estimate_dispersion)`: S=0.64, F=0.48, T=5.1%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_dispersion / close)`: S=-0.06, F=-0.01, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_dispersion, 5))`: S=0.40, F=0.13, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_estimate_dispersion)` | TOP3000 | 0.81 | 0.48 | 13.5% | 80% | bull-only |
| `rank(sales_estimate_dispersion)` | TOP1000 | 0.72 | 0.45 | 16.7% | 80% | bull-only |
| `rank(sales_estimate_dispersion / close)` | TOP1000 | 0.72 | 0.45 | 9.6% | 100% | mixed |
| `rank(sales_estimate_dispersion / close)` | TOP3000 | 0.59 | 0.33 | 11.8% | 100% | all-weather |
| `rank(sales_estimate_dispersion / close)` | TOP500 | 0.45 | 0.24 | 16.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- highest_sales_estimate: 0.821 (strongly positively correlated)
- sales_estimate_stddev_quarterly: 0.809 (strongly positively correlated)
- sales_estimate_standard_deviation: 0.809 (strongly positively correlated)
- anl4_dts_ptp: 0.808 (strongly positively correlated)
- median_sales_estimate: 0.807 (strongly positively correlated)

Redundancy cluster #32: 9 similar fields, mean |rho| 0.765 (representative: fnd6_fopox). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| operating_profit_before_depr_amort_max_guidance_qtr | analyst4 | -0.30 | 1.47 | +0.52 | -0.98 | no |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.29 | 1.34 | +0.43 | -0.38 | yes |
| operating_profit_before_depr_amort_min_guidance_qtr | analyst4 | -0.30 | 1.48 | +0.52 | -0.98 | no |
| snt_value_fast_d1 | socialmedia12 | -0.16 | 1.27 | +0.38 | -0.54 | yes |
| fnd6_txtubadjust | fundamental6 | -0.06 | 1.20 | +0.35 | -0.84 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
