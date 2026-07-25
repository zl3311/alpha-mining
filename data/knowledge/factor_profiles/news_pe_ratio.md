---
field: news_pe_ratio
dataset: news12
cluster: news12_income_earnings
coverage: 0.9662
community_alphas: 2817
best_template: ts_zscore
best_sharpe: 0.58
best_fitness: 0.12
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 23
regime_profile: weak
n_variations_with_pnl: 1
max_drawdown: 0.2522
ann_vol: 0.1131
hit_rate: 0.5093
rolling_sharpe_min: -1.67
rolling_sharpe_max: 2.601
negated_best_sharpe: 0.44
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 4
direction_gap: -0.14
---
# news_pe_ratio (news12)

*Reported price-to-earnings ratio for the calendar day of the session*

## Signal Profile
- `rank(news_pe_ratio)`: S=0.22, F=0.06, T=38.3%, INFERIOR (TOP200)
- `rank(news_pe_ratio / close)`: S=-0.30, F=-0.05, T=61.9%, INFERIOR (TOP3000)
- `rank(ts_delta(news_pe_ratio, 5))`: S=-0.44, F=-0.07, T=112.8%, INFERIOR (TOP3000)
- `-rank(news_pe_ratio)`: S=0.17, F=0.02, T=62.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pe_ratio, 5))`: S=0.44, F=0.07, T=112.8%, INFERIOR (TOP3000)
- `-ts_zscore(news_pe_ratio, 63)`: S=0.58, F=0.12, T=68.2%, INFERIOR (TOP3000)
- `ts_mean(news_pe_ratio, 10)`: S=-0.06, F=-0.02, T=7.1%, INFERIOR (TOP3000)
- `rank(ts_rank(news_pe_ratio, 22))`: S=-0.75, F=-0.18, T=78.6%, INFERIOR (TOP3000)
- `rank(-1 * news_pe_ratio)`: S=0.09, F=0.01, T=75.4%, INFERIOR (TOP3000)
- `rank(-1 * news_pe_ratio / close)`: S=0.18, F=0.02, T=73.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/14P
- HIGH_TURNOVER: 14F/9P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 23F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.24, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.12 (weak), ret=+1.1%
  - 2020: S=1.12 (moderate), ret=+11.6%
  - 2021: S=-0.88 (negative), ret=-13.0%
  - 2022: S=-0.66 (negative), ret=-7.7%
  - 2023: S=2.52 (strong), ret=+21.4%

## Risk & Drawdown
- Max drawdown: 25.22% over 1102 days (not yet recovered, ongoing at window end)
- Annualized: return +2.8%, volatility 11.3% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.41, excess kurtosis +5.33

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.67, max 2.60, latest 2.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +8.09%; worst month: -7.36%
Positive months: 54%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.17
- Sideways: S=0.82
- Bear: S=0.20

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_pe_ratio, 5))` S=0.44, F=0.07, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_pe_ratio)`: S=0.09, F=0.01, T=75.4%, INFERIOR (TOP3000)
- `rank(-1 * news_pe_ratio / close)`: S=0.18, F=0.02, T=73.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_pe_ratio, 5))`: S=0.44, F=0.07, T=112.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_pe_ratio)` | TOP200 | 0.24 | 0.06 | 25.2% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_cstk: -0.424 (moderately negatively correlated)
- fn_accum_oth_income_loss_net_of_tax_q: 0.423 (moderately positively correlated)
- fnd6_incorp: -0.422 (moderately negatively correlated)
- fnd6_cstkcvq: -0.420 (moderately negatively correlated)
- fnd2_a_rvndm: -0.418 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
