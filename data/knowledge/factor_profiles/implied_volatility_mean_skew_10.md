---
field: implied_volatility_mean_skew_10
dataset: option8
best_template: ts_mean
best_sharpe: 0.78
best_fitness: 0.61
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.202
ann_vol: 0.0668
hit_rate: 0.5093
rolling_sharpe_min: -2.882
rolling_sharpe_max: 2.257
redundancy_cluster: 28
negated_best_sharpe: 1.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: 0.39
---
# implied_volatility_mean_skew_10 (option8)

*Skew steepness for the implied volatility duration of 10 calendar days by subtracting the mean implied volatility of the call and put options with strikes at 110% of the money from the mean implied volatility of the call and put options with strikes at 90% of the money*

## Signal Profile
- `rank(implied_volatility_mean_skew_10)`: S=0.51, F=0.14, T=47.3%, INFERIOR (TOP3000)
- `rank(implied_volatility_mean_skew_10 / close)`: S=0.56, F=0.22, T=31.2%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_skew_10, 5))`: S=-0.58, F=-0.15, T=61.8%, INFERIOR (TOP200)
- `-rank(implied_volatility_mean_skew_10)`: S=-0.32, F=-0.08, T=38.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_10, 5))`: S=1.17, F=0.26, T=76.4%, INFERIOR (TOP3000)
- `-ts_zscore(implied_volatility_mean_skew_10, 63)`: S=0.67, F=0.19, T=45.0%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_skew_10, 10)`: S=0.78, F=0.61, T=13.9%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_skew_10, 22))`: S=-0.90, F=-0.25, T=50.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_10)`: S=-0.51, F=-0.14, T=47.3%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_10 / close)`: S=-0.71, F=-0.24, T=43.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- HIGH_TURNOVER: 4F/23P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.51, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.04 (moderate), ret=+3.0%
  - 2020: S=-1.55 (negative), ret=-7.6%
  - 2021: S=0.73 (moderate), ret=+7.7%
  - 2022: S=1.29 (moderate), ret=+9.3%
  - 2023: S=0.93 (moderate), ret=+4.3%

## Risk & Drawdown
- Max drawdown: 20.20% over 631 days (recovered)
- Annualized: return +3.4%, volatility 6.7% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew -0.06, excess kurtosis +2.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.88, max 2.26, latest 0.89

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.64%; worst month: -8.05%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.12
- Sideways: S=0.69
- Bear: S=-1.40

## Negated Direction
Best negated: `rank(-1 * ts_delta(implied_volatility_mean_skew_10, 5))` S=1.17, F=0.26, INFERIOR
Direction gap: +0.39 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * implied_volatility_mean_skew_10)`: S=-0.51, F=-0.14, T=47.3%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_10 / close)`: S=-0.71, F=-0.24, T=43.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_10, 5))`: S=1.17, F=0.26, T=76.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_mean_skew_10)` | TOP3000 | 0.51 | 0.14 | 20.2% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_10)` | TOP500 | 0.35 | 0.10 | 20.8% | 60% | bull-only |
| `rank(implied_volatility_mean_skew_10)` | TOP1000 | 0.32 | 0.08 | 24.9% | 80% | bull-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_skew_30: 0.983 (strongly positively correlated)
- implied_volatility_mean_skew_60: 0.949 (strongly positively correlated)
- implied_volatility_mean_skew_90: 0.935 (strongly positively correlated)
- implied_volatility_mean_skew_120: 0.924 (strongly positively correlated)
- implied_volatility_mean_skew_150: 0.912 (strongly positively correlated)

Redundancy cluster #28: 4 similar fields, mean |rho| 0.904 (representative: implied_volatility_mean_skew_360). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
