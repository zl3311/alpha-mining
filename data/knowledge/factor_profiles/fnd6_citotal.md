---
field: fnd6_citotal
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.52
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 2
max_drawdown: 0.2722
ann_vol: 0.2149
hit_rate: 0.4729
rolling_sharpe_min: -1.195
rolling_sharpe_max: 1.293
negated_best_sharpe: 0.52
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.35
---
# fnd6_citotal (fundamental6)

*Comprehensive Income - Parent*

## Signal Profile
- `rank(fnd6_citotal)`: S=0.01, F=0.00, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_citotal / close)`: S=0.11, F=0.03, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_citotal, 5))`: S=0.17, F=0.06, T=29.2%, INFERIOR (TOP200)
- `-rank(fnd6_citotal)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_citotal, 5))`: S=0.52, F=0.25, T=40.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_citotal, 63)`: S=-0.33, F=-0.17, T=20.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_citotal, 10)`: S=0.12, F=0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_citotal, 22))`: S=-0.40, F=-0.19, T=19.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_citotal)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_citotal / close)`: S=-0.02, F=0.00, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.17, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.12 (moderate), ret=+14.0%
  - 2020: S=0.19 (weak), ret=+2.8%
  - 2021: S=0.41 (weak), ret=+10.9%
  - 2022: S=-0.14 (negative), ret=-4.4%
  - 2023: S=-0.34 (negative), ret=-5.3%

## Risk & Drawdown
- Max drawdown: 27.22% over 551 days (recovered)
- Annualized: return +3.7%, volatility 21.5% (fraction of booksize)
- Hit rate: 47.3% positive days
- Tail shape: skew -1.06, excess kurtosis +22.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.20, max 1.29, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +22.78%; worst month: -15.09%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.84
- Sideways: S=0.94
- Bear: S=0.71

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_citotal, 5))` S=0.52, F=0.25, INFERIOR
Direction gap: +0.35 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_citotal)`: S=0.05, F=0.01, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_citotal / close)`: S=-0.02, F=0.00, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_citotal, 5))`: S=0.52, F=0.25, T=40.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_citotal, 5))` | TOP200 | 0.17 | 0.06 | 27.2% | 60% | bear-only |
| `rank(fnd6_citotal / close)` | TOP3000 | 0.10 | 0.03 | 35.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cibegni: 0.878 (strongly positively correlated)
- fnd6_newa1v1300_ibc: 0.621 (moderately positively correlated)
- fnd6_newa1v1300_epsfi: 0.557 (moderately positively correlated)
- fnd6_newa1v1300_epsfx: 0.556 (moderately positively correlated)
- fnd6_newa1v1300_epspi: 0.550 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
