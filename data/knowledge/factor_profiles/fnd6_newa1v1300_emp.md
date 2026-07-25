---
field: fnd6_newa1v1300_emp
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
max_drawdown: 0.1034
ann_vol: 0.0796
hit_rate: 0.4842
rolling_sharpe_min: -1.514
rolling_sharpe_max: 2.257
redundancy_cluster: 1
negated_best_sharpe: 0.76
negated_best_template: rank_neg_delta
negated_best_fitness: 0.48
n_negated_sims: 10
direction_gap: -0.01
---
# fnd6_newa1v1300_emp (fundamental6)

*Employees*

## Signal Profile
- `rank(fnd6_newa1v1300_emp)`: S=0.66, F=0.51, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_emp / close)`: S=0.77, F=0.54, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_emp, 5))`: S=0.34, F=0.12, T=39.7%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_emp)`: S=-0.30, F=-0.17, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_emp, 5))`: S=0.76, F=0.48, T=35.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_emp, 63)`: S=-0.03, F=0.00, T=20.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_emp, 10)`: S=0.16, F=0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_emp, 22))`: S=0.34, F=0.14, T=18.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_emp)`: S=-0.07, F=-0.02, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_emp / close)`: S=-0.27, F=-0.13, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.37 (negative), ret=-1.8%
  - 2020: S=0.38 (weak), ret=+3.6%
  - 2021: S=1.26 (moderate), ret=+12.7%
  - 2022: S=1.53 (strong), ret=+12.0%
  - 2023: S=0.72 (moderate), ret=+3.5%

## Risk & Drawdown
- Max drawdown: 10.34% over 238 days (recovered)
- Annualized: return +6.1%, volatility 8.0% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +0.58, excess kurtosis +2.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.51, max 2.26, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +9.57%; worst month: -3.75%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.92
- Sideways: S=0.06
- Bear: S=-1.21

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_emp, 5))` S=0.76, F=0.48, INFERIOR
Direction gap: -0.01 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_emp)`: S=-0.07, F=-0.02, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_emp / close)`: S=-0.27, F=-0.13, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_emp, 5))`: S=0.76, F=0.48, T=35.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_emp / close)` | TOP3000 | 0.77 | 0.54 | 10.3% | 80% | bull-only |
| `rank(fnd6_newa1v1300_emp)` | TOP3000 | 0.66 | 0.51 | 28.1% | 80% | bull-only |
| `rank(fnd6_newa1v1300_emp / close)` | TOP1000 | 0.41 | 0.24 | 14.5% | 60% | bull-only |
| `rank(fnd6_newa1v1300_emp)` | TOP1000 | 0.30 | 0.17 | 33.9% | 60% | bull-only |
| `rank(fnd6_newa1v1300_emp / close)` | TOP500 | 0.27 | 0.13 | 20.0% | 40% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_emp, 5))` | TOP1000 | 0.34 | 0.12 | 22.2% | 80% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_emp, 5))` | TOP3000 | 0.22 | 0.06 | 16.8% | 60% | weak |
| `rank(fnd6_newa1v1300_emp)` | TOP500 | 0.06 | 0.02 | 45.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- employee: 1.000 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.974 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.973 (strongly positively correlated)
- fnd6_newa1v1300_ap: 0.969 (strongly positively correlated)
- fnd6_newa1v1300_cogs: 0.968 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
