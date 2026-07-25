---
field: fnd6_recta
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.42
best_fitness: 0.25
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.3369
ann_vol: 0.1063
hit_rate: 0.5036
rolling_sharpe_min: -1.696
rolling_sharpe_max: 4.179
negated_best_sharpe: 0.35
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.07
---
# fnd6_recta (fundamental6)

*Retained Earnings - Cumulative Translation Adjustment*

## Signal Profile
- `rank(fnd6_recta)`: S=0.40, F=0.24, T=3.2%, INFERIOR (TOP200)
- `rank(fnd6_recta / close)`: S=0.42, F=0.25, T=3.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_recta, 5))`: S=0.14, F=0.04, T=38.7%, INFERIOR (TOP1000)
- `-rank(fnd6_recta)`: S=0.20, F=0.07, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_recta, 5))`: S=0.34, F=0.13, T=40.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_recta, 63)`: S=0.27, F=0.14, T=19.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_recta, 10)`: S=-0.29, F=-0.13, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_recta, 22))`: S=0.46, F=0.25, T=19.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_recta)`: S=0.27, F=0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_recta / close)`: S=0.35, F=0.13, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.43, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.98 (moderate), ret=+5.8%
  - 2020: S=3.72 (strong), ret=+28.3%
  - 2021: S=-0.23 (negative), ret=-2.8%
  - 2022: S=-1.43 (negative), ret=-21.3%
  - 2023: S=1.39 (moderate), ret=+12.6%

## Risk & Drawdown
- Max drawdown: 33.69% over 1043 days (not yet recovered, ongoing at window end)
- Annualized: return +4.6%, volatility 10.6% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.28, excess kurtosis +2.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.70, max 4.18, latest 1.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.66%; worst month: -8.88%
Positive months: 63%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.73
- Sideways: S=0.70
- Bear: S=3.39

## Negated Direction
Best negated: `rank(-1 * fnd6_recta / close)` S=0.35, F=0.13, INFERIOR
Direction gap: -0.07 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_recta)`: S=0.27, F=0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_recta / close)`: S=0.35, F=0.13, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_recta, 5))`: S=0.34, F=0.13, T=40.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_recta / close)` | TOP200 | 0.43 | 0.25 | 33.7% | 60% | bear-only |
| `rank(fnd6_recta)` | TOP200 | 0.43 | 0.24 | 34.9% | 60% | bear-only |
| `rank(ts_delta(fnd6_recta, 5))` | TOP1000 | 0.14 | 0.04 | 45.6% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_accum_oth_income_loss_net_of_tax_a: 0.835 (strongly positively correlated)
- fn_accum_oth_income_loss_net_of_tax_q: 0.803 (strongly positively correlated)
- est_cashflow_fin: 0.747 (strongly positively correlated)
- anl4_cff_median: 0.728 (strongly positively correlated)
- cashflow_dividends: -0.723 (strongly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
