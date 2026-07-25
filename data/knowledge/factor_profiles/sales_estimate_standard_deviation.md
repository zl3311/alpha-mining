---
field: sales_estimate_standard_deviation
dataset: analyst4
best_template: rank_level
best_sharpe: 0.89
best_fitness: 0.59
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: bull-only
n_variations_with_pnl: 11
max_drawdown: 0.1137
ann_vol: 0.0622
hit_rate: 0.5441
rolling_sharpe_min: -1.392
rolling_sharpe_max: 2.91
top_merge_partner: fn_def_tax_assets_liab_net_a
redundancy_cluster: 50
negated_best_sharpe: -0.39
negated_best_template: rank_neg_delta
negated_best_fitness: -0.07
n_negated_sims: 4
direction_gap: -1.28
---
# sales_estimate_standard_deviation (analyst4)

*Sales - standard deviation of estimations*

## Signal Profile
- `rank(sales_estimate_standard_deviation)`: S=0.89, F=0.59, T=4.2%, INFERIOR (TOP3000)
- `rank(sales_estimate_standard_deviation / close)`: S=0.82, F=0.52, T=4.4%, INFERIOR (TOP3000)
- `rank(ts_delta(sales_estimate_standard_deviation, 5))`: S=0.53, F=0.15, T=38.9%, INFERIOR (TOP500)
- `-rank(sales_estimate_standard_deviation)`: S=-0.48, F=-0.26, T=5.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_standard_deviation, 5))`: S=-0.39, F=-0.07, T=38.4%, INFERIOR (TOP3000)
- `ts_zscore(sales_estimate_standard_deviation, 22)`: S=0.47, F=0.13, T=33.6%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_standard_deviation, 10)`: S=0.05, F=0.01, T=4.1%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_standard_deviation, 22))`: S=0.82, F=0.34, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_standard_deviation)`: S=-0.89, F=-0.59, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_standard_deviation / close)`: S=-0.82, F=-0.52, T=4.4%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.88, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.33 (weak), ret=+1.3%
  - 2020: S=-0.88 (negative), ret=-4.9%
  - 2021: S=1.27 (moderate), ret=+10.2%
  - 2022: S=2.30 (strong), ret=+15.9%
  - 2023: S=0.83 (moderate), ret=+4.3%

## Risk & Drawdown
- Max drawdown: 11.37% over 605 days (recovered)
- Annualized: return +5.5%, volatility 6.2% (fraction of booksize)
- Hit rate: 54.4% positive days
- Tail shape: skew -0.05, excess kurtosis +0.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.39, max 2.91, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.43%; worst month: -3.56%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.23
- Sideways: S=1.00
- Bear: S=-2.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(sales_estimate_standard_deviation, 5))` S=-0.39, F=-0.07, INFERIOR
Direction gap: -1.28 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * sales_estimate_standard_deviation)`: S=-0.89, F=-0.59, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_standard_deviation / close)`: S=-0.82, F=-0.52, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_standard_deviation, 5))`: S=-0.39, F=-0.07, T=38.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(sales_estimate_standard_deviation)` | TOP3000 | 0.88 | 0.59 | 11.4% | 80% | bull-only |
| `rank(sales_estimate_standard_deviation / close)` | TOP3000 | 0.82 | 0.52 | 10.7% | 80% | all-weather |
| `rank(sales_estimate_standard_deviation / close)` | TOP1000 | 0.62 | 0.39 | 10.4% | 100% | mixed |
| `rank(sales_estimate_standard_deviation)` | TOP1000 | 0.47 | 0.26 | 13.0% | 80% | bull-only |
| `rank(sales_estimate_standard_deviation)` | TOP500 | 0.34 | 0.17 | 18.1% | 80% | bull-only |
| `rank(ts_delta(sales_estimate_standard_deviation, 5))` | TOP500 | 0.54 | 0.15 | 12.8% | 80% | all-weather |
| `rank(sales_estimate_standard_deviation / close)` | TOP200 | 0.30 | 0.14 | 19.6% | 80% | mixed |
| `rank(ts_delta(sales_estimate_standard_deviation, 5))` | TOP1000 | 0.44 | 0.10 | 6.7% | 60% | mixed |
| `rank(sales_estimate_standard_deviation / close)` | TOP500 | 0.21 | 0.08 | 11.7% | 100% | mixed |
| `rank(sales_estimate_standard_deviation)` | TOP200 | 0.19 | 0.08 | 23.2% | 60% | bull-only |
| `rank(ts_delta(sales_estimate_standard_deviation, 5))` | TOP3000 | 0.39 | 0.07 | 5.9% | 60% | weak |

## Correlation Notes
Top correlates:
- sales_estimate_stddev_quarterly: 1.000 (strongly positively correlated)
- highest_sales_estimate: 0.893 (strongly positively correlated)
- median_sales_estimate: 0.889 (strongly positively correlated)
- sales_estimate_average_annual: 0.888 (strongly positively correlated)
- anl4_ebit_std: 0.885 (strongly positively correlated)

Redundancy cluster #50: 3 similar fields, mean |rho| 0.824 (representative: sales_estimate_stddev_quarterly). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.35 | 1.45 | +0.54 | -0.25 | yes |
| operating_profit_before_depr_amort_max_guidance_qtr | analyst4 | -0.33 | 1.56 | +0.61 | -0.91 | no |
| operating_profit_before_depr_amort_min_guidance_qtr | analyst4 | -0.33 | 1.56 | +0.60 | -0.91 | no |
| fnd6_txtubadjust | fundamental6 | -0.14 | 1.31 | +0.43 | -0.90 | yes |
| parkinson_volatility_120 | option8 | -0.22 | 1.40 | +0.51 | +0.02 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
