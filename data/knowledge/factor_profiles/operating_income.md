---
field: operating_income
dataset: fundamental6
cluster: fundamental6_income_expense
coverage: 0.5
community_alphas: 51233
best_template: rank_value_norm
best_sharpe: 0.45
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 37
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.3484
ann_vol: 0.1175
hit_rate: 0.5077
rolling_sharpe_min: -4.353
rolling_sharpe_max: 2.784
negated_best_sharpe: 0.62
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: 0.17
---
# operating_income (fundamental6)

*Operating Income After Depreciation - Quarterly*

## Signal Profile
- `rank(operating_income)`: S=0.31, F=0.18, T=1.8%, INFERIOR (TOP3000)
- `rank(operating_income / close)`: S=0.45, F=0.29, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(operating_income, 5))`: S=-0.22, F=-0.06, T=38.3%, INFERIOR (TOP200)
- `ts_decay_linear(rank(operating_income), 5)`: S=0.30, F=0.17, T=1.7%, INFERIOR (TOP3000)
- `trade_when(ts_std_dev(returns,20)>0.02, rank(operating_income), ts_std_dev(returns,20)<0.01)`: S=0.26, F=0.14, T=2.6%, INFERIOR (TOP3000)
- `-rank(operating_income)`: S=-0.10, F=-0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_income, 5))`: S=0.62, F=0.18, T=37.6%, INFERIOR (TOP3000)
- `ts_zscore(operating_income, 22)`: S=0.49, F=0.17, T=37.7%, INFERIOR (TOP3000)
- `ts_mean(operating_income, 10)`: S=0.16, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(operating_income, 22))`: S=0.30, F=0.08, T=16.7%, INFERIOR (TOP3000)
- `rank(-1 * operating_income)`: S=-0.31, F=-0.18, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * operating_income / close)`: S=-0.45, F=-0.29, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/31P
- LOW_FITNESS: 37F/0P
- LOW_SHARPE: 37F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.44, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.34 (weak), ret=+1.6%
  - 2020: S=-3.22 (negative), ret=-20.8%
  - 2021: S=1.33 (moderate), ret=+18.6%
  - 2022: S=1.57 (strong), ret=+27.3%
  - 2023: S=-0.11 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 34.84% over 810 days (recovered)
- Annualized: return +5.2%, volatility 11.8% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew -0.09, excess kurtosis +1.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.35, max 2.78, latest -0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.55%; worst month: -7.20%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.08
- Sideways: S=0.92
- Bear: S=-3.53

## Negated Direction
Best negated: `rank(-1 * ts_delta(operating_income, 5))` S=0.62, F=0.18, INFERIOR
Direction gap: +0.17 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * operating_income)`: S=-0.31, F=-0.18, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * operating_income / close)`: S=-0.45, F=-0.29, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_income, 5))`: S=0.62, F=0.18, T=37.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(operating_income / close)` | TOP3000 | 0.44 | 0.29 | 34.8% | 60% | bull-only |
| `rank(operating_income)` | TOP3000 | 0.30 | 0.18 | 44.0% | 60% | bull-only |
| `ts_decay_linear(rank(operating_income), 5)` | TOP3000 | 0.30 | 0.17 | 44.0% | 60% | bull-only |
| `trade_when(ts_std_dev(returns,20)>0.02, rank(operating_income), ts_std_dev(returns,20)<0.01)` | TOP3000 | 0.26 | 0.14 | 43.2% | 60% | bull-only |
| `rank(operating_income / close)` | TOP1000 | 0.13 | 0.05 | 39.1% | 60% | bull-only |
| `rank(operating_income)` | TOP1000 | 0.09 | 0.03 | 48.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_oiadpq: 1.000 (strongly positively correlated)
- anl4_ebit_value: 0.990 (strongly positively correlated)
- ebit_reported_value: 0.990 (strongly positively correlated)
- anl4_ptp_value: 0.981 (strongly positively correlated)
- pretax_income_standalone_value: 0.981 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
