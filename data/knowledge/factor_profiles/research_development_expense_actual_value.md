---
field: research_development_expense_actual_value
dataset: analyst4
best_template: rank_level
best_sharpe: 0.69
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.3512
ann_vol: 0.1112
hit_rate: 0.5166
rolling_sharpe_min: -2.677
rolling_sharpe_max: 3.102
redundancy_cluster: 17
negated_best_sharpe: 0.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.44
---
# research_development_expense_actual_value (analyst4)

*Research and Development Expense- announced financial value*

## Signal Profile
- `rank(research_development_expense_actual_value)`: S=0.69, F=0.54, T=1.6%, INFERIOR (TOP3000)
- `rank(research_development_expense_actual_value / close)`: S=0.40, F=0.22, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(research_development_expense_actual_value, 5))`: S=0.65, F=0.24, T=37.4%, INFERIOR (TOP3000)
- `-rank(research_development_expense_actual_value)`: S=-0.31, F=-0.19, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(research_development_expense_actual_value, 5))`: S=0.25, F=0.07, T=34.2%, INFERIOR (TOP3000)
- `ts_zscore(research_development_expense_actual_value, 22)`: S=0.39, F=0.15, T=39.9%, INFERIOR (TOP3000)
- `ts_mean(research_development_expense_actual_value, 10)`: S=0.11, F=0.04, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(research_development_expense_actual_value, 22))`: S=-0.32, F=-0.12, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * research_development_expense_actual_value)`: S=0.08, F=0.03, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * research_development_expense_actual_value / close)`: S=-0.08, F=-0.02, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.69, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.84 (moderate), ret=+5.2%
  - 2020: S=-1.08 (negative), ret=-10.5%
  - 2021: S=0.83 (moderate), ret=+13.7%
  - 2022: S=1.96 (strong), ret=+20.3%
  - 2023: S=0.99 (moderate), ret=+8.9%

## Risk & Drawdown
- Max drawdown: 35.12% over 643 days (recovered)
- Annualized: return +7.7%, volatility 11.1% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.07, excess kurtosis +1.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.68, max 3.10, latest 0.80

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.75%; worst month: -7.80%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.96
- Sideways: S=1.17
- Bear: S=-2.28

## Negated Direction
Best negated: `rank(-1 * ts_delta(research_development_expense_actual_value, 5))` S=0.25, F=0.07, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * research_development_expense_actual_value)`: S=0.08, F=0.03, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * research_development_expense_actual_value / close)`: S=-0.08, F=-0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(research_development_expense_actual_value, 5))`: S=0.25, F=0.07, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(research_development_expense_actual_value)` | TOP3000 | 0.69 | 0.54 | 35.1% | 80% | bull-only |
| `rank(ts_delta(research_development_expense_actual_value, 5))` | TOP3000 | 0.63 | 0.24 | 15.2% | 80% | bull-only |
| `rank(research_development_expense_actual_value / close)` | TOP1000 | 0.39 | 0.22 | 19.4% | 80% | bull-only |
| `rank(research_development_expense_actual_value / close)` | TOP3000 | 0.39 | 0.22 | 14.7% | 80% | all-weather |
| `rank(research_development_expense_actual_value / close)` | TOP500 | 0.37 | 0.21 | 31.6% | 60% | bull-only |
| `rank(research_development_expense_actual_value)` | TOP1000 | 0.31 | 0.19 | 45.4% | 80% | bull-only |
| `rank(ts_delta(research_development_expense_actual_value, 5))` | TOP1000 | 0.24 | 0.06 | 20.5% | 40% | mixed |
| `rank(research_development_expense_actual_value)` | TOP500 | 0.12 | 0.05 | 64.4% | 60% | bull-only |
| `rank(research_development_expense_actual_value / close)` | TOP200 | 0.09 | 0.02 | 23.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- research_development_expense_reported_value: 1.000 (strongly positively correlated)
- research_development_expense: 0.974 (strongly positively correlated)
- fnd6_newqv1300_xrdq: 0.957 (strongly positively correlated)
- cash: 0.918 (strongly positively correlated)
- assets_curr: 0.908 (strongly positively correlated)

Redundancy cluster #17: 12 similar fields, mean |rho| 0.768 (representative: fnd6_newqv1300_aol2q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
