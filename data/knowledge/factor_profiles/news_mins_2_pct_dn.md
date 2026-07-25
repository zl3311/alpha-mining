---
field: news_mins_2_pct_dn
dataset: news12
best_template: rank_level
best_sharpe: 0.72
best_fitness: 0.15
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.2289
ann_vol: 0.0915
hit_rate: 0.5061
rolling_sharpe_min: -1.541
rolling_sharpe_max: 3.198
redundancy_cluster: 64
negated_best_sharpe: 0.28
negated_best_template: rank_neg_delta
negated_best_fitness: 0.05
n_negated_sims: 4
direction_gap: -0.44
---
# news_mins_2_pct_dn (news12)

*Number of minutes before the price decreased by at least 2 percent after the news release*

## Signal Profile
- `rank(news_mins_2_pct_dn)`: S=0.72, F=0.15, T=151.8%, INFERIOR (TOP3000)
- `rank(ts_delta(news_mins_2_pct_dn, 5))`: S=-0.13, F=-0.02, T=167.3%, INFERIOR (TOP1000)
- `-rank(news_mins_2_pct_dn)`: S=-0.62, F=-0.13, T=150.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_2_pct_dn, 5))`: S=0.28, F=0.05, T=173.1%, INFERIOR (TOP3000)
- `ts_zscore(news_mins_2_pct_dn, 22)`: S=0.30, F=0.04, T=151.4%, INFERIOR (TOP3000)
- `ts_mean(news_mins_2_pct_dn, 10)`: S=-0.39, F=-0.10, T=30.0%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_2_pct_dn, 22))`: S=0.10, F=0.01, T=153.2%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_2_pct_dn)`: S=-0.72, F=-0.15, T=151.8%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_2_pct_dn / close)`: S=-0.16, F=-0.02, T=144.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/4P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.76, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.52 (strong), ret=+16.9%
  - 2020: S=3.35 (strong), ret=+25.8%
  - 2021: S=0.33 (weak), ret=+3.2%
  - 2022: S=-0.83 (negative), ret=-7.4%
  - 2023: S=-0.67 (negative), ret=-4.3%

## Risk & Drawdown
- Max drawdown: 22.89% over 987 days (not yet recovered, ongoing at window end)
- Annualized: return +7.0%, volatility 9.2% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.18, excess kurtosis +3.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.54, max 3.20, latest -0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +7.88%; worst month: -4.89%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.51
- Sideways: S=1.80
- Bear: S=-0.10

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_mins_2_pct_dn, 5))` S=0.28, F=0.05, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_mins_2_pct_dn)`: S=-0.72, F=-0.15, T=151.8%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_2_pct_dn / close)`: S=-0.16, F=-0.02, T=144.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_2_pct_dn, 5))`: S=0.28, F=0.05, T=173.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mins_2_pct_dn)` | TOP3000 | 0.76 | 0.15 | 22.9% | 60% | mixed |
| `rank(news_mins_2_pct_dn)` | TOP1000 | 0.66 | 0.13 | 22.9% | 60% | bull-only |
| `rank(news_mins_2_pct_dn)` | TOP500 | 0.25 | 0.03 | 33.4% | 40% | mixed |

## Correlation Notes
Top correlates:
- news_mins_3_pct_dn: 0.769 (strongly positively correlated)
- news_mins_1_pct_dn: 0.735 (strongly positively correlated)
- news_mins_2_chg: 0.640 (moderately positively correlated)
- news_mins_3_chg: 0.590 (moderately positively correlated)
- news_mins_4_pct_dn: 0.562 (moderately positively correlated)

Redundancy cluster #64: 2 similar fields, mean |rho| 0.735 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
