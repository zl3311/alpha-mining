---
field: anl4_afv4_cfps_low
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.93
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1122
ann_vol: 0.0781
hit_rate: 0.5069
rolling_sharpe_min: -0.901
rolling_sharpe_max: 2.516
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.1
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.83
---
# anl4_afv4_cfps_low (analyst4)

*Cash Flow Per Share - The lowest estimation for the upcoming fiscal year*

## Signal Profile
- `rank(anl4_afv4_cfps_low)`: S=0.31, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_afv4_cfps_low / close)`: S=0.93, F=0.71, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_afv4_cfps_low, 5))`: S=0.56, F=0.23, T=35.0%, INFERIOR (TOP200)
- `-rank(anl4_afv4_cfps_low)`: S=-0.13, F=-0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_cfps_low, 5))`: S=-0.56, F=-0.23, T=35.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_afv4_cfps_low, 22)`: S=0.21, F=0.05, T=34.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_cfps_low, 10)`: S=-0.02, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_cfps_low, 22))`: S=0.05, F=0.01, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_low)`: S=0.03, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_low / close)`: S=0.10, F=0.03, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.92, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.31 (weak), ret=+1.9%
  - 2020: S=0.44 (weak), ret=+4.9%
  - 2021: S=1.23 (moderate), ret=+9.2%
  - 2022: S=2.24 (strong), ret=+16.0%
  - 2023: S=0.64 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 11.22% over 503 days (recovered)
- Annualized: return +7.2%, volatility 7.8% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.77, excess kurtosis +4.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.90, max 2.52, latest 0.68

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.51%; worst month: -4.96%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.76
- Sideways: S=-0.14
- Bear: S=-0.04

## Negated Direction
Best negated: `rank(-1 * anl4_afv4_cfps_low / close)` S=0.10, F=0.03, INFERIOR
Direction gap: -0.83 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_afv4_cfps_low)`: S=0.03, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_low / close)`: S=0.10, F=0.03, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_cfps_low, 5))`: S=-0.56, F=-0.23, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_cfps_low / close)` | TOP3000 | 0.92 | 0.71 | 11.2% | 100% | mixed |
| `rank(anl4_afv4_cfps_low / close)` | TOP1000 | 0.56 | 0.37 | 14.0% | 80% | bull-only |
| `rank(ts_delta(anl4_afv4_cfps_low, 5))` | TOP200 | 0.57 | 0.23 | 14.2% | 80% | all-weather |
| `rank(ts_delta(anl4_afv4_cfps_low, 5))` | TOP3000 | 0.69 | 0.18 | 5.0% | 80% | mixed |
| `rank(anl4_afv4_cfps_low)` | TOP3000 | 0.30 | 0.14 | 29.8% | 80% | bull-only |
| `rank(ts_delta(anl4_afv4_cfps_low, 5))` | TOP1000 | 0.32 | 0.07 | 8.4% | 80% | mixed |
| `rank(anl4_afv4_cfps_low)` | TOP1000 | 0.13 | 0.04 | 30.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_afv4_cfps_mean: 0.990 (strongly positively correlated)
- anl4_afv4_cfps_median: 0.990 (strongly positively correlated)
- anl4_afv4_cfps_high: 0.980 (strongly positively correlated)
- sales_ps: 0.878 (strongly positively correlated)
- anl4_qf_az_cfps_mean: 0.865 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.36 | 1.57 | +0.65 | -0.45 | yes |
| fnd6_txtubadjust | fundamental6 | -0.23 | 1.43 | +0.51 | -0.85 | yes |
| anl4_epsr_flag | analyst4 | -0.33 | 1.82 | +0.64 | -0.38 | no |
| news_open_vol | news12 | -0.14 | 1.40 | +0.48 | -0.47 | yes |
| max_gross_income_guidance | analyst4 | -0.31 | 1.50 | +0.58 | -0.86 | no |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
