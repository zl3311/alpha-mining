---
field: anl4_afv4_div_median
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.58
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1638
ann_vol: 0.0907
hit_rate: 0.4907
rolling_sharpe_min: -1.703
rolling_sharpe_max: 1.695
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: 0.21
---
# anl4_afv4_div_median (analyst4)

*Dividend per share - Median value among forecasts*

## Signal Profile
- `rank(anl4_afv4_div_median)`: S=-0.06, F=-0.01, T=1.3%, INFERIOR (TOP1000)
- `rank(anl4_afv4_div_median / close)`: S=0.21, F=0.08, T=1.8%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_afv4_div_median, 5))`: S=-0.12, F=-0.01, T=36.7%, INFERIOR (TOP3000)
- `-rank(anl4_afv4_div_median)`: S=0.06, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_median, 5))`: S=0.58, F=0.24, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_afv4_div_median, 63)`: S=0.37, F=0.11, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_div_median, 10)`: S=-0.08, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_div_median, 22))`: S=-0.73, F=-0.30, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_median)`: S=0.15, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_median / close)`: S=0.19, F=0.09, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.20, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.15 (weak), ret=+0.7%
  - 2020: S=-1.17 (negative), ret=-8.4%
  - 2021: S=0.55 (moderate), ret=+5.9%
  - 2022: S=1.43 (moderate), ret=+17.8%
  - 2023: S=-1.05 (negative), ret=-7.1%

## Risk & Drawdown
- Max drawdown: 16.38% over 814 days (recovered)
- Annualized: return +1.8%, volatility 9.1% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.14, excess kurtosis +2.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.70, max 1.70, latest -1.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.13%; worst month: -4.79%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.55
- Sideways: S=-0.09
- Bear: S=-2.88

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_div_median, 5))` S=0.58, F=0.24, INFERIOR
Direction gap: +0.21 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_afv4_div_median)`: S=0.15, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_median / close)`: S=0.19, F=0.09, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_median, 5))`: S=0.58, F=0.24, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_div_median / close)` | TOP1000 | 0.20 | 0.08 | 16.4% | 60% | bull-only |
| `rank(anl4_afv4_div_median / close)` | TOP500 | 0.07 | 0.02 | 21.7% | 40% | bull-only |
| `rank(anl4_afv4_div_median / close)` | TOP3000 | 0.08 | 0.02 | 19.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_afv4_div_mean: 1.000 (strongly positively correlated)
- anl4_afv4_div_high: 0.998 (strongly positively correlated)
- anl4_af_div_value: 0.949 (strongly positively correlated)
- fnd6_newa1v1300_dv: 0.939 (strongly positively correlated)
- cashflow_dividends: 0.938 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
