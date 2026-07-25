---
field: fnd6_newqv1300_xrdq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.63
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.3092
ann_vol: 0.1046
hit_rate: 0.5174
rolling_sharpe_min: -2.402
rolling_sharpe_max: 2.822
redundancy_cluster: 17
negated_best_sharpe: 0.48
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.15
---
# fnd6_newqv1300_xrdq (fundamental6)

*Research and Development Expense*

## Signal Profile
- `rank(fnd6_newqv1300_xrdq)`: S=0.63, F=0.45, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_xrdq / close)`: S=0.48, F=0.30, T=2.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newqv1300_xrdq, 5))`: S=0.64, F=0.34, T=36.2%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_xrdq)`: S=-0.28, F=-0.16, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_xrdq, 5))`: S=0.48, F=0.23, T=37.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_xrdq, 22)`: S=-0.09, F=-0.02, T=38.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_xrdq, 10)`: S=0.18, F=0.09, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_xrdq, 22))`: S=0.00, F=0.00, T=17.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xrdq)`: S=-0.28, F=-0.16, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xrdq / close)`: S=-0.48, F=-0.30, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.59 (moderate), ret=+3.5%
  - 2020: S=-0.76 (negative), ret=-6.7%
  - 2021: S=0.74 (moderate), ret=+12.1%
  - 2022: S=1.43 (moderate), ret=+12.9%
  - 2023: S=1.32 (moderate), ret=+10.5%

## Risk & Drawdown
- Max drawdown: 30.92% over 622 days (recovered)
- Annualized: return +6.6%, volatility 10.5% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.05, excess kurtosis +2.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.40, max 2.82, latest 1.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.10%; worst month: -6.96%
Positive months: 68%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.58
- Sideways: S=1.31
- Bear: S=-2.09

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_xrdq, 5))` S=0.48, F=0.23, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_xrdq)`: S=-0.28, F=-0.16, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_xrdq / close)`: S=-0.48, F=-0.30, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_xrdq, 5))`: S=0.48, F=0.23, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_xrdq)` | TOP3000 | 0.63 | 0.45 | 30.9% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_xrdq, 5))` | TOP500 | 0.64 | 0.34 | 19.4% | 100% | mixed |
| `rank(fnd6_newqv1300_xrdq / close)` | TOP1000 | 0.48 | 0.30 | 21.2% | 80% | bull-only |
| `rank(fnd6_newqv1300_xrdq / close)` | TOP3000 | 0.47 | 0.28 | 16.8% | 80% | all-weather |
| `rank(fnd6_newqv1300_xrdq / close)` | TOP500 | 0.38 | 0.24 | 41.9% | 80% | bull-only |
| `rank(fnd6_newqv1300_xrdq)` | TOP1000 | 0.28 | 0.16 | 48.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_xrdq, 5))` | TOP3000 | 0.38 | 0.15 | 26.1% | 60% | mixed |
| `rank(fnd6_newqv1300_xrdq / close)` | TOP200 | 0.22 | 0.11 | 30.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_xrdq)` | TOP500 | 0.17 | 0.08 | 68.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_xrdq, 5))` | TOP200 | 0.20 | 0.06 | 37.0% | 60% | mixed |

## Correlation Notes
Top correlates:
- research_development_expense_actual_value: 0.957 (strongly positively correlated)
- research_development_expense_reported_value: 0.957 (strongly positively correlated)
- research_development_expense: 0.941 (strongly positively correlated)
- cash: 0.925 (strongly positively correlated)
- sga_expense: 0.906 (strongly positively correlated)

Redundancy cluster #17: 12 similar fields, mean |rho| 0.768 (representative: fnd6_newqv1300_aol2q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
