---
field: dividend_min_guidance_quarterly
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
max_drawdown: 0.1738
ann_vol: 0.0911
hit_rate: 0.515
rolling_sharpe_min: -1.137
rolling_sharpe_max: 3.391
redundancy_cluster: 40
negated_best_sharpe: 0.6
negated_best_template: neg_rank_level
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: 0.02
---
# dividend_min_guidance_quarterly (analyst4)

*Minimum guidance value for Dividend per share*

## Signal Profile
- `rank(dividend_min_guidance_quarterly)`: S=-0.11, F=-0.03, T=1.3%, INFERIOR (TOP1000)
- `rank(dividend_min_guidance_quarterly / close)`: S=0.05, F=0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(dividend_min_guidance_quarterly, 5))`: S=0.58, F=0.23, T=33.6%, INFERIOR (TOP200)
- `-rank(dividend_min_guidance_quarterly)`: S=0.11, F=0.03, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_min_guidance_quarterly, 5))`: S=0.26, F=0.05, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(dividend_min_guidance_quarterly, 63)`: S=0.51, F=0.19, T=19.8%, INFERIOR (TOP3000)
- `ts_mean(dividend_min_guidance_quarterly, 10)`: S=-0.09, F=-0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(dividend_min_guidance_quarterly, 22))`: S=-0.25, F=-0.08, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * dividend_min_guidance_quarterly)`: S=0.60, F=0.32, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * dividend_min_guidance_quarterly / close)`: S=-0.05, F=-0.01, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.60, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.46 (weak), ret=+3.0%
  - 2020: S=3.08 (strong), ret=+24.7%
  - 2021: S=-0.30 (negative), ret=-3.2%
  - 2022: S=-0.05 (negative), ret=-0.5%
  - 2023: S=0.31 (weak), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 17.38% over 975 days (not yet recovered, ongoing at window end)
- Annualized: return +5.4%, volatility 9.1% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.63, excess kurtosis +5.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 3.39, latest 0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.38%; worst month: -4.44%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.96
- Sideways: S=0.55
- Bear: S=2.68

## Negated Direction
Best negated: `rank(-1 * dividend_min_guidance_quarterly)` S=0.60, F=0.32, INFERIOR
Direction gap: +0.02 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * dividend_min_guidance_quarterly)`: S=0.60, F=0.32, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * dividend_min_guidance_quarterly / close)`: S=-0.05, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(dividend_min_guidance_quarterly, 5))`: S=0.26, F=0.05, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(dividend_min_guidance_quarterly, 5))` | TOP200 | 0.60 | 0.23 | 17.4% | 60% | bear-only |

## Correlation Notes
Top correlates:
- dividend_max_guidance_quarterly: 0.990 (strongly positively correlated)
- max_stock_option_expense_guidance: 0.958 (strongly positively correlated)
- min_stock_option_expense_guidance_2: 0.958 (strongly positively correlated)
- dividend_max_guidance_value: 0.953 (strongly positively correlated)
- dividend_min_guidance_value: 0.948 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
