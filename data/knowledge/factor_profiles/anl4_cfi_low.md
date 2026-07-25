---
field: anl4_cfi_low
dataset: analyst4
best_template: rank_level
best_sharpe: 0.37
best_fitness: 0.23
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.3303
ann_vol: 0.1261
hit_rate: 0.5134
rolling_sharpe_min: -1.485
rolling_sharpe_max: 3.4
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: 0.22
---
# anl4_cfi_low (analyst4)

*Cash Flow From Investing - The lowest estimation*

## Signal Profile
- `rank(anl4_cfi_low)`: S=0.37, F=0.23, T=2.7%, INFERIOR (TOP200)
- `rank(anl4_cfi_low / close)`: S=0.22, F=0.10, T=2.6%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cfi_low, 5))`: S=0.01, F=0.00, T=33.8%, INFERIOR (TOP200)
- `-rank(anl4_cfi_low)`: S=0.17, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_low, 5))`: S=0.59, F=0.20, T=37.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_cfi_low, 22)`: S=0.16, F=0.03, T=34.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfi_low, 10)`: S=0.10, F=0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfi_low, 22))`: S=0.41, F=0.16, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_low)`: S=0.17, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_low / close)`: S=0.13, F=0.04, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 8F/24P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.38, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.10 (weak), ret=+0.8%
  - 2020: S=2.73 (strong), ret=+33.1%
  - 2021: S=-0.19 (negative), ret=-3.0%
  - 2022: S=-0.35 (negative), ret=-5.2%
  - 2023: S=-0.20 (negative), ret=-1.9%

## Risk & Drawdown
- Max drawdown: 33.03% over 1052 days (not yet recovered, ongoing at window end)
- Annualized: return +4.9%, volatility 12.6% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.10, excess kurtosis +1.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.49, max 3.40, latest -0.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.82%; worst month: -9.99%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.78
- Sideways: S=0.78
- Bear: S=2.68

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cfi_low, 5))` S=0.59, F=0.20, INFERIOR
Direction gap: +0.22 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_cfi_low)`: S=0.17, F=0.06, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_low / close)`: S=0.13, F=0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_low, 5))`: S=0.59, F=0.20, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfi_low)` | TOP200 | 0.38 | 0.23 | 33.0% | 40% | bear-only |
| `rank(anl4_cfi_low / close)` | TOP200 | 0.23 | 0.10 | 24.8% | 40% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cfi_mean: 0.990 (strongly positively correlated)
- anl4_cfi_median: 0.990 (strongly positively correlated)
- anl4_cfi_high: 0.970 (strongly positively correlated)
- anl4_cff_median: 0.740 (strongly positively correlated)
- anl4_cff_low: 0.740 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
