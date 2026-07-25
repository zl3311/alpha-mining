---
field: fnd6_newa2v1300_txach
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.74
best_fitness: 0.92
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.4241
ann_vol: 0.2469
hit_rate: 0.4955
rolling_sharpe_min: -0.881
rolling_sharpe_max: 1.881
negated_best_sharpe: 0.88
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.64
n_negated_sims: 10
direction_gap: 0.14
---
# fnd6_newa2v1300_txach (fundamental6)

*Income Taxes - Accrued - Increase/(Decrease)*

## Signal Profile
- `rank(fnd6_newa2v1300_txach)`: S=-0.42, F=-0.16, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_txach / close)`: S=-0.44, F=-0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_txach, 5))`: S=0.27, F=0.14, T=26.3%, INFERIOR (TOP500)
- `-rank(fnd6_newa2v1300_txach)`: S=0.63, F=0.32, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_txach, 5))`: S=-0.16, F=-0.06, T=26.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa2v1300_txach, 63)`: S=0.74, F=0.92, T=11.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_txach, 10)`: S=-0.66, F=-0.46, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_txach, 22))`: S=-0.15, F=-0.06, T=17.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txach)`: S=0.84, F=0.58, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txach / close)`: S=0.88, F=0.64, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 25F/4P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.27, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.43 (negative), ret=-10.0%
  - 2020: S=1.35 (moderate), ret=+29.7%
  - 2021: S=0.53 (moderate), ret=+15.8%
  - 2022: S=-0.03 (negative), ret=-0.9%
  - 2023: S=-0.11 (negative), ret=-1.7%

## Risk & Drawdown
- Max drawdown: 42.41% over 352 days (recovered)
- Annualized: return +6.7%, volatility 24.7% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +1.93, excess kurtosis +23.24

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.88, max 1.88, latest -0.09

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +18.04%; worst month: -15.64%
Positive months: 57%

## Regime Profile
Regime profile: **weak**
- Bull: S=0.16
- Sideways: S=0.25
- Bear: S=0.43

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_txach / close)` S=0.88, F=0.64, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_txach)`: S=0.84, F=0.58, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_txach / close)`: S=0.88, F=0.64, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_txach, 5))`: S=-0.16, F=-0.06, T=26.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa2v1300_txach, 5))` | TOP500 | 0.27 | 0.14 | 42.4% | 40% | weak |
| `rank(ts_delta(fnd6_newa2v1300_txach, 5))` | TOP200 | 0.18 | 0.09 | 38.9% | 40% | weak |
| `rank(ts_delta(fnd6_newa2v1300_txach, 5))` | TOP3000 | 0.24 | 0.08 | 52.5% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_mfma2_txach: 1.000 (strongly positively correlated)
- fnd6_txr: 0.221 (weakly positively correlated)
- fnd6_lqpl1: 0.181 (weakly positively correlated)
- fnd6_txdfo: 0.181 (weakly positively correlated)
- fnd6_optrfr: 0.178 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
