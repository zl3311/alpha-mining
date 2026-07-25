---
field: min_gross_income_guidance_2
dataset: analyst4
best_template: rank_level
best_sharpe: 0.8
best_fitness: 0.64
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.174
ann_vol: 0.1002
hit_rate: 0.5012
rolling_sharpe_min: -1.124
rolling_sharpe_max: 2.901
redundancy_cluster: 56
negated_best_sharpe: 0.17
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.63
---
# min_gross_income_guidance_2 (analyst4)

*The minimum guidance for Gross Income on an annual basis.*

## Signal Profile
- `rank(min_gross_income_guidance_2)`: S=0.80, F=0.64, T=1.9%, INFERIOR (TOP500)
- `rank(min_gross_income_guidance_2 / close)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP500)
- `rank(ts_delta(min_gross_income_guidance_2, 5))`: S=0.27, F=0.07, T=33.8%, INFERIOR (TOP200)
- `-rank(min_gross_income_guidance_2)`: S=-0.56, F=-0.32, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_gross_income_guidance_2, 5))`: S=0.17, F=0.03, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(min_gross_income_guidance_2, 63)`: S=0.10, F=0.02, T=21.5%, INFERIOR (TOP3000)
- `ts_mean(min_gross_income_guidance_2, 10)`: S=0.55, F=0.32, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(min_gross_income_guidance_2, 22))`: S=-0.12, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * min_gross_income_guidance_2)`: S=-0.80, F=-0.64, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * min_gross_income_guidance_2 / close)`: S=-0.05, F=-0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.80, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.23 (strong), ret=+18.5%
  - 2020: S=0.93 (moderate), ret=+9.0%
  - 2021: S=-0.22 (negative), ret=-2.2%
  - 2022: S=0.49 (weak), ret=+6.1%
  - 2023: S=0.92 (moderate), ret=+7.7%

## Risk & Drawdown
- Max drawdown: 17.40% over 505 days (recovered)
- Annualized: return +8.0%, volatility 10.0% (fraction of booksize)
- Hit rate: 50.1% positive days
- Tail shape: skew +0.34, excess kurtosis +2.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 2.90, latest 0.86

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +7.43%; worst month: -4.86%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.00
- Sideways: S=1.90
- Bear: S=0.76

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_gross_income_guidance_2, 5))` S=0.17, F=0.03, INFERIOR
Direction gap: -0.63 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * min_gross_income_guidance_2)`: S=-0.80, F=-0.64, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * min_gross_income_guidance_2 / close)`: S=-0.05, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_gross_income_guidance_2, 5))`: S=0.17, F=0.03, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_gross_income_guidance_2)` | TOP500 | 0.80 | 0.64 | 17.4% | 80% | mixed |
| `rank(min_gross_income_guidance_2)` | TOP1000 | 0.56 | 0.32 | 13.8% | 60% | mixed |
| `rank(min_gross_income_guidance_2)` | TOP200 | 0.17 | 0.08 | 38.3% | 60% | mixed |
| `rank(ts_delta(min_gross_income_guidance_2, 5))` | TOP200 | 0.28 | 0.07 | 21.0% | 40% | bear-only |
| `rank(min_gross_income_guidance_2)` | TOP3000 | 0.22 | 0.07 | 13.1% | 60% | bear-only |

## Correlation Notes
Top correlates:
- max_gross_income_guidance_2: 1.000 (strongly positively correlated)
- max_gross_income_guidance: 0.599 (moderately positively correlated)
- min_gross_income_guidance: 0.598 (moderately positively correlated)
- fnd6_cstkcvq: -0.428 (moderately negatively correlated)
- fnd6_cstkcv: -0.405 (moderately negatively correlated)

Redundancy cluster #56: 2 similar fields, mean |rho| 1.0 (representative: max_gross_income_guidance_2). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
