---
field: anl4_cfi_mean
dataset: analyst4
best_template: rank_level
best_sharpe: 0.42
best_fitness: 0.27
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.3134
ann_vol: 0.1223
hit_rate: 0.5134
rolling_sharpe_min: -1.415
rolling_sharpe_max: 3.49
negated_best_sharpe: 0.33
negated_best_template: neg_rank_level
negated_best_fitness: 0.16
n_negated_sims: 10
direction_gap: -0.09
---
# anl4_cfi_mean (analyst4)

*Cash Flow From Investing - mean of estimations*

## Signal Profile
- `rank(anl4_cfi_mean)`: S=0.42, F=0.27, T=2.7%, INFERIOR (TOP200)
- `rank(anl4_cfi_mean / close)`: S=0.23, F=0.10, T=2.6%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cfi_mean, 5))`: S=0.47, F=0.18, T=34.2%, INFERIOR (TOP200)
- `-rank(anl4_cfi_mean)`: S=0.10, F=0.03, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_mean, 5))`: S=0.42, F=0.11, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_cfi_mean, 22)`: S=0.08, F=0.01, T=34.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfi_mean, 10)`: S=0.10, F=0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfi_mean, 22))`: S=0.48, F=0.19, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_mean)`: S=0.33, F=0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_mean / close)`: S=0.29, F=0.11, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/21P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.43, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+1.7%
  - 2020: S=2.93 (strong), ret=+33.8%
  - 2021: S=-0.25 (negative), ret=-3.9%
  - 2022: S=-0.38 (negative), ret=-5.5%
  - 2023: S=-0.03 (negative), ret=-0.3%

## Risk & Drawdown
- Max drawdown: 31.34% over 1053 days (not yet recovered, ongoing at window end)
- Annualized: return +5.3%, volatility 12.2% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.09, excess kurtosis +1.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.42, max 3.49, latest -0.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.24%; worst month: -9.87%
Positive months: 58%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.76
- Sideways: S=0.88
- Bear: S=2.84

## Negated Direction
Best negated: `rank(-1 * anl4_cfi_mean)` S=0.33, F=0.16, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_cfi_mean)`: S=0.33, F=0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_mean / close)`: S=0.29, F=0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_mean, 5))`: S=0.42, F=0.11, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfi_mean)` | TOP200 | 0.43 | 0.27 | 31.3% | 40% | bear-only |
| `rank(ts_delta(anl4_cfi_mean, 5))` | TOP200 | 0.48 | 0.18 | 21.7% | 80% | mixed |
| `rank(anl4_cfi_mean / close)` | TOP200 | 0.24 | 0.10 | 24.2% | 40% | bear-only |
| `rank(ts_delta(anl4_cfi_mean, 5))` | TOP500 | 0.23 | 0.05 | 13.1% | 40% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cfi_median: 0.999 (strongly positively correlated)
- anl4_cfi_low: 0.990 (strongly positively correlated)
- anl4_cfi_high: 0.989 (strongly positively correlated)
- anl4_cff_median: 0.733 (strongly positively correlated)
- anl4_cff_low: 0.731 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
