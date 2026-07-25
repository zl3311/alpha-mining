---
field: cash_flow_operations_min_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.59
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1349
ann_vol: 0.061
hit_rate: 0.515
rolling_sharpe_min: -2.45
rolling_sharpe_max: 2.505
redundancy_cluster: 95
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.07
---
# cash_flow_operations_min_guidance (analyst4)

*Minimum guidance value for Cash Flow from Operations on an annual basis.*

## Signal Profile
- `rank(cash_flow_operations_min_guidance)`: S=0.59, F=0.31, T=0.9%, INFERIOR (TOP3000)
- `rank(cash_flow_operations_min_guidance / close)`: S=0.18, F=0.08, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(cash_flow_operations_min_guidance, 5))`: S=0.30, F=0.08, T=33.4%, INFERIOR (TOP200)
- `-rank(cash_flow_operations_min_guidance)`: S=0.03, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash_flow_operations_min_guidance, 5))`: S=-0.30, F=-0.08, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(cash_flow_operations_min_guidance, 63)`: S=0.46, F=0.17, T=20.2%, INFERIOR (TOP3000)
- `ts_mean(cash_flow_operations_min_guidance, 10)`: S=-0.02, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(cash_flow_operations_min_guidance, 22))`: S=-0.22, F=-0.06, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_operations_min_guidance)`: S=0.52, F=0.31, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_operations_min_guidance / close)`: S=0.37, F=0.21, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.57, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.48 (moderate), ret=+5.0%
  - 2020: S=-1.63 (negative), ret=-7.5%
  - 2021: S=1.19 (moderate), ret=+8.5%
  - 2022: S=1.31 (moderate), ret=+11.6%
  - 2023: S=-0.12 (negative), ret=-0.5%

## Risk & Drawdown
- Max drawdown: 13.49% over 769 days (recovered)
- Annualized: return +3.5%, volatility 6.1% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.08, excess kurtosis +2.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.45, max 2.50, latest -0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +4.85%; worst month: -3.41%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.28
- Sideways: S=0.21
- Bear: S=-1.48

## Negated Direction
Best negated: `rank(-1 * cash_flow_operations_min_guidance)` S=0.52, F=0.31, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cash_flow_operations_min_guidance)`: S=0.52, F=0.31, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * cash_flow_operations_min_guidance / close)`: S=0.37, F=0.21, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cash_flow_operations_min_guidance, 5))`: S=-0.30, F=-0.08, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(cash_flow_operations_min_guidance)` | TOP3000 | 0.57 | 0.31 | 13.5% | 60% | bull-only |
| `rank(cash_flow_operations_min_guidance / close)` | TOP3000 | 0.18 | 0.08 | 44.7% | 60% | bull-only |
| `rank(ts_delta(cash_flow_operations_min_guidance, 5))` | TOP200 | 0.32 | 0.08 | 18.6% | 60% | bear-only |

## Correlation Notes
Top correlates:
- max_operating_cashflow_guidance_2: 1.000 (strongly positively correlated)
- max_capital_expenditure_guidance: 0.805 (strongly positively correlated)
- min_capital_expenditure_guidance: 0.800 (strongly positively correlated)
- max_free_cash_flow_guidance: 0.799 (strongly positively correlated)
- min_free_cash_flow_guidance: 0.798 (strongly positively correlated)

Redundancy cluster #95: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
