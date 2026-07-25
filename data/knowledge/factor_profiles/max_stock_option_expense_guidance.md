---
field: max_stock_option_expense_guidance
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 1.08
best_fitness: 1.26
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.1545
ann_vol: 0.0904
hit_rate: 0.5126
rolling_sharpe_min: -1.052
rolling_sharpe_max: 3.304
redundancy_cluster: 40
negated_best_sharpe: 1.08
negated_best_template: neg_rank_level
negated_best_fitness: 1.26
n_negated_sims: 10
direction_gap: 0.49
---
# max_stock_option_expense_guidance (analyst4)

*Stock option expense - Maximum guidance value for the annual period*

## Signal Profile
- `rank(max_stock_option_expense_guidance)`: S=0.26, F=0.21, T=2.9%, INFERIOR (TOP3000)
- `rank(max_stock_option_expense_guidance / close)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_stock_option_expense_guidance, 5))`: S=0.56, F=0.22, T=33.7%, INFERIOR (TOP200)
- `-rank(max_stock_option_expense_guidance)`: S=0.38, F=0.28, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_stock_option_expense_guidance, 5))`: S=0.11, F=0.01, T=35.8%, INFERIOR (TOP3000)
- `-ts_zscore(max_stock_option_expense_guidance, 63)`: S=0.59, F=0.23, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(max_stock_option_expense_guidance, 10)`: S=0.12, F=0.03, T=24.1%, INFERIOR (TOP3000)
- `rank(ts_rank(max_stock_option_expense_guidance, 22))`: S=-0.22, F=-0.07, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_stock_option_expense_guidance)`: S=1.08, F=1.26, T=2.7%, AVERAGE (TOP3000)
- `rank(-1 * max_stock_option_expense_guidance / close)`: S=0.06, F=0.01, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 29F/3P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.57, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.59 (moderate), ret=+3.9%
  - 2020: S=3.06 (strong), ret=+24.1%
  - 2021: S=-0.14 (negative), ret=-1.5%
  - 2022: S=-0.08 (negative), ret=-0.9%
  - 2023: S=-0.03 (negative), ret=-0.2%

## Risk & Drawdown
- Max drawdown: 15.45% over 975 days (not yet recovered, ongoing at window end)
- Annualized: return +5.2%, volatility 9.0% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.61, excess kurtosis +5.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.05, max 3.30, latest 0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.94%; worst month: -5.00%
Positive months: 58%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.87
- Sideways: S=0.65
- Bear: S=2.37

## Negated Direction
Best negated: `rank(-1 * max_stock_option_expense_guidance)` S=1.08, F=1.26, AVERAGE
Direction gap: +0.49 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * max_stock_option_expense_guidance)`: S=1.08, F=1.26, T=2.7%, AVERAGE (TOP3000)
- `rank(-1 * max_stock_option_expense_guidance / close)`: S=0.06, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_stock_option_expense_guidance, 5))`: S=0.11, F=0.01, T=35.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(max_stock_option_expense_guidance, 5))` | TOP200 | 0.57 | 0.22 | 15.4% | 40% | bear-only |
| `rank(max_stock_option_expense_guidance)` | TOP3000 | 0.27 | 0.21 | 44.3% | 60% | mixed |
| `rank(max_stock_option_expense_guidance)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(max_stock_option_expense_guidance / close)` | TOP3000 | 0.07 | 0.02 | 53.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_stock_option_expense_guidance_2: 1.000 (strongly positively correlated)
- dividend_max_guidance_value: 0.995 (strongly positively correlated)
- dividend_min_guidance_value: 0.990 (strongly positively correlated)
- dividend_max_guidance_quarterly: 0.988 (strongly positively correlated)
- min_tangible_book_value_per_share_guidance_2: 0.984 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
