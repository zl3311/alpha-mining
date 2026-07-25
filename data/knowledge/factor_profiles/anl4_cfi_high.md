---
field: anl4_cfi_high
dataset: analyst4
best_template: rank_ts_rank
best_sharpe: 0.68
best_fitness: 0.32
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.283
ann_vol: 0.1172
hit_rate: 0.5158
rolling_sharpe_min: -1.332
rolling_sharpe_max: 3.585
negated_best_sharpe: 0.35
negated_best_template: neg_rank_level
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.33
---
# anl4_cfi_high (analyst4)

*Cash Flow From Investing - The highest estimation*

## Signal Profile
- `rank(anl4_cfi_high)`: S=0.46, F=0.30, T=2.7%, INFERIOR (TOP200)
- `rank(anl4_cfi_high / close)`: S=0.29, F=0.14, T=2.6%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cfi_high, 5))`: S=0.13, F=0.03, T=33.6%, INFERIOR (TOP200)
- `-rank(anl4_cfi_high)`: S=0.08, F=0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_high, 5))`: S=0.22, F=0.04, T=37.2%, INFERIOR (TOP3000)
- `ts_zscore(anl4_cfi_high, 22)`: S=0.14, F=0.03, T=34.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfi_high, 10)`: S=0.10, F=0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfi_high, 22))`: S=0.68, F=0.32, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_high)`: S=0.35, F=0.18, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_high / close)`: S=0.32, F=0.13, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.48, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+1.5%
  - 2020: S=3.03 (strong), ret=+32.6%
  - 2021: S=-0.14 (negative), ret=-2.1%
  - 2022: S=-0.43 (negative), ret=-5.8%
  - 2023: S=0.15 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 28.30% over 1053 days (not yet recovered, ongoing at window end)
- Annualized: return +5.6%, volatility 11.7% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.06, excess kurtosis +1.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.33, max 3.58, latest 0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.74%; worst month: -10.14%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.62
- Sideways: S=1.07
- Bear: S=2.68

## Negated Direction
Best negated: `rank(-1 * anl4_cfi_high)` S=0.35, F=0.18, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_cfi_high)`: S=0.35, F=0.18, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_high / close)`: S=0.32, F=0.13, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_high, 5))`: S=0.22, F=0.04, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfi_high)` | TOP200 | 0.48 | 0.30 | 28.3% | 60% | bear-only |
| `rank(anl4_cfi_high / close)` | TOP200 | 0.30 | 0.14 | 22.2% | 40% | bear-only |
| `rank(ts_delta(anl4_cfi_high, 5))` | TOP200 | 0.14 | 0.03 | 26.6% | 60% | weak |

## Correlation Notes
Top correlates:
- anl4_cfi_median: 0.990 (strongly positively correlated)
- anl4_cfi_mean: 0.989 (strongly positively correlated)
- anl4_cfi_low: 0.970 (strongly positively correlated)
- anl4_cff_median: 0.703 (strongly positively correlated)
- anl4_cff_low: 0.699 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
