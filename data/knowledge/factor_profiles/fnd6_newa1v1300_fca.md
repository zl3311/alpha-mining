---
field: fnd6_newa1v1300_fca
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.44
best_fitness: 0.34
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.4444
ann_vol: 0.2499
hit_rate: 0.5093
rolling_sharpe_min: -0.868
rolling_sharpe_max: 1.779
negated_best_sharpe: 0.48
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: 0.04
---
# fnd6_newa1v1300_fca (fundamental6)

*Foreign Exchange Income (Loss)*

## Signal Profile
- `rank(fnd6_newa1v1300_fca)`: S=0.10, F=0.02, T=2.5%, INFERIOR (TOP1000)
- `rank(fnd6_newa1v1300_fca / close)`: S=0.07, F=0.01, T=2.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newa1v1300_fca, 5))`: S=0.44, F=0.34, T=18.9%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_fca)`: S=-0.10, F=-0.02, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_fca, 5))`: S=0.48, F=0.31, T=25.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_fca, 63)`: S=-0.06, F=-0.02, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_fca, 10)`: S=-0.54, F=-0.39, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_fca, 22))`: S=0.18, F=0.07, T=20.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_fca)`: S=0.08, F=0.02, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_fca / close)`: S=0.30, F=0.13, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.43, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.96 (moderate), ret=+12.1%
  - 2020: S=-0.18 (negative), ret=-3.7%
  - 2021: S=1.37 (moderate), ret=+37.7%
  - 2022: S=-0.68 (negative), ret=-24.2%
  - 2023: S=1.54 (strong), ret=+31.0%

## Risk & Drawdown
- Max drawdown: 44.44% over 661 days (not yet recovered, ongoing at window end)
- Annualized: return +10.8%, volatility 25.0% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.68, excess kurtosis +19.30

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.87, max 1.78, latest 1.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +12.56%; worst month: -21.76%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.63
- Sideways: S=-0.10
- Bear: S=0.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_fca, 5))` S=0.48, F=0.31, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_fca)`: S=0.08, F=0.02, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_fca / close)`: S=0.30, F=0.13, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_fca, 5))`: S=0.48, F=0.31, T=25.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_fca, 5))` | TOP200 | 0.43 | 0.34 | 44.4% | 60% | all-weather |
| `rank(ts_delta(fnd6_newa1v1300_fca, 5))` | TOP3000 | 0.52 | 0.27 | 40.2% | 60% | mixed |
| `rank(ts_delta(fnd6_newa1v1300_fca, 5))` | TOP1000 | 0.31 | 0.13 | 58.3% | 60% | mixed |
| `rank(fnd6_newa1v1300_fca)` | TOP1000 | 0.09 | 0.02 | 22.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_tfvl: 0.439 (moderately positively correlated)
- fnd6_txndb: -0.406 (moderately negatively correlated)
- fnd6_lol2: 0.327 (weakly positively correlated)
- ebit: -0.290 (weakly negatively correlated)
- fnd6_cibegni: -0.290 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
