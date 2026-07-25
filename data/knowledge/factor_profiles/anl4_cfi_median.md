---
field: anl4_cfi_median
dataset: analyst4
best_template: rank_level
best_sharpe: 0.44
best_fitness: 0.29
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.2988
ann_vol: 0.1214
hit_rate: 0.5142
rolling_sharpe_min: -1.334
rolling_sharpe_max: 3.526
negated_best_sharpe: 0.32
negated_best_template: neg_rank_level
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.12
---
# anl4_cfi_median (analyst4)

*Cash Flow From Investing - median of estimations*

## Signal Profile
- `rank(anl4_cfi_median)`: S=0.44, F=0.29, T=2.7%, INFERIOR (TOP200)
- `rank(anl4_cfi_median / close)`: S=0.27, F=0.13, T=2.6%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cfi_median, 5))`: S=0.15, F=0.03, T=34.0%, INFERIOR (TOP200)
- `-rank(anl4_cfi_median)`: S=0.08, F=0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_median, 5))`: S=0.37, F=0.09, T=37.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_cfi_median, 22)`: S=0.09, F=0.01, T=34.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfi_median, 10)`: S=0.11, F=0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfi_median, 22))`: S=0.62, F=0.28, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_median)`: S=0.32, F=0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_median / close)`: S=0.28, F=0.11, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/22P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.46, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+2.1%
  - 2020: S=2.94 (strong), ret=+33.7%
  - 2021: S=-0.16 (negative), ret=-2.4%
  - 2022: S=-0.36 (negative), ret=-5.2%
  - 2023: S=-0.10 (negative), ret=-1.0%

## Risk & Drawdown
- Max drawdown: 29.88% over 1053 days (not yet recovered, ongoing at window end)
- Annualized: return +5.5%, volatility 12.1% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.09, excess kurtosis +1.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.33, max 3.53, latest -0.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.31%; worst month: -9.85%
Positive months: 58%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.71
- Sideways: S=0.91
- Bear: S=2.82

## Negated Direction
Best negated: `rank(-1 * anl4_cfi_median)` S=0.32, F=0.16, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_cfi_median)`: S=0.32, F=0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_median / close)`: S=0.28, F=0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_median, 5))`: S=0.37, F=0.09, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfi_median)` | TOP200 | 0.46 | 0.29 | 29.9% | 40% | bear-only |
| `rank(anl4_cfi_median / close)` | TOP200 | 0.27 | 0.13 | 23.2% | 40% | bear-only |
| `rank(ts_delta(anl4_cfi_median, 5))` | TOP200 | 0.17 | 0.03 | 19.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cfi_mean: 0.999 (strongly positively correlated)
- anl4_cfi_high: 0.990 (strongly positively correlated)
- anl4_cfi_low: 0.990 (strongly positively correlated)
- anl4_cff_median: 0.727 (strongly positively correlated)
- anl4_cff_low: 0.726 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
