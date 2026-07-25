---
field: news_curr_vol
dataset: news12
best_template: neg_rank_value_norm
best_sharpe: 0.24
best_fitness: 0.04
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: weak
n_variations_with_pnl: 1
max_drawdown: 0.2289
ann_vol: 0.0937
hit_rate: 0.4964
rolling_sharpe_min: -1.821
rolling_sharpe_max: 2.048
negated_best_sharpe: 0.24
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: 0.06
---
# news_curr_vol (news12)

*Current day's session volume*

## Signal Profile
- `rank(news_curr_vol)`: S=0.18, F=0.03, T=56.0%, INFERIOR (TOP200)
- `rank(news_curr_vol / close)`: S=-0.04, F=0.00, T=76.0%, INFERIOR (TOP3000)
- `rank(ts_delta(news_curr_vol, 5))`: S=0.10, F=0.01, T=117.2%, INFERIOR (TOP500)
- `-rank(news_curr_vol)`: S=0.02, F=0.00, T=82.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_curr_vol, 5))`: S=0.01, F=0.00, T=135.2%, INFERIOR (TOP3000)
- `ts_zscore(news_curr_vol, 22)`: S=0.23, F=0.03, T=110.6%, INFERIOR (TOP3000)
- `ts_mean(news_curr_vol, 10)`: S=0.08, F=0.03, T=9.8%, INFERIOR (TOP3000)
- `rank(ts_rank(news_curr_vol, 22))`: S=-0.02, F=0.00, T=113.3%, INFERIOR (TOP3000)
- `rank(-1 * news_curr_vol)`: S=0.23, F=0.03, T=94.7%, INFERIOR (TOP3000)
- `rank(-1 * news_curr_vol / close)`: S=0.24, F=0.04, T=91.8%, INFERIOR (TOP3000)

## Check Summary
- HIGH_TURNOVER: 19F/2P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.17, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.73 (moderate), ret=+4.9%
  - 2020: S=-0.35 (negative), ret=-3.6%
  - 2021: S=-0.70 (negative), ret=-8.5%
  - 2022: S=0.72 (moderate), ret=+6.6%
  - 2023: S=1.34 (moderate), ret=+8.6%

## Risk & Drawdown
- Max drawdown: 22.89% over 1019 days (not yet recovered, ongoing at window end)
- Annualized: return +1.6%, volatility 9.4% (fraction of booksize)
- Hit rate: 49.6% positive days
- Tail shape: skew +0.41, excess kurtosis +3.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.82, max 2.05, latest 1.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +8.71%; worst month: -4.99%
Positive months: 49%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.34
- Sideways: S=-0.31
- Bear: S=0.40

## Negated Direction
Best negated: `rank(-1 * news_curr_vol / close)` S=0.24, F=0.04, INFERIOR
Direction gap: +0.06 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * news_curr_vol)`: S=0.23, F=0.03, T=94.7%, INFERIOR (TOP3000)
- `rank(-1 * news_curr_vol / close)`: S=0.24, F=0.04, T=91.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_curr_vol, 5))`: S=0.01, F=0.00, T=135.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_curr_vol)` | TOP200 | 0.17 | 0.03 | 22.9% | 60% | weak |

## Correlation Notes
Top correlates:
- news_mov_vol: 0.877 (strongly positively correlated)
- volume: 0.871 (strongly positively correlated)
- fnd6_cshtrq: 0.754 (strongly positively correlated)
- anl4_epsa_flag: 0.662 (moderately positively correlated)
- fn_antidilutive_securities_excl_from_eps_a: 0.584 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
