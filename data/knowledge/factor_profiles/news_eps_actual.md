---
field: news_eps_actual
dataset: news12
best_template: ts_mean
best_sharpe: 0.75
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.3313
ann_vol: 0.2233
hit_rate: 0.2372
rolling_sharpe_min: -1.091
rolling_sharpe_max: 2.258
negated_best_sharpe: 0.18
negated_best_template: neg_rank
negated_best_fitness: 0.04
n_negated_sims: 4
direction_gap: -0.57
---
# news_eps_actual (news12)

*Actual Earnings Per Share reported in the news release*

## Signal Profile
- `rank(news_eps_actual)`: S=0.57, F=0.27, T=54.6%, INFERIOR (TOP200)
- `rank(news_eps_actual / close)`: S=-0.22, F=-0.06, T=98.3%, INFERIOR (TOP3000)
- `rank(ts_delta(news_eps_actual, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `-rank(news_eps_actual)`: S=0.18, F=0.04, T=98.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_eps_actual, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `-ts_zscore(news_eps_actual, 63)`: S=0.67, F=0.34, T=74.6%, INFERIOR (TOP3000)
- `ts_mean(news_eps_actual, 10)`: S=0.75, F=0.42, T=48.4%, INFERIOR (TOP3000)
- `rank(ts_rank(news_eps_actual, 22))`: S=-0.17, F=-0.04, T=103.8%, INFERIOR (TOP3000)
- `rank(-1 * news_eps_actual)`: S=-0.49, F=-0.18, T=120.5%, INFERIOR (TOP3000)
- `rank(-1 * news_eps_actual / close)`: S=-0.46, F=-0.17, T=121.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 11F/10P
- LOW_FITNESS: 14F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/5P
- LOW_TURNOVER: 7F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.61 (strong), ret=+23.4%
  - 2020: S=-1.00 (negative), ret=-28.9%
  - 2021: S=1.71 (strong), ret=+36.3%
  - 2022: S=0.79 (moderate), ret=+18.2%
  - 2023: S=0.68 (moderate), ret=+12.4%

## Risk & Drawdown
- Max drawdown: 33.13% over 720 days (recovered)
- Annualized: return +12.5%, volatility 22.3% (fraction of booksize)
- Hit rate: 23.7% positive days
- Tail shape: skew -1.43, excess kurtosis +30.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 2.26, latest 0.68

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +18.02%; worst month: -14.14%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.97
- Sideways: S=1.43
- Bear: S=-0.43

## Negated Direction
Best negated: `-rank(news_eps_actual)` S=0.18, F=0.04, INFERIOR
Direction gap: -0.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * news_eps_actual)`: S=-0.49, F=-0.18, T=120.5%, INFERIOR (TOP3000)
- `rank(-1 * news_eps_actual / close)`: S=-0.46, F=-0.17, T=121.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_eps_actual, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(news_eps_actual)` | TOP200 | 0.56 | 0.27 | 33.1% | 80% | mixed |
| `rank(news_eps_actual)` | TOP3000 | 0.49 | 0.18 | 35.9% | 80% | mixed |
| `rank(news_eps_actual)` | TOP500 | 0.11 | 0.02 | 38.3% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_prcl: 0.124 (weakly positively correlated)
- rp_ess_revenue: -0.123 (weakly negatively correlated)
- anl4_qf_az_div_median: 0.121 (weakly positively correlated)
- anl4_qfd1_az_div_median: 0.121 (weakly positively correlated)
- anl4_qf_az_div_mean: 0.120 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
