---
field: max_operating_cashflow_guidance
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.53
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.1483
ann_vol: 0.0906
hit_rate: 0.5069
rolling_sharpe_min: -1.023
rolling_sharpe_max: 3.18
redundancy_cluster: 40
negated_best_sharpe: 0.53
negated_best_template: neg_rank_level
negated_best_fitness: 0.45
n_negated_sims: 10
direction_gap: -0.03
---
# max_operating_cashflow_guidance (analyst4)

*The maximum guidance value for Cash Flow from Operations.*

## Signal Profile
- `rank(max_operating_cashflow_guidance)`: S=0.38, F=0.20, T=1.1%, INFERIOR (TOP3000)
- `rank(max_operating_cashflow_guidance / close)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_operating_cashflow_guidance, 5))`: S=0.56, F=0.22, T=33.7%, INFERIOR (TOP200)
- `-rank(max_operating_cashflow_guidance)`: S=0.05, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_operating_cashflow_guidance, 5))`: S=0.19, F=0.04, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(max_operating_cashflow_guidance, 63)`: S=-0.02, F=0.00, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(max_operating_cashflow_guidance, 10)`: S=-0.04, F=-0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(max_operating_cashflow_guidance, 22))`: S=-0.13, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_operating_cashflow_guidance)`: S=0.53, F=0.45, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * max_operating_cashflow_guidance / close)`: S=0.10, F=0.03, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/25P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.57, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.65 (moderate), ret=+4.3%
  - 2020: S=2.92 (strong), ret=+23.0%
  - 2021: S=-0.23 (negative), ret=-2.4%
  - 2022: S=0.05 (weak), ret=+0.5%
  - 2023: S=-0.00 (negative), ret=-0.0%

## Risk & Drawdown
- Max drawdown: 14.83% over 975 days (not yet recovered, ongoing at window end)
- Annualized: return +5.2%, volatility 9.1% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew +0.64, excess kurtosis +5.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.02, max 3.18, latest 0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.06%; worst month: -5.00%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.93
- Sideways: S=0.63
- Bear: S=2.39

## Negated Direction
Best negated: `rank(-1 * max_operating_cashflow_guidance)` S=0.53, F=0.45, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_operating_cashflow_guidance)`: S=0.53, F=0.45, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * max_operating_cashflow_guidance / close)`: S=0.10, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_operating_cashflow_guidance, 5))`: S=0.19, F=0.04, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(max_operating_cashflow_guidance, 5))` | TOP200 | 0.57 | 0.22 | 14.8% | 60% | bear-only |
| `rank(max_operating_cashflow_guidance)` | TOP3000 | 0.38 | 0.20 | 20.4% | 40% | mixed |
| `rank(max_operating_cashflow_guidance / close)` | TOP3000 | 0.09 | 0.03 | 51.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_operating_cashflow_guidance: 0.999 (strongly positively correlated)
- min_tangible_book_value_per_share_guidance_2: 0.996 (strongly positively correlated)
- tangible_book_value_per_share_max_guidance: 0.996 (strongly positively correlated)
- cashflow_per_share_max_guidance: 0.995 (strongly positively correlated)
- cashflow_per_share_min_guidance: 0.994 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
