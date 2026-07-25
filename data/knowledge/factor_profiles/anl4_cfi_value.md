---
field: anl4_cfi_value
dataset: analyst4
best_template: rank_level
best_sharpe: 0.57
best_fitness: 0.36
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.1202
ann_vol: 0.0874
hit_rate: 0.5166
rolling_sharpe_min: -0.636
rolling_sharpe_max: 2.076
redundancy_cluster: 92
negated_best_sharpe: 0.81
negated_best_template: rank_neg_delta
negated_best_fitness: 0.34
n_negated_sims: 10
direction_gap: 0.24
---
# anl4_cfi_value (analyst4)

*Cash Flow From Investing - announced financial value*

## Signal Profile
- `rank(anl4_cfi_value)`: S=0.57, F=0.36, T=4.9%, INFERIOR (TOP200)
- `rank(anl4_cfi_value / close)`: S=0.32, F=0.15, T=4.9%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cfi_value, 5))`: S=-0.42, F=-0.12, T=40.6%, INFERIOR (TOP3000)
- `-rank(anl4_cfi_value)`: S=0.28, F=0.10, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_value, 5))`: S=0.81, F=0.34, T=39.1%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_cfi_value, 63)`: S=0.39, F=0.12, T=18.1%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfi_value, 10)`: S=0.19, F=0.08, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfi_value, 22))`: S=-1.07, F=-0.61, T=16.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_value)`: S=0.28, F=0.10, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_value / close)`: S=0.35, F=0.14, T=4.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.04 (moderate), ret=+6.2%
  - 2020: S=1.39 (moderate), ret=+11.8%
  - 2021: S=0.66 (moderate), ret=+6.8%
  - 2022: S=0.09 (weak), ret=+0.9%
  - 2023: S=-0.02 (negative), ret=-0.2%

## Risk & Drawdown
- Max drawdown: 12.02% over 218 days (recovered)
- Annualized: return +5.2%, volatility 8.7% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.15, excess kurtosis +1.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.64, max 2.08, latest 0.01

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +6.82%; worst month: -5.07%
Positive months: 52%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.71
- Sideways: S=1.30
- Bear: S=1.29

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cfi_value, 5))` S=0.81, F=0.34, INFERIOR
Direction gap: +0.24 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_cfi_value)`: S=0.28, F=0.10, T=4.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_value / close)`: S=0.35, F=0.14, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_value, 5))`: S=0.81, F=0.34, T=39.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfi_value)` | TOP200 | 0.59 | 0.36 | 12.0% | 80% | bear-only |
| `rank(anl4_cfi_value / close)` | TOP200 | 0.34 | 0.15 | 12.3% | 80% | mixed |

## Correlation Notes
Top correlates:
- investing_cashflow_reported_value: 1.000 (strongly positively correlated)
- anl4_cfi_high: 0.602 (moderately positively correlated)
- anl4_cfi_median: 0.600 (moderately positively correlated)
- anl4_cfi_mean: 0.594 (moderately positively correlated)
- anl4_cfi_low: 0.592 (moderately positively correlated)

Redundancy cluster #92: 2 similar fields, mean |rho| 1.0 (representative: investing_cashflow_reported_value). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
