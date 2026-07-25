---
field: fnd6_txo
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.54
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 5
max_drawdown: 0.9545
ann_vol: 0.3118
hit_rate: 0.5077
rolling_sharpe_min: -1.86
rolling_sharpe_max: 2.618
negated_best_sharpe: 0.09
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.45
---
# fnd6_txo (fundamental6)

*Income Taxes - Other*

## Signal Profile
- `rank(fnd6_txo)`: S=0.21, F=0.15, T=4.0%, INFERIOR (TOP200)
- `rank(fnd6_txo / close)`: S=0.21, F=0.15, T=4.0%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_txo, 5))`: S=0.06, F=0.02, T=6.8%, INFERIOR (TOP200)
- `-rank(fnd6_txo)`: S=-0.09, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txo, 5))`: S=0.09, F=0.03, T=10.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_txo, 63)`: S=0.54, F=0.47, T=3.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txo, 10)`: S=-0.01, F=0.00, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txo, 22))`: S=-0.17, F=-0.09, T=8.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txo)`: S=-0.09, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txo / close)`: S=-0.09, F=-0.03, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.21, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.69 (strong), ret=+41.0%
  - 2020: S=1.84 (strong), ret=+42.5%
  - 2021: S=0.85 (moderate), ret=+24.1%
  - 2022: S=-1.36 (negative), ret=-63.0%
  - 2023: S=-0.53 (negative), ret=-13.0%

## Risk & Drawdown
- Max drawdown: 95.45% over 834 days (not yet recovered, ongoing at window end)
- Annualized: return +6.5%, volatility 31.2% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.65, excess kurtosis +11.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.86, max 2.62, latest -0.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +22.21%; worst month: -22.10%
Positive months: 61%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.55
- Sideways: S=-0.04
- Bear: S=1.46

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txo, 5))` S=0.09, F=0.03, INFERIOR
Direction gap: -0.45 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txo)`: S=-0.09, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txo / close)`: S=-0.09, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txo, 5))`: S=0.09, F=0.03, T=10.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txo)` | TOP200 | 0.21 | 0.15 | 95.5% | 60% | bear-only |
| `rank(fnd6_txo / close)` | TOP200 | 0.21 | 0.15 | 95.5% | 60% | bear-only |
| `rank(fnd6_txo)` | TOP1000 | 0.10 | 0.03 | 26.3% | 80% | weak |
| `rank(fnd6_txo / close)` | TOP1000 | 0.10 | 0.03 | 26.3% | 80% | weak |
| `rank(ts_delta(fnd6_txo, 5))` | TOP200 | 0.06 | 0.02 | 29.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_cff_median: 0.411 (moderately positively correlated)
- anl4_cff_low: 0.403 (moderately positively correlated)
- fnd6_recta: 0.402 (moderately positively correlated)
- est_cashflow_fin: 0.395 (weakly positively correlated)
- anl4_af_div_value: -0.389 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
