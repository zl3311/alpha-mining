---
field: fnd6_mfma2_txach
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.75
best_fitness: 0.94
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.4241
ann_vol: 0.2467
hit_rate: 0.4923
rolling_sharpe_min: -0.906
rolling_sharpe_max: 1.878
negated_best_sharpe: 0.9
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.66
n_negated_sims: 10
direction_gap: 0.15
---
# fnd6_mfma2_txach (fundamental6)

*Income Taxes - Accrued - Increase/(Decrease)*

## Signal Profile
- `rank(fnd6_mfma2_txach)`: S=-0.47, F=-0.19, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_mfma2_txach / close)`: S=-0.48, F=-0.20, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mfma2_txach, 5))`: S=0.27, F=0.14, T=26.2%, INFERIOR (TOP500)
- `-rank(fnd6_mfma2_txach)`: S=0.63, F=0.32, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma2_txach, 5))`: S=-0.17, F=-0.07, T=25.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mfma2_txach, 63)`: S=0.75, F=0.94, T=11.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma2_txach, 10)`: S=-0.66, F=-0.46, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma2_txach, 22))`: S=-0.21, F=-0.10, T=16.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_txach)`: S=0.87, F=0.62, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_txach / close)`: S=0.90, F=0.66, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 25F/4P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.28, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.43 (negative), ret=-10.0%
  - 2020: S=1.35 (moderate), ret=+29.9%
  - 2021: S=0.56 (moderate), ret=+16.8%
  - 2022: S=-0.06 (negative), ret=-1.6%
  - 2023: S=-0.11 (negative), ret=-1.8%

## Risk & Drawdown
- Max drawdown: 42.41% over 352 days (recovered)
- Annualized: return +6.8%, volatility 24.7% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +1.94, excess kurtosis +23.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.91, max 1.88, latest -0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +18.02%; worst month: -15.64%
Positive months: 55%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.17
- Sideways: S=0.23
- Bear: S=0.45

## Negated Direction
Best negated: `rank(-1 * fnd6_mfma2_txach / close)` S=0.90, F=0.66, INFERIOR
Direction gap: +0.15 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_mfma2_txach)`: S=0.87, F=0.62, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_txach / close)`: S=0.90, F=0.66, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma2_txach, 5))`: S=-0.17, F=-0.07, T=25.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_mfma2_txach, 5))` | TOP500 | 0.28 | 0.14 | 42.4% | 40% | weak |
| `rank(ts_delta(fnd6_mfma2_txach, 5))` | TOP200 | 0.17 | 0.09 | 39.7% | 40% | weak |
| `rank(ts_delta(fnd6_mfma2_txach, 5))` | TOP3000 | 0.12 | 0.03 | 53.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_txach: 1.000 (strongly positively correlated)
- fnd6_txr: 0.221 (weakly positively correlated)
- fnd6_lqpl1: 0.180 (weakly positively correlated)
- fnd6_txdfo: 0.180 (weakly positively correlated)
- fnd6_optrfr: 0.178 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
