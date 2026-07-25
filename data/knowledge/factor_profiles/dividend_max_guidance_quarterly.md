---
field: dividend_max_guidance_quarterly
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.6
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 1
max_drawdown: 0.1607
ann_vol: 0.0917
hit_rate: 0.5085
rolling_sharpe_min: -1.06
rolling_sharpe_max: 3.367
redundancy_cluster: 40
negated_best_sharpe: 0.6
negated_best_template: neg_rank_level
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.01
---
# dividend_max_guidance_quarterly (analyst4)

*Maximum guidance value for Dividend per share*

## Signal Profile
- `rank(dividend_max_guidance_quarterly)`: S=-0.11, F=-0.03, T=1.3%, INFERIOR (TOP1000)
- `rank(dividend_max_guidance_quarterly / close)`: S=0.05, F=0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(dividend_max_guidance_quarterly, 5))`: S=0.58, F=0.23, T=33.5%, INFERIOR (TOP200)
- `-rank(dividend_max_guidance_quarterly)`: S=0.11, F=0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_max_guidance_quarterly, 5))`: S=0.18, F=0.03, T=33.5%, INFERIOR (TOP3000)
- `-ts_zscore(dividend_max_guidance_quarterly, 63)`: S=0.61, F=0.24, T=22.1%, INFERIOR (TOP3000)
- `ts_mean(dividend_max_guidance_quarterly, 10)`: S=0.00, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(dividend_max_guidance_quarterly, 22))`: S=-0.22, F=-0.07, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * dividend_max_guidance_quarterly)`: S=0.60, F=0.32, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * dividend_max_guidance_quarterly / close)`: S=-0.05, F=-0.01, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.60, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.51 (moderate), ret=+3.4%
  - 2020: S=3.12 (strong), ret=+24.9%
  - 2021: S=-0.25 (negative), ret=-2.7%
  - 2022: S=-0.04 (negative), ret=-0.4%
  - 2023: S=0.22 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 16.07% over 975 days (not yet recovered, ongoing at window end)
- Annualized: return +5.5%, volatility 9.2% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.62, excess kurtosis +5.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.06, max 3.37, latest 0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.21%; worst month: -4.80%
Positive months: 58%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.90
- Sideways: S=0.56
- Bear: S=2.59

## Negated Direction
Best negated: `rank(-1 * dividend_max_guidance_quarterly)` S=0.60, F=0.32, INFERIOR
Direction gap: -0.01 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * dividend_max_guidance_quarterly)`: S=0.60, F=0.32, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * dividend_max_guidance_quarterly / close)`: S=-0.05, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_max_guidance_quarterly, 5))`: S=0.18, F=0.03, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(dividend_max_guidance_quarterly, 5))` | TOP200 | 0.60 | 0.23 | 16.1% | 60% | bear-only |

## Correlation Notes
Top correlates:
- dividend_min_guidance_quarterly: 0.990 (strongly positively correlated)
- max_stock_option_expense_guidance: 0.988 (strongly positively correlated)
- min_stock_option_expense_guidance_2: 0.988 (strongly positively correlated)
- dividend_max_guidance_value: 0.982 (strongly positively correlated)
- dividend_min_guidance_value: 0.978 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
