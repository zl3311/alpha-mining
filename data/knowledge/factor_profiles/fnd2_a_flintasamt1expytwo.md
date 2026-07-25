---
field: fnd2_a_flintasamt1expytwo
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.82
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.0749
ann_vol: 0.0611
hit_rate: 0.4834
rolling_sharpe_min: -1.239
rolling_sharpe_max: 2.213
negated_best_sharpe: 0.45
negated_best_template: neg_rank_level
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: -0.37
---
# fnd2_a_flintasamt1expytwo (fundamental2)

*Amount of amortization expense for assets, excluding financial assets and goodwill, lacking physical substance with a finite life expected to be recognized during the 2nd fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date*

## Signal Profile
- `rank(fnd2_a_flintasamt1expytwo)`: S=0.26, F=0.10, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_a_flintasamt1expytwo / close)`: S=0.48, F=0.23, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_flintasamt1expytwo, 5))`: S=0.12, F=0.03, T=30.2%, INFERIOR (TOP200)
- `-rank(fnd2_a_flintasamt1expytwo)`: S=0.03, F=0.00, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasamt1expytwo, 5))`: S=0.26, F=0.09, T=32.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_flintasamt1expytwo, 63)`: S=0.82, F=0.71, T=16.3%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_flintasamt1expytwo, 10)`: S=0.05, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_flintasamt1expytwo, 22))`: S=-0.31, F=-0.14, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expytwo)`: S=0.45, F=0.30, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expytwo / close)`: S=0.31, F=0.15, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.38 (weak), ret=+1.7%
  - 2020: S=0.21 (weak), ret=+1.6%
  - 2021: S=1.03 (moderate), ret=+7.2%
  - 2022: S=0.61 (moderate), ret=+3.3%
  - 2023: S=0.14 (weak), ret=+0.7%

## Risk & Drawdown
- Max drawdown: 7.49% over 582 days (not yet recovered, ongoing at window end)
- Annualized: return +2.9%, volatility 6.1% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.65, excess kurtosis +3.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.24, max 2.21, latest 0.31

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.08%; worst month: -2.73%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.15
- Sideways: S=-0.07
- Bear: S=-1.00

## Negated Direction
Best negated: `rank(-1 * fnd2_a_flintasamt1expytwo)` S=0.45, F=0.30, INFERIOR
Direction gap: -0.37 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_flintasamt1expytwo)`: S=0.45, F=0.30, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expytwo / close)`: S=0.31, F=0.15, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasamt1expytwo, 5))`: S=0.26, F=0.09, T=32.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_flintasamt1expytwo / close)` | TOP3000 | 0.48 | 0.23 | 7.5% | 100% | bull-only |
| `rank(fnd2_a_flintasamt1expytwo)` | TOP3000 | 0.26 | 0.10 | 22.5% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_flintasamt1expytwo, 5))` | TOP200 | 0.13 | 0.03 | 59.1% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd2_a_flintasamt1expnext12m: 0.996 (strongly positively correlated)
- fnd2_a_flintasamt1expythree: 0.995 (strongly positively correlated)
- fnd2_a_flintasamt1expy5: 0.977 (strongly positively correlated)
- fn_finite_lived_intangible_assets_gross_a: 0.960 (strongly positively correlated)
- fn_amortization_of_intangible_assets_q: 0.943 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
