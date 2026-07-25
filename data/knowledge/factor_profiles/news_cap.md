---
field: news_cap
dataset: news12
cluster: news12_valuation
coverage: 0.8272
community_alphas: 6635
best_template: rank_neg_delta
best_sharpe: 0.46
best_fitness: 0.07
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4115
ann_vol: 0.1294
hit_rate: 0.5134
rolling_sharpe_min: -2.972
rolling_sharpe_max: 2.1
negated_best_sharpe: 0.46
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 4
direction_gap: 0.13
---
# news_cap (news12)

*Reported total market capitalization for the calendar day of the session*

## Signal Profile
- `rank(news_cap)`: S=0.24, F=0.05, T=72.2%, INFERIOR (TOP3000)
- `rank(ts_delta(news_cap, 5))`: S=-0.33, F=-0.05, T=106.5%, INFERIOR (TOP500)
- `-rank(news_cap)`: S=-0.04, F=0.00, T=59.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_cap, 5))`: S=0.46, F=0.07, T=122.9%, INFERIOR (TOP3000)
- `-ts_zscore(news_cap, 63)`: S=0.33, F=0.06, T=83.1%, INFERIOR (TOP3000)
- `ts_mean(news_cap, 10)`: S=0.11, F=0.04, T=3.8%, INFERIOR (TOP3000)
- `rank(ts_rank(news_cap, 22))`: S=-0.29, F=-0.04, T=94.9%, INFERIOR (TOP3000)
- `rank(-1 * news_cap)`: S=-0.24, F=-0.05, T=72.2%, INFERIOR (TOP3000)
- `rank(-1 * news_cap / close)`: S=-0.49, F=-0.11, T=73.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/11P
- HIGH_TURNOVER: 13F/7P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.24, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.31 (moderate), ret=+11.2%
  - 2020: S=-1.64 (negative), ret=-17.7%
  - 2021: S=0.28 (weak), ret=+4.7%
  - 2022: S=1.15 (moderate), ret=+15.9%
  - 2023: S=0.09 (weak), ret=+1.1%

## Risk & Drawdown
- Max drawdown: 41.15% over 1117 days (recovered)
- Annualized: return +3.1%, volatility 12.9% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.11, excess kurtosis +0.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.97, max 2.10, latest -0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +8.34%; worst month: -8.61%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.19
- Sideways: S=1.42
- Bear: S=-3.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_cap, 5))` S=0.46, F=0.07, INFERIOR
Direction gap: +0.13 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_cap)`: S=-0.24, F=-0.05, T=72.2%, INFERIOR (TOP3000)
- `rank(-1 * news_cap / close)`: S=-0.49, F=-0.11, T=73.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_cap, 5))`: S=0.46, F=0.07, T=122.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_cap)` | TOP3000 | 0.24 | 0.05 | 41.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- cap: 0.935 (strongly positively correlated)
- fnd6_newqv1300_seqq: 0.919 (strongly positively correlated)
- fnd6_cptmfmq_ceqq: 0.919 (strongly positively correlated)
- equity: 0.919 (strongly positively correlated)
- fnd6_cptnewqv1300_ceqq: 0.919 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
