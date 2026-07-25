---
field: rp_css_equity
dataset: news18
cluster: news18_balance_sheet_equity
coverage: 0.5
community_alphas: 938
best_template: rank_level
best_sharpe: 0.43
best_fitness: 0.05
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.0844
ann_vol: 0.044
hit_rate: 0.549
rolling_sharpe_min: -1.928
rolling_sharpe_max: 2.451
negated_best_sharpe: 0.01
negated_best_template: neg_rank
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.42
---
# rp_css_equity (news18)

*Composite sentiment score of equity action news*

## Signal Profile
- `rank(rp_css_equity)`: S=0.43, F=0.05, T=140.3%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_css_equity, 5))`: S=0.15, F=0.01, T=145.0%, INFERIOR (TOP500)
- `-rank(rp_css_equity)`: S=0.01, F=0.00, T=121.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_equity, 5))`: S=0.03, F=0.00, T=164.0%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_equity, 63)`: S=0.16, F=0.01, T=129.0%, INFERIOR (TOP3000)
- `ts_mean(rp_css_equity, 10)`: S=-0.14, F=-0.03, T=16.2%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_equity, 22))`: S=0.09, F=0.00, T=133.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_equity)`: S=-0.43, F=-0.05, T=140.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_equity / close)`: S=-0.64, F=-0.09, T=143.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/18P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.44, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.46 (moderate), ret=+6.2%
  - 2020: S=-0.27 (negative), ret=-1.1%
  - 2021: S=1.18 (moderate), ret=+5.4%
  - 2022: S=1.38 (moderate), ret=+6.3%
  - 2023: S=-1.83 (negative), ret=-7.2%

## Risk & Drawdown
- Max drawdown: 8.44% over 366 days (not yet recovered, ongoing at window end)
- Annualized: return +1.9%, volatility 4.4% (fraction of booksize)
- Hit rate: 54.9% positive days
- Tail shape: skew -0.57, excess kurtosis +2.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.93, max 2.45, latest -1.92

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +2.99%; worst month: -3.06%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.33
- Sideways: S=1.22
- Bear: S=0.54

## Negated Direction
Best negated: `-rank(rp_css_equity)` S=0.01, F=0.00, INFERIOR
Direction gap: -0.42 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_equity)`: S=-0.43, F=-0.05, T=140.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_equity / close)`: S=-0.64, F=-0.09, T=143.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_equity, 5))`: S=0.03, F=0.00, T=164.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_equity)` | TOP3000 | 0.44 | 0.05 | 8.4% | 60% | mixed |
| `rank(rp_css_equity)` | TOP200 | 0.35 | 0.05 | 9.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_prch: -0.527 (moderately negatively correlated)
- fn_oth_comp_fair_value_a: -0.521 (moderately negatively correlated)
- fn_oth_comp_grants_weighted_avg_grant_date_fair_value_a: -0.505 (moderately negatively correlated)
- fn_oth_comp_forfeitures_fair_value_a: -0.500 (moderately negatively correlated)
- fnd6_prchq: -0.493 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
