---
field: rp_ess_business
dataset: news18
best_template: neg_rank_value_norm
best_sharpe: 0.49
best_fitness: 0.08
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.1279
ann_vol: 0.0769
hit_rate: 0.4947
rolling_sharpe_min: -1.068
rolling_sharpe_max: 1.23
negated_best_sharpe: 0.49
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.08
n_negated_sims: 4
direction_gap: 0.28
---
# rp_ess_business (news18)

*Event sentiment score of business-related news*

## Signal Profile
- `rank(rp_ess_business)`: S=-0.12, F=-0.02, T=50.2%, INFERIOR (TOP200)
- `rank(ts_delta(rp_ess_business, 5))`: S=0.21, F=0.03, T=81.1%, INFERIOR (TOP200)
- `-rank(rp_ess_business)`: S=0.19, F=0.03, T=71.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_business, 5))`: S=0.06, F=0.00, T=130.5%, INFERIOR (TOP3000)
- `-ts_zscore(rp_ess_business, 63)`: S=0.01, F=0.00, T=78.7%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_business, 10)`: S=-0.25, F=-0.10, T=14.1%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_business, 22))`: S=-0.31, F=-0.04, T=85.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_business)`: S=0.31, F=0.05, T=97.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_business / close)`: S=0.49, F=0.08, T=97.9%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 17F/3P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.21, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.46 (weak), ret=+2.6%
  - 2020: S=0.09 (weak), ret=+0.7%
  - 2021: S=0.53 (moderate), ret=+5.2%
  - 2022: S=-0.23 (negative), ret=-1.9%
  - 2023: S=0.20 (weak), ret=+1.1%

## Risk & Drawdown
- Max drawdown: 12.79% over 758 days (not yet recovered, ongoing at window end)
- Annualized: return +1.6%, volatility 7.7% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew -0.51, excess kurtosis +6.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.07, max 1.23, latest 0.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +6.77%; worst month: -4.57%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.09
- Sideways: S=-0.80
- Bear: S=1.24

## Negated Direction
Best negated: `rank(-1 * rp_ess_business / close)` S=0.49, F=0.08, INFERIOR
Direction gap: +0.28 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_ess_business)`: S=0.31, F=0.05, T=97.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_business / close)`: S=0.49, F=0.08, T=97.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_business, 5))`: S=0.06, F=0.00, T=130.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_business, 5))` | TOP200 | 0.21 | 0.03 | 12.8% | 80% | mixed |

## Correlation Notes
Top correlates:
- rp_css_business: 0.383 (weakly positively correlated)
- rp_ess_price: 0.322 (weakly positively correlated)
- rank(scl12_buzz * (-1 * returns)): -0.222 (weakly negatively correlated)
- scl12_sentiment_fast_d1: 0.212 (weakly positively correlated)
- rank(fnd6_acdo) * rank(-1 * returns): -0.203 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
