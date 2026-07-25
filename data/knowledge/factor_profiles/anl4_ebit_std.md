---
field: anl4_ebit_std
dataset: analyst4
best_template: rank_level
best_sharpe: 0.87
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1255
ann_vol: 0.0608
hit_rate: 0.5393
rolling_sharpe_min: -1.425
rolling_sharpe_max: 3.048
top_merge_partner: fn_def_tax_assets_liab_net_a
redundancy_cluster: 32
negated_best_sharpe: 0.67
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.2
---
# anl4_ebit_std (analyst4)

*Earnings before interest and taxes - standard deviation of estimations*

## Signal Profile
- `rank(anl4_ebit_std)`: S=0.87, F=0.56, T=4.5%, INFERIOR (TOP3000)
- `rank(anl4_ebit_std / close)`: S=0.42, F=0.21, T=4.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ebit_std, 5))`: S=0.43, F=0.10, T=39.1%, INFERIOR (TOP1000)
- `-rank(anl4_ebit_std)`: S=-0.47, F=-0.25, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_std, 5))`: S=0.67, F=0.28, T=38.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_ebit_std, 22)`: S=0.39, F=0.10, T=34.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_ebit_std, 10)`: S=0.64, F=0.50, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ebit_std, 22))`: S=0.54, F=0.19, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_std)`: S=-0.03, F=0.00, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_std / close)`: S=-0.29, F=-0.14, T=6.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.87, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+1.8%
  - 2020: S=-0.44 (negative), ret=-2.6%
  - 2021: S=1.21 (moderate), ret=+9.8%
  - 2022: S=2.22 (strong), ret=+13.3%
  - 2023: S=0.74 (moderate), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 12.55% over 601 days (recovered)
- Annualized: return +5.3%, volatility 6.1% (fraction of booksize)
- Hit rate: 53.9% positive days
- Tail shape: skew -0.07, excess kurtosis +0.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.43, max 3.05, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +4.91%; worst month: -3.01%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.89
- Sideways: S=1.15
- Bear: S=-1.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_ebit_std, 5))` S=0.67, F=0.28, INFERIOR
Direction gap: -0.20 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_ebit_std)`: S=-0.03, F=0.00, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ebit_std / close)`: S=-0.29, F=-0.14, T=6.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ebit_std, 5))`: S=0.67, F=0.28, T=38.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_ebit_std)` | TOP3000 | 0.87 | 0.56 | 12.6% | 80% | bull-only |
| `rank(anl4_ebit_std)` | TOP1000 | 0.46 | 0.25 | 15.1% | 60% | bull-only |
| `rank(anl4_ebit_std / close)` | TOP3000 | 0.41 | 0.21 | 13.0% | 60% | mixed |
| `rank(anl4_ebit_std)` | TOP500 | 0.39 | 0.21 | 18.7% | 80% | bull-only |
| `rank(anl4_ebit_std / close)` | TOP500 | 0.31 | 0.15 | 12.2% | 80% | bull-only |
| `rank(anl4_ebit_std / close)` | TOP200 | 0.30 | 0.14 | 21.4% | 80% | bull-only |
| `rank(anl4_ebit_std / close)` | TOP1000 | 0.24 | 0.10 | 10.4% | 80% | mixed |
| `rank(ts_delta(anl4_ebit_std, 5))` | TOP1000 | 0.41 | 0.10 | 13.2% | 60% | bull-only |
| `rank(ts_delta(anl4_ebit_std, 5))` | TOP3000 | 0.17 | 0.03 | 11.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_dts_ptp: 0.953 (strongly positively correlated)
- anl4_netprofit_std: 0.933 (strongly positively correlated)
- sales_estimate_stddev_quarterly: 0.885 (strongly positively correlated)
- sales_estimate_standard_deviation: 0.885 (strongly positively correlated)
- highest_sales_estimate: 0.841 (strongly positively correlated)

Redundancy cluster #32: 9 similar fields, mean |rho| 0.765 (representative: fnd6_fopox). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.31 | 1.41 | +0.50 | -0.31 | yes |
| operating_profit_before_depr_amort_max_guidance_qtr | analyst4 | -0.31 | 1.53 | +0.58 | -0.89 | no |
| operating_profit_before_depr_amort_min_guidance_qtr | analyst4 | -0.31 | 1.54 | +0.58 | -0.88 | no |
| parkinson_volatility_120 | option8 | -0.23 | 1.39 | +0.50 | -0.01 | yes |
| snt_value_fast_d1 | socialmedia12 | -0.20 | 1.34 | +0.46 | -0.27 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
