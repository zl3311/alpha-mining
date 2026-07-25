---
field: fnd6_newa2v1300_rdip
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.56
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 8
max_drawdown: 0.2648
ann_vol: 0.1038
hit_rate: 0.5198
rolling_sharpe_min: -1.731
rolling_sharpe_max: 2.309
negated_best_sharpe: 0.56
negated_best_template: rank_neg_delta
negated_best_fitness: 0.44
n_negated_sims: 10
direction_gap: 0.2
---
# fnd6_newa2v1300_rdip (fundamental6)

*In Process R&D Expense*

## Signal Profile
- `rank(fnd6_newa2v1300_rdip)`: S=0.35, F=0.19, T=1.5%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_rdip / close)`: S=0.36, F=0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_rdip, 5))`: S=0.12, F=0.04, T=15.7%, INFERIOR (TOP1000)
- `-rank(fnd6_newa2v1300_rdip)`: S=-0.18, F=-0.07, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_rdip, 5))`: S=0.56, F=0.44, T=10.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_rdip, 22)`: S=0.26, F=0.20, T=6.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_rdip, 10)`: S=0.13, F=0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_rdip, 22))`: S=-0.66, F=-0.70, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdip)`: S=-0.20, F=-0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdip / close)`: S=-0.22, F=-0.13, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/11P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.35, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.91 (moderate), ret=+9.2%
  - 2020: S=1.15 (moderate), ret=+10.8%
  - 2021: S=-0.96 (negative), ret=-10.3%
  - 2022: S=-0.10 (negative), ret=-1.1%
  - 2023: S=0.94 (moderate), ret=+9.1%

## Risk & Drawdown
- Max drawdown: 26.48% over 1101 days (not yet recovered, ongoing at window end)
- Annualized: return +3.6%, volatility 10.4% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew -0.03, excess kurtosis +1.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.73, max 2.31, latest 0.94

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +6.79%; worst month: -6.41%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-2.11
- Sideways: S=1.25
- Bear: S=2.04

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_rdip, 5))` S=0.56, F=0.44, INFERIOR
Direction gap: +0.20 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_rdip)`: S=-0.20, F=-0.11, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdip / close)`: S=-0.22, F=-0.13, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_rdip, 5))`: S=0.56, F=0.44, T=10.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_rdip / close)` | TOP3000 | 0.35 | 0.20 | 26.5% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdip)` | TOP3000 | 0.35 | 0.19 | 26.5% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdip / close)` | TOP200 | 0.21 | 0.13 | 34.7% | 80% | mixed |
| `rank(fnd6_newa2v1300_rdip)` | TOP200 | 0.20 | 0.11 | 35.2% | 60% | mixed |
| `rank(fnd6_newa2v1300_rdip / close)` | TOP1000 | 0.19 | 0.08 | 23.3% | 80% | bear-only |
| `rank(fnd6_newa2v1300_rdip)` | TOP1000 | 0.19 | 0.07 | 23.2% | 80% | bear-only |
| `rank(ts_delta(fnd6_newa2v1300_rdip, 5))` | TOP1000 | 0.11 | 0.04 | 39.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_rdip, 5))` | TOP500 | 0.06 | 0.02 | 31.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_rdipa: 0.989 (strongly positively correlated)
- fnd6_invfg: -0.527 (moderately negatively correlated)
- fn_employee_related_liab_q: -0.517 (moderately negatively correlated)
- est_cashflow_op: -0.516 (moderately negatively correlated)
- fnd6_newqv1300_tfvlq: -0.509 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
