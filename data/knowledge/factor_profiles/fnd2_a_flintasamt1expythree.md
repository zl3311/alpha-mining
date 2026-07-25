---
field: fnd2_a_flintasamt1expythree
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.64
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.0828
ann_vol: 0.06
hit_rate: 0.4834
rolling_sharpe_min: -1.512
rolling_sharpe_max: 2.298
negated_best_sharpe: 0.64
negated_best_template: rank_neg_delta
negated_best_fitness: 0.37
n_negated_sims: 10
direction_gap: 0.14
---
# fnd2_a_flintasamt1expythree (fundamental2)

*Amount of amortization expense for assets, excluding financial assets and goodwill, lacking physical substance with a finite life expected to be recognized during the 3rd fiscal year following the latest fiscal year. Excludes interim and annual periods when interim periods are reported on a rolling approach, from latest balance sheet date.*

## Signal Profile
- `rank(fnd2_a_flintasamt1expythree)`: S=0.27, F=0.11, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_a_flintasamt1expythree / close)`: S=0.50, F=0.24, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_flintasamt1expythree, 5))`: S=0.20, F=0.07, T=30.4%, INFERIOR (TOP200)
- `-rank(fnd2_a_flintasamt1expythree)`: S=0.06, F=0.01, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasamt1expythree, 5))`: S=0.64, F=0.37, T=32.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_flintasamt1expythree, 63)`: S=0.36, F=0.21, T=15.8%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_flintasamt1expythree, 10)`: S=0.06, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_flintasamt1expythree, 22))`: S=-0.16, F=-0.05, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expythree)`: S=0.45, F=0.29, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expythree / close)`: S=0.35, F=0.18, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 20F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.49, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.26 (weak), ret=+1.1%
  - 2020: S=0.28 (weak), ret=+2.1%
  - 2021: S=1.10 (moderate), ret=+7.6%
  - 2022: S=0.62 (moderate), ret=+3.4%
  - 2023: S=0.08 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 8.28% over 582 days (not yet recovered, ongoing at window end)
- Annualized: return +3.0%, volatility 6.0% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.60, excess kurtosis +3.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.51, max 2.30, latest 0.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.08%; worst month: -2.76%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.23
- Sideways: S=-0.06
- Bear: S=-1.09

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_flintasamt1expythree, 5))` S=0.64, F=0.37, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_flintasamt1expythree)`: S=0.45, F=0.29, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_flintasamt1expythree / close)`: S=0.35, F=0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_flintasamt1expythree, 5))`: S=0.64, F=0.37, T=32.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_flintasamt1expythree / close)` | TOP3000 | 0.49 | 0.24 | 8.3% | 100% | bull-only |
| `rank(fnd2_a_flintasamt1expythree)` | TOP3000 | 0.26 | 0.11 | 21.5% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_flintasamt1expythree, 5))` | TOP200 | 0.20 | 0.07 | 73.2% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd2_a_flintasamt1expytwo: 0.995 (strongly positively correlated)
- fnd2_a_flintasamt1expnext12m: 0.990 (strongly positively correlated)
- fnd2_a_flintasamt1expy5: 0.983 (strongly positively correlated)
- fn_finite_lived_intangible_assets_gross_a: 0.961 (strongly positively correlated)
- fn_amortization_of_intangible_assets_q: 0.942 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
