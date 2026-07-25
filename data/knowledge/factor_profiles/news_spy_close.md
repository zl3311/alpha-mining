---
field: news_spy_close
dataset: news12
best_template: rank_delta
best_sharpe: 0.48
best_fitness: 0.07
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1237
ann_vol: 0.0569
hit_rate: 0.5004
rolling_sharpe_min: -1.697
rolling_sharpe_max: 2.452
negated_best_sharpe: 0.45
negated_best_template: neg_rank
negated_best_fitness: 0.05
n_negated_sims: 4
direction_gap: -0.03
---
# news_spy_close (news12)

*SPY price at session close*

## Signal Profile
- `rank(news_spy_close)`: S=0.37, F=0.05, T=112.3%, INFERIOR (TOP500)
- `rank(news_spy_close / close)`: S=-0.04, F=0.00, T=60.3%, INFERIOR (TOP3000)
- `rank(ts_delta(news_spy_close, 5))`: S=0.48, F=0.07, T=123.5%, INFERIOR (TOP500)
- `-rank(news_spy_close)`: S=0.45, F=0.05, T=118.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_spy_close, 5))`: S=-0.01, F=0.00, T=140.6%, INFERIOR (TOP3000)
- `ts_zscore(news_spy_close, 22)`: S=0.19, F=0.02, T=96.4%, INFERIOR (TOP3000)
- `ts_mean(news_spy_close, 10)`: S=-0.55, F=-0.17, T=33.5%, INFERIOR (TOP3000)
- `rank(ts_rank(news_spy_close, 22))`: S=0.10, F=0.01, T=96.0%, INFERIOR (TOP3000)
- `rank(-1 * news_spy_close)`: S=-0.03, F=0.00, T=125.5%, INFERIOR (TOP3000)
- `rank(-1 * news_spy_close / close)`: S=0.17, F=0.03, T=70.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 19F/2P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.48, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.19 (negative), ret=-0.9%
  - 2020: S=1.88 (strong), ret=+11.0%
  - 2021: S=-0.65 (negative), ret=-4.2%
  - 2022: S=0.41 (weak), ret=+2.5%
  - 2023: S=1.15 (moderate), ret=+5.0%

## Risk & Drawdown
- Max drawdown: 12.37% over 997 days (recovered)
- Annualized: return +2.7%, volatility 5.7% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew -0.01, excess kurtosis +1.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.70, max 2.45, latest 1.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +4.76%; worst month: -4.41%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.03
- Sideways: S=0.92
- Bear: S=0.58

## Negated Direction
Best negated: `-rank(news_spy_close)` S=0.45, F=0.05, INFERIOR
Direction gap: -0.03 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_spy_close)`: S=-0.03, F=0.00, T=125.5%, INFERIOR (TOP3000)
- `rank(-1 * news_spy_close / close)`: S=0.17, F=0.03, T=70.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_spy_close, 5))`: S=-0.01, F=0.00, T=140.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_spy_close, 5))` | TOP500 | 0.48 | 0.07 | 12.4% | 60% | mixed |
| `rank(news_spy_close)` | TOP500 | 0.39 | 0.05 | 6.9% | 60% | weak |

## Correlation Notes
Top correlates:
- dividend_max_guidance_quarterly: -0.176 (weakly negatively correlated)
- max_stock_option_expense_guidance: -0.173 (weakly negatively correlated)
- min_stock_option_expense_guidance_2: -0.173 (weakly negatively correlated)
- dividend_min_guidance_quarterly: -0.172 (weakly negatively correlated)
- dividend_max_guidance_value: -0.170 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
