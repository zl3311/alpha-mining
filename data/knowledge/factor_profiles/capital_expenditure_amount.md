---
field: capital_expenditure_amount
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.46
best_fitness: 0.24
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.107
ann_vol: 0.0746
hit_rate: 0.4794
rolling_sharpe_min: -1.473
rolling_sharpe_max: 2.104
negated_best_sharpe: 0.66
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: 0.2
---
# capital_expenditure_amount (analyst4)

*Capital Expenditures - Total value*

## Signal Profile
- `rank(capital_expenditure_amount)`: S=0.39, F=0.22, T=1.1%, INFERIOR (TOP3000)
- `rank(capital_expenditure_amount / close)`: S=0.46, F=0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(capital_expenditure_amount, 5))`: S=-0.18, F=-0.03, T=36.5%, INFERIOR (TOP500)
- `-rank(capital_expenditure_amount)`: S=-0.15, F=-0.05, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(capital_expenditure_amount, 5))`: S=0.66, F=0.20, T=35.4%, INFERIOR (TOP3000)
- `-ts_zscore(capital_expenditure_amount, 63)`: S=0.38, F=0.14, T=20.6%, INFERIOR (TOP3000)
- `ts_mean(capital_expenditure_amount, 10)`: S=-0.02, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(capital_expenditure_amount, 22))`: S=-0.06, F=-0.01, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * capital_expenditure_amount)`: S=-0.39, F=-0.22, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * capital_expenditure_amount / close)`: S=-0.46, F=-0.24, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.46, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.83 (negative), ret=-4.1%
  - 2020: S=0.30 (weak), ret=+2.6%
  - 2021: S=1.03 (moderate), ret=+8.9%
  - 2022: S=0.94 (moderate), ret=+7.2%
  - 2023: S=0.39 (weak), ret=+2.2%

## Risk & Drawdown
- Max drawdown: 10.70% over 672 days (recovered)
- Annualized: return +3.4%, volatility 7.5% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.59, excess kurtosis +2.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.47, max 2.10, latest 0.42

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.03%; worst month: -3.41%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.33
- Sideways: S=-0.10
- Bear: S=-1.31

## Negated Direction
Best negated: `rank(-1 * ts_delta(capital_expenditure_amount, 5))` S=0.66, F=0.20, INFERIOR
Direction gap: +0.20 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * capital_expenditure_amount)`: S=-0.39, F=-0.22, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * capital_expenditure_amount / close)`: S=-0.46, F=-0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(capital_expenditure_amount, 5))`: S=0.66, F=0.20, T=35.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(capital_expenditure_amount / close)` | TOP3000 | 0.46 | 0.24 | 10.7% | 80% | bull-only |
| `rank(capital_expenditure_amount)` | TOP3000 | 0.39 | 0.22 | 26.6% | 60% | bull-only |
| `rank(capital_expenditure_amount / close)` | TOP1000 | 0.18 | 0.07 | 15.0% | 40% | bull-only |
| `rank(capital_expenditure_amount)` | TOP1000 | 0.14 | 0.05 | 31.4% | 60% | bull-only |
| `rank(capital_expenditure_amount / close)` | TOP500 | 0.10 | 0.03 | 26.7% | 80% | bull-only |

## Correlation Notes
Top correlates:
- total_assets_amount: 0.954 (strongly positively correlated)
- est_capex: 0.935 (strongly positively correlated)
- fnd6_mfma1_at: 0.932 (strongly positively correlated)
- liabilities_curr: 0.932 (strongly positively correlated)
- fnd6_cptnewqv1300_lctq: 0.932 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
