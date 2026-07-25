---
field: fnd6_lol2
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.67
best_fitness: 0.6
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.2064
ann_vol: 0.1562
hit_rate: 0.4826
rolling_sharpe_min: -1.292
rolling_sharpe_max: 3.459
negated_best_sharpe: 0.39
negated_best_template: neg_rank_level
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.28
---
# fnd6_lol2 (fundamental6)

*Liabilities Level 2 (Observable)*

## Signal Profile
- `rank(fnd6_lol2)`: S=0.55, F=0.30, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_lol2 / close)`: S=0.66, F=0.38, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_lol2, 5))`: S=0.75, F=0.51, T=25.5%, INFERIOR (TOP200)
- `-rank(fnd6_lol2)`: S=-0.16, F=-0.05, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lol2, 5))`: S=-0.15, F=-0.04, T=25.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_lol2, 22)`: S=0.67, F=0.60, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_lol2, 10)`: S=0.33, F=0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_lol2, 22))`: S=-0.60, F=-0.36, T=19.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lol2)`: S=0.39, F=0.24, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lol2 / close)`: S=0.37, F=0.22, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.41 (strong), ret=+30.7%
  - 2020: S=0.42 (weak), ret=+6.6%
  - 2021: S=1.26 (moderate), ret=+26.1%
  - 2022: S=0.90 (moderate), ret=+11.0%
  - 2023: S=-1.29 (negative), ret=-17.6%

## Risk & Drawdown
- Max drawdown: 20.64% over 359 days (recovered)
- Annualized: return +11.6%, volatility 15.6% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew -0.37, excess kurtosis +17.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 3.46, latest -1.29

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +10.86%; worst month: -9.47%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.09
- Sideways: S=0.76
- Bear: S=-0.79

## Negated Direction
Best negated: `rank(-1 * fnd6_lol2)` S=0.39, F=0.24, INFERIOR
Direction gap: -0.28 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_lol2)`: S=0.39, F=0.24, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lol2 / close)`: S=0.37, F=0.22, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lol2, 5))`: S=-0.15, F=-0.04, T=25.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_lol2, 5))` | TOP200 | 0.74 | 0.51 | 20.6% | 80% | bull-only |
| `rank(fnd6_lol2 / close)` | TOP3000 | 0.66 | 0.38 | 10.5% | 80% | bull-only |
| `rank(fnd6_lol2)` | TOP3000 | 0.55 | 0.30 | 16.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_lol2, 5))` | TOP3000 | 0.43 | 0.18 | 24.7% | 100% | mixed |
| `rank(fnd6_lol2 / close)` | TOP1000 | 0.22 | 0.08 | 17.6% | 20% | bull-only |
| `rank(fnd6_lol2)` | TOP1000 | 0.16 | 0.05 | 21.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_tfvl: 0.647 (moderately positively correlated)
- fnd6_dcvsub: 0.331 (weakly positively correlated)
- fnd6_newa1v1300_fca: 0.327 (weakly positively correlated)
- fnd6_rea: 0.264 (weakly positively correlated)
- fnd6_itcb: 0.203 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
