---
field: fnd6_state
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.6
best_fitness: 0.68
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.868
ann_vol: 0.2131
hit_rate: 0.4737
rolling_sharpe_min: -2.498
rolling_sharpe_max: 3.445
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.68
n_negated_sims: 10
direction_gap: 0.23
---
# fnd6_state (fundamental6)

*integer for identifying the state of the company*

## Signal Profile
- `rank(fnd6_state)`: S=0.23, F=0.06, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd6_state / close)`: S=0.40, F=0.21, T=2.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_state, 5))`: S=0.38, F=0.26, T=16.6%, INFERIOR (TOP3000)
- `-rank(fnd6_state)`: S=-0.05, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_state, 5))`: S=0.60, F=0.68, T=11.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_state, 22)`: S=0.37, F=0.35, T=1.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_state, 10)`: S=-0.02, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_state, 22))`: S=-0.16, F=-0.11, T=10.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_state)`: S=0.22, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_state / close)`: S=0.06, F=0.01, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.37, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-1.61 (negative), ret=-17.1%
  - 2020: S=-1.36 (negative), ret=-28.6%
  - 2021: S=-1.17 (negative), ret=-27.8%
  - 2022: S=3.40 (strong), ret=+96.2%
  - 2023: S=1.08 (moderate), ret=+16.3%

## Risk & Drawdown
- Max drawdown: 86.80% over 1281 days (recovered)
- Annualized: return +8.0%, volatility 21.3% (fraction of booksize)
- Hit rate: 47.4% positive days
- Tail shape: skew +0.66, excess kurtosis +13.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.50, max 3.44, latest 1.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +25.08%; worst month: -11.99%
Positive months: 46%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.84
- Sideways: S=0.36
- Bear: S=-1.14

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_state, 5))` S=0.60, F=0.68, INFERIOR
Direction gap: +0.23 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_state)`: S=0.22, F=0.07, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_state / close)`: S=0.06, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_state, 5))`: S=0.60, F=0.68, T=11.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_state, 5))` | TOP3000 | 0.37 | 0.26 | 86.8% | 40% | bull-only |
| `rank(ts_delta(fnd6_state, 5))` | TOP200 | 0.32 | 0.22 | 29.6% | 60% | bull-only |
| `rank(fnd6_state / close)` | TOP200 | 0.39 | 0.21 | 17.5% | 40% | mixed |
| `rank(fnd6_state)` | TOP3000 | 0.20 | 0.06 | 12.6% | 60% | bear-only |
| `rank(fnd6_state)` | TOP200 | 0.14 | 0.05 | 17.9% | 40% | weak |
| `rank(fnd6_state / close)` | TOP3000 | 0.09 | 0.03 | 32.1% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_city: 0.313 (weakly positively correlated)
- fnd6_zipcode: 0.265 (weakly positively correlated)
- max_share_buyback_guidance: 0.260 (weakly positively correlated)
- min_adjusted_funds_from_operations_adj_guidance: 0.260 (weakly positively correlated)
- max_total_goodwill_guidance_2: 0.260 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
