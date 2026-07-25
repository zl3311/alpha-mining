---
field: fnd6_txr
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.54
best_fitness: 0.38
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1991
ann_vol: 0.1745
hit_rate: 0.4899
rolling_sharpe_min: -1.628
rolling_sharpe_max: 2.543
negated_best_sharpe: 0.16
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.38
---
# fnd6_txr (fundamental6)

*Income Tax Refund*

## Signal Profile
- `rank(fnd6_txr)`: S=0.39, F=0.14, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_txr / close)`: S=0.43, F=0.16, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txr, 5))`: S=0.54, F=0.38, T=19.4%, INFERIOR (TOP500)
- `-rank(fnd6_txr)`: S=-0.14, F=-0.03, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txr, 5))`: S=-0.25, F=-0.15, T=12.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txr, 22)`: S=0.33, F=0.21, T=11.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txr, 10)`: S=-0.22, F=-0.08, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txr, 22))`: S=0.48, F=0.32, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txr)`: S=0.14, F=0.04, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txr / close)`: S=0.16, F=0.05, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.54, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.66 (moderate), ret=+10.7%
  - 2020: S=0.61 (moderate), ret=+11.5%
  - 2021: S=1.66 (strong), ret=+29.9%
  - 2022: S=0.52 (moderate), ret=+10.6%
  - 2023: S=-1.62 (negative), ret=-16.8%

## Risk & Drawdown
- Max drawdown: 19.91% over 294 days (not yet recovered, ongoing at window end)
- Annualized: return +9.4%, volatility 17.4% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +1.39, excess kurtosis +29.87

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.63, max 2.54, latest -1.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +16.98%; worst month: -8.91%
Positive months: 49%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.25
- Sideways: S=0.40
- Bear: S=-0.08

## Negated Direction
Best negated: `rank(-1 * fnd6_txr / close)` S=0.16, F=0.05, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txr)`: S=0.14, F=0.04, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txr / close)`: S=0.16, F=0.05, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txr, 5))`: S=-0.25, F=-0.15, T=12.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txr, 5))` | TOP500 | 0.54 | 0.38 | 19.9% | 80% | mixed |
| `rank(ts_delta(fnd6_txr, 5))` | TOP1000 | 0.41 | 0.20 | 26.9% | 60% | mixed |
| `rank(fnd6_txr / close)` | TOP3000 | 0.43 | 0.16 | 9.1% | 80% | bull-only |
| `rank(fnd6_txr)` | TOP3000 | 0.39 | 0.14 | 10.8% | 80% | bull-only |
| `rank(fnd6_txr / close)` | TOP1000 | 0.16 | 0.04 | 7.9% | 60% | bull-only |
| `rank(fnd6_txr)` | TOP1000 | 0.14 | 0.03 | 8.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_txr, 5))` | TOP3000 | 0.07 | 0.02 | 51.7% | 40% | mixed |
| `rank(ts_delta(fnd6_txr, 5))` | TOP200 | 0.06 | 0.02 | 32.6% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_tfvl: 0.332 (weakly positively correlated)
- fnd6_newa1v1300_fca: 0.272 (weakly positively correlated)
- fnd6_optrfr: 0.271 (weakly positively correlated)
- fnd6_esopnr: 0.256 (weakly positively correlated)
- min_free_cashflow_per_share_guidance: 0.245 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
