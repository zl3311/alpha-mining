---
field: anl4_qf_az_cfps_mean
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1198
ann_vol: 0.0814
hit_rate: 0.4915
rolling_sharpe_min: -1.639
rolling_sharpe_max: 2.885
redundancy_cluster: 1
negated_best_sharpe: 0.4
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: -0.38
---
# anl4_qf_az_cfps_mean (analyst4)

*Cash Flow Per Share - average of estimations*

## Signal Profile
- `rank(anl4_qf_az_cfps_mean)`: S=0.30, F=0.13, T=0.9%, INFERIOR (TOP3000)
- `rank(anl4_qf_az_cfps_mean / close)`: S=0.78, F=0.55, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qf_az_cfps_mean, 5))`: S=0.64, F=0.21, T=36.2%, INFERIOR (TOP3000)
- `-rank(anl4_qf_az_cfps_mean)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_cfps_mean, 5))`: S=-0.30, F=-0.11, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_qf_az_cfps_mean, 63)`: S=0.21, F=0.06, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_qf_az_cfps_mean, 10)`: S=-0.06, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qf_az_cfps_mean, 22))`: S=0.06, F=0.01, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_cfps_mean)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_cfps_mean / close)`: S=0.40, F=0.25, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.78, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.48 (negative), ret=-3.0%
  - 2020: S=0.01 (weak), ret=+0.1%
  - 2021: S=2.07 (strong), ret=+17.5%
  - 2022: S=1.73 (strong), ret=+14.6%
  - 2023: S=0.34 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 11.98% over 771 days (recovered)
- Annualized: return +6.3%, volatility 8.1% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.41, excess kurtosis +1.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.64, max 2.88, latest 0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.16%; worst month: -4.92%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.60
- Sideways: S=-0.49
- Bear: S=-0.05

## Negated Direction
Best negated: `rank(-1 * anl4_qf_az_cfps_mean / close)` S=0.40, F=0.25, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_qf_az_cfps_mean)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_cfps_mean / close)`: S=0.40, F=0.25, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_cfps_mean, 5))`: S=-0.30, F=-0.11, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qf_az_cfps_mean / close)` | TOP3000 | 0.78 | 0.55 | 12.0% | 80% | mixed |
| `rank(ts_delta(anl4_qf_az_cfps_mean, 5))` | TOP3000 | 0.67 | 0.21 | 11.1% | 80% | mixed |
| `rank(anl4_qf_az_cfps_mean / close)` | TOP1000 | 0.36 | 0.19 | 16.9% | 40% | bull-only |
| `rank(ts_delta(anl4_qf_az_cfps_mean, 5))` | TOP200 | 0.34 | 0.13 | 31.1% | 80% | weak |
| `rank(anl4_qf_az_cfps_mean)` | TOP3000 | 0.29 | 0.13 | 26.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cashflow_per_share_average: 1.000 (strongly positively correlated)
- anl4_qf_az_cfps_median: 1.000 (strongly positively correlated)
- anl4_qfd1_az_cfps_median: 1.000 (strongly positively correlated)
- anl4_qf_az_hgih_spfc: 0.998 (strongly positively correlated)
- anl4_qfd1_az_hgih_spfc: 0.998 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
