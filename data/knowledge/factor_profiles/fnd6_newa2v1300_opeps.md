---
field: fnd6_newa2v1300_opeps
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 0.41
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.2658
ann_vol: 0.1176
hit_rate: 0.502
rolling_sharpe_min: -2.47
rolling_sharpe_max: 2.375
negated_best_sharpe: 0.41
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: 0.0
---
# fnd6_newa2v1300_opeps (fundamental6)

*Earnings Per Share from Operations*

## Signal Profile
- `rank(fnd6_newa2v1300_opeps)`: S=0.16, F=0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_opeps / close)`: S=0.41, F=0.26, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_opeps, 5))`: S=0.56, F=0.21, T=36.3%, INFERIOR (TOP3000)
- `-rank(fnd6_newa2v1300_opeps)`: S=-0.11, F=-0.04, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_opeps, 5))`: S=-0.21, F=-0.07, T=34.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_opeps, 22)`: S=0.38, F=0.19, T=30.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_opeps, 10)`: S=0.04, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_opeps, 22))`: S=0.25, F=0.09, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_opeps)`: S=0.23, F=0.12, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_opeps / close)`: S=0.41, F=0.31, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.01 (weak), ret=+0.1%
  - 2020: S=-1.39 (negative), ret=-11.9%
  - 2021: S=1.13 (moderate), ret=+15.8%
  - 2022: S=1.22 (moderate), ret=+20.6%
  - 2023: S=-0.17 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 26.58% over 783 days (recovered)
- Annualized: return +4.7%, volatility 11.8% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.10, excess kurtosis +1.78

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.47, max 2.38, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.06%; worst month: -6.24%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.86
- Sideways: S=0.33
- Bear: S=-2.91

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_opeps / close)` S=0.41, F=0.31, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_opeps)`: S=0.23, F=0.12, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_opeps / close)`: S=0.41, F=0.31, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_opeps, 5))`: S=-0.21, F=-0.07, T=34.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa2v1300_opeps / close)` | TOP3000 | 0.40 | 0.26 | 26.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_opeps, 5))` | TOP3000 | 0.57 | 0.21 | 9.3% | 80% | mixed |
| `rank(fnd6_newa2v1300_opeps / close)` | TOP1000 | 0.22 | 0.12 | 27.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_opeps, 5))` | TOP1000 | 0.36 | 0.11 | 16.5% | 60% | all-weather |
| `rank(ts_delta(fnd6_newa2v1300_opeps, 5))` | TOP200 | 0.22 | 0.08 | 51.6% | 60% | mixed |
| `rank(fnd6_newa2v1300_opeps)` | TOP3000 | 0.15 | 0.06 | 44.2% | 60% | bull-only |
| `rank(fnd6_newa2v1300_opeps)` | TOP1000 | 0.10 | 0.04 | 40.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfma2_opeps: 1.000 (strongly positively correlated)
- fnd6_oprepsx: 1.000 (strongly positively correlated)
- anl4_af_eps_value: 0.978 (strongly positively correlated)
- earnings_per_share_reported: 0.971 (strongly positively correlated)
- fnd6_cptnewqv1300_oeps12: 0.964 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
