---
field: fnd6_zipcode
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.66
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.3418
ann_vol: 0.1365
hit_rate: 0.485
rolling_sharpe_min: -2.214
rolling_sharpe_max: 2.731
negated_best_sharpe: 0.66
negated_best_template: rank_neg_delta
negated_best_fitness: 0.56
n_negated_sims: 10
direction_gap: 0.52
---
# fnd6_zipcode (fundamental6)

*ZIP code related to the company*

## Signal Profile
- `rank(fnd6_zipcode)`: S=0.11, F=0.02, T=1.3%, INFERIOR (TOP1000)
- `rank(fnd6_zipcode / close)`: S=0.11, F=0.03, T=1.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_zipcode, 5))`: S=0.14, F=0.05, T=18.0%, INFERIOR (TOP3000)
- `-rank(fnd6_zipcode)`: S=-0.11, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_zipcode, 5))`: S=0.66, F=0.56, T=17.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_zipcode, 22)`: S=-0.25, F=-0.21, T=1.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_zipcode, 10)`: S=-0.08, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_zipcode, 22))`: S=-0.62, F=-0.69, T=11.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_zipcode)`: S=-0.11, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_zipcode / close)`: S=-0.11, F=-0.03, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.14, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.30 (negative), ret=-2.2%
  - 2020: S=-1.93 (negative), ret=-20.9%
  - 2021: S=0.82 (moderate), ret=+14.3%
  - 2022: S=1.16 (moderate), ret=+20.7%
  - 2023: S=-0.23 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 34.18% over 1076 days (recovered)
- Annualized: return +1.9%, volatility 13.7% (fraction of booksize)
- Hit rate: 48.5% positive days
- Tail shape: skew -0.40, excess kurtosis +5.45

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.21, max 2.73, latest -0.16

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.71%; worst month: -14.16%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.07
- Sideways: S=-0.07
- Bear: S=-1.92

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_zipcode, 5))` S=0.66, F=0.56, INFERIOR
Direction gap: +0.52 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_zipcode)`: S=-0.11, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_zipcode / close)`: S=-0.11, F=-0.03, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_zipcode, 5))`: S=0.66, F=0.56, T=17.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_zipcode, 5))` | TOP3000 | 0.14 | 0.05 | 34.2% | 40% | bull-only |
| `rank(fnd6_zipcode / close)` | TOP1000 | 0.12 | 0.03 | 25.4% | 60% | bear-only |
| `rank(fnd6_zipcode)` | TOP1000 | 0.12 | 0.02 | 8.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- max_share_buyback_guidance: 0.426 (moderately positively correlated)
- min_adjusted_funds_from_operations_adj_guidance: 0.426 (moderately positively correlated)
- max_total_goodwill_guidance_2: 0.426 (moderately positively correlated)
- min_custom_eps_guidance: 0.426 (moderately positively correlated)
- max_adjusted_funds_from_operations_adj_guidance: 0.426 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
