---
field: news_max_dn_amt
dataset: news12
best_template: rank_delta
best_sharpe: 0.78
best_fitness: 0.17
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1221
ann_vol: 0.0761
hit_rate: 0.5198
rolling_sharpe_min: -0.989
rolling_sharpe_max: 3.229
redundancy_cluster: 42
negated_best_sharpe: 0.35
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.06
n_negated_sims: 4
direction_gap: -0.43
---
# news_max_dn_amt (news12)

*Price at the time of the news minus the after-news low*

## Signal Profile
- `rank(news_max_dn_amt)`: S=0.41, F=0.08, T=82.7%, INFERIOR (TOP500)
- `rank(news_max_dn_amt / close)`: S=0.24, F=0.04, T=111.0%, INFERIOR (TOP3000)
- `rank(ts_delta(news_max_dn_amt, 5))`: S=0.78, F=0.17, T=124.6%, INFERIOR (TOP500)
- `-rank(news_max_dn_amt)`: S=-0.37, F=-0.06, T=95.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_max_dn_amt, 5))`: S=-0.51, F=-0.08, T=144.5%, INFERIOR (TOP3000)
- `ts_zscore(news_max_dn_amt, 22)`: S=0.57, F=0.09, T=114.3%, INFERIOR (TOP3000)
- `ts_mean(news_max_dn_amt, 10)`: S=-0.36, F=-0.18, T=12.6%, INFERIOR (TOP3000)
- `rank(ts_rank(news_max_dn_amt, 22))`: S=0.81, F=0.15, T=118.6%, INFERIOR (TOP3000)
- `rank(-1 * news_max_dn_amt)`: S=-0.04, F=0.00, T=111.5%, INFERIOR (TOP3000)
- `rank(-1 * news_max_dn_amt / close)`: S=0.35, F=0.06, T=125.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/20P
- HIGH_TURNOVER: 19F/2P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=2.17 (strong), ret=+14.0%
  - 2020: S=0.31 (weak), ret=+2.3%
  - 2021: S=0.60 (moderate), ret=+5.5%
  - 2022: S=0.72 (moderate), ret=+6.2%
  - 2023: S=0.16 (weak), ret=+0.8%

## Risk & Drawdown
- Max drawdown: 12.21% over 562 days (not yet recovered, ongoing at window end)
- Annualized: return +5.9%, volatility 7.6% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.07, excess kurtosis +2.39

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 3.23, latest 0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +5.61%; worst month: -6.89%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.83
- Sideways: S=1.13
- Bear: S=-0.59

## Negated Direction
Best negated: `rank(-1 * news_max_dn_amt / close)` S=0.35, F=0.06, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_max_dn_amt)`: S=-0.04, F=0.00, T=111.5%, INFERIOR (TOP3000)
- `rank(-1 * news_max_dn_amt / close)`: S=0.35, F=0.06, T=125.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_max_dn_amt, 5))`: S=-0.51, F=-0.08, T=144.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_max_dn_amt, 5))` | TOP500 | 0.77 | 0.17 | 12.2% | 100% | bull-only |
| `rank(ts_delta(news_max_dn_amt, 5))` | TOP1000 | 0.78 | 0.15 | 8.5% | 100% | mixed |
| `rank(ts_delta(news_max_dn_amt, 5))` | TOP200 | 0.51 | 0.11 | 15.5% | 60% | bull-only |
| `rank(news_max_dn_amt)` | TOP500 | 0.42 | 0.08 | 16.5% | 40% | bull-only |
| `rank(ts_delta(news_max_dn_amt, 5))` | TOP3000 | 0.50 | 0.08 | 8.1% | 80% | mixed |
| `rank(news_max_dn_amt)` | TOP1000 | 0.37 | 0.06 | 23.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- news_low_exc_stddev: 0.772 (strongly positively correlated)
- news_max_dn_ret: 0.579 (moderately positively correlated)
- news_session_range: 0.428 (moderately positively correlated)
- news_range_stddev: 0.325 (weakly positively correlated)
- news_tot_ticks: 0.325 (weakly positively correlated)

Redundancy cluster #42: 2 similar fields, mean |rho| 0.772 (representative: news_low_exc_stddev). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
