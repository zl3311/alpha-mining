---
field: fnd6_newa2v1300_rdipa
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.31
best_fitness: 0.16
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 7
max_drawdown: 0.2816
ann_vol: 0.1059
hit_rate: 0.5166
rolling_sharpe_min: -1.751
rolling_sharpe_max: 2.302
negated_best_sharpe: 0.08
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.23
---
# fnd6_newa2v1300_rdipa (fundamental6)

*In-Process R&D Expense After-tax*

## Signal Profile
- `rank(fnd6_newa2v1300_rdipa)`: S=0.30, F=0.15, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_rdipa / close)`: S=0.31, F=0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_rdipa, 5))`: S=0.08, F=0.02, T=16.0%, INFERIOR (TOP1000)
- `-rank(fnd6_newa2v1300_rdipa)`: S=-0.14, F=-0.05, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_rdipa, 5))`: S=0.08, F=0.02, T=10.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_rdipa, 63)`: S=0.20, F=0.12, T=7.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_rdipa, 10)`: S=0.11, F=0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_rdipa, 22))`: S=-0.57, F=-0.58, T=12.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdipa)`: S=-0.19, F=-0.11, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdipa / close)`: S=-0.20, F=-0.12, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/11P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.30, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.64 (moderate), ret=+7.0%
  - 2020: S=1.23 (moderate), ret=+11.7%
  - 2021: S=-1.11 (negative), ret=-12.1%
  - 2022: S=-0.07 (negative), ret=-0.8%
  - 2023: S=1.02 (moderate), ret=+9.8%

## Risk & Drawdown
- Max drawdown: 28.16% over 1101 days (not yet recovered, ongoing at window end)
- Annualized: return +3.2%, volatility 10.6% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew -0.07, excess kurtosis +1.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.75, max 2.30, latest 1.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +7.13%; worst month: -6.44%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-2.03
- Sideways: S=1.05
- Bear: S=2.00

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_rdipa, 5))` S=0.08, F=0.02, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_rdipa)`: S=-0.19, F=-0.11, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_rdipa / close)`: S=-0.20, F=-0.12, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_rdipa, 5))`: S=0.08, F=0.02, T=10.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_rdipa / close)` | TOP3000 | 0.30 | 0.16 | 28.2% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdipa)` | TOP3000 | 0.30 | 0.15 | 28.1% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdipa / close)` | TOP200 | 0.20 | 0.12 | 33.4% | 60% | mixed |
| `rank(fnd6_newa2v1300_rdipa)` | TOP200 | 0.18 | 0.11 | 33.7% | 60% | mixed |
| `rank(fnd6_newa2v1300_rdipa / close)` | TOP1000 | 0.16 | 0.05 | 26.2% | 60% | bear-only |
| `rank(fnd6_newa2v1300_rdipa)` | TOP1000 | 0.15 | 0.05 | 26.1% | 60% | bear-only |
| `rank(ts_delta(fnd6_newa2v1300_rdipa, 5))` | TOP1000 | 0.08 | 0.02 | 45.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_rdip: 0.989 (strongly positively correlated)
- fnd6_invfg: -0.517 (moderately negatively correlated)
- est_cashflow_op: -0.508 (moderately negatively correlated)
- fnd6_am: -0.506 (moderately negatively correlated)
- fn_employee_related_liab_q: -0.504 (moderately negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
