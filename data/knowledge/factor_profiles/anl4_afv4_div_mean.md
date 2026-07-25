---
field: anl4_afv4_div_mean
dataset: analyst4
best_template: rank_neg_delta
best_sharpe: 0.54
best_fitness: 0.13
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.168
ann_vol: 0.0916
hit_rate: 0.4923
rolling_sharpe_min: -1.757
rolling_sharpe_max: 1.663
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: 0.33
---
# anl4_afv4_div_mean (analyst4)

*Dividend per share - average of estimations for annual frequency*

## Signal Profile
- `rank(anl4_afv4_div_mean)`: S=-0.05, F=-0.01, T=1.3%, INFERIOR (TOP1000)
- `rank(anl4_afv4_div_mean / close)`: S=0.21, F=0.08, T=1.8%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_afv4_div_mean, 5))`: S=-0.08, F=-0.01, T=36.0%, INFERIOR (TOP3000)
- `-rank(anl4_afv4_div_mean)`: S=0.05, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_mean, 5))`: S=0.54, F=0.13, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_afv4_div_mean, 63)`: S=0.25, F=0.06, T=18.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_afv4_div_mean, 10)`: S=-0.09, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_afv4_div_mean, 22))`: S=-0.43, F=-0.14, T=13.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_mean)`: S=0.05, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_mean / close)`: S=-0.21, F=-0.08, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.20, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.16 (weak), ret=+0.8%
  - 2020: S=-1.23 (negative), ret=-8.8%
  - 2021: S=0.58 (moderate), ret=+6.4%
  - 2022: S=1.39 (moderate), ret=+17.5%
  - 2023: S=-1.04 (negative), ret=-7.1%

## Risk & Drawdown
- Max drawdown: 16.80% over 814 days (recovered)
- Annualized: return +1.8%, volatility 9.2% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.12, excess kurtosis +2.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.76, max 1.66, latest -1.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.16%; worst month: -4.71%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.53
- Sideways: S=-0.09
- Bear: S=-2.91

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_afv4_div_mean, 5))` S=0.54, F=0.13, INFERIOR
Direction gap: +0.33 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_afv4_div_mean)`: S=0.05, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_afv4_div_mean / close)`: S=-0.21, F=-0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_afv4_div_mean, 5))`: S=0.54, F=0.13, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_afv4_div_mean / close)` | TOP1000 | 0.20 | 0.08 | 16.8% | 60% | bull-only |
| `rank(anl4_afv4_div_mean / close)` | TOP3000 | 0.08 | 0.02 | 19.9% | 60% | bull-only |
| `rank(anl4_afv4_div_mean / close)` | TOP500 | 0.06 | 0.02 | 22.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_afv4_div_median: 1.000 (strongly positively correlated)
- anl4_afv4_div_high: 0.997 (strongly positively correlated)
- anl4_af_div_value: 0.951 (strongly positively correlated)
- fnd6_newa1v1300_dv: 0.942 (strongly positively correlated)
- cashflow_dividends: 0.941 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
