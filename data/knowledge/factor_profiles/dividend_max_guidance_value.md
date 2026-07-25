---
field: dividend_max_guidance_value
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 1.18
best_fitness: 1.13
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.1823
ann_vol: 0.0903
hit_rate: 0.5101
rolling_sharpe_min: -1.238
rolling_sharpe_max: 3.345
redundancy_cluster: 40
negated_best_sharpe: 1.18
negated_best_template: neg_rank_level
negated_best_fitness: 1.13
n_negated_sims: 10
direction_gap: 0.33
---
# dividend_max_guidance_value (analyst4)

*The maximum guidance value for Dividend per share on an annual basis.*

## Signal Profile
- `rank(dividend_max_guidance_value)`: S=0.26, F=0.16, T=13.4%, INFERIOR (TOP200)
- `rank(dividend_max_guidance_value / close)`: S=0.03, F=0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(dividend_max_guidance_value, 5))`: S=0.51, F=0.19, T=33.6%, INFERIOR (TOP200)
- `-rank(dividend_max_guidance_value)`: S=0.75, F=0.50, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_max_guidance_value, 5))`: S=0.24, F=0.05, T=36.1%, INFERIOR (TOP3000)
- `-ts_zscore(dividend_max_guidance_value, 63)`: S=0.85, F=0.39, T=21.4%, INFERIOR (TOP3000)
- `ts_mean(dividend_max_guidance_value, 10)`: S=-0.56, F=-0.32, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(dividend_max_guidance_value, 22))`: S=-0.24, F=-0.08, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * dividend_max_guidance_value)`: S=1.18, F=1.13, T=2.2%, AVERAGE (TOP3000)
- `rank(-1 * dividend_max_guidance_value / close)`: S=0.16, F=0.06, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/25P
- LOW_FITNESS: 29F/3P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.53, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.63 (moderate), ret=+4.2%
  - 2020: S=3.11 (strong), ret=+24.5%
  - 2021: S=-0.26 (negative), ret=-2.7%
  - 2022: S=-0.12 (negative), ret=-1.3%
  - 2023: S=-0.16 (negative), ret=-1.3%

## Risk & Drawdown
- Max drawdown: 18.23% over 975 days (not yet recovered, ongoing at window end)
- Annualized: return +4.8%, volatility 9.0% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.60, excess kurtosis +5.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.24, max 3.35, latest -0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.95%; worst month: -5.15%
Positive months: 51%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.92
- Sideways: S=0.60
- Bear: S=2.32

## Negated Direction
Best negated: `rank(-1 * dividend_max_guidance_value)` S=1.18, F=1.13, AVERAGE
Direction gap: +0.33 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * dividend_max_guidance_value)`: S=1.18, F=1.13, T=2.2%, AVERAGE (TOP3000)
- `rank(-1 * dividend_max_guidance_value / close)`: S=0.16, F=0.06, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_max_guidance_value, 5))`: S=0.24, F=0.05, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(dividend_max_guidance_value, 5))` | TOP200 | 0.53 | 0.19 | 18.2% | 40% | bear-only |
| `rank(dividend_max_guidance_value)` | TOP200 | 0.26 | 0.16 | 51.5% | 40% | weak |

## Correlation Notes
Top correlates:
- dividend_min_guidance_value: 0.998 (strongly positively correlated)
- max_stock_option_expense_guidance: 0.995 (strongly positively correlated)
- min_stock_option_expense_guidance_2: 0.995 (strongly positively correlated)
- dividend_max_guidance_quarterly: 0.982 (strongly positively correlated)
- min_tangible_book_value_per_share_guidance_2: 0.979 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
