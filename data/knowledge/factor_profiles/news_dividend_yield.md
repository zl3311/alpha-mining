---
field: news_dividend_yield
dataset: news12
best_template: ts_mean
best_sharpe: 1.0
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1476
ann_vol: 0.0876
hit_rate: 0.4891
rolling_sharpe_min: -1.533
rolling_sharpe_max: 2.378
negated_best_sharpe: 0.07
negated_best_template: neg_rank
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.93
---
# news_dividend_yield (news12)

*Reported annual dividend yield percentage for the calendar day of the session*

## Signal Profile
- `rank(news_dividend_yield)`: S=0.64, F=0.16, T=88.5%, INFERIOR (TOP3000)
- `rank(news_dividend_yield / close)`: S=0.26, F=0.05, T=73.1%, INFERIOR (TOP3000)
- `rank(ts_delta(news_dividend_yield, 5))`: S=-0.05, F=0.00, T=109.9%, INFERIOR (TOP3000)
- `-rank(news_dividend_yield)`: S=0.07, F=0.01, T=72.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_dividend_yield, 5))`: S=0.05, F=0.00, T=109.9%, INFERIOR (TOP3000)
- `ts_zscore(news_dividend_yield, 22)`: S=0.93, F=0.28, T=81.2%, INFERIOR (TOP3000)
- `ts_mean(news_dividend_yield, 10)`: S=1.00, F=0.78, T=16.2%, INFERIOR (TOP3000)
- `rank(ts_rank(news_dividend_yield, 22))`: S=0.75, F=0.19, T=86.3%, INFERIOR (TOP3000)
- `rank(-1 * news_dividend_yield)`: S=-0.64, F=-0.16, T=88.5%, INFERIOR (TOP3000)
- `rank(-1 * news_dividend_yield / close)`: S=-0.81, F=-0.25, T=87.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 17F/4P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-1.26 (negative), ret=-10.3%
  - 2020: S=1.04 (moderate), ret=+9.5%
  - 2021: S=0.92 (moderate), ret=+10.2%
  - 2022: S=1.42 (moderate), ret=+11.7%
  - 2023: S=1.15 (moderate), ret=+5.9%

## Risk & Drawdown
- Max drawdown: 14.76% over 743 days (recovered)
- Annualized: return +5.5%, volatility 8.8% (fraction of booksize)
- Hit rate: 48.9% positive days
- Tail shape: skew +2.25, excess kurtosis +26.05

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.53, max 2.38, latest 1.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +12.64%; worst month: -4.65%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.17
- Sideways: S=-1.15
- Bear: S=0.39

## Negated Direction
Best negated: `-rank(news_dividend_yield)` S=0.07, F=0.01, INFERIOR
Direction gap: -0.93 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_dividend_yield)`: S=-0.64, F=-0.16, T=88.5%, INFERIOR (TOP3000)
- `rank(-1 * news_dividend_yield / close)`: S=-0.81, F=-0.25, T=87.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_dividend_yield, 5))`: S=0.05, F=0.00, T=109.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_dividend_yield)` | TOP3000 | 0.63 | 0.16 | 14.8% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_bkvlps: 0.485 (moderately positively correlated)
- fscore_bfl_value: 0.485 (moderately positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_q: 0.483 (moderately positively correlated)
- fn_line_of_credit_facility_max_borrowing_capacity_a: 0.476 (moderately positively correlated)
- fn_comp_options_exercisable_weighted_avg_a: 0.475 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
