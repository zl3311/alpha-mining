---
field: fnd6_acqgdwl
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 1.17
best_fitness: 1.54
best_universe: TOP3000
grade: GOOD
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.3366
ann_vol: 0.2163
hit_rate: 0.447
rolling_sharpe_min: -1.166
rolling_sharpe_max: 2.412
negated_best_sharpe: 1.17
negated_best_template: rank_neg_delta
negated_best_fitness: 1.54
n_negated_sims: 10
direction_gap: 0.58
---
# fnd6_acqgdwl (fundamental6)

*Acquired Assets - Goodwill*

## Signal Profile
- `rank(fnd6_acqgdwl)`: S=0.28, F=0.10, T=2.6%, INFERIOR (TOP3000)
- `rank(fnd6_acqgdwl / close)`: S=-0.15, F=-0.04, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_acqgdwl, 5))`: S=0.50, F=0.43, T=14.8%, INFERIOR (TOP200)
- `-rank(fnd6_acqgdwl)`: S=0.62, F=0.39, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_acqgdwl, 5))`: S=1.17, F=1.54, T=14.7%, GOOD (TOP3000)
- `-ts_zscore(fnd6_acqgdwl, 63)`: S=0.59, F=0.60, T=11.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_acqgdwl, 10)`: S=-0.50, F=-0.30, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_acqgdwl, 22))`: S=-0.39, F=-0.28, T=21.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acqgdwl)`: S=0.62, F=0.50, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acqgdwl / close)`: S=1.02, F=1.05, T=4.5%, AVERAGE (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/12P
- LOW_FITNESS: 26F/6P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.48, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.24 (negative), ret=-2.4%
  - 2020: S=0.14 (weak), ret=+2.6%
  - 2021: S=1.11 (moderate), ret=+23.4%
  - 2022: S=-0.09 (negative), ret=-2.4%
  - 2023: S=1.21 (moderate), ret=+29.7%

## Risk & Drawdown
- Max drawdown: 33.66% over 502 days (recovered)
- Annualized: return +10.4%, volatility 21.6% (fraction of booksize)
- Hit rate: 44.7% positive days
- Tail shape: skew -0.30, excess kurtosis +5.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 2.41, latest 1.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +17.17%; worst month: -22.65%
Positive months: 60%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.91
- Sideways: S=0.28
- Bear: S=-0.75

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_acqgdwl, 5))` S=1.17, F=1.54, GOOD
Direction gap: +0.58 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_acqgdwl)`: S=0.62, F=0.50, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acqgdwl / close)`: S=1.02, F=1.05, T=4.5%, AVERAGE (TOP3000)
- `rank(-1 * ts_delta(fnd6_acqgdwl, 5))`: S=1.17, F=1.54, T=14.7%, GOOD (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_acqgdwl, 5))` | TOP200 | 0.48 | 0.43 | 33.7% | 60% | bull-only |
| `rank(fnd6_acqgdwl)` | TOP3000 | 0.28 | 0.10 | 16.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_acqintan: 0.752 (strongly positively correlated)
- pretax_income_reported: 0.216 (weakly positively correlated)
- anl4_cfi_median: -0.213 (weakly negatively correlated)
- free_cash_flow_total: 0.213 (weakly positively correlated)
- anl4_cfi_low: -0.212 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
