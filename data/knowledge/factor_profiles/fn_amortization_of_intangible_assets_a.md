---
field: fn_amortization_of_intangible_assets_a
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.62
best_fitness: 0.32
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1943
ann_vol: 0.1427
hit_rate: 0.5093
rolling_sharpe_min: -1.055
rolling_sharpe_max: 2.799
negated_best_sharpe: 0.35
negated_best_template: neg_rank_level
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.27
---
# fn_amortization_of_intangible_assets_a (fundamental2)

*The aggregate expense charged against earnings to allocate the cost of intangible assets (nonphysical assets not used in production) in a systematic and rational manner to the periods expected to benefit from such assets. As a noncash expense, this element is added back to net income when calculating cash provided by or used in operations using the indirect method.*

## Signal Profile
- `rank(fn_amortization_of_intangible_assets_a)`: S=0.28, F=0.12, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_amortization_of_intangible_assets_a / close)`: S=0.50, F=0.25, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_amortization_of_intangible_assets_a, 5))`: S=0.62, F=0.32, T=33.9%, INFERIOR (TOP1000)
- `-rank(fn_amortization_of_intangible_assets_a)`: S=0.00, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_amortization_of_intangible_assets_a, 5))`: S=-0.25, F=-0.09, T=33.2%, INFERIOR (TOP3000)
- `ts_zscore(fn_amortization_of_intangible_assets_a, 22)`: S=0.16, F=0.06, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(fn_amortization_of_intangible_assets_a, 10)`: S=0.16, F=0.06, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_amortization_of_intangible_assets_a, 22))`: S=-0.49, F=-0.27, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_amortization_of_intangible_assets_a)`: S=0.35, F=0.21, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_amortization_of_intangible_assets_a / close)`: S=0.22, F=0.09, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.86 (negative), ret=-10.9%
  - 2020: S=0.66 (moderate), ret=+9.3%
  - 2021: S=0.70 (moderate), ret=+9.7%
  - 2022: S=0.81 (moderate), ret=+12.1%
  - 2023: S=1.63 (strong), ret=+23.2%

## Risk & Drawdown
- Max drawdown: 19.43% over 244 days (recovered)
- Annualized: return +8.9%, volatility 14.3% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.06, excess kurtosis +4.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.05, max 2.80, latest 1.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +9.48%; worst month: -7.27%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.32
- Sideways: S=0.05
- Bear: S=0.37

## Negated Direction
Best negated: `rank(-1 * fn_amortization_of_intangible_assets_a)` S=0.35, F=0.21, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_amortization_of_intangible_assets_a)`: S=0.35, F=0.21, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_amortization_of_intangible_assets_a / close)`: S=0.22, F=0.09, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_amortization_of_intangible_assets_a, 5))`: S=-0.25, F=-0.09, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_amortization_of_intangible_assets_a, 5))` | TOP1000 | 0.62 | 0.32 | 19.4% | 80% | mixed |
| `rank(fn_amortization_of_intangible_assets_a / close)` | TOP3000 | 0.50 | 0.25 | 7.7% | 100% | bull-only |
| `rank(fn_amortization_of_intangible_assets_a)` | TOP3000 | 0.28 | 0.12 | 23.3% | 80% | bull-only |
| `rank(fn_amortization_of_intangible_assets_a / close)` | TOP1000 | 0.12 | 0.03 | 17.0% | 60% | bull-only |
| `rank(ts_delta(fn_amortization_of_intangible_assets_a, 5))` | TOP500 | 0.11 | 0.02 | 34.4% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd2_propplteqflublgland: 0.188 (weakly positively correlated)
- fnd2_a_gwllimrml: 0.177 (weakly positively correlated)
- fn_new_shares_options_a: -0.164 (weakly negatively correlated)
- fn_finite_lived_intangible_assets_net_a: 0.163 (weakly positively correlated)
- fnd2_a_ltrmdmrepoplinytwo: 0.148 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
