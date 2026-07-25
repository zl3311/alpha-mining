---
field: fnd6_optrfr
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.71
best_fitness: 0.68
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.2264
ann_vol: 0.2375
hit_rate: 0.4761
rolling_sharpe_min: -1.482
rolling_sharpe_max: 1.87
negated_best_sharpe: 0.36
negated_best_template: neg_rank_level
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.35
---
# fnd6_optrfr (fundamental6)

*Risk-Free Rate - Assumption (%)*

## Signal Profile
- `rank(fnd6_optrfr)`: S=-0.13, F=-0.03, T=3.7%, INFERIOR (TOP500)
- `rank(fnd6_optrfr / close)`: S=0.38, F=0.23, T=3.9%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_optrfr, 5))`: S=0.71, F=0.68, T=18.6%, INFERIOR (TOP200)
- `-rank(fnd6_optrfr)`: S=0.32, F=0.12, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optrfr, 5))`: S=0.03, F=0.00, T=38.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_optrfr, 63)`: S=0.29, F=0.20, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optrfr, 10)`: S=-0.06, F=-0.01, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optrfr, 22))`: S=0.07, F=0.02, T=20.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optrfr)`: S=0.36, F=0.13, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optrfr / close)`: S=0.12, F=0.05, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.70, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.58 (negative), ret=-5.9%
  - 2020: S=0.47 (weak), ret=+7.5%
  - 2021: S=1.24 (moderate), ret=+38.9%
  - 2022: S=0.92 (moderate), ret=+29.6%
  - 2023: S=0.64 (moderate), ret=+11.9%

## Risk & Drawdown
- Max drawdown: 22.64% over 152 days (recovered)
- Annualized: return +16.7%, volatility 23.8% (fraction of booksize)
- Hit rate: 47.6% positive days
- Tail shape: skew +2.01, excess kurtosis +32.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.48, max 1.87, latest 0.65

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +24.91%; worst month: -7.71%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.72
- Sideways: S=0.78
- Bear: S=0.66

## Negated Direction
Best negated: `rank(-1 * fnd6_optrfr)` S=0.36, F=0.13, INFERIOR
Direction gap: -0.35 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_optrfr)`: S=0.36, F=0.13, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optrfr / close)`: S=0.12, F=0.05, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optrfr, 5))`: S=0.03, F=0.00, T=38.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_optrfr, 5))` | TOP200 | 0.70 | 0.68 | 22.6% | 80% | all-weather |
| `rank(ts_delta(fnd6_optrfr, 5))` | TOP500 | 0.67 | 0.48 | 25.0% | 80% | all-weather |
| `rank(fnd6_optrfr / close)` | TOP200 | 0.37 | 0.23 | 27.9% | 60% | mixed |
| `rank(fnd6_optrfr / close)` | TOP500 | 0.33 | 0.17 | 27.1% | 60% | mixed |
| `rank(ts_delta(fnd6_optrfr, 5))` | TOP1000 | 0.29 | 0.13 | 56.0% | 80% | bull-only |
| `rank(fnd6_optrfr / close)` | TOP1000 | 0.16 | 0.06 | 29.0% | 60% | bear-only |
| `rank(ts_delta(fnd6_optrfr, 5))` | TOP3000 | 0.04 | 0.02 | 50.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_tfvl: 0.310 (weakly positively correlated)
- fnd6_txr: 0.271 (weakly positively correlated)
- fnd6_newa1v1300_epspi: -0.245 (weakly negatively correlated)
- fnd6_newa1v1300_epspx: -0.241 (weakly negatively correlated)
- fnd6_newa1v1300_epsfi: -0.239 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
