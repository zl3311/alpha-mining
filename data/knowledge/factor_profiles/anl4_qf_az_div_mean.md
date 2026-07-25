---
field: anl4_qf_az_div_mean
dataset: analyst4
best_template: neg_rank_value_norm
best_sharpe: 0.56
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0973
ann_vol: 0.0804
hit_rate: 0.4988
rolling_sharpe_min: -1.246
rolling_sharpe_max: 1.834
negated_best_sharpe: 0.56
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: 0.09
---
# anl4_qf_az_div_mean (analyst4)

*Dividend per share - average of estimations*

## Signal Profile
- `rank(anl4_qf_az_div_mean)`: S=-0.09, F=-0.02, T=1.3%, INFERIOR (TOP1000)
- `rank(anl4_qf_az_div_mean / close)`: S=0.47, F=0.26, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qf_az_div_mean, 5))`: S=0.48, F=0.15, T=35.1%, INFERIOR (TOP500)
- `-rank(anl4_qf_az_div_mean)`: S=0.09, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_div_mean, 5))`: S=-0.13, F=-0.03, T=33.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qf_az_div_mean, 22)`: S=0.34, F=0.10, T=32.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_qf_az_div_mean, 10)`: S=0.10, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qf_az_div_mean, 22))`: S=0.39, F=0.13, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_div_mean)`: S=0.50, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_div_mean / close)`: S=0.56, F=0.40, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.69 (moderate), ret=+3.2%
  - 2020: S=-0.22 (negative), ret=-1.8%
  - 2021: S=0.66 (moderate), ret=+6.0%
  - 2022: S=1.71 (strong), ret=+17.3%
  - 2023: S=-1.14 (negative), ret=-7.0%

## Risk & Drawdown
- Max drawdown: 9.73% over 357 days (not yet recovered, ongoing at window end)
- Annualized: return +3.6%, volatility 8.0% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.34, excess kurtosis +2.76

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.25, max 1.83, latest -1.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +6.74%; worst month: -4.26%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.67
- Sideways: S=-0.50
- Bear: S=-1.59

## Negated Direction
Best negated: `rank(-1 * anl4_qf_az_div_mean / close)` S=0.56, F=0.40, INFERIOR
Direction gap: +0.09 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_qf_az_div_mean)`: S=0.50, F=0.31, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_div_mean / close)`: S=0.56, F=0.40, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_div_mean, 5))`: S=-0.13, F=-0.03, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qf_az_div_mean / close)` | TOP1000 | 0.45 | 0.26 | 9.7% | 60% | bull-only |
| `rank(anl4_qf_az_div_mean / close)` | TOP3000 | 0.41 | 0.20 | 9.5% | 60% | bull-only |
| `rank(ts_delta(anl4_qf_az_div_mean, 5))` | TOP3000 | 0.35 | 0.07 | 10.7% | 40% | mixed |
| `rank(ts_delta(anl4_qf_az_div_mean, 5))` | TOP200 | 0.13 | 0.03 | 24.8% | 40% | mixed |

## Correlation Notes
Top correlates:
- dividend_estimate_average: 1.000 (strongly positively correlated)
- anl4_qfd1_az_div_median: 1.000 (strongly positively correlated)
- anl4_qf_az_div_median: 1.000 (strongly positively correlated)
- anl4_qfd1_az_wol_vid: 0.985 (strongly positively correlated)
- anl4_qf_az_wol_vid: 0.985 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
