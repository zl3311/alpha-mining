---
field: max_operating_cashflow_guidance_2
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.99
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1356
ann_vol: 0.0612
hit_rate: 0.5142
rolling_sharpe_min: -2.459
rolling_sharpe_max: 2.517
redundancy_cluster: 95
negated_best_sharpe: 0.53
negated_best_template: neg_rank_level
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.46
---
# max_operating_cashflow_guidance_2 (analyst4)

*The maximum guidance value for Cash Flow from Operations on an annual basis.*

## Signal Profile
- `rank(max_operating_cashflow_guidance_2)`: S=0.58, F=0.31, T=0.9%, INFERIOR (TOP3000)
- `rank(max_operating_cashflow_guidance_2 / close)`: S=0.18, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_operating_cashflow_guidance_2, 5))`: S=0.52, F=0.20, T=33.2%, INFERIOR (TOP200)
- `-rank(max_operating_cashflow_guidance_2)`: S=0.03, F=0.00, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_operating_cashflow_guidance_2, 5))`: S=-0.52, F=-0.20, T=33.2%, INFERIOR (TOP3000)
- `-ts_zscore(max_operating_cashflow_guidance_2, 63)`: S=0.99, F=0.53, T=21.5%, INFERIOR (TOP3000)
- `ts_mean(max_operating_cashflow_guidance_2, 10)`: S=0.03, F=0.00, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(max_operating_cashflow_guidance_2, 22))`: S=-0.22, F=-0.07, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * max_operating_cashflow_guidance_2)`: S=0.53, F=0.32, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * max_operating_cashflow_guidance_2 / close)`: S=0.37, F=0.21, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.57, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.47 (moderate), ret=+4.9%
  - 2020: S=-1.64 (negative), ret=-7.5%
  - 2021: S=1.20 (moderate), ret=+8.6%
  - 2022: S=1.30 (moderate), ret=+11.6%
  - 2023: S=-0.11 (negative), ret=-0.5%

## Risk & Drawdown
- Max drawdown: 13.56% over 769 days (recovered)
- Annualized: return +3.5%, volatility 6.1% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.08, excess kurtosis +2.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.46, max 2.52, latest -0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +4.87%; worst month: -3.39%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.27
- Sideways: S=0.22
- Bear: S=-1.48

## Negated Direction
Best negated: `rank(-1 * max_operating_cashflow_guidance_2)` S=0.53, F=0.32, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_operating_cashflow_guidance_2)`: S=0.53, F=0.32, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * max_operating_cashflow_guidance_2 / close)`: S=0.37, F=0.21, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_operating_cashflow_guidance_2, 5))`: S=-0.52, F=-0.20, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_operating_cashflow_guidance_2)` | TOP3000 | 0.57 | 0.31 | 13.6% | 60% | bull-only |
| `rank(ts_delta(max_operating_cashflow_guidance_2, 5))` | TOP200 | 0.54 | 0.20 | 14.2% | 80% | mixed |
| `rank(max_operating_cashflow_guidance_2 / close)` | TOP3000 | 0.18 | 0.07 | 45.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cash_flow_operations_min_guidance: 1.000 (strongly positively correlated)
- max_capital_expenditure_guidance: 0.805 (strongly positively correlated)
- max_free_cash_flow_guidance: 0.800 (strongly positively correlated)
- min_capital_expenditure_guidance: 0.799 (strongly positively correlated)
- min_free_cash_flow_guidance: 0.799 (strongly positively correlated)

Redundancy cluster #95: 2 similar fields, mean |rho| 1.0 (representative: cash_flow_operations_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
