---
field: fnd6_newa1v1300_gdwl
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 0.72
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.1545
ann_vol: 0.128
hit_rate: 0.5174
rolling_sharpe_min: -1.136
rolling_sharpe_max: 2.443
negated_best_sharpe: 0.4
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.32
---
# fnd6_newa1v1300_gdwl (fundamental6)

*Goodwill*

## Signal Profile
- `rank(fnd6_newa1v1300_gdwl)`: S=0.31, F=0.16, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_gdwl / close)`: S=0.45, F=0.24, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_gdwl, 5))`: S=0.79, F=0.42, T=34.8%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_gdwl)`: S=-0.07, F=-0.02, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_gdwl, 5))`: S=0.40, F=0.20, T=32.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_gdwl, 22)`: S=-0.17, F=-0.07, T=23.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_gdwl, 10)`: S=-0.08, F=-0.02, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_gdwl, 22))`: S=0.72, F=0.43, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_gdwl)`: S=0.29, F=0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_gdwl / close)`: S=0.23, F=0.11, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.78, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.05 (negative), ret=-0.6%
  - 2020: S=0.49 (weak), ret=+5.9%
  - 2021: S=1.41 (moderate), ret=+17.1%
  - 2022: S=1.09 (moderate), ret=+17.0%
  - 2023: S=0.91 (moderate), ret=+9.4%

## Risk & Drawdown
- Max drawdown: 15.45% over 707 days (recovered)
- Annualized: return +10.0%, volatility 12.8% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.50, excess kurtosis +5.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 2.44, latest 0.82

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.31%; worst month: -5.83%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.09
- Sideways: S=-0.44
- Bear: S=1.76

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_gdwl, 5))` S=0.40, F=0.20, INFERIOR
Direction gap: -0.32 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_gdwl)`: S=0.29, F=0.17, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_gdwl / close)`: S=0.23, F=0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_gdwl, 5))`: S=0.40, F=0.20, T=32.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_gdwl, 5))` | TOP1000 | 0.78 | 0.42 | 15.4% | 80% | all-weather |
| `rank(fnd6_newa1v1300_gdwl / close)` | TOP3000 | 0.45 | 0.24 | 15.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_gdwl, 5))` | TOP500 | 0.43 | 0.20 | 31.6% | 80% | all-weather |
| `rank(fnd6_newa1v1300_gdwl)` | TOP3000 | 0.30 | 0.16 | 28.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_gdwl / close)` | TOP1000 | 0.19 | 0.08 | 17.7% | 60% | bull-only |
| `rank(fnd6_newa1v1300_gdwl)` | TOP1000 | 0.07 | 0.02 | 31.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_aqc: 0.180 (weakly positively correlated)
- fnd6_dlcch: 0.160 (weakly positively correlated)
- fnd6_citotal: -0.158 (weakly negatively correlated)
- fnd6_txpd: 0.158 (weakly positively correlated)
- fnd6_invrm: 0.154 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
