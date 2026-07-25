---
field: rp_css_credit_ratings
dataset: news18
best_template: rank_level
best_sharpe: 0.54
best_fitness: 0.17
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.5032
ann_vol: 0.2375
hit_rate: 0.4883
rolling_sharpe_min: -2.351
rolling_sharpe_max: 2.104
negated_best_sharpe: 0.08
negated_best_template: rank_neg_delta
negated_best_fitness: 0.01
n_negated_sims: 4
direction_gap: -0.46
---
# rp_css_credit_ratings (news18)

*Composite sentiment score of credit ratings news*

## Signal Profile
- `rank(rp_css_credit_ratings)`: S=0.54, F=0.17, T=135.5%, INFERIOR (TOP1000)
- `rank(ts_delta(rp_css_credit_ratings, 5))`: S=0.27, F=0.11, T=63.2%, INFERIOR (TOP500)
- `-rank(rp_css_credit_ratings)`: S=-0.54, F=-0.17, T=135.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_credit_ratings, 5))`: S=0.08, F=0.01, T=76.9%, INFERIOR (TOP3000)
- `ts_zscore(rp_css_credit_ratings, 22)`: S=-0.04, F=0.00, T=102.1%, INFERIOR (TOP3000)
- `ts_mean(rp_css_credit_ratings, 10)`: S=0.37, F=0.12, T=38.0%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_credit_ratings, 22))`: S=-0.26, F=-0.06, T=125.6%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_credit_ratings)`: S=-0.08, F=-0.01, T=157.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_credit_ratings / close)`: S=-0.04, F=0.00, T=161.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 13F/7P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.55, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.17 (moderate), ret=+19.0%
  - 2020: S=-0.88 (negative), ret=-16.7%
  - 2021: S=-1.25 (negative), ret=-16.7%
  - 2022: S=0.39 (weak), ret=+7.0%
  - 2023: S=1.80 (strong), ret=+71.4%

## Risk & Drawdown
- Max drawdown: 50.32% over 1336 days (recovered)
- Annualized: return +13.1%, volatility 23.8% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +6.32, excess kurtosis +100.30

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.35, max 2.10, latest 1.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +37.89%; worst month: -15.00%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.58
- Sideways: S=1.19
- Bear: S=-0.31

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_css_credit_ratings, 5))` S=0.08, F=0.01, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_credit_ratings)`: S=-0.08, F=-0.01, T=157.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_credit_ratings / close)`: S=-0.04, F=0.00, T=161.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_credit_ratings, 5))`: S=0.08, F=0.01, T=76.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_credit_ratings)` | TOP1000 | 0.55 | 0.17 | 50.3% | 60% | mixed |
| `rank(ts_delta(rp_css_credit_ratings, 5))` | TOP500 | 0.28 | 0.11 | 45.1% | 60% | mixed |
| `rank(rp_css_credit_ratings)` | TOP500 | 0.29 | 0.07 | 68.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- rp_ess_credit_ratings: 0.497 (moderately positively correlated)
- anl4_qfv4_div_mean: 0.183 (weakly positively correlated)
- est_dividend_ps: 0.182 (weakly positively correlated)
- anl4_rd_exp_flag: 0.146 (weakly positively correlated)
- rp_css_mna: 0.135 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
