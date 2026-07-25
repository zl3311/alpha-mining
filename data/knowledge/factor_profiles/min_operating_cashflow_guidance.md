---
field: min_operating_cashflow_guidance
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
max_drawdown: 0.1509
ann_vol: 0.0903
hit_rate: 0.5077
rolling_sharpe_min: -1.066
rolling_sharpe_max: 3.179
redundancy_cluster: 40
negated_best_sharpe: 0.53
negated_best_template: neg_rank_level
negated_best_fitness: 0.45
n_negated_sims: 10
direction_gap: -0.02
---
# min_operating_cashflow_guidance (analyst4)

*Minimum guidance value for Cash Flow from Operations*

## Signal Profile
- `rank(min_operating_cashflow_guidance)`: S=0.38, F=0.20, T=1.1%, INFERIOR (TOP3000)
- `rank(min_operating_cashflow_guidance / close)`: S=0.09, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_operating_cashflow_guidance, 5))`: S=0.55, F=0.21, T=33.7%, INFERIOR (TOP200)
- `-rank(min_operating_cashflow_guidance)`: S=0.05, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_operating_cashflow_guidance, 5))`: S=0.23, F=0.05, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(min_operating_cashflow_guidance, 63)`: S=0.08, F=0.01, T=21.8%, INFERIOR (TOP3000)
- `ts_mean(min_operating_cashflow_guidance, 10)`: S=-0.01, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(min_operating_cashflow_guidance, 22))`: S=-0.14, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * min_operating_cashflow_guidance)`: S=0.53, F=0.45, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * min_operating_cashflow_guidance / close)`: S=0.10, F=0.03, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/25P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.56, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+4.3%
  - 2020: S=2.95 (strong), ret=+23.1%
  - 2021: S=-0.23 (negative), ret=-2.4%
  - 2022: S=0.03 (weak), ret=+0.3%
  - 2023: S=-0.04 (negative), ret=-0.3%

## Risk & Drawdown
- Max drawdown: 15.09% over 975 days (not yet recovered, ongoing at window end)
- Annualized: return +5.1%, volatility 9.0% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.65, excess kurtosis +5.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.07, max 3.18, latest 0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.07%; worst month: -5.00%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.94
- Sideways: S=0.61
- Bear: S=2.40

## Negated Direction
Best negated: `rank(-1 * min_operating_cashflow_guidance)` S=0.53, F=0.45, INFERIOR
Direction gap: -0.02 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * min_operating_cashflow_guidance)`: S=0.53, F=0.45, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * min_operating_cashflow_guidance / close)`: S=0.10, F=0.03, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_operating_cashflow_guidance, 5))`: S=0.23, F=0.05, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(min_operating_cashflow_guidance, 5))` | TOP200 | 0.56 | 0.21 | 15.1% | 60% | bear-only |
| `rank(min_operating_cashflow_guidance)` | TOP3000 | 0.38 | 0.20 | 20.3% | 40% | mixed |
| `rank(min_operating_cashflow_guidance / close)` | TOP3000 | 0.09 | 0.03 | 51.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_operating_cashflow_guidance: 0.999 (strongly positively correlated)
- min_tangible_book_value_per_share_guidance_2: 0.994 (strongly positively correlated)
- tangible_book_value_per_share_max_guidance: 0.994 (strongly positively correlated)
- cashflow_per_share_max_guidance: 0.993 (strongly positively correlated)
- cashflow_per_share_min_guidance: 0.992 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
