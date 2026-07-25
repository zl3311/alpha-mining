---
field: fnd6_newa2v1300_xsga
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.79
best_fitness: 0.63
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2563
ann_vol: 0.0997
hit_rate: 0.5166
rolling_sharpe_min: -2.79
rolling_sharpe_max: 2.756
redundancy_cluster: 13
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: -0.25
---
# fnd6_newa2v1300_xsga (fundamental6)

*Selling, General and Administrative Expense*

## Signal Profile
- `rank(fnd6_newa2v1300_xsga)`: S=0.79, F=0.63, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_xsga / close)`: S=0.69, F=0.46, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_xsga, 5))`: S=0.31, F=0.13, T=34.8%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_xsga)`: S=-0.34, F=-0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_xsga, 5))`: S=0.54, F=0.26, T=35.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_xsga, 22)`: S=0.37, F=0.19, T=29.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_xsga, 10)`: S=0.22, F=0.10, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_xsga, 22))`: S=0.20, F=0.06, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xsga)`: S=-0.08, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xsga / close)`: S=-0.27, F=-0.13, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.80 (moderate), ret=+4.0%
  - 2020: S=-1.18 (negative), ret=-8.2%
  - 2021: S=1.12 (moderate), ret=+17.2%
  - 2022: S=1.67 (strong), ret=+18.8%
  - 2023: S=0.97 (moderate), ret=+6.7%

## Risk & Drawdown
- Max drawdown: 25.63% over 777 days (recovered)
- Annualized: return +7.9%, volatility 10.0% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.08, excess kurtosis +2.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.79, max 2.76, latest 0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.26%; worst month: -5.52%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.01
- Sideways: S=1.14
- Bear: S=-2.47

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_xsga, 5))` S=0.54, F=0.26, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_xsga)`: S=-0.08, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xsga / close)`: S=-0.27, F=-0.13, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_xsga, 5))`: S=0.54, F=0.26, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_xsga)` | TOP3000 | 0.79 | 0.63 | 25.6% | 80% | bull-only |
| `rank(fnd6_newa2v1300_xsga / close)` | TOP3000 | 0.69 | 0.46 | 9.3% | 80% | mixed |
| `rank(fnd6_newa2v1300_xsga / close)` | TOP1000 | 0.45 | 0.26 | 12.2% | 80% | bull-only |
| `rank(fnd6_newa2v1300_xsga)` | TOP1000 | 0.34 | 0.20 | 34.7% | 80% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_xsga, 5))` | TOP200 | 0.31 | 0.13 | 34.4% | 40% | mixed |
| `rank(fnd6_newa2v1300_xsga / close)` | TOP500 | 0.28 | 0.13 | 20.7% | 80% | bull-only |
| `rank(fnd6_newa2v1300_xsga)` | TOP500 | 0.08 | 0.02 | 50.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- sga_expense: 0.990 (strongly positively correlated)
- fnd6_newqv1300_xsgaq: 0.990 (strongly positively correlated)
- fnd6_newa1v1300_act: 0.975 (strongly positively correlated)
- fnd6_newqv1300_xoprq: 0.975 (strongly positively correlated)
- operating_expense: 0.975 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
