---
field: fn_prepaid_expense_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.58
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2406
ann_vol: 0.0915
hit_rate: 0.515
rolling_sharpe_min: -2.813
rolling_sharpe_max: 2.456
redundancy_cluster: 13
negated_best_sharpe: 0.34
negated_best_template: neg_rank_level
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.24
---
# fn_prepaid_expense_a (fundamental2)

*Carrying amount for an unclassified balance sheet date of expenditures made in advance of when the economic benefit of the cost will be realized, and which will be expensed in future periods with the passage of time or when a triggering event occurs. For a classified balance sheet, represents the noncurrent portion of prepaid expenses (the current portion has a separate concept).*

## Signal Profile
- `rank(fn_prepaid_expense_a)`: S=0.64, F=0.44, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_prepaid_expense_a / close)`: S=0.64, F=0.40, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_prepaid_expense_a, 5))`: S=0.41, F=0.18, T=33.9%, INFERIOR (TOP1000)
- `-rank(fn_prepaid_expense_a)`: S=-0.28, F=-0.15, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_prepaid_expense_a, 5))`: S=0.42, F=0.24, T=28.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_prepaid_expense_a, 63)`: S=0.58, F=0.47, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(fn_prepaid_expense_a, 10)`: S=0.02, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_prepaid_expense_a, 22))`: S=-0.02, F=0.00, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_prepaid_expense_a)`: S=0.34, F=0.24, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_prepaid_expense_a / close)`: S=0.14, F=0.06, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.14 (moderate), ret=+5.0%
  - 2020: S=-1.44 (negative), ret=-9.6%
  - 2021: S=0.94 (moderate), ret=+12.6%
  - 2022: S=1.77 (strong), ret=+19.3%
  - 2023: S=0.16 (weak), ret=+1.1%

## Risk & Drawdown
- Max drawdown: 24.06% over 759 days (recovered)
- Annualized: return +5.8%, volatility 9.2% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew -0.00, excess kurtosis +1.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.81, max 2.46, latest -0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.92%; worst month: -4.66%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.96
- Sideways: S=1.20
- Bear: S=-2.83

## Negated Direction
Best negated: `rank(-1 * fn_prepaid_expense_a)` S=0.34, F=0.24, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_prepaid_expense_a)`: S=0.34, F=0.24, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fn_prepaid_expense_a / close)`: S=0.14, F=0.06, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_prepaid_expense_a, 5))`: S=0.42, F=0.24, T=28.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_prepaid_expense_a)` | TOP3000 | 0.63 | 0.44 | 24.1% | 80% | bull-only |
| `rank(fn_prepaid_expense_a / close)` | TOP3000 | 0.63 | 0.40 | 9.2% | 100% | mixed |
| `rank(fn_prepaid_expense_a / close)` | TOP1000 | 0.57 | 0.39 | 9.6% | 80% | bull-only |
| `rank(ts_delta(fn_prepaid_expense_a, 5))` | TOP1000 | 0.40 | 0.18 | 21.8% | 60% | bear-only |
| `rank(fn_prepaid_expense_a)` | TOP1000 | 0.28 | 0.15 | 28.7% | 60% | bull-only |
| `rank(ts_delta(fn_prepaid_expense_a, 5))` | TOP3000 | 0.23 | 0.07 | 30.8% | 80% | mixed |
| `rank(fn_prepaid_expense_a / close)` | TOP500 | 0.14 | 0.05 | 22.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- operating_expense: 0.964 (strongly positively correlated)
- fnd6_newqv1300_xoprq: 0.964 (strongly positively correlated)
- invested_capital: 0.961 (strongly positively correlated)
- fnd6_newqv1300_icaptq: 0.961 (strongly positively correlated)
- fnd6_newa1v1300_act: 0.960 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
