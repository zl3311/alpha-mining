---
field: fnd6_optca
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.77
best_fitness: 0.6
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 10
max_drawdown: 0.2185
ann_vol: 0.2223
hit_rate: 0.5134
rolling_sharpe_min: -0.198
rolling_sharpe_max: 2.076
negated_best_sharpe: 0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.75
---
# fnd6_optca (fundamental6)

*Options - Cancelled (-)*

## Signal Profile
- `rank(fnd6_optca)`: S=0.68, F=0.48, T=3.5%, INFERIOR (TOP200)
- `rank(fnd6_optca / close)`: S=0.57, F=0.38, T=3.7%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_optca, 5))`: S=0.77, F=0.60, T=28.4%, INFERIOR (TOP500)
- `-rank(fnd6_optca)`: S=-0.28, F=-0.10, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optca, 5))`: S=-0.09, F=-0.02, T=40.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optca, 22)`: S=0.59, F=0.59, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optca, 10)`: S=0.34, F=0.18, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optca, 22))`: S=0.08, F=0.02, T=20.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optca)`: S=-0.07, F=-0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optca / close)`: S=0.02, F=0.00, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.78, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.46 (weak), ret=+7.8%
  - 2020: S=1.02 (moderate), ret=+19.3%
  - 2021: S=0.64 (moderate), ret=+14.8%
  - 2022: S=0.70 (moderate), ret=+21.5%
  - 2023: S=1.31 (moderate), ret=+21.4%

## Risk & Drawdown
- Max drawdown: 21.85% over 28 days (recovered)
- Annualized: return +17.3%, volatility 22.2% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.64, excess kurtosis +16.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.20, max 2.08, latest 1.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +32.97%; worst month: -9.17%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.98
- Sideways: S=0.60
- Bear: S=0.72

## Negated Direction
Best negated: `rank(-1 * fnd6_optca / close)` S=0.02, F=0.00, INFERIOR
Direction gap: -0.75 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_optca)`: S=-0.07, F=-0.01, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optca / close)`: S=0.02, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optca, 5))`: S=-0.09, F=-0.02, T=40.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_optca, 5))` | TOP500 | 0.78 | 0.60 | 21.9% | 100% | all-weather |
| `rank(ts_delta(fnd6_optca, 5))` | TOP1000 | 0.83 | 0.56 | 27.7% | 100% | all-weather |
| `rank(fnd6_optca)` | TOP200 | 0.71 | 0.48 | 16.7% | 60% | mixed |
| `rank(fnd6_optca / close)` | TOP200 | 0.59 | 0.38 | 16.3% | 40% | mixed |
| `rank(fnd6_optca / close)` | TOP500 | 0.27 | 0.11 | 26.0% | 60% | bear-only |
| `rank(fnd6_optca)` | TOP500 | 0.29 | 0.11 | 22.8% | 60% | bear-only |
| `rank(fnd6_optca / close)` | TOP1000 | 0.26 | 0.10 | 21.9% | 60% | bear-only |
| `rank(fnd6_optca)` | TOP1000 | 0.29 | 0.10 | 15.7% | 60% | bear-only |
| `rank(ts_delta(fnd6_optca, 5))` | TOP200 | 0.15 | 0.07 | 38.7% | 60% | mixed |
| `rank(ts_delta(fnd6_optca, 5))` | TOP3000 | 0.12 | 0.03 | 32.2% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_cibegni: 0.324 (weakly positively correlated)
- fnd6_citotal: 0.321 (weakly positively correlated)
- fnd6_newa2v1300_re: 0.299 (weakly positively correlated)
- fnd6_newa2v1300_reuna: 0.299 (weakly positively correlated)
- fnd6_newa1v1300_ebit: 0.279 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
