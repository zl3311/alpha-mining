---
field: fn_finite_lived_intangible_assets_gross_a
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.57
best_fitness: 0.31
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0736
ann_vol: 0.064
hit_rate: 0.4802
rolling_sharpe_min: -1.325
rolling_sharpe_max: 2.149
negated_best_sharpe: 0.57
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: 0.09
---
# fn_finite_lived_intangible_assets_gross_a (fundamental2)

*Amount before amortization of assets, excluding financial assets and goodwill, lacking physical substance with a finite life.*

## Signal Profile
- `rank(fn_finite_lived_intangible_assets_gross_a)`: S=0.29, F=0.13, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_finite_lived_intangible_assets_gross_a / close)`: S=0.48, F=0.24, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_finite_lived_intangible_assets_gross_a, 5))`: S=0.22, F=0.06, T=34.4%, INFERIOR (TOP3000)
- `-rank(fn_finite_lived_intangible_assets_gross_a)`: S=-0.05, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_finite_lived_intangible_assets_gross_a, 5))`: S=0.57, F=0.31, T=33.9%, INFERIOR (TOP3000)
- `-ts_zscore(fn_finite_lived_intangible_assets_gross_a, 63)`: S=0.24, F=0.11, T=16.6%, INFERIOR (TOP3000)
- `ts_mean(fn_finite_lived_intangible_assets_gross_a, 10)`: S=0.18, F=0.07, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_finite_lived_intangible_assets_gross_a, 22))`: S=-0.05, F=-0.01, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_gross_a)`: S=0.33, F=0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_gross_a / close)`: S=0.20, F=0.09, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.30 (weak), ret=+1.4%
  - 2020: S=0.08 (weak), ret=+0.7%
  - 2021: S=1.03 (moderate), ret=+7.8%
  - 2022: S=0.94 (moderate), ret=+5.6%
  - 2023: S=-0.10 (negative), ret=-0.4%

## Risk & Drawdown
- Max drawdown: 7.36% over 269 days (recovered)
- Annualized: return +3.1%, volatility 6.4% (fraction of booksize)
- Hit rate: 48.0% positive days
- Tail shape: skew +0.60, excess kurtosis +3.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.32, max 2.15, latest 0.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +5.94%; worst month: -3.27%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.45
- Sideways: S=-0.22
- Bear: S=-1.26

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_finite_lived_intangible_assets_gross_a, 5))` S=0.57, F=0.31, INFERIOR
Direction gap: +0.09 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_finite_lived_intangible_assets_gross_a)`: S=0.33, F=0.20, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_gross_a / close)`: S=0.20, F=0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_finite_lived_intangible_assets_gross_a, 5))`: S=0.57, F=0.31, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_finite_lived_intangible_assets_gross_a / close)` | TOP3000 | 0.48 | 0.24 | 7.4% | 80% | bull-only |
| `rank(fn_finite_lived_intangible_assets_gross_a)` | TOP3000 | 0.28 | 0.13 | 23.2% | 60% | bull-only |
| `rank(fn_finite_lived_intangible_assets_gross_a / close)` | TOP1000 | 0.18 | 0.07 | 16.4% | 60% | bull-only |
| `rank(ts_delta(fn_finite_lived_intangible_assets_gross_a, 5))` | TOP3000 | 0.23 | 0.06 | 20.2% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd2_a_flintasamt1expnext12m: 0.961 (strongly positively correlated)
- fnd2_a_flintasamt1expythree: 0.961 (strongly positively correlated)
- fnd2_a_flintasamt1expytwo: 0.960 (strongly positively correlated)
- fn_intangible_assets_accum_amort_a: 0.954 (strongly positively correlated)
- fnd2_a_flintasamt1expy5: 0.949 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
