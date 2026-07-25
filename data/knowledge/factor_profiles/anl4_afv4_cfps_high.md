---
field: anl4_afv4_cfps_high
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.85
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.1185
ann_vol: 0.08
hit_rate: 0.5012
rolling_sharpe_min: -1.163
rolling_sharpe_max: 2.511
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.64
---
# anl4_afv4_cfps_high (analyst4)

*Cash Flow Per Share - The highest estimation for the annual forecast*

## Signal Profile
- `rank(anl4_afv4_cfps_high)`: S=0.31, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_afv4_cfps_high / close)`: S=0.85, F=0.63, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_afv4_cfps_high, 5))`: S=0.22, F=0.05, T=35.2%, INFERIOR (TOP200)
- `-rank(anl4_afv4_cfps_high)`: S=-0.21, F=-0.08, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_cfps_high, 5))`: S=0.21, F=0.04, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_afv4_cfps_high, 22)`: S=0.04, F=0.00, T=34.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_cfps_high, 10)`: S=-0.02, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_cfps_high, 22))`: S=-0.41, F=-0.14, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_high)`: S=-0.21, F=-0.08, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_high / close)`: S=-0.60, F=-0.41, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.84, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.13 (weak), ret=+0.8%
  - 2020: S=0.37 (weak), ret=+4.1%
  - 2021: S=0.97 (moderate), ret=+7.5%
  - 2022: S=2.39 (strong), ret=+17.1%
  - 2023: S=0.67 (moderate), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 11.85% over 497 days (recovered)
- Annualized: return +6.7%, volatility 8.0% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.80, excess kurtosis +4.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.16, max 2.51, latest 0.72

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +7.11%; worst month: -5.30%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.53
- Sideways: S=-0.10
- Bear: S=-0.06

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_cfps_high, 5))` S=0.21, F=0.04, INFERIOR
Direction gap: -0.64 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_afv4_cfps_high)`: S=-0.21, F=-0.08, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_cfps_high / close)`: S=-0.60, F=-0.41, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_cfps_high, 5))`: S=0.21, F=0.04, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_cfps_high / close)` | TOP3000 | 0.84 | 0.63 | 11.8% | 100% | mixed |
| `rank(anl4_afv4_cfps_high / close)` | TOP1000 | 0.59 | 0.41 | 17.1% | 80% | bull-only |
| `rank(anl4_afv4_cfps_high)` | TOP3000 | 0.30 | 0.14 | 30.0% | 80% | bull-only |
| `rank(anl4_afv4_cfps_high)` | TOP200 | 0.23 | 0.11 | 33.7% | 40% | bull-only |
| `rank(anl4_afv4_cfps_high / close)` | TOP200 | 0.22 | 0.11 | 38.8% | 40% | bull-only |
| `rank(anl4_afv4_cfps_high)` | TOP1000 | 0.20 | 0.08 | 29.3% | 80% | bull-only |
| `rank(anl4_afv4_cfps_high / close)` | TOP500 | 0.14 | 0.06 | 24.7% | 60% | bull-only |
| `rank(ts_delta(anl4_afv4_cfps_high, 5))` | TOP200 | 0.23 | 0.05 | 21.8% | 60% | weak |
| `rank(ts_delta(anl4_afv4_cfps_high, 5))` | TOP3000 | 0.19 | 0.03 | 7.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_afv4_cfps_median: 0.997 (strongly positively correlated)
- anl4_afv4_cfps_mean: 0.997 (strongly positively correlated)
- anl4_afv4_cfps_low: 0.980 (strongly positively correlated)
- sales_ps: 0.854 (strongly positively correlated)
- anl4_afv4_eps_high: 0.852 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.50 | +0.61 | -0.33 | yes |
| fnd6_txtubadjust | fundamental6 | -0.20 | 1.33 | +0.48 | -0.89 | yes |
| rp_css_revenue | news18 | -0.20 | 1.34 | +0.49 | +0.67 | yes |
| min_gross_income_guidance | analyst4 | -0.28 | 1.41 | +0.54 | -0.92 | no |
| max_gross_income_guidance | analyst4 | -0.28 | 1.42 | +0.54 | -0.91 | no |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
