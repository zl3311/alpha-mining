---
field: fnd6_newa2v1300_mii
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.52
best_fitness: 0.28
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1071
ann_vol: 0.0699
hit_rate: 0.5134
rolling_sharpe_min: -1.418
rolling_sharpe_max: 2.067
negated_best_sharpe: 0.29
negated_best_template: rank_neg_delta
negated_best_fitness: 0.14
n_negated_sims: 10
direction_gap: -0.23
---
# fnd6_newa2v1300_mii (fundamental6)

*Noncontrolling Interest (Income Account)*

## Signal Profile
- `rank(fnd6_newa2v1300_mii)`: S=0.52, F=0.28, T=2.1%, INFERIOR (TOP200)
- `rank(fnd6_newa2v1300_mii / close)`: S=0.52, F=0.28, T=2.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa2v1300_mii, 5))`: S=0.47, F=0.22, T=34.0%, INFERIOR (TOP3000)
- `-rank(fnd6_newa2v1300_mii)`: S=0.13, F=0.03, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_mii, 5))`: S=0.29, F=0.14, T=24.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_mii, 22)`: S=0.00, F=0.00, T=20.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_mii, 10)`: S=-0.47, F=-0.23, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_mii, 22))`: S=-0.37, F=-0.19, T=15.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_mii)`: S=-0.52, F=-0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_mii / close)`: S=-0.52, F=-0.28, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.51, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.58 (moderate), ret=+2.9%
  - 2020: S=0.44 (weak), ret=+2.6%
  - 2021: S=0.66 (moderate), ret=+6.5%
  - 2022: S=0.63 (moderate), ret=+4.4%
  - 2023: S=0.21 (weak), ret=+1.2%

## Risk & Drawdown
- Max drawdown: 10.71% over 555 days (not yet recovered, ongoing at window end)
- Annualized: return +3.6%, volatility 7.0% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.14, excess kurtosis +1.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.42, max 2.07, latest 0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +3.86%; worst month: -4.15%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.43
- Sideways: S=0.70
- Bear: S=-0.75

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa2v1300_mii, 5))` S=0.29, F=0.14, INFERIOR
Direction gap: -0.23 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_mii)`: S=-0.52, F=-0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_mii / close)`: S=-0.52, F=-0.28, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_mii, 5))`: S=0.29, F=0.14, T=24.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_mii / close)` | TOP200 | 0.51 | 0.28 | 10.7% | 100% | bull-only |
| `rank(fnd6_newa2v1300_mii)` | TOP200 | 0.51 | 0.28 | 10.5% | 100% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_mii, 5))` | TOP3000 | 0.46 | 0.22 | 31.5% | 60% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_mii, 5))` | TOP1000 | 0.39 | 0.17 | 27.4% | 80% | weak |
| `rank(fnd6_newa2v1300_mii / close)` | TOP3000 | 0.35 | 0.13 | 15.1% | 80% | bull-only |
| `rank(fnd6_newa2v1300_mii)` | TOP3000 | 0.27 | 0.09 | 16.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_miiq: 0.629 (moderately positively correlated)
- fnd6_newqv1300_cimiiq: 0.574 (moderately positively correlated)
- fnd6_newa1v1300_dv: 0.407 (moderately positively correlated)
- cashflow_dividends: 0.406 (moderately positively correlated)
- fnd6_loxdr: 0.397 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
