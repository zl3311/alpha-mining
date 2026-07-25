---
field: fnd6_lifr
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.78
best_fitness: 0.56
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.2282
ann_vol: 0.0871
hit_rate: 0.4785
rolling_sharpe_min: -2.494
rolling_sharpe_max: 2.729
negated_best_sharpe: 0.41
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.37
---
# fnd6_lifr (fundamental6)

*LIFO Reserve*

## Signal Profile
- `rank(fnd6_lifr)`: S=0.49, F=0.25, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_lifr / close)`: S=0.50, F=0.25, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_lifr, 5))`: S=0.78, F=0.56, T=13.2%, INFERIOR (TOP500)
- `-rank(fnd6_lifr)`: S=-0.40, F=-0.17, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lifr, 5))`: S=-0.48, F=-0.29, T=9.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_lifr, 63)`: S=0.50, F=0.28, T=5.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_lifr, 10)`: S=-0.19, F=-0.07, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_lifr, 22))`: S=-0.34, F=-0.17, T=19.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lifr)`: S=0.39, F=0.27, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lifr / close)`: S=0.41, F=0.28, T=3.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/12P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.22 (moderate), ret=+11.7%
  - 2020: S=-0.99 (negative), ret=-6.4%
  - 2021: S=1.50 (moderate), ret=+17.9%
  - 2022: S=0.88 (moderate), ret=+6.6%
  - 2023: S=0.56 (moderate), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 22.82% over 547 days (recovered)
- Annualized: return +6.7%, volatility 8.7% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +1.07, excess kurtosis +11.80

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.49, max 2.73, latest 0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +11.45%; worst month: -7.34%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.54
- Sideways: S=1.24
- Bear: S=-0.56

## Negated Direction
Best negated: `rank(-1 * fnd6_lifr / close)` S=0.41, F=0.28, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_lifr)`: S=0.39, F=0.27, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lifr / close)`: S=0.41, F=0.28, T=3.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lifr, 5))`: S=-0.48, F=-0.29, T=9.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_lifr, 5))` | TOP500 | 0.77 | 0.56 | 22.8% | 80% | bull-only |
| `rank(ts_delta(fnd6_lifr, 5))` | TOP200 | 0.64 | 0.46 | 18.4% | 80% | bull-only |
| `rank(fnd6_lifr / close)` | TOP3000 | 0.48 | 0.25 | 22.5% | 60% | bull-only |
| `rank(fnd6_lifr)` | TOP3000 | 0.47 | 0.25 | 22.8% | 60% | bull-only |
| `rank(fnd6_lifr)` | TOP1000 | 0.39 | 0.17 | 10.2% | 60% | bull-only |
| `rank(fnd6_lifr / close)` | TOP1000 | 0.38 | 0.16 | 10.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_lifr, 5))` | TOP1000 | 0.15 | 0.06 | 29.0% | 40% | mixed |
| `rank(fnd6_lifr)` | TOP500 | 0.18 | 0.06 | 10.6% | 60% | weak |
| `rank(fnd6_lifr / close)` | TOP500 | 0.16 | 0.05 | 10.5% | 60% | weak |
| `rank(ts_delta(fnd6_lifr, 5))` | TOP3000 | 0.08 | 0.02 | 28.0% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd6_dvpa: 0.538 (moderately positively correlated)
- fnd6_esopnr: 0.479 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.472 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.472 (moderately positively correlated)
- min_total_assets_guidance: 0.472 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
