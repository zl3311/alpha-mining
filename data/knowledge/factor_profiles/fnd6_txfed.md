---
field: fnd6_txfed
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.81
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2369
ann_vol: 0.0846
hit_rate: 0.5069
rolling_sharpe_min: -3.672
rolling_sharpe_max: 2.142
negated_best_sharpe: 0.81
negated_best_template: rank_neg_delta
negated_best_fitness: 0.5
n_negated_sims: 10
direction_gap: 0.3
---
# fnd6_txfed (fundamental6)

*Income Taxes - Federal*

## Signal Profile
- `rank(fnd6_txfed)`: S=0.14, F=0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_txfed / close)`: S=0.21, F=0.08, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txfed, 5))`: S=0.19, F=0.05, T=42.9%, INFERIOR (TOP3000)
- `-rank(fnd6_txfed)`: S=0.03, F=0.00, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txfed, 5))`: S=0.81, F=0.50, T=41.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txfed, 63)`: S=0.51, F=0.36, T=18.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txfed, 10)`: S=0.08, F=0.02, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txfed, 22))`: S=-0.67, F=-0.41, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txfed)`: S=0.03, F=0.00, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txfed / close)`: S=-0.02, F=0.00, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.20, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+0.8%
  - 2020: S=-2.75 (negative), ret=-14.2%
  - 2021: S=0.64 (moderate), ret=+5.3%
  - 2022: S=1.23 (moderate), ret=+15.6%
  - 2023: S=0.10 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 23.69% over 938 days (recovered)
- Annualized: return +1.7%, volatility 8.5% (fraction of booksize)
- Hit rate: 50.7% positive days
- Tail shape: skew -0.04, excess kurtosis +1.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -3.67, max 2.14, latest -0.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.36%; worst month: -5.44%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.32
- Sideways: S=0.78
- Bear: S=-3.12

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txfed, 5))` S=0.81, F=0.50, INFERIOR
Direction gap: +0.30 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txfed)`: S=0.03, F=0.00, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txfed / close)`: S=-0.02, F=0.00, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txfed, 5))`: S=0.81, F=0.50, T=41.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txfed / close)` | TOP3000 | 0.20 | 0.08 | 23.7% | 80% | bull-only |
| `rank(ts_delta(fnd6_txfed, 5))` | TOP3000 | 0.18 | 0.05 | 33.1% | 60% | mixed |
| `rank(fnd6_txfed)` | TOP3000 | 0.13 | 0.05 | 28.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_ci: 0.945 (strongly positively correlated)
- pretax_income_reported: 0.935 (strongly positively correlated)
- fnd6_newa2v1300_txt: 0.933 (strongly positively correlated)
- net_income_total_2: 0.929 (strongly positively correlated)
- pretax_income_total: 0.929 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
