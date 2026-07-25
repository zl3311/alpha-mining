---
field: cashflow_per_share_average
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1198
ann_vol: 0.0814
hit_rate: 0.4915
rolling_sharpe_min: -1.639
rolling_sharpe_max: 2.885
redundancy_cluster: 1
negated_best_sharpe: 0.57
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.21
---
# cashflow_per_share_average (analyst4)

*Cash Flow Per Share - average of estimations with a delay of 1 quarter*

## Signal Profile
- `rank(cashflow_per_share_average)`: S=0.30, F=0.13, T=0.9%, INFERIOR (TOP3000)
- `rank(cashflow_per_share_average / close)`: S=0.78, F=0.55, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(cashflow_per_share_average, 5))`: S=0.23, F=0.04, T=35.7%, INFERIOR (TOP3000)
- `-rank(cashflow_per_share_average)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_average, 5))`: S=0.57, F=0.18, T=36.6%, INFERIOR (TOP3000)
- `-ts_zscore(cashflow_per_share_average, 63)`: S=0.07, F=0.01, T=16.3%, INFERIOR (TOP3000)
- `ts_mean(cashflow_per_share_average, 10)`: S=-0.06, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_per_share_average, 22))`: S=0.01, F=0.00, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_average)`: S=-0.05, F=-0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_average / close)`: S=-0.03, F=0.00, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
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
Best negated: `rank(-1 * ts_delta(cashflow_per_share_average, 5))` S=0.57, F=0.18, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cashflow_per_share_average)`: S=-0.05, F=-0.01, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_average / close)`: S=-0.03, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_average, 5))`: S=0.57, F=0.18, T=36.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cashflow_per_share_average / close)` | TOP3000 | 0.78 | 0.55 | 12.0% | 80% | mixed |
| `rank(cashflow_per_share_average / close)` | TOP1000 | 0.36 | 0.19 | 16.9% | 40% | bull-only |
| `rank(cashflow_per_share_average)` | TOP3000 | 0.29 | 0.13 | 26.7% | 60% | bull-only |
| `rank(ts_delta(cashflow_per_share_average, 5))` | TOP3000 | 0.24 | 0.04 | 12.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qf_az_cfps_mean: 1.000 (strongly positively correlated)
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
