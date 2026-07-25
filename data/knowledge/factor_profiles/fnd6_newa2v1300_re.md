---
field: fnd6_newa2v1300_re
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.74
best_fitness: 0.52
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 4
max_drawdown: 0.3088
ann_vol: 0.207
hit_rate: 0.4988
rolling_sharpe_min: -0.918
rolling_sharpe_max: 3.561
redundancy_cluster: 58
negated_best_sharpe: 0.5
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.35
n_negated_sims: 10
direction_gap: -0.24
---
# fnd6_newa2v1300_re (fundamental6)

*Retained Earnings*

## Signal Profile
- `rank(fnd6_newa2v1300_re)`: S=0.00, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_re / close)`: S=0.16, F=0.06, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_re, 5))`: S=0.74, F=0.52, T=31.0%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_re)`: S=0.03, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_re, 5))`: S=-0.76, F=-0.54, T=31.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_re, 22)`: S=0.13, F=0.04, T=28.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_re, 10)`: S=-0.06, F=-0.01, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_re, 22))`: S=0.51, F=0.28, T=15.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_re)`: S=0.44, F=0.29, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_re / close)`: S=0.50, F=0.35, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.73, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.77 (strong), ret=+35.6%
  - 2020: S=0.33 (weak), ret=+5.3%
  - 2021: S=0.86 (moderate), ret=+19.8%
  - 2022: S=0.64 (moderate), ret=+18.6%
  - 2023: S=-0.29 (negative), ret=-4.7%

## Risk & Drawdown
- Max drawdown: 30.88% over 545 days (recovered)
- Annualized: return +15.2%, volatility 20.7% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew -1.04, excess kurtosis +18.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.92, max 3.56, latest -0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +12.46%; worst month: -9.28%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.66
- Sideways: S=1.11
- Bear: S=0.52

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_re / close)` S=0.50, F=0.35, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_re)`: S=0.44, F=0.29, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_re / close)`: S=0.50, F=0.35, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_re, 5))`: S=-0.76, F=-0.54, T=31.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa2v1300_re, 5))` | TOP200 | 0.73 | 0.52 | 30.9% | 80% | all-weather |
| `rank(ts_delta(fnd6_newa2v1300_re, 5))` | TOP1000 | 0.70 | 0.36 | 21.5% | 80% | mixed |
| `rank(ts_delta(fnd6_newa2v1300_re, 5))` | TOP3000 | 0.42 | 0.14 | 27.9% | 80% | bull-only |
| `rank(fnd6_newa2v1300_re / close)` | TOP3000 | 0.16 | 0.06 | 35.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_reuna: 0.944 (strongly positively correlated)
- fnd6_newa1v1300_ibc: 0.565 (moderately positively correlated)
- fnd6_newa1v1300_epsfx: 0.545 (moderately positively correlated)
- fnd6_newa1v1300_epsfi: 0.544 (moderately positively correlated)
- fnd6_citotal: 0.542 (moderately positively correlated)

Redundancy cluster #58: 2 similar fields, mean |rho| 0.944 (representative: fnd6_newa2v1300_reuna). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
