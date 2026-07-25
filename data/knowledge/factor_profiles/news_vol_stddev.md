---
field: news_vol_stddev
dataset: news12
cluster: news12_analyst_rating
coverage: 0.9672
community_alphas: 903
best_template: neg_rank_level
best_sharpe: 1.05
best_fitness: 0.26
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: weak
n_variations_with_pnl: 4
max_drawdown: 0.1665
ann_vol: 0.0991
hit_rate: 0.5255
rolling_sharpe_min: -1.462
rolling_sharpe_max: 1.946
negated_best_sharpe: 1.05
negated_best_template: neg_rank_level
negated_best_fitness: 0.26
n_negated_sims: 4
direction_gap: 0.68
---
# news_vol_stddev (news12)

*Z-score of current volume compared to 30-day average volume, using 30-day volume standard deviation*

## Signal Profile
- `rank(news_vol_stddev)`: S=0.29, F=0.06, T=65.1%, INFERIOR (TOP200)
- `rank(ts_delta(news_vol_stddev, 5))`: S=0.37, F=0.07, T=99.9%, INFERIOR (TOP200)
- `-rank(news_vol_stddev)`: S=0.13, F=0.01, T=85.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_vol_stddev, 5))`: S=0.01, F=0.00, T=133.3%, INFERIOR (TOP3000)
- `ts_zscore(news_vol_stddev, 22)`: S=0.39, F=0.06, T=95.2%, INFERIOR (TOP3000)
- `ts_mean(news_vol_stddev, 10)`: S=0.07, F=0.01, T=17.4%, INFERIOR (TOP3000)
- `rank(ts_rank(news_vol_stddev, 22))`: S=0.39, F=0.05, T=95.5%, INFERIOR (TOP3000)
- `rank(-1 * news_vol_stddev)`: S=1.05, F=0.26, T=96.0%, INFERIOR (TOP3000)
- `rank(-1 * news_vol_stddev / close)`: S=0.16, F=0.02, T=81.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 18F/2P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.36, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.62 (moderate), ret=+5.1%
  - 2020: S=-0.84 (negative), ret=-7.4%
  - 2021: S=0.03 (weak), ret=+0.4%
  - 2022: S=1.80 (strong), ret=+21.8%
  - 2023: S=-0.34 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 16.65% over 755 days (recovered)
- Annualized: return +3.6%, volatility 9.9% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew -0.36, excess kurtosis +7.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.46, max 1.95, latest -0.36

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.08%; worst month: -7.10%
Positive months: 59%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.40
- Sideways: S=0.65
- Bear: S=0.08

## Negated Direction
Best negated: `rank(-1 * news_vol_stddev)` S=1.05, F=0.26, INFERIOR
Direction gap: +0.68 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * news_vol_stddev)`: S=1.05, F=0.26, T=96.0%, INFERIOR (TOP3000)
- `rank(-1 * news_vol_stddev / close)`: S=0.16, F=0.02, T=81.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_vol_stddev, 5))`: S=0.01, F=0.00, T=133.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_vol_stddev, 5))` | TOP200 | 0.36 | 0.07 | 16.7% | 60% | weak |
| `rank(news_vol_stddev)` | TOP200 | 0.28 | 0.06 | 16.6% | 60% | mixed |
| `rank(ts_delta(news_vol_stddev, 5))` | TOP500 | 0.33 | 0.05 | 13.2% | 40% | mixed |
| `rank(news_vol_stddev)` | TOP500 | 0.29 | 0.05 | 20.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- news_range_stddev: 0.542 (moderately positively correlated)
- news_tot_ticks: 0.530 (moderately positively correlated)
- news_session_range: 0.476 (moderately positively correlated)
- news_atr_ratio: 0.476 (moderately positively correlated)
- scl12_buzz_fast_d1: 0.354 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
