---
field: fnd6_newa2v1300_txt
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.79
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2254
ann_vol: 0.0831
hit_rate: 0.502
rolling_sharpe_min: -3.571
rolling_sharpe_max: 1.953
negated_best_sharpe: 0.56
negated_best_template: neg_rank_level
negated_best_fitness: 0.43
n_negated_sims: 10
direction_gap: -0.23
---
# fnd6_newa2v1300_txt (fundamental6)

*Income Taxes - Total*

## Signal Profile
- `rank(fnd6_newa2v1300_txt)`: S=0.21, F=0.09, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_txt / close)`: S=0.37, F=0.18, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_txt, 5))`: S=0.15, F=0.04, T=34.0%, INFERIOR (TOP500)
- `-rank(fnd6_newa2v1300_txt)`: S=0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_txt, 5))`: S=0.00, F=0.00, T=33.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_txt, 22)`: S=0.79, F=0.60, T=28.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_txt, 10)`: S=0.09, F=0.02, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_txt, 22))`: S=-0.12, F=-0.03, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txt)`: S=0.56, F=0.43, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txt / close)`: S=0.47, F=0.32, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.36, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.20 (moderate), ret=+4.8%
  - 2020: S=-2.42 (negative), ret=-13.3%
  - 2021: S=0.61 (moderate), ret=+5.5%
  - 2022: S=1.24 (moderate), ret=+15.5%
  - 2023: S=0.33 (weak), ret=+2.3%

## Risk & Drawdown
- Max drawdown: 22.54% over 917 days (recovered)
- Annualized: return +3.0%, volatility 8.3% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew -0.07, excess kurtosis +1.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.57, max 1.95, latest 0.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.75%; worst month: -3.97%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.78
- Sideways: S=1.10
- Bear: S=-3.47

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_txt)` S=0.56, F=0.43, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_txt)`: S=0.56, F=0.43, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txt / close)`: S=0.47, F=0.32, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_txt, 5))`: S=0.00, F=0.00, T=33.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_txt / close)` | TOP3000 | 0.36 | 0.18 | 22.5% | 80% | bull-only |
| `rank(fnd6_newa2v1300_txt)` | TOP3000 | 0.20 | 0.09 | 34.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_txt, 5))` | TOP500 | 0.17 | 0.04 | 60.2% | 60% | bull-only |
| `rank(fnd6_newa2v1300_txt / close)` | TOP1000 | 0.12 | 0.04 | 22.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_income_tax_expense_a: 0.983 (strongly positively correlated)
- pretax_income_total: 0.959 (strongly positively correlated)
- net_income_adjusted: 0.957 (strongly positively correlated)
- net_income_total_2: 0.956 (strongly positively correlated)
- operating_profit_before_interest_tax: 0.950 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
