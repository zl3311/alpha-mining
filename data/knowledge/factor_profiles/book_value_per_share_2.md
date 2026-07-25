---
field: book_value_per_share_2
dataset: analyst4
best_template: ts_zscore
best_sharpe: 0.53
best_fitness: 0.2
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 2
max_drawdown: 0.1584
ann_vol: 0.0914
hit_rate: 0.4648
rolling_sharpe_min: -1.853
rolling_sharpe_max: 2.074
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: 0.05
---
# book_value_per_share_2 (analyst4)

*Book Value Per Share - Actual Value*

## Signal Profile
- `rank(book_value_per_share_2)`: S=0.00, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(book_value_per_share_2 / close)`: S=0.32, F=0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(book_value_per_share_2, 5))`: S=-0.09, F=-0.01, T=37.1%, INFERIOR (TOP500)
- `-rank(book_value_per_share_2)`: S=0.20, F=0.07, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(book_value_per_share_2, 5))`: S=0.58, F=0.15, T=35.4%, INFERIOR (TOP3000)
- `-ts_zscore(book_value_per_share_2, 63)`: S=0.53, F=0.20, T=21.0%, INFERIOR (TOP3000)
- `ts_mean(book_value_per_share_2, 10)`: S=-0.15, F=-0.06, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(book_value_per_share_2, 22))`: S=-0.03, F=0.00, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * book_value_per_share_2)`: S=0.00, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * book_value_per_share_2 / close)`: S=-0.32, F=-0.15, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.31, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.79 (negative), ret=-5.5%
  - 2020: S=0.09 (weak), ret=+1.0%
  - 2021: S=0.65 (moderate), ret=+4.7%
  - 2022: S=1.09 (moderate), ret=+9.9%
  - 2023: S=0.45 (weak), ret=+3.7%

## Risk & Drawdown
- Max drawdown: 15.84% over 762 days (recovered)
- Annualized: return +2.8%, volatility 9.1% (fraction of booksize)
- Hit rate: 46.5% positive days
- Tail shape: skew +1.10, excess kurtosis +5.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.85, max 2.07, latest 0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +5.84%; worst month: -5.07%
Positive months: 51%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.29
- Sideways: S=-1.17
- Bear: S=0.56

## Negated Direction
Best negated: `rank(-1 * ts_delta(book_value_per_share_2, 5))` S=0.58, F=0.15, INFERIOR
Direction gap: +0.05 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * book_value_per_share_2)`: S=0.00, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * book_value_per_share_2 / close)`: S=-0.32, F=-0.15, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(book_value_per_share_2, 5))`: S=0.58, F=0.15, T=35.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(book_value_per_share_2 / close)` | TOP3000 | 0.31 | 0.15 | 15.8% | 80% | all-weather |
| `rank(book_value_per_share_2 / close)` | TOP1000 | 0.15 | 0.05 | 16.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- book_value_per_share_reported_value: 0.925 (strongly positively correlated)
- fnd6_newa1v1300_bkvlps: 0.910 (strongly positively correlated)
- est_bookvalue_ps: 0.880 (strongly positively correlated)
- anl4_bvps_high: 0.821 (strongly positively correlated)
- anl4_bvps_median: 0.819 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
