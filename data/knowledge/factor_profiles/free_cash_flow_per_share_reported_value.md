---
field: free_cash_flow_per_share_reported_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.65
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2101
ann_vol: 0.0852
hit_rate: 0.5134
rolling_sharpe_min: -2.985
rolling_sharpe_max: 3.124
redundancy_cluster: 85
negated_best_sharpe: 0.76
negated_best_template: rank_neg_delta
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: 0.11
---
# free_cash_flow_per_share_reported_value (analyst4)

*Free cash flow per share- announced financial value*

## Signal Profile
- `rank(free_cash_flow_per_share_reported_value)`: S=0.23, F=0.09, T=4.3%, INFERIOR (TOP3000)
- `rank(free_cash_flow_per_share_reported_value / close)`: S=0.65, F=0.43, T=5.1%, INFERIOR (TOP3000)
- `rank(ts_delta(free_cash_flow_per_share_reported_value, 5))`: S=-0.23, F=-0.06, T=35.6%, INFERIOR (TOP200)
- `-rank(free_cash_flow_per_share_reported_value)`: S=-0.04, F=-0.01, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(free_cash_flow_per_share_reported_value, 5))`: S=0.76, F=0.28, T=38.1%, INFERIOR (TOP3000)
- `-ts_zscore(free_cash_flow_per_share_reported_value, 63)`: S=0.24, F=0.06, T=17.8%, INFERIOR (TOP3000)
- `ts_mean(free_cash_flow_per_share_reported_value, 10)`: S=-0.12, F=-0.04, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(free_cash_flow_per_share_reported_value, 22))`: S=-0.66, F=-0.29, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_per_share_reported_value)`: S=0.15, F=0.05, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_per_share_reported_value / close)`: S=0.04, F=0.01, T=5.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.63, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.3%
  - 2020: S=-2.75 (negative), ret=-16.1%
  - 2021: S=2.02 (strong), ret=+17.2%
  - 2022: S=2.14 (strong), ret=+25.7%
  - 2023: S=0.01 (weak), ret=+0.1%

## Risk & Drawdown
- Max drawdown: 21.01% over 751 days (recovered)
- Annualized: return +5.4%, volatility 8.5% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.02, excess kurtosis +1.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.98, max 3.12, latest -0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.91%; worst month: -4.14%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.32
- Sideways: S=0.33
- Bear: S=-2.25

## Negated Direction
Best negated: `rank(-1 * ts_delta(free_cash_flow_per_share_reported_value, 5))` S=0.76, F=0.28, INFERIOR
Direction gap: +0.11 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * free_cash_flow_per_share_reported_value)`: S=0.15, F=0.05, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_per_share_reported_value / close)`: S=0.04, F=0.01, T=5.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(free_cash_flow_per_share_reported_value, 5))`: S=0.76, F=0.28, T=38.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(free_cash_flow_per_share_reported_value / close)` | TOP3000 | 0.63 | 0.43 | 21.0% | 60% | bull-only |
| `rank(free_cash_flow_per_share_reported_value / close)` | TOP1000 | 0.25 | 0.12 | 23.0% | 40% | bull-only |
| `rank(free_cash_flow_per_share_reported_value)` | TOP3000 | 0.21 | 0.09 | 34.3% | 40% | bull-only |

## Correlation Notes
Top correlates:
- free_cash_flow_per_share_actual_value: 1.000 (strongly positively correlated)
- free_cash_flow_reported_value: 0.883 (strongly positively correlated)
- anl4_fcf_value: 0.883 (strongly positively correlated)
- anl4_cfo_value: 0.862 (strongly positively correlated)
- operating_cashflow_reported_value: 0.862 (strongly positively correlated)

Redundancy cluster #85: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
