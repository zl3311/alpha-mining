---
field: fn_income_tax_expense_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.54
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2409
ann_vol: 0.0806
hit_rate: 0.5126
rolling_sharpe_min: -4.114
rolling_sharpe_max: 2.41
redundancy_cluster: 13
negated_best_sharpe: 0.38
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.16
---
# fn_income_tax_expense_q (fundamental2)

*Income Tax Expense (Benefit)*

## Signal Profile
- `rank(fn_income_tax_expense_q)`: S=0.42, F=0.25, T=2.2%, INFERIOR (TOP3000)
- `rank(fn_income_tax_expense_q / close)`: S=0.54, F=0.32, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_income_tax_expense_q, 5))`: S=0.09, F=0.01, T=36.8%, INFERIOR (TOP3000)
- `-rank(fn_income_tax_expense_q)`: S=-0.17, F=-0.07, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_income_tax_expense_q, 5))`: S=0.40, F=0.16, T=37.3%, INFERIOR (TOP3000)
- `-ts_zscore(fn_income_tax_expense_q, 63)`: S=0.35, F=0.10, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fn_income_tax_expense_q, 10)`: S=0.06, F=0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_income_tax_expense_q, 22))`: S=-0.21, F=-0.05, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_tax_expense_q)`: S=0.36, F=0.21, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_tax_expense_q / close)`: S=0.38, F=0.22, T=3.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.53, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.70 (strong), ret=+6.3%
  - 2020: S=-3.25 (negative), ret=-15.9%
  - 2021: S=1.10 (moderate), ret=+10.6%
  - 2022: S=1.73 (strong), ret=+20.5%
  - 2023: S=-0.11 (negative), ret=-0.7%

## Risk & Drawdown
- Max drawdown: 24.09% over 790 days (recovered)
- Annualized: return +4.2%, volatility 8.1% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.14, excess kurtosis +1.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.11, max 2.41, latest -0.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.19%; worst month: -5.53%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.01
- Sideways: S=1.33
- Bear: S=-3.45

## Negated Direction
Best negated: `rank(-1 * fn_income_tax_expense_q / close)` S=0.38, F=0.22, INFERIOR
Direction gap: -0.16 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_income_tax_expense_q)`: S=0.36, F=0.21, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * fn_income_tax_expense_q / close)`: S=0.38, F=0.22, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_income_tax_expense_q, 5))`: S=0.40, F=0.16, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_income_tax_expense_q / close)` | TOP3000 | 0.53 | 0.32 | 24.1% | 60% | bull-only |
| `rank(fn_income_tax_expense_q)` | TOP3000 | 0.41 | 0.25 | 31.6% | 60% | bull-only |
| `rank(fn_income_tax_expense_q)` | TOP1000 | 0.16 | 0.07 | 34.3% | 60% | bull-only |
| `rank(fn_income_tax_expense_q / close)` | TOP1000 | 0.12 | 0.04 | 26.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_txtq: 0.975 (strongly positively correlated)
- income_tax: 0.975 (strongly positively correlated)
- pretax_income_standalone_value: 0.957 (strongly positively correlated)
- anl4_ptp_value: 0.957 (strongly positively correlated)
- net_profit_reported_value: 0.954 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
