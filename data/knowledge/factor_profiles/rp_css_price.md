---
field: rp_css_price
dataset: news18
best_template: rank_neg_delta
best_sharpe: 0.54
best_fitness: 0.08
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.2151
ann_vol: 0.0719
hit_rate: 0.5093
rolling_sharpe_min: -1.75
rolling_sharpe_max: 3.003
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 4
direction_gap: 0.14
---
# rp_css_price (news18)

*Composite sentiment score of stock price news*

## Signal Profile
- `rank(rp_css_price)`: S=0.11, F=0.01, T=116.4%, INFERIOR (TOP1000)
- `rank(ts_delta(rp_css_price, 5))`: S=0.40, F=0.06, T=123.7%, INFERIOR (TOP500)
- `-rank(rp_css_price)`: S=-0.11, F=-0.01, T=116.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_price, 5))`: S=0.54, F=0.08, T=149.7%, INFERIOR (TOP3000)
- `ts_zscore(rp_css_price, 22)`: S=0.24, F=0.02, T=122.1%, INFERIOR (TOP3000)
- `ts_mean(rp_css_price, 10)`: S=-0.03, F=0.00, T=20.4%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_price, 22))`: S=0.26, F=0.03, T=124.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_price)`: S=0.05, F=0.00, T=136.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_price / close)`: S=0.19, F=0.02, T=138.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/19P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.40, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=2.45 (strong), ret=+19.1%
  - 2020: S=1.62 (strong), ret=+12.0%
  - 2021: S=-0.52 (negative), ret=-4.4%
  - 2022: S=-1.46 (negative), ret=-9.6%
  - 2023: S=-0.76 (negative), ret=-3.2%

## Risk & Drawdown
- Max drawdown: 21.51% over 1081 days (not yet recovered, ongoing at window end)
- Annualized: return +2.9%, volatility 7.2% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.15, excess kurtosis +2.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.75, max 3.00, latest -0.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +4.68%; worst month: -4.62%
Positive months: 51%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.35
- Sideways: S=1.57
- Bear: S=0.98

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_css_price, 5))` S=0.54, F=0.08, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_css_price)`: S=0.05, F=0.00, T=136.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_price / close)`: S=0.19, F=0.02, T=138.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_price, 5))`: S=0.54, F=0.08, T=149.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_css_price, 5))` | TOP500 | 0.40 | 0.06 | 21.5% | 40% | bear-only |
| `rank(ts_delta(rp_css_price, 5))` | TOP1000 | 0.26 | 0.03 | 19.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- rp_css_business: 0.322 (weakly positively correlated)
- rp_ess_price: 0.143 (weakly positively correlated)
- rp_ess_ratings: 0.118 (weakly positively correlated)
- min_capex_guidance: 0.113 (weakly positively correlated)
- capital_expenditure_max_guidance_qtr: 0.113 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
