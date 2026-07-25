---
field: implied_volatility_mean_skew_30
dataset: option8
best_template: ts_mean
best_sharpe: 0.78
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2407
ann_vol: 0.0727
hit_rate: 0.4988
rolling_sharpe_min: -3.362
rolling_sharpe_max: 2.195
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.29
---
# implied_volatility_mean_skew_30 (option8)

*Skew steepness for the implied volatility duration of 30 calendar days by subtracting the mean implied volatility of the call and put options with strikes at 110% of the money from the mean implied volatility of the call and put options with strikes at 90% of the money*

## Signal Profile
- `rank(implied_volatility_mean_skew_30)`: S=0.47, F=0.13, T=45.8%, INFERIOR (TOP3000)
- `rank(implied_volatility_mean_skew_30 / close)`: S=0.57, F=0.25, T=26.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_skew_30, 5))`: S=0.04, F=0.00, T=67.1%, INFERIOR (TOP1000)
- `-rank(implied_volatility_mean_skew_30)`: S=-0.36, F=-0.11, T=34.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_30, 5))`: S=0.49, F=0.07, T=78.1%, INFERIOR (TOP3000)
- `-ts_zscore(implied_volatility_mean_skew_30, 63)`: S=0.57, F=0.15, T=41.7%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_skew_30, 10)`: S=0.78, F=0.67, T=12.4%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_skew_30, 22))`: S=-0.74, F=-0.19, T=47.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_30)`: S=-0.47, F=-0.13, T=45.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_30 / close)`: S=-0.68, F=-0.24, T=40.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- HIGH_TURNOVER: 4F/23P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.47, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.04 (moderate), ret=+2.9%
  - 2020: S=-2.07 (negative), ret=-10.7%
  - 2021: S=0.75 (moderate), ret=+8.6%
  - 2022: S=1.26 (moderate), ret=+10.5%
  - 2023: S=1.15 (moderate), ret=+5.3%

## Risk & Drawdown
- Max drawdown: 24.07% over 746 days (recovered)
- Annualized: return +3.4%, volatility 7.3% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.03, excess kurtosis +2.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.36, max 2.19, latest 1.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.65%; worst month: -8.33%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.17
- Sideways: S=0.69
- Bear: S=-1.73

## Negated Direction
Best negated: `rank(-1 * ts_delta(implied_volatility_mean_skew_30, 5))` S=0.49, F=0.07, INFERIOR
Direction gap: -0.29 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * implied_volatility_mean_skew_30)`: S=-0.47, F=-0.13, T=45.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_30 / close)`: S=-0.68, F=-0.24, T=40.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_30, 5))`: S=0.49, F=0.07, T=78.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_mean_skew_30)` | TOP3000 | 0.47 | 0.13 | 24.1% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_30)` | TOP1000 | 0.35 | 0.11 | 26.5% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_30)` | TOP500 | 0.33 | 0.11 | 24.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_skew_10: 0.983 (strongly positively correlated)
- implied_volatility_mean_skew_60: 0.977 (strongly positively correlated)
- implied_volatility_mean_skew_90: 0.963 (strongly positively correlated)
- implied_volatility_mean_skew_120: 0.952 (strongly positively correlated)
- implied_volatility_mean_skew_150: 0.941 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
