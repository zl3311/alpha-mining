---
field: implied_volatility_mean_skew_20
dataset: option8
best_template: ts_mean
best_sharpe: 0.81
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 27
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2334
ann_vol: 0.0964
hit_rate: 0.5206
rolling_sharpe_min: -2.233
rolling_sharpe_max: 2.286
negated_best_sharpe: 1.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.35
---
# implied_volatility_mean_skew_20 (option8)

*Skew steepness for the implied volatility duration of 20 calendar days by subtracting the mean implied volatility of the call and put options with strikes at 110% of the money from implied volatility of the call and put options with strikes at 90% of the money*

## Signal Profile
- `rank(implied_volatility_mean_skew_20)`: S=0.40, F=0.14, T=33.0%, INFERIOR (TOP500)
- `rank(implied_volatility_mean_skew_20 / close)`: S=0.54, F=0.22, T=28.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_skew_20, 5))`: S=-0.53, F=-0.09, T=66.4%, INFERIOR (TOP1000)
- `-rank(implied_volatility_mean_skew_20)`: S=-0.37, F=-0.11, T=36.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_20, 5))`: S=1.16, F=0.25, T=77.1%, INFERIOR (TOP3000)
- `-ts_zscore(implied_volatility_mean_skew_20, 63)`: S=0.66, F=0.19, T=42.8%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_skew_20, 10)`: S=0.81, F=0.67, T=13.1%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_skew_20, 22))`: S=-0.98, F=-0.29, T=48.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_20)`: S=-0.49, F=-0.13, T=46.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_20 / close)`: S=-0.67, F=-0.23, T=42.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 26F/1P
- HIGH_TURNOVER: 4F/23P
- LOW_FITNESS: 27F/0P
- LOW_SHARPE: 27F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.39, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.00 (moderate), ret=+4.2%
  - 2020: S=-1.36 (negative), ret=-10.3%
  - 2021: S=1.07 (moderate), ret=+16.9%
  - 2022: S=1.24 (moderate), ret=+10.7%
  - 2023: S=-0.42 (negative), ret=-3.0%

## Risk & Drawdown
- Max drawdown: 23.34% over 749 days (recovered)
- Annualized: return +3.8%, volatility 9.6% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew -0.12, excess kurtosis +3.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.23, max 2.29, latest -0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.65%; worst month: -8.42%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.31
- Sideways: S=0.47
- Bear: S=-1.89

## Negated Direction
Best negated: `rank(-1 * ts_delta(implied_volatility_mean_skew_20, 5))` S=1.16, F=0.25, INFERIOR
Direction gap: +0.35 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * implied_volatility_mean_skew_20)`: S=-0.49, F=-0.13, T=46.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_skew_20 / close)`: S=-0.67, F=-0.23, T=42.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_skew_20, 5))`: S=1.16, F=0.25, T=77.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(implied_volatility_mean_skew_20)` | TOP500 | 0.39 | 0.14 | 23.3% | 60% | bull-only |
| `rank(implied_volatility_mean_skew_20)` | TOP3000 | 0.48 | 0.13 | 21.7% | 80% | bull-only |
| `rank(implied_volatility_mean_skew_20)` | TOP1000 | 0.36 | 0.11 | 25.5% | 80% | bull-only |

## Correlation Notes
Top correlates:
- min_free_cashflow_per_share_guidance: 0.797 (strongly positively correlated)
- shareholders_equity_min_guidance: 0.797 (strongly positively correlated)
- min_total_assets_guidance: 0.797 (strongly positively correlated)
- max_free_cashflow_per_share_guidance: 0.797 (strongly positively correlated)
- shareholders_equity_max_guidance: 0.797 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
