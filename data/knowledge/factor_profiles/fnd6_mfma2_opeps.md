---
field: fnd6_mfma2_opeps
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
max_drawdown: 0.2643
ann_vol: 0.1173
hit_rate: 0.502
rolling_sharpe_min: -2.481
rolling_sharpe_max: 2.362
negated_best_sharpe: 0.41
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: 0.0
---
# fnd6_mfma2_opeps (fundamental6)

*Earnings Per Share from Operations*

## Signal Profile
- `rank(fnd6_mfma2_opeps)`: S=0.16, F=0.06, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_mfma2_opeps / close)`: S=0.41, F=0.25, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mfma2_opeps, 5))`: S=0.56, F=0.21, T=36.3%, INFERIOR (TOP3000)
- `-rank(fnd6_mfma2_opeps)`: S=-0.10, F=-0.03, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma2_opeps, 5))`: S=-0.23, F=-0.08, T=35.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_mfma2_opeps, 22)`: S=0.38, F=0.19, T=30.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma2_opeps, 10)`: S=0.03, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma2_opeps, 22))`: S=0.24, F=0.09, T=14.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_opeps)`: S=0.21, F=0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_opeps / close)`: S=0.41, F=0.31, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.40, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.12 (weak), ret=+0.5%
  - 2020: S=-1.40 (negative), ret=-11.9%
  - 2021: S=1.12 (moderate), ret=+15.6%
  - 2022: S=1.19 (moderate), ret=+20.2%
  - 2023: S=-0.16 (negative), ret=-1.6%

## Risk & Drawdown
- Max drawdown: 26.43% over 783 days (recovered)
- Annualized: return +4.7%, volatility 11.7% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.10, excess kurtosis +1.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.48, max 2.36, latest -0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.98%; worst month: -6.23%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.85
- Sideways: S=0.37
- Bear: S=-2.93

## Negated Direction
Best negated: `rank(-1 * fnd6_mfma2_opeps / close)` S=0.41, F=0.31, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_mfma2_opeps)`: S=0.21, F=0.10, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma2_opeps / close)`: S=0.41, F=0.31, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma2_opeps, 5))`: S=-0.23, F=-0.08, T=35.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfma2_opeps / close)` | TOP3000 | 0.40 | 0.25 | 26.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma2_opeps, 5))` | TOP3000 | 0.57 | 0.21 | 8.9% | 80% | mixed |
| `rank(ts_delta(fnd6_mfma2_opeps, 5))` | TOP1000 | 0.38 | 0.12 | 16.4% | 60% | all-weather |
| `rank(fnd6_mfma2_opeps / close)` | TOP1000 | 0.20 | 0.11 | 27.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_mfma2_opeps, 5))` | TOP200 | 0.26 | 0.10 | 49.2% | 60% | mixed |
| `rank(fnd6_mfma2_opeps)` | TOP3000 | 0.15 | 0.06 | 44.1% | 60% | bull-only |
| `rank(fnd6_mfma2_opeps)` | TOP1000 | 0.09 | 0.03 | 40.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_opeps: 1.000 (strongly positively correlated)
- fnd6_oprepsx: 0.999 (strongly positively correlated)
- anl4_af_eps_value: 0.977 (strongly positively correlated)
- earnings_per_share_reported: 0.972 (strongly positively correlated)
- fnd6_cptnewqv1300_oeps12: 0.964 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
