---
field: free_cash_flow_total
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.49
best_fitness: 0.13
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.3656
ann_vol: 0.1118
hit_rate: 0.5004
rolling_sharpe_min: -4.32
rolling_sharpe_max: 2.319
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: 0.27
---
# free_cash_flow_total (analyst4)

*Free Cash Flow value - Annual*

## Signal Profile
- `rank(free_cash_flow_total)`: S=0.00, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(free_cash_flow_total / close)`: S=0.22, F=0.10, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(free_cash_flow_total, 5))`: S=0.21, F=0.05, T=34.2%, INFERIOR (TOP200)
- `-rank(free_cash_flow_total)`: S=0.10, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(free_cash_flow_total, 5))`: S=0.49, F=0.13, T=36.1%, INFERIOR (TOP3000)
- `ts_zscore(free_cash_flow_total, 22)`: S=0.31, F=0.09, T=38.6%, INFERIOR (TOP3000)
- `ts_mean(free_cash_flow_total, 10)`: S=-0.14, F=-0.05, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(free_cash_flow_total, 22))`: S=-0.38, F=-0.14, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_total)`: S=0.00, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_total / close)`: S=-0.22, F=-0.10, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.20, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.04 (weak), ret=+0.2%
  - 2020: S=-3.42 (negative), ret=-23.9%
  - 2021: S=1.03 (moderate), ret=+12.6%
  - 2022: S=1.43 (moderate), ret=+23.2%
  - 2023: S=-0.10 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 36.56% over 925 days (recovered)
- Annualized: return +2.3%, volatility 11.2% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.04, excess kurtosis +1.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.32, max 2.32, latest -0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.00%; worst month: -4.86%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.01
- Sideways: S=0.35
- Bear: S=-3.67

## Negated Direction
Best negated: `rank(-1 * ts_delta(free_cash_flow_total, 5))` S=0.49, F=0.13, INFERIOR
Direction gap: +0.27 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * free_cash_flow_total)`: S=0.00, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_total / close)`: S=-0.22, F=-0.10, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(free_cash_flow_total, 5))`: S=0.49, F=0.13, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(free_cash_flow_total / close)` | TOP3000 | 0.20 | 0.10 | 36.6% | 60% | bull-only |
| `rank(ts_delta(free_cash_flow_total, 5))` | TOP200 | 0.20 | 0.05 | 22.3% | 80% | bull-only |

## Correlation Notes
Top correlates:
- cash_flow_from_operations: 0.967 (strongly positively correlated)
- pretax_income_total: 0.965 (strongly positively correlated)
- net_income_adjusted: 0.963 (strongly positively correlated)
- net_income_total_2: 0.961 (strongly positively correlated)
- pretax_income_reported: 0.959 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
