---
field: fnd6_newa2v1300_xrd
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.6
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.1519
ann_vol: 0.0807
hit_rate: 0.4834
rolling_sharpe_min: -1.279
rolling_sharpe_max: 2.795
redundancy_cluster: 83
negated_best_sharpe: 0.15
negated_best_template: neg_rank_level
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.45
---
# fnd6_newa2v1300_xrd (fundamental6)

*Research and Development Expense*

## Signal Profile
- `rank(fnd6_newa2v1300_xrd)`: S=0.54, F=0.36, T=1.3%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_xrd / close)`: S=0.60, F=0.37, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_xrd, 5))`: S=0.50, F=0.31, T=29.3%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_xrd)`: S=-0.25, F=-0.14, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_xrd, 5))`: S=-0.20, F=-0.08, T=29.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_xrd, 63)`: S=-0.06, F=-0.01, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_xrd, 10)`: S=0.24, F=0.14, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_xrd, 22))`: S=0.38, F=0.19, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xrd)`: S=0.15, F=0.07, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xrd / close)`: S=-0.15, F=-0.06, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+2.6%
  - 2020: S=1.73 (strong), ret=+10.7%
  - 2021: S=1.06 (moderate), ret=+8.5%
  - 2022: S=-0.38 (negative), ret=-3.6%
  - 2023: S=0.55 (moderate), ret=+5.3%

## Risk & Drawdown
- Max drawdown: 15.19% over 707 days (not yet recovered, ongoing at window end)
- Annualized: return +4.8%, volatility 8.1% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.44, excess kurtosis +1.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.28, max 2.79, latest 0.71

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +7.08%; worst month: -4.83%
Positive months: 52%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.17
- Sideways: S=0.02
- Bear: S=0.51

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_xrd)` S=0.15, F=0.07, INFERIOR
Direction gap: -0.45 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_xrd)`: S=0.15, F=0.07, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xrd / close)`: S=-0.15, F=-0.06, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_xrd, 5))`: S=-0.20, F=-0.08, T=29.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_xrd / close)` | TOP3000 | 0.59 | 0.37 | 15.2% | 80% | all-weather |
| `rank(fnd6_newa2v1300_xrd)` | TOP3000 | 0.54 | 0.36 | 27.8% | 80% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_xrd, 5))` | TOP200 | 0.50 | 0.31 | 47.6% | 60% | weak |
| `rank(fnd6_newa2v1300_xrd / close)` | TOP1000 | 0.45 | 0.28 | 18.9% | 80% | bull-only |
| `rank(fnd6_newa2v1300_xrd / close)` | TOP500 | 0.29 | 0.16 | 44.0% | 80% | bull-only |
| `rank(fnd6_newa2v1300_xrd)` | TOP1000 | 0.25 | 0.14 | 45.9% | 80% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_xrd, 5))` | TOP3000 | 0.26 | 0.10 | 27.0% | 60% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_xrd, 5))` | TOP500 | 0.21 | 0.08 | 36.2% | 60% | mixed |
| `rank(fnd6_newa2v1300_xrd / close)` | TOP200 | 0.16 | 0.06 | 36.0% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_stkcpa: 0.819 (strongly positively correlated)
- est_sga: 0.819 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_a: 0.816 (strongly positively correlated)
- selling_general_admin_expense_actual_value: 0.786 (strongly positively correlated)
- selling_general_admin_expense_reported_value: 0.786 (strongly positively correlated)

Redundancy cluster #83: 3 similar fields, mean |rho| 0.764 (representative: fnd2_a_alsbcmpexrsus). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
