---
field: cashflow_per_share_min_guidance
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.53
best_fitness: 0.2
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.1614
ann_vol: 0.0902
hit_rate: 0.5101
rolling_sharpe_min: -1.036
rolling_sharpe_max: 3.189
redundancy_cluster: 40
negated_best_sharpe: 0.3
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.23
---
# cashflow_per_share_min_guidance (analyst4)

*Cash Flow Per Share - Minimum guidance value for the annual period*

## Signal Profile
- `rank(cashflow_per_share_min_guidance)`: S=-0.03, F=-0.01, T=3.6%, INFERIOR (TOP200)
- `rank(cashflow_per_share_min_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(cashflow_per_share_min_guidance, 5))`: S=0.53, F=0.20, T=33.7%, INFERIOR (TOP200)
- `-rank(cashflow_per_share_min_guidance)`: S=0.15, F=0.06, T=0.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_min_guidance, 5))`: S=0.30, F=0.07, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(cashflow_per_share_min_guidance, 63)`: S=0.15, F=0.03, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(cashflow_per_share_min_guidance, 10)`: S=-0.04, F=-0.01, T=5.0%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_per_share_min_guidance, 22))`: S=-0.12, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_min_guidance)`: S=-0.03, F=-0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_min_guidance / close)`: S=0.08, F=0.02, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.54, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.64 (moderate), ret=+4.2%
  - 2020: S=2.93 (strong), ret=+23.0%
  - 2021: S=-0.23 (negative), ret=-2.4%
  - 2022: S=-0.06 (negative), ret=-0.6%
  - 2023: S=-0.03 (negative), ret=-0.2%

## Risk & Drawdown
- Max drawdown: 16.14% over 975 days (not yet recovered, ongoing at window end)
- Annualized: return +4.9%, volatility 9.0% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.62, excess kurtosis +5.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.04, max 3.19, latest 0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.05%; worst month: -5.00%
Positive months: 59%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.99
- Sideways: S=0.69
- Bear: S=2.35

## Negated Direction
Best negated: `rank(-1 * ts_delta(cashflow_per_share_min_guidance, 5))` S=0.30, F=0.07, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cashflow_per_share_min_guidance)`: S=-0.03, F=-0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_min_guidance / close)`: S=0.08, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_min_guidance, 5))`: S=0.30, F=0.07, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(cashflow_per_share_min_guidance, 5))` | TOP200 | 0.54 | 0.20 | 16.1% | 40% | bear-only |
| `rank(cashflow_per_share_min_guidance / close)` | TOP3000 | 0.07 | 0.02 | 52.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- cashflow_per_share_max_guidance: 1.000 (strongly positively correlated)
- min_tangible_book_value_per_share_guidance_2: 0.998 (strongly positively correlated)
- tangible_book_value_per_share_max_guidance: 0.998 (strongly positively correlated)
- max_operating_cashflow_guidance: 0.994 (strongly positively correlated)
- max_reported_pretax_income_guidance_2: 0.993 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
