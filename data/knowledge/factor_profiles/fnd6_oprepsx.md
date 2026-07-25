---
field: fnd6_oprepsx
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
max_drawdown: 0.2662
ann_vol: 0.119
hit_rate: 0.4988
rolling_sharpe_min: -2.467
rolling_sharpe_max: 2.352
negated_best_sharpe: 0.41
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.01
---
# fnd6_oprepsx (fundamental6)

*Earnings Per Share - Diluted - from Operations*

## Signal Profile
- `rank(fnd6_oprepsx)`: S=0.17, F=0.07, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_oprepsx / close)`: S=0.42, F=0.27, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_oprepsx, 5))`: S=0.43, F=0.21, T=34.8%, INFERIOR (TOP200)
- `-rank(fnd6_oprepsx)`: S=-0.12, F=-0.04, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_oprepsx, 5))`: S=-0.41, F=-0.20, T=34.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_oprepsx, 22)`: S=0.45, F=0.24, T=30.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_oprepsx, 10)`: S=0.04, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_oprepsx, 22))`: S=0.28, F=0.11, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_oprepsx)`: S=0.24, F=0.13, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_oprepsx / close)`: S=0.41, F=0.31, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.01 (weak), ret=+0.0%
  - 2020: S=-1.38 (negative), ret=-11.9%
  - 2021: S=1.12 (moderate), ret=+15.7%
  - 2022: S=1.23 (moderate), ret=+21.2%
  - 2023: S=-0.12 (negative), ret=-1.2%

## Risk & Drawdown
- Max drawdown: 26.62% over 768 days (recovered)
- Annualized: return +4.9%, volatility 11.9% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.09, excess kurtosis +1.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.47, max 2.35, latest -0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +8.11%; worst month: -6.28%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.87
- Sideways: S=0.33
- Bear: S=-2.90

## Negated Direction
Best negated: `rank(-1 * fnd6_oprepsx / close)` S=0.41, F=0.31, INFERIOR
Direction gap: -0.01 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_oprepsx)`: S=0.24, F=0.13, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_oprepsx / close)`: S=0.41, F=0.31, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_oprepsx, 5))`: S=-0.41, F=-0.20, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_oprepsx / close)` | TOP3000 | 0.41 | 0.27 | 26.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_oprepsx, 5))` | TOP200 | 0.43 | 0.21 | 51.1% | 80% | mixed |
| `rank(ts_delta(fnd6_oprepsx, 5))` | TOP3000 | 0.53 | 0.19 | 9.3% | 100% | mixed |
| `rank(ts_delta(fnd6_oprepsx, 5))` | TOP1000 | 0.42 | 0.15 | 16.0% | 60% | all-weather |
| `rank(fnd6_oprepsx / close)` | TOP1000 | 0.24 | 0.14 | 27.5% | 60% | bull-only |
| `rank(fnd6_oprepsx)` | TOP3000 | 0.15 | 0.07 | 44.2% | 60% | bull-only |
| `rank(fnd6_oprepsx)` | TOP1000 | 0.11 | 0.04 | 40.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_opeps: 1.000 (strongly positively correlated)
- fnd6_mfma2_opeps: 0.999 (strongly positively correlated)
- anl4_af_eps_value: 0.977 (strongly positively correlated)
- earnings_per_share_reported: 0.972 (strongly positively correlated)
- fnd6_cptnewqv1300_oeps12: 0.965 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
