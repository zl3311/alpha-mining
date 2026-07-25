---
field: fnd6_sppe
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.47
best_fitness: 0.36
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0965
ann_vol: 0.0432
hit_rate: 0.498
rolling_sharpe_min: -1.832
rolling_sharpe_max: 2.823
negated_best_sharpe: 0.45
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.02
---
# fnd6_sppe (fundamental6)

*Sale of Property*

## Signal Profile
- `rank(fnd6_sppe)`: S=0.64, F=0.31, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_sppe / close)`: S=0.67, F=0.32, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_sppe, 5))`: S=0.24, F=0.09, T=33.1%, INFERIOR (TOP1000)
- `-rank(fnd6_sppe)`: S=-0.27, F=-0.10, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_sppe, 5))`: S=0.45, F=0.21, T=33.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_sppe, 63)`: S=0.47, F=0.36, T=15.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_sppe, 10)`: S=0.08, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_sppe, 22))`: S=-0.07, F=-0.02, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_sppe)`: S=-0.64, F=-0.31, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_sppe / close)`: S=-0.67, F=-0.32, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.66, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.78 (negative), ret=-2.2%
  - 2020: S=-1.43 (negative), ret=-5.5%
  - 2021: S=0.77 (moderate), ret=+3.3%
  - 2022: S=2.36 (strong), ret=+14.0%
  - 2023: S=1.24 (moderate), ret=+4.4%

## Risk & Drawdown
- Max drawdown: 9.65% over 1066 days (recovered)
- Annualized: return +2.9%, volatility 4.3% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.02, excess kurtosis +0.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.83, max 2.82, latest 1.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.92%; worst month: -3.62%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.43
- Sideways: S=0.40
- Bear: S=-2.16

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_sppe, 5))` S=0.45, F=0.21, INFERIOR
Direction gap: -0.02 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_sppe)`: S=-0.64, F=-0.31, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_sppe / close)`: S=-0.67, F=-0.32, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_sppe, 5))`: S=0.45, F=0.21, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_sppe / close)` | TOP3000 | 0.66 | 0.32 | 9.7% | 60% | bull-only |
| `rank(fnd6_sppe)` | TOP3000 | 0.63 | 0.31 | 11.2% | 60% | bull-only |
| `rank(fnd6_sppe)` | TOP1000 | 0.26 | 0.10 | 8.9% | 20% | bull-only |
| `rank(fnd6_sppe / close)` | TOP1000 | 0.27 | 0.10 | 8.3% | 20% | bull-only |
| `rank(ts_delta(fnd6_sppe, 5))` | TOP1000 | 0.23 | 0.09 | 38.4% | 60% | mixed |
| `rank(fnd6_sppe / close)` | TOP500 | 0.18 | 0.06 | 12.8% | 20% | bull-only |
| `rank(fnd6_sppe)` | TOP500 | 0.17 | 0.05 | 12.3% | 20% | bull-only |
| `rank(fnd6_sppe)` | TOP200 | 0.12 | 0.05 | 20.0% | 60% | mixed |
| `rank(fnd6_sppe / close)` | TOP200 | 0.11 | 0.04 | 21.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_ivaeq: 0.735 (strongly positively correlated)
- fnd6_fatb: 0.732 (strongly positively correlated)
- fnd6_newa2v1300_txp: 0.727 (strongly positively correlated)
- est_ebit: 0.716 (strongly positively correlated)
- est_ebitda: 0.714 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
