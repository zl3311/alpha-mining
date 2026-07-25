---
field: cashflow_per_share_median_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1212
ann_vol: 0.0449
hit_rate: 0.5085
rolling_sharpe_min: -2.138
rolling_sharpe_max: 2.291
negated_best_sharpe: 0.39
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.38
---
# cashflow_per_share_median_value (analyst4)

*Cash Flow Per Share - Median value among forecasts*

## Signal Profile
- `rank(cashflow_per_share_median_value)`: S=0.30, F=0.13, T=0.9%, INFERIOR (TOP3000)
- `rank(cashflow_per_share_median_value / close)`: S=0.77, F=0.54, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(cashflow_per_share_median_value, 5))`: S=0.29, F=0.06, T=35.7%, INFERIOR (TOP3000)
- `-rank(cashflow_per_share_median_value)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_median_value, 5))`: S=0.49, F=0.18, T=34.0%, INFERIOR (TOP3000)
- `ts_zscore(cashflow_per_share_median_value, 22)`: S=0.19, F=0.05, T=32.0%, INFERIOR (TOP3000)
- `ts_mean(cashflow_per_share_median_value, 10)`: S=-0.06, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_per_share_median_value, 22))`: S=0.02, F=0.00, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_median_value)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_median_value / close)`: S=0.39, F=0.24, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.30, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.05 (moderate), ret=+4.0%
  - 2020: S=-0.74 (negative), ret=-3.5%
  - 2021: S=0.18 (weak), ret=+0.9%
  - 2022: S=0.50 (weak), ret=+2.4%
  - 2023: S=0.74 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 12.12% over 1247 days (recovered)
- Annualized: return +1.3%, volatility 4.5% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.03, excess kurtosis +0.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.14, max 2.29, latest 0.71

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +2.72%; worst month: -2.93%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.42
- Sideways: S=0.38
- Bear: S=-0.91

## Negated Direction
Best negated: `rank(-1 * cashflow_per_share_median_value / close)` S=0.39, F=0.24, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cashflow_per_share_median_value)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_median_value / close)`: S=0.39, F=0.24, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_median_value, 5))`: S=0.49, F=0.18, T=34.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(cashflow_per_share_median_value, 5))` | TOP3000 | 0.30 | 0.06 | 12.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- cashflow_per_share_maximum: 0.927 (strongly positively correlated)
- cashflow_per_share_minimum: 0.902 (strongly positively correlated)
- est_cashflow_ps: 0.720 (strongly positively correlated)
- anl4_qfv4_cfps_high: 0.671 (moderately positively correlated)
- anl4_qf_az_wol_spfc: 0.649 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
