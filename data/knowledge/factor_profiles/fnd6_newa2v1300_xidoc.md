---
field: fnd6_newa2v1300_xidoc
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.87
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.1725
ann_vol: 0.1833
hit_rate: 0.5158
rolling_sharpe_min: -0.52
rolling_sharpe_max: 2.28
negated_best_sharpe: 0.52
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.35
---
# fnd6_newa2v1300_xidoc (fundamental6)

*Extraordinary Items and Discontinued Operations (Cash Flow)*

## Signal Profile
- `rank(fnd6_newa2v1300_xidoc)`: S=-0.25, F=-0.10, T=3.1%, INFERIOR (TOP200)
- `rank(fnd6_newa2v1300_xidoc / close)`: S=-0.26, F=-0.11, T=3.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newa2v1300_xidoc, 5))`: S=0.77, F=0.54, T=29.2%, INFERIOR (TOP3000)
- `-rank(fnd6_newa2v1300_xidoc)`: S=0.52, F=0.22, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_xidoc, 5))`: S=0.04, F=0.01, T=24.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_xidoc, 22)`: S=0.87, F=0.82, T=6.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_xidoc, 10)`: S=-0.14, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_xidoc, 22))`: S=-0.14, F=-0.06, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xidoc)`: S=0.52, F=0.22, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xidoc / close)`: S=0.52, F=0.23, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.14 (weak), ret=+2.6%
  - 2020: S=0.91 (moderate), ret=+18.7%
  - 2021: S=1.02 (moderate), ret=+23.3%
  - 2022: S=0.94 (moderate), ret=+13.3%
  - 2023: S=1.03 (moderate), ret=+10.9%

## Risk & Drawdown
- Max drawdown: 17.25% over 322 days (recovered)
- Annualized: return +14.0%, volatility 18.3% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.12, excess kurtosis +13.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.52, max 2.28, latest 0.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +21.13%; worst month: -8.91%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.88
- Sideways: S=-0.09
- Bear: S=0.51

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_xidoc / close)` S=0.52, F=0.23, INFERIOR
Direction gap: -0.35 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_xidoc)`: S=0.52, F=0.22, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_xidoc / close)`: S=0.52, F=0.23, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_xidoc, 5))`: S=0.04, F=0.01, T=24.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa2v1300_xidoc, 5))` | TOP500 | 0.64 | 0.54 | 33.8% | 80% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_xidoc, 5))` | TOP3000 | 0.77 | 0.54 | 17.2% | 100% | all-weather |
| `rank(ts_delta(fnd6_newa2v1300_xidoc, 5))` | TOP1000 | 0.20 | 0.09 | 44.5% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dcom: 0.134 (weakly positively correlated)
- fnd6_newa1v1300_fca: 0.128 (weakly positively correlated)
- fnd6_txr: 0.123 (weakly positively correlated)
- actual_dividend_value_quarterly: 0.115 (weakly positively correlated)
- fnd6_nopio: 0.112 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
