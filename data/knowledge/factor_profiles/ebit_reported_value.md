---
field: ebit_reported_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.48
best_fitness: 0.33
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.3688
ann_vol: 0.1206
hit_rate: 0.5045
rolling_sharpe_min: -4.44
rolling_sharpe_max: 2.827
negated_best_sharpe: 0.64
negated_best_template: rank_neg_delta
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: 0.16
---
# ebit_reported_value (analyst4)

*Earnings Before Interest & Taxes - actual value for the quarter*

## Signal Profile
- `rank(ebit_reported_value)`: S=0.30, F=0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(ebit_reported_value / close)`: S=0.48, F=0.33, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(ebit_reported_value, 5))`: S=-0.48, F=-0.11, T=37.6%, INFERIOR (TOP1000)
- `-rank(ebit_reported_value)`: S=-0.06, F=-0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(ebit_reported_value, 5))`: S=0.64, F=0.16, T=37.2%, INFERIOR (TOP3000)
- `-ts_zscore(ebit_reported_value, 63)`: S=-0.26, F=-0.07, T=16.9%, INFERIOR (TOP3000)
- `ts_mean(ebit_reported_value, 10)`: S=-0.09, F=-0.03, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(ebit_reported_value, 22))`: S=-0.18, F=-0.04, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * ebit_reported_value)`: S=-0.30, F=-0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ebit_reported_value / close)`: S=-0.48, F=-0.33, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.47, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+1.3%
  - 2020: S=-3.44 (negative), ret=-23.3%
  - 2021: S=1.49 (moderate), ret=+20.9%
  - 2022: S=1.67 (strong), ret=+30.2%
  - 2023: S=-0.12 (negative), ret=-1.2%

## Risk & Drawdown
- Max drawdown: 36.88% over 810 days (recovered)
- Annualized: return +5.7%, volatility 12.1% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew -0.11, excess kurtosis +1.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.44, max 2.83, latest -0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +11.53%; worst month: -7.63%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.14
- Sideways: S=0.91
- Bear: S=-3.49

## Negated Direction
Best negated: `rank(-1 * ts_delta(ebit_reported_value, 5))` S=0.64, F=0.16, INFERIOR
Direction gap: +0.16 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * ebit_reported_value)`: S=-0.30, F=-0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ebit_reported_value / close)`: S=-0.48, F=-0.33, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(ebit_reported_value, 5))`: S=0.64, F=0.16, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ebit_reported_value / close)` | TOP3000 | 0.47 | 0.33 | 36.9% | 60% | bull-only |
| `rank(ebit_reported_value)` | TOP3000 | 0.29 | 0.17 | 47.6% | 60% | bull-only |
| `rank(ebit_reported_value / close)` | TOP1000 | 0.13 | 0.05 | 38.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ebit_value: 1.000 (strongly positively correlated)
- operating_income: 0.990 (strongly positively correlated)
- fnd6_cptnewqv1300_oiadpq: 0.990 (strongly positively correlated)
- net_profit_adjusted_value: 0.986 (strongly positively correlated)
- anl4_netprofita_value: 0.986 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
