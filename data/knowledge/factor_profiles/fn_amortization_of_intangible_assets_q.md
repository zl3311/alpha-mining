---
field: fn_amortization_of_intangible_assets_q
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.59
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0984
ann_vol: 0.0631
hit_rate: 0.4737
rolling_sharpe_min: -1.388
rolling_sharpe_max: 1.823
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.22
---
# fn_amortization_of_intangible_assets_q (fundamental2)

*The aggregate expense charged against earnings to allocate the cost of intangible assets (nonphysical assets not used in production) in a systematic and rational manner to the periods expected to benefit from such assets. As a noncash expense, this element is added back to net income when calculating cash provided by or used in operations using the indirect method.*

## Signal Profile
- `rank(fn_amortization_of_intangible_assets_q)`: S=0.32, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(fn_amortization_of_intangible_assets_q / close)`: S=0.37, F=0.16, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_amortization_of_intangible_assets_q, 5))`: S=0.44, F=0.14, T=35.8%, INFERIOR (TOP3000)
- `-rank(fn_amortization_of_intangible_assets_q)`: S=-0.08, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_amortization_of_intangible_assets_q, 5))`: S=0.59, F=0.30, T=37.4%, INFERIOR (TOP3000)
- `-ts_zscore(fn_amortization_of_intangible_assets_q, 63)`: S=0.34, F=0.12, T=17.2%, INFERIOR (TOP3000)
- `ts_mean(fn_amortization_of_intangible_assets_q, 10)`: S=0.06, F=0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_amortization_of_intangible_assets_q, 22))`: S=-0.34, F=-0.13, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_amortization_of_intangible_assets_q)`: S=0.33, F=0.21, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_amortization_of_intangible_assets_q / close)`: S=0.31, F=0.18, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.36, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.09 (weak), ret=+0.4%
  - 2020: S=0.55 (moderate), ret=+4.3%
  - 2021: S=0.79 (moderate), ret=+5.6%
  - 2022: S=-0.11 (negative), ret=-0.6%
  - 2023: S=0.30 (weak), ret=+1.5%

## Risk & Drawdown
- Max drawdown: 9.84% over 582 days (not yet recovered, ongoing at window end)
- Annualized: return +2.3%, volatility 6.3% (fraction of booksize)
- Hit rate: 47.4% positive days
- Tail shape: skew +0.57, excess kurtosis +2.30

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.39, max 1.82, latest 0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +4.87%; worst month: -3.40%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.87
- Sideways: S=-0.48
- Bear: S=-0.57

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_amortization_of_intangible_assets_q, 5))` S=0.59, F=0.30, INFERIOR
Direction gap: +0.22 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fn_amortization_of_intangible_assets_q)`: S=0.33, F=0.21, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_amortization_of_intangible_assets_q / close)`: S=0.31, F=0.18, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_amortization_of_intangible_assets_q, 5))`: S=0.59, F=0.30, T=37.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_amortization_of_intangible_assets_q / close)` | TOP3000 | 0.36 | 0.16 | 9.8% | 80% | bull-only |
| `rank(ts_delta(fn_amortization_of_intangible_assets_q, 5))` | TOP3000 | 0.44 | 0.14 | 19.6% | 40% | bear-only |
| `rank(fn_amortization_of_intangible_assets_q)` | TOP3000 | 0.32 | 0.14 | 20.2% | 60% | bull-only |
| `rank(fn_amortization_of_intangible_assets_q / close)` | TOP1000 | 0.12 | 0.04 | 15.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_flintasamt1expnext12m: 0.944 (strongly positively correlated)
- fnd2_a_flintasamt1expytwo: 0.943 (strongly positively correlated)
- fnd2_a_flintasamt1expythree: 0.942 (strongly positively correlated)
- fnd2_a_flintasamt1expy5: 0.924 (strongly positively correlated)
- fn_finite_lived_intangible_assets_gross_a: 0.917 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
