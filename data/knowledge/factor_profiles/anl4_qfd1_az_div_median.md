---
field: anl4_qfd1_az_div_median
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
max_drawdown: 0.098
ann_vol: 0.0804
hit_rate: 0.5004
rolling_sharpe_min: -1.268
rolling_sharpe_max: 1.825
negated_best_sharpe: 0.56
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.4
n_negated_sims: 10
direction_gap: 0.1
---
# anl4_qfd1_az_div_median (analyst4)

*Dividend per share - median of estimations*

## Signal Profile
- `rank(anl4_qfd1_az_div_median)`: S=-0.09, F=-0.02, T=1.3%, INFERIOR (TOP1000)
- `rank(anl4_qfd1_az_div_median / close)`: S=0.46, F=0.25, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qfd1_az_div_median, 5))`: S=0.50, F=0.16, T=34.6%, INFERIOR (TOP500)
- `-rank(anl4_qfd1_az_div_median)`: S=0.09, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_div_median, 5))`: S=0.16, F=0.04, T=33.0%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_qfd1_az_div_median, 63)`: S=0.28, F=0.08, T=19.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfd1_az_div_median, 10)`: S=0.11, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfd1_az_div_median, 22))`: S=0.18, F=0.04, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_div_median)`: S=0.51, F=0.32, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_div_median / close)`: S=0.56, F=0.40, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/11P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.44, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.69 (moderate), ret=+3.2%
  - 2020: S=-0.26 (negative), ret=-2.0%
  - 2021: S=0.67 (moderate), ret=+6.2%
  - 2022: S=1.70 (strong), ret=+17.3%
  - 2023: S=-1.16 (negative), ret=-7.1%

## Risk & Drawdown
- Max drawdown: 9.80% over 357 days (not yet recovered, ongoing at window end)
- Annualized: return +3.6%, volatility 8.0% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.33, excess kurtosis +2.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.27, max 1.82, latest -1.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +6.71%; worst month: -4.26%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.67
- Sideways: S=-0.51
- Bear: S=-1.63

## Negated Direction
Best negated: `rank(-1 * anl4_qfd1_az_div_median / close)` S=0.56, F=0.40, INFERIOR
Direction gap: +0.10 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_qfd1_az_div_median)`: S=0.51, F=0.32, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_div_median / close)`: S=0.56, F=0.40, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_div_median, 5))`: S=0.16, F=0.04, T=33.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qfd1_az_div_median / close)` | TOP1000 | 0.44 | 0.25 | 9.8% | 60% | bull-only |
| `rank(anl4_qfd1_az_div_median / close)` | TOP3000 | 0.41 | 0.20 | 9.6% | 60% | bull-only |
| `rank(ts_delta(anl4_qfd1_az_div_median, 5))` | TOP500 | 0.50 | 0.16 | 13.7% | 80% | mixed |
| `rank(ts_delta(anl4_qfd1_az_div_median, 5))` | TOP3000 | 0.30 | 0.06 | 12.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_qf_az_div_median: 1.000 (strongly positively correlated)
- anl4_qf_az_div_mean: 1.000 (strongly positively correlated)
- dividend_estimate_average: 1.000 (strongly positively correlated)
- anl4_qfd1_az_wol_vid: 0.986 (strongly positively correlated)
- anl4_qf_az_wol_vid: 0.986 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
