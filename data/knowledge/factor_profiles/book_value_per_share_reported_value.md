---
field: book_value_per_share_reported_value
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.76
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1458
ann_vol: 0.0846
hit_rate: 0.481
rolling_sharpe_min: -2.011
rolling_sharpe_max: 2.078
negated_best_sharpe: 0.41
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.27
n_negated_sims: 10
direction_gap: -0.35
---
# book_value_per_share_reported_value (analyst4)

*Book Value Per Share - Actual Value*

## Signal Profile
- `rank(book_value_per_share_reported_value)`: S=0.15, F=0.04, T=2.1%, INFERIOR (TOP3000)
- `rank(book_value_per_share_reported_value / close)`: S=0.46, F=0.26, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(book_value_per_share_reported_value, 5))`: S=0.64, F=0.18, T=38.6%, INFERIOR (TOP1000)
- `-rank(book_value_per_share_reported_value)`: S=-0.03, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(book_value_per_share_reported_value, 5))`: S=0.04, F=0.00, T=37.1%, INFERIOR (TOP3000)
- `ts_zscore(book_value_per_share_reported_value, 22)`: S=0.76, F=0.30, T=40.8%, INFERIOR (TOP3000)
- `ts_mean(book_value_per_share_reported_value, 10)`: S=-0.44, F=-0.28, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(book_value_per_share_reported_value, 22))`: S=0.61, F=0.25, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * book_value_per_share_reported_value)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * book_value_per_share_reported_value / close)`: S=0.41, F=0.27, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.45, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.82 (negative), ret=-5.2%
  - 2020: S=0.44 (weak), ret=+5.3%
  - 2021: S=0.47 (weak), ret=+3.3%
  - 2022: S=1.71 (strong), ret=+12.2%
  - 2023: S=0.44 (weak), ret=+3.1%

## Risk & Drawdown
- Max drawdown: 14.58% over 683 days (recovered)
- Annualized: return +3.8%, volatility 8.5% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +0.96, excess kurtosis +5.60

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.01, max 2.08, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +6.42%; worst month: -5.06%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.74
- Sideways: S=-0.62
- Bear: S=0.12

## Negated Direction
Best negated: `rank(-1 * book_value_per_share_reported_value / close)` S=0.41, F=0.27, INFERIOR
Direction gap: -0.35 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * book_value_per_share_reported_value)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * book_value_per_share_reported_value / close)`: S=0.41, F=0.27, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(book_value_per_share_reported_value, 5))`: S=0.04, F=0.00, T=37.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(book_value_per_share_reported_value / close)` | TOP3000 | 0.45 | 0.26 | 14.6% | 80% | mixed |
| `rank(ts_delta(book_value_per_share_reported_value, 5))` | TOP1000 | 0.64 | 0.18 | 8.9% | 60% | mixed |
| `rank(ts_delta(book_value_per_share_reported_value, 5))` | TOP500 | 0.39 | 0.09 | 5.1% | 60% | mixed |
| `rank(book_value_per_share_reported_value / close)` | TOP1000 | 0.14 | 0.05 | 16.7% | 60% | mixed |
| `rank(book_value_per_share_reported_value)` | TOP3000 | 0.14 | 0.04 | 22.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- book_value_per_share_2: 0.925 (strongly positively correlated)
- est_bookvalue_ps: 0.896 (strongly positively correlated)
- anl4_bvps_high: 0.894 (strongly positively correlated)
- anl4_bvps_median: 0.894 (strongly positively correlated)
- anl4_bvps_mean: 0.894 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
