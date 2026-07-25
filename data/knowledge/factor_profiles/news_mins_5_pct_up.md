---
field: news_mins_5_pct_up
dataset: news12
best_template: rank_level
best_sharpe: 0.82
best_fitness: 0.34
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.4468
ann_vol: 0.3407
hit_rate: 0.532
rolling_sharpe_min: -1.079
rolling_sharpe_max: 2.72
top_merge_partner: multi_factor_static_score_derivative
negated_best_sharpe: -0.5
negated_best_template: rank_neg_delta
negated_best_fitness: -0.22
n_negated_sims: 4
direction_gap: -1.32
---
# news_mins_5_pct_up (news12)

*Number of minutes before the price increased by at least 5 percent after the news release*

## Signal Profile
- `rank(news_mins_5_pct_up)`: S=0.82, F=0.34, T=163.3%, INFERIOR (TOP1000)
- `rank(ts_delta(news_mins_5_pct_up, 5))`: S=0.50, F=0.22, T=161.6%, INFERIOR (TOP3000)
- `-rank(news_mins_5_pct_up)`: S=-0.82, F=-0.34, T=163.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_5_pct_up, 5))`: S=-0.50, F=-0.22, T=161.6%, INFERIOR (TOP3000)
- `ts_zscore(news_mins_5_pct_up, 22)`: S=0.40, F=0.13, T=159.5%, INFERIOR (TOP3000)
- `ts_mean(news_mins_5_pct_up, 10)`: S=-0.31, F=-0.09, T=36.4%, INFERIOR (TOP3000)
- `rank(ts_rank(news_mins_5_pct_up, 22))`: S=0.46, F=0.15, T=164.4%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_5_pct_up)`: S=-0.82, F=-0.28, T=160.0%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_5_pct_up / close)`: S=-0.97, F=-0.37, T=156.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 17F/3P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/11P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.84, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.99 (moderate), ret=+31.9%
  - 2020: S=0.02 (weak), ret=+0.7%
  - 2021: S=2.19 (strong), ret=+102.4%
  - 2022: S=0.27 (weak), ret=+6.5%
  - 2023: S=-0.03 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 44.68% over 347 days (recovered)
- Annualized: return +28.7%, volatility 34.1% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew +1.34, excess kurtosis +17.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.08, max 2.72, latest 0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +63.13%; worst month: -19.78%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.84
- Sideways: S=0.58
- Bear: S=-0.05

## Negated Direction
Best negated: `rank(-1 * ts_delta(news_mins_5_pct_up, 5))` S=-0.50, F=-0.22, INFERIOR
Direction gap: -1.32 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_mins_5_pct_up)`: S=-0.82, F=-0.28, T=160.0%, INFERIOR (TOP3000)
- `rank(-1 * news_mins_5_pct_up / close)`: S=-0.97, F=-0.37, T=156.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_mins_5_pct_up, 5))`: S=-0.50, F=-0.22, T=161.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_mins_5_pct_up)` | TOP1000 | 0.84 | 0.34 | 44.7% | 80% | mixed |
| `rank(news_mins_5_pct_up)` | TOP3000 | 0.84 | 0.28 | 35.6% | 60% | mixed |
| `rank(ts_delta(news_mins_5_pct_up, 5))` | TOP3000 | 0.51 | 0.22 | 73.4% | 60% | mixed |
| `rank(news_mins_5_pct_up)` | TOP500 | 0.29 | 0.08 | 49.4% | 60% | weak |

## Correlation Notes
Top correlates:
- news_mins_5_chg: 0.160 (weakly positively correlated)
- news_mins_4_chg: 0.144 (weakly positively correlated)
- scl12_buzz: -0.115 (weakly negatively correlated)
- scl12_buzz_fast_d1: -0.114 (weakly negatively correlated)
- news_ratio_vol: -0.105 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| multi_factor_static_score_derivative | model16 | -0.07 | 1.18 | +0.34 | -0.60 | yes |
| fnd6_cimii | fundamental6 | -0.04 | 1.16 | +0.32 | -0.77 | yes |
| cashflow_efficiency_rank_derivative | model16 | -0.07 | 1.17 | +0.33 | -0.62 | yes |
| growth_potential_rank_derivative | model16 | -0.07 | 1.21 | +0.32 | -0.57 | yes |
| fnd2_propplteqflublgland | fundamental2 | -0.04 | 1.14 | +0.30 | -0.76 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
