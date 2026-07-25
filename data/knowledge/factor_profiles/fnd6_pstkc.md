---
field: fnd6_pstkc
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.75
best_fitness: 0.68
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.2554
ann_vol: 0.137
hit_rate: 0.4842
rolling_sharpe_min: -1.097
rolling_sharpe_max: 2.822
negated_best_sharpe: 0.6
negated_best_template: neg_rank_level
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: -0.15
---
# fnd6_pstkc (fundamental6)

*Preferred Stock - Convertible*

## Signal Profile
- `rank(fnd6_pstkc)`: S=0.04, F=0.01, T=3.7%, INFERIOR (TOP200)
- `rank(fnd6_pstkc / close)`: S=0.04, F=0.01, T=3.7%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_pstkc, 5))`: S=0.75, F=0.68, T=8.9%, INFERIOR (TOP500)
- `-rank(fnd6_pstkc)`: S=0.04, F=0.01, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pstkc, 5))`: S=0.27, F=0.14, T=20.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_pstkc, 63)`: S=-0.12, F=-0.08, T=5.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_pstkc, 10)`: S=-0.46, F=-0.28, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_pstkc, 22))`: S=-0.39, F=-0.32, T=13.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pstkc)`: S=0.60, F=0.36, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pstkc / close)`: S=0.59, F=0.35, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 16F/16P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.74, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.01 (weak), ret=+0.1%
  - 2020: S=0.03 (weak), ret=+0.4%
  - 2021: S=1.06 (moderate), ret=+16.3%
  - 2022: S=2.03 (strong), ret=+31.2%
  - 2023: S=0.43 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 25.54% over 500 days (recovered)
- Annualized: return +10.2%, volatility 13.7% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew -1.64, excess kurtosis +47.65

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.10, max 2.82, latest 0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +16.61%; worst month: -10.90%
Positive months: 62%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.43
- Sideways: S=0.94
- Bear: S=-0.94

## Negated Direction
Best negated: `rank(-1 * fnd6_pstkc)` S=0.60, F=0.36, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_pstkc)`: S=0.60, F=0.36, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_pstkc / close)`: S=0.59, F=0.35, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_pstkc, 5))`: S=0.27, F=0.14, T=20.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_pstkc, 5))` | TOP500 | 0.74 | 0.68 | 25.5% | 100% | bull-only |
| `rank(ts_delta(fnd6_pstkc, 5))` | TOP200 | 0.55 | 0.38 | 22.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_pstkc, 5))` | TOP3000 | 0.17 | 0.07 | 36.9% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd6_dvpa: 0.455 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.305 (weakly positively correlated)
- shareholders_equity_min_guidance: 0.305 (weakly positively correlated)
- min_total_assets_guidance: 0.305 (weakly positively correlated)
- max_free_cashflow_per_share_guidance: 0.305 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
