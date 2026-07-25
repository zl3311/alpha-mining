---
field: employee
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1028
ann_vol: 0.0797
hit_rate: 0.4826
rolling_sharpe_min: -1.513
rolling_sharpe_max: 2.274
redundancy_cluster: 1
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.47
n_negated_sims: 10
direction_gap: -0.02
---
# employee (fundamental6)

*Employees*

## Signal Profile
- `rank(employee)`: S=0.65, F=0.50, T=1.8%, INFERIOR (TOP3000)
- `rank(employee / close)`: S=0.77, F=0.54, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(employee, 5))`: S=0.33, F=0.12, T=40.0%, INFERIOR (TOP1000)
- `-rank(employee)`: S=-0.28, F=-0.15, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(employee, 5))`: S=0.75, F=0.47, T=35.2%, INFERIOR (TOP3000)
- `-ts_zscore(employee, 63)`: S=-0.06, F=-0.01, T=20.2%, INFERIOR (TOP3000)
- `ts_mean(employee, 10)`: S=0.15, F=0.05, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(employee, 22))`: S=0.35, F=0.15, T=18.6%, INFERIOR (TOP3000)
- `rank(-1 * employee)`: S=-0.06, F=-0.02, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * employee / close)`: S=-0.27, F=-0.13, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.38 (negative), ret=-1.9%
  - 2020: S=0.40 (weak), ret=+3.8%
  - 2021: S=1.28 (moderate), ret=+13.0%
  - 2022: S=1.53 (strong), ret=+11.9%
  - 2023: S=0.67 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 10.28% over 237 days (recovered)
- Annualized: return +6.1%, volatility 8.0% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.59, excess kurtosis +2.96

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.51, max 2.27, latest 0.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +9.55%; worst month: -3.62%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.93
- Sideways: S=0.06
- Bear: S=-1.21

## Negated Direction
Best negated: `rank(-1 * ts_delta(employee, 5))` S=0.75, F=0.47, INFERIOR
Direction gap: -0.02 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * employee)`: S=-0.06, F=-0.02, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * employee / close)`: S=-0.27, F=-0.13, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(employee, 5))`: S=0.75, F=0.47, T=35.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(employee / close)` | TOP3000 | 0.77 | 0.54 | 10.3% | 80% | bull-only |
| `rank(employee)` | TOP3000 | 0.65 | 0.50 | 27.9% | 80% | bull-only |
| `rank(employee / close)` | TOP1000 | 0.39 | 0.22 | 14.5% | 40% | bull-only |
| `rank(employee)` | TOP1000 | 0.27 | 0.15 | 34.1% | 60% | bull-only |
| `rank(employee / close)` | TOP500 | 0.27 | 0.13 | 20.0% | 40% | bull-only |
| `rank(ts_delta(employee, 5))` | TOP1000 | 0.33 | 0.12 | 23.1% | 60% | mixed |
| `rank(ts_delta(employee, 5))` | TOP3000 | 0.28 | 0.09 | 16.4% | 60% | weak |
| `rank(employee)` | TOP500 | 0.06 | 0.02 | 45.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_emp: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.974 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.973 (strongly positively correlated)
- fnd6_newa1v1300_ap: 0.969 (strongly positively correlated)
- fnd6_cptnewqv1300_ltq: 0.968 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
