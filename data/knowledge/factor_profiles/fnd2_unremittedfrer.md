---
field: fnd2_unremittedfrer
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.69
best_fitness: 0.68
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1494
ann_vol: 0.1432
hit_rate: 0.4915
rolling_sharpe_min: -0.718
rolling_sharpe_max: 1.745
negated_best_sharpe: 0.72
negated_best_template: neg_rank_level
negated_best_fitness: 0.47
n_negated_sims: 10
direction_gap: 0.03
---
# fnd2_unremittedfrer (fundamental2)

*Unremitted Foreign Earnings*

## Signal Profile
- `rank(fnd2_unremittedfrer)`: S=-0.25, F=-0.09, T=0.6%, INFERIOR (TOP3000)
- `rank(fnd2_unremittedfrer / close)`: S=0.09, F=0.02, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_unremittedfrer, 5))`: S=0.66, F=0.36, T=31.4%, INFERIOR (TOP1000)
- `-rank(fnd2_unremittedfrer)`: S=0.53, F=0.27, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unremittedfrer, 5))`: S=-0.06, F=-0.01, T=29.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_unremittedfrer, 63)`: S=0.69, F=0.68, T=13.4%, INFERIOR (TOP3000)
- `ts_mean(fnd2_unremittedfrer, 10)`: S=-0.38, F=-0.18, T=0.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_unremittedfrer, 22))`: S=-0.19, F=-0.07, T=16.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unremittedfrer)`: S=0.72, F=0.47, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unremittedfrer / close)`: S=0.66, F=0.41, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.64, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.83 (moderate), ret=+13.7%
  - 2020: S=0.22 (weak), ret=+2.9%
  - 2021: S=0.41 (weak), ret=+5.4%
  - 2022: S=0.46 (weak), ret=+6.6%
  - 2023: S=1.32 (moderate), ret=+16.6%

## Risk & Drawdown
- Max drawdown: 14.94% over 727 days (recovered)
- Annualized: return +9.2%, volatility 14.3% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.81, excess kurtosis +11.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.72, max 1.75, latest 1.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +9.25%; worst month: -10.36%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.07
- Sideways: S=0.54
- Bear: S=0.22

## Negated Direction
Best negated: `rank(-1 * fnd2_unremittedfrer)` S=0.72, F=0.47, INFERIOR
Direction gap: +0.03 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_unremittedfrer)`: S=0.72, F=0.47, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unremittedfrer / close)`: S=0.66, F=0.41, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unremittedfrer, 5))`: S=-0.06, F=-0.01, T=29.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_unremittedfrer, 5))` | TOP1000 | 0.64 | 0.36 | 14.9% | 100% | mixed |
| `rank(ts_delta(fnd2_unremittedfrer, 5))` | TOP3000 | 0.56 | 0.29 | 17.5% | 60% | mixed |
| `rank(ts_delta(fnd2_unremittedfrer, 5))` | TOP200 | 0.15 | 0.05 | 22.8% | 20% | bull-only |
| `rank(fnd2_unremittedfrer / close)` | TOP3000 | 0.07 | 0.02 | 8.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_flintasamt1expyfour: 0.139 (weakly positively correlated)
- fnd2_currfedtxexp: 0.127 (weakly positively correlated)
- fn_payments_for_repurchase_of_common_stock_a: 0.117 (weakly positively correlated)
- pcr_oi_30: -0.107 (weakly negatively correlated)
- fnd6_newa1v1300_dcom: -0.103 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
