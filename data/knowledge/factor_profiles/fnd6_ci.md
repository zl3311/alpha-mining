---
field: fnd6_ci
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.49
best_fitness: 0.23
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.3499
ann_vol: 0.1084
hit_rate: 0.4955
rolling_sharpe_min: -4.233
rolling_sharpe_max: 2.174
negated_best_sharpe: 0.49
negated_best_template: rank_neg_delta
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: 0.39
---
# fnd6_ci (fundamental6)

*Comprehensive Income - Total*

## Signal Profile
- `rank(fnd6_ci)`: S=0.00, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_ci / close)`: S=0.10, F=0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_ci, 5))`: S=0.06, F=0.01, T=29.0%, INFERIOR (TOP200)
- `-rank(fnd6_ci)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ci, 5))`: S=0.49, F=0.23, T=40.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_ci, 63)`: S=-0.31, F=-0.16, T=20.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_ci, 10)`: S=0.10, F=0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_ci, 22))`: S=-0.30, F=-0.12, T=19.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ci)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ci / close)`: S=-0.02, F=0.00, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.09, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.26 (weak), ret=+1.3%
  - 2020: S=-2.96 (negative), ret=-20.0%
  - 2021: S=0.62 (moderate), ret=+7.6%
  - 2022: S=1.18 (moderate), ret=+18.4%
  - 2023: S=-0.26 (negative), ret=-2.7%

## Risk & Drawdown
- Max drawdown: 34.99% over 942 days (recovered)
- Annualized: return +0.9%, volatility 10.8% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew -0.04, excess kurtosis +1.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -4.23, max 2.17, latest -0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.73%; worst month: -7.33%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.44
- Sideways: S=0.68
- Bear: S=-3.67

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_ci, 5))` S=0.49, F=0.23, INFERIOR
Direction gap: +0.39 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_ci)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_ci / close)`: S=-0.02, F=0.00, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_ci, 5))`: S=0.49, F=0.23, T=40.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_ci / close)` | TOP3000 | 0.09 | 0.03 | 35.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- net_income_total_2: 0.977 (strongly positively correlated)
- pretax_income_total: 0.972 (strongly positively correlated)
- pretax_income_reported: 0.959 (strongly positively correlated)
- earnings_per_share_reported: 0.957 (strongly positively correlated)
- net_income_adjusted: 0.955 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
