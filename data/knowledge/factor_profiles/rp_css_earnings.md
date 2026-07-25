---
field: rp_css_earnings
dataset: news18
cluster: news18_income_earnings
coverage: 0.5
community_alphas: 1694
best_template: rank_level
best_sharpe: 0.39
best_fitness: 0.07
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.094
ann_vol: 0.0789
hit_rate: 0.5142
rolling_sharpe_min: -1.031
rolling_sharpe_max: 1.479
negated_best_sharpe: 0.2
negated_best_template: neg_rank_level
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.19
---
# rp_css_earnings (news18)

*Composite sentiment score of earnings news*

## Signal Profile
- `rank(rp_css_earnings)`: S=0.39, F=0.07, T=96.1%, INFERIOR (TOP200)
- `rank(ts_delta(rp_css_earnings, 5))`: S=0.06, F=0.00, T=130.6%, INFERIOR (TOP200)
- `-rank(rp_css_earnings)`: S=-0.16, F=-0.01, T=117.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_earnings, 5))`: S=0.17, F=0.01, T=162.4%, INFERIOR (TOP3000)
- `-ts_zscore(rp_css_earnings, 63)`: S=0.23, F=0.02, T=125.7%, INFERIOR (TOP3000)
- `ts_mean(rp_css_earnings, 10)`: S=0.04, F=0.00, T=17.4%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_css_earnings, 22))`: S=-0.33, F=-0.03, T=129.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_earnings)`: S=0.20, F=0.02, T=135.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_earnings / close)`: S=0.08, F=0.00, T=138.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/18P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.42, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.40 (negative), ret=-2.4%
  - 2020: S=1.04 (moderate), ret=+8.9%
  - 2021: S=0.42 (weak), ret=+3.8%
  - 2022: S=0.29 (weak), ret=+2.4%
  - 2023: S=0.53 (moderate), ret=+3.4%

## Risk & Drawdown
- Max drawdown: 9.40% over 484 days (recovered)
- Annualized: return +3.3%, volatility 7.9% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.10, excess kurtosis +0.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.03, max 1.48, latest 0.51

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +5.35%; worst month: -4.69%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.89
- Sideways: S=0.62
- Bear: S=-0.27

## Negated Direction
Best negated: `rank(-1 * rp_css_earnings)` S=0.20, F=0.02, INFERIOR
Direction gap: -0.19 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_css_earnings)`: S=0.20, F=0.02, T=135.3%, INFERIOR (TOP3000)
- `rank(-1 * rp_css_earnings / close)`: S=0.08, F=0.00, T=138.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_css_earnings, 5))`: S=0.17, F=0.01, T=162.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_css_earnings)` | TOP200 | 0.42 | 0.07 | 9.4% | 80% | mixed |
| `rank(rp_css_earnings)` | TOP500 | 0.32 | 0.04 | 10.0% | 80% | weak |

## Correlation Notes
Top correlates:
- rp_css_ptg: 0.578 (moderately positively correlated)
- rp_css_revenue: 0.498 (moderately positively correlated)
- fnd6_prchq: -0.362 (weakly negatively correlated)
- rp_ess_price: 0.356 (weakly positively correlated)
- fnd6_prch: -0.353 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
