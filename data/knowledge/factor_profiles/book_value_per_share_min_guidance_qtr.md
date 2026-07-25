---
field: book_value_per_share_min_guidance_qtr
dataset: analyst4
best_template: rank_level
best_sharpe: 0.44
best_fitness: 0.34
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2873
ann_vol: 0.1672
hit_rate: 0.4486
rolling_sharpe_min: -1.461
rolling_sharpe_max: 1.934
negated_best_sharpe: 0.45
negated_best_template: neg_rank_level
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.01
---
# book_value_per_share_min_guidance_qtr (analyst4)

*Book value per share - minimum guidance value*

## Signal Profile
- `rank(book_value_per_share_min_guidance_qtr)`: S=0.44, F=0.34, T=4.1%, INFERIOR (TOP200)
- `rank(book_value_per_share_min_guidance_qtr / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(book_value_per_share_min_guidance_qtr, 5))`: S=0.53, F=0.20, T=33.7%, INFERIOR (TOP200)
- `-rank(book_value_per_share_min_guidance_qtr)`: S=0.16, F=0.07, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(book_value_per_share_min_guidance_qtr, 5))`: S=0.07, F=0.01, T=33.5%, INFERIOR (TOP3000)
- `-ts_zscore(book_value_per_share_min_guidance_qtr, 63)`: S=0.12, F=0.02, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(book_value_per_share_min_guidance_qtr, 10)`: S=-0.07, F=-0.02, T=9.2%, INFERIOR (TOP3000)
- `rank(ts_rank(book_value_per_share_min_guidance_qtr, 22))`: S=-0.13, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * book_value_per_share_min_guidance_qtr)`: S=0.45, F=0.25, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * book_value_per_share_min_guidance_qtr / close)`: S=-0.07, F=-0.02, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.44, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.44 (weak), ret=+8.6%
  - 2020: S=-1.15 (negative), ret=-15.0%
  - 2021: S=1.03 (moderate), ret=+21.7%
  - 2022: S=0.66 (moderate), ret=+6.4%
  - 2023: S=0.92 (moderate), ret=+14.5%

## Risk & Drawdown
- Max drawdown: 28.73% over 548 days (recovered)
- Annualized: return +7.4%, volatility 16.7% (fraction of booksize)
- Hit rate: 44.9% positive days
- Tail shape: skew -0.32, excess kurtosis +9.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.46, max 1.93, latest 0.91

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.97%; worst month: -14.09%
Positive months: 62%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.74
- Sideways: S=0.50
- Bear: S=-0.77

## Negated Direction
Best negated: `rank(-1 * book_value_per_share_min_guidance_qtr)` S=0.45, F=0.25, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * book_value_per_share_min_guidance_qtr)`: S=0.45, F=0.25, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * book_value_per_share_min_guidance_qtr / close)`: S=-0.07, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(book_value_per_share_min_guidance_qtr, 5))`: S=0.07, F=0.01, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(book_value_per_share_min_guidance_qtr)` | TOP200 | 0.44 | 0.34 | 28.7% | 80% | bull-only |
| `rank(ts_delta(book_value_per_share_min_guidance_qtr, 5))` | TOP200 | 0.55 | 0.20 | 15.8% | 60% | bear-only |
| `rank(book_value_per_share_min_guidance_qtr / close)` | TOP3000 | 0.07 | 0.02 | 52.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_book_value_per_share_guidance: 1.000 (strongly positively correlated)
- min_book_value_per_share_guidance: 1.000 (strongly positively correlated)
- max_book_value_per_share_guidance_2: 1.000 (strongly positively correlated)
- min_free_cashflow_per_share_guidance: 0.402 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.402 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
