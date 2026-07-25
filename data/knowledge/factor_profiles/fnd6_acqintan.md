---
field: fnd6_acqintan
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.61
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.4258
ann_vol: 0.2204
hit_rate: 0.4559
rolling_sharpe_min: -1.676
rolling_sharpe_max: 2.736
negated_best_sharpe: 0.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.19
n_negated_sims: 10
direction_gap: -0.27
---
# fnd6_acqintan (fundamental6)

*Acquired Assets - Intangibles*

## Signal Profile
- `rank(fnd6_acqintan)`: S=0.46, F=0.22, T=2.6%, INFERIOR (TOP3000)
- `rank(fnd6_acqintan / close)`: S=0.13, F=0.03, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_acqintan, 5))`: S=0.45, F=0.39, T=13.2%, INFERIOR (TOP200)
- `-rank(fnd6_acqintan)`: S=0.35, F=0.18, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_acqintan, 5))`: S=0.34, F=0.19, T=28.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_acqintan, 63)`: S=0.61, F=0.60, T=11.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_acqintan, 10)`: S=-0.17, F=-0.07, T=2.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_acqintan, 22))`: S=-0.50, F=-0.40, T=21.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acqintan)`: S=0.35, F=0.18, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acqintan / close)`: S=0.37, F=0.18, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.44, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.77 (moderate), ret=+6.7%
  - 2020: S=0.60 (moderate), ret=+9.9%
  - 2021: S=0.14 (weak), ret=+2.7%
  - 2022: S=0.03 (weak), ret=+0.9%
  - 2023: S=1.04 (moderate), ret=+27.4%

## Risk & Drawdown
- Max drawdown: 42.58% over 595 days (recovered)
- Annualized: return +9.7%, volatility 22.0% (fraction of booksize)
- Hit rate: 45.6% positive days
- Tail shape: skew -0.48, excess kurtosis +7.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.68, max 2.74, latest 0.98

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +21.85%; worst month: -25.35%
Positive months: 55%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.44
- Sideways: S=0.89
- Bear: S=-0.92

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_acqintan, 5))` S=0.34, F=0.19, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_acqintan)`: S=0.35, F=0.18, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acqintan / close)`: S=0.37, F=0.18, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_acqintan, 5))`: S=0.34, F=0.19, T=28.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_acqintan, 5))` | TOP200 | 0.44 | 0.39 | 42.6% | 100% | bull-only |
| `rank(fnd6_acqintan)` | TOP3000 | 0.45 | 0.22 | 11.0% | 60% | bull-only |
| `rank(fnd6_acqintan / close)` | TOP3000 | 0.13 | 0.03 | 13.9% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_acqgdwl: 0.752 (strongly positively correlated)
- parkinson_volatility_150: -0.353 (weakly negatively correlated)
- parkinson_volatility_180: -0.351 (weakly negatively correlated)
- historical_volatility_150: -0.351 (weakly negatively correlated)
- historical_volatility_180: -0.350 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
