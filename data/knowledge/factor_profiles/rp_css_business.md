---
field: rp_css_business
dataset: news18
cluster: news18_analyst_rating
coverage: 0.5
community_alphas: 3294
best_template: rank_delta
best_sharpe: 0.73
best_fitness: 0.18
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0951
ann_vol: 0.0722
hit_rate: 0.5061
rolling_sharpe_min: -0.698
rolling_sharpe_max: 2.115
negated_best_sharpe: 0.39
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: -0.34
---
# rp_css_business (news18)

*Composite sentiment score of business-related news*

## Signal Profile
- `rank(rp_css_business)`: S=0.34, F=0.07, T=57.0%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_business, 5))`: S=0.73, F=0.18, T=84.0%, INFERIOR (TOP200)
- `-rank(rp_css_business)`: S=-0.16, F=-0.02, T=79.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_business, 5))`: S=0.39, F=0.04, T=132.4%, INFERIOR (TOP3000)
- `ts_zscore(rp_css_business, 22)`: S=0.11, F=0.01, T=89.1%, INFERIOR (TOP3000)
- `ts_mean(rp_css_business, 10)`: S=-0.13, F=-0.03, T=16.8%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_business, 22))`: S=0.15, F=0.01, T=91.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_business)`: S=0.08, F=0.00, T=105.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_business / close)`: S=0.24, F=0.02, T=105.9%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 17F/3P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.73, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.90 (strong), ret=+10.2%
  - 2020: S=0.52 (moderate), ret=+3.7%
  - 2021: S=0.70 (moderate), ret=+6.6%
  - 2022: S=0.03 (weak), ret=+0.2%
  - 2023: S=1.01 (moderate), ret=+5.2%

## Risk & Drawdown
- Max drawdown: 9.51% over 182 days (recovered)
- Annualized: return +5.3%, volatility 7.2% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew -0.02, excess kurtosis +6.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.70, max 2.12, latest 0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +6.48%; worst month: -5.63%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.30
- Sideways: S=1.02
- Bear: S=1.01

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_css_business, 5))` S=0.39, F=0.04, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_business)`: S=0.08, F=0.00, T=105.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_business / close)`: S=0.24, F=0.02, T=105.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_business, 5))`: S=0.39, F=0.04, T=132.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_css_business, 5))` | TOP200 | 0.73 | 0.18 | 9.5% | 100% | mixed |
| `rank(rp_css_business)` | TOP200 | 0.36 | 0.07 | 12.1% | 80% | mixed |
| `rank(ts_delta(rp_css_business, 5))` | TOP500 | 0.29 | 0.04 | 12.6% | 80% | bear-only |
| `rank(rp_css_business)` | TOP500 | 0.16 | 0.02 | 11.5% | 60% | weak |

## Correlation Notes
Top correlates:
- rp_ess_business: 0.383 (weakly positively correlated)
- rp_css_price: 0.322 (weakly positively correlated)
- rp_ess_price: 0.255 (weakly positively correlated)
- scl12_sentiment_fast_d1: 0.191 (weakly positively correlated)
- rp_css_earnings: 0.186 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
