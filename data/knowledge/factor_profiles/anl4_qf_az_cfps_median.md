---
field: anl4_qf_az_cfps_median
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1206
ann_vol: 0.0814
hit_rate: 0.4907
rolling_sharpe_min: -1.645
rolling_sharpe_max: 2.886
redundancy_cluster: 1
negated_best_sharpe: 0.39
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.38
---
# anl4_qf_az_cfps_median (analyst4)

*Cash Flow Per Share - Median value among forecasts*

## Signal Profile
- `rank(anl4_qf_az_cfps_median)`: S=0.30, F=0.13, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_qf_az_cfps_median / close)`: S=0.77, F=0.54, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qf_az_cfps_median, 5))`: S=0.76, F=0.27, T=36.3%, INFERIOR (TOP3000)
- `-rank(anl4_qf_az_cfps_median)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_cfps_median, 5))`: S=-0.34, F=-0.14, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_qf_az_cfps_median, 63)`: S=0.20, F=0.06, T=16.3%, INFERIOR (TOP3000)
- `ts_mean(anl4_qf_az_cfps_median, 10)`: S=-0.06, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qf_az_cfps_median, 22))`: S=0.02, F=0.00, T=13.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_cfps_median)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_cfps_median / close)`: S=0.39, F=0.24, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.48 (negative), ret=-3.0%
  - 2020: S=-0.00 (negative), ret=-0.0%
  - 2021: S=2.08 (strong), ret=+17.5%
  - 2022: S=1.72 (strong), ret=+14.6%
  - 2023: S=0.31 (weak), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 12.06% over 772 days (recovered)
- Annualized: return +6.3%, volatility 8.1% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.41, excess kurtosis +1.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.65, max 2.89, latest 0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.15%; worst month: -4.94%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.60
- Sideways: S=-0.50
- Bear: S=-0.06

## Negated Direction
Best negated: `rank(-1 * anl4_qf_az_cfps_median / close)` S=0.39, F=0.24, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_qf_az_cfps_median)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_cfps_median / close)`: S=0.39, F=0.24, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_cfps_median, 5))`: S=-0.34, F=-0.14, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qf_az_cfps_median / close)` | TOP3000 | 0.77 | 0.54 | 12.1% | 60% | mixed |
| `rank(ts_delta(anl4_qf_az_cfps_median, 5))` | TOP3000 | 0.79 | 0.27 | 8.7% | 80% | all-weather |
| `rank(anl4_qf_az_cfps_median / close)` | TOP1000 | 0.36 | 0.19 | 16.9% | 40% | bull-only |
| `rank(ts_delta(anl4_qf_az_cfps_median, 5))` | TOP200 | 0.39 | 0.17 | 30.3% | 60% | weak |
| `rank(anl4_qf_az_cfps_median)` | TOP3000 | 0.29 | 0.13 | 26.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_cfps_median: 1.000 (strongly positively correlated)
- anl4_qf_az_cfps_mean: 1.000 (strongly positively correlated)
- cashflow_per_share_average: 1.000 (strongly positively correlated)
- anl4_qf_az_hgih_spfc: 0.998 (strongly positively correlated)
- anl4_qfd1_az_hgih_spfc: 0.998 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
