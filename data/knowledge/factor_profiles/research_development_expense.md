---
field: research_development_expense
dataset: analyst4
best_template: rank_level
best_sharpe: 0.57
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.3386
ann_vol: 0.1148
hit_rate: 0.5126
rolling_sharpe_min: -2.545
rolling_sharpe_max: 2.795
redundancy_cluster: 13
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: -0.07
---
# research_development_expense (analyst4)

*Research & Development Expense - Actual Value (Annual)*

## Signal Profile
- `rank(research_development_expense)`: S=0.57, F=0.41, T=1.2%, INFERIOR (TOP3000)
- `rank(research_development_expense / close)`: S=0.40, F=0.21, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(research_development_expense, 5))`: S=-0.02, F=0.00, T=34.8%, INFERIOR (TOP1000)
- `-rank(research_development_expense)`: S=-0.18, F=-0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(research_development_expense, 5))`: S=0.50, F=0.22, T=32.5%, INFERIOR (TOP3000)
- `ts_zscore(research_development_expense, 22)`: S=-0.13, F=-0.03, T=38.4%, INFERIOR (TOP3000)
- `ts_mean(research_development_expense, 10)`: S=0.13, F=0.05, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(research_development_expense, 22))`: S=0.21, F=0.08, T=13.0%, INFERIOR (TOP3000)
- `rank(-1 * research_development_expense)`: S=0.16, F=0.08, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * research_development_expense / close)`: S=-0.09, F=-0.03, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.32 (weak), ret=+2.0%
  - 2020: S=-1.02 (negative), ret=-9.8%
  - 2021: S=0.73 (moderate), ret=+12.4%
  - 2022: S=1.87 (strong), ret=+22.1%
  - 2023: S=0.65 (moderate), ret=+5.8%

## Risk & Drawdown
- Max drawdown: 33.86% over 643 days (recovered)
- Annualized: return +6.6%, volatility 11.5% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.10, excess kurtosis +1.67

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.54, max 2.79, latest 0.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.99%; worst month: -6.67%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.00
- Sideways: S=0.80
- Bear: S=-2.45

## Negated Direction
Best negated: `rank(-1 * ts_delta(research_development_expense, 5))` S=0.50, F=0.22, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * research_development_expense)`: S=0.16, F=0.08, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * research_development_expense / close)`: S=-0.09, F=-0.03, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(research_development_expense, 5))`: S=0.50, F=0.22, T=32.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(research_development_expense)` | TOP3000 | 0.58 | 0.41 | 33.9% | 80% | bull-only |
| `rank(research_development_expense / close)` | TOP3000 | 0.39 | 0.21 | 11.5% | 80% | mixed |
| `rank(research_development_expense / close)` | TOP1000 | 0.30 | 0.15 | 25.1% | 60% | bull-only |
| `rank(research_development_expense / close)` | TOP500 | 0.25 | 0.12 | 41.3% | 60% | bull-only |
| `rank(research_development_expense)` | TOP1000 | 0.18 | 0.09 | 52.7% | 80% | bull-only |
| `rank(research_development_expense / close)` | TOP200 | 0.10 | 0.03 | 29.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- research_development_expense_reported_value: 0.974 (strongly positively correlated)
- research_development_expense_actual_value: 0.974 (strongly positively correlated)
- fnd6_newqv1300_xrdq: 0.941 (strongly positively correlated)
- fnd6_newa1v1300_act: 0.925 (strongly positively correlated)
- assets_curr: 0.924 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
