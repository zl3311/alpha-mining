---
field: max_gross_income_guidance_2
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
max_drawdown: 0.1724
ann_vol: 0.0997
hit_rate: 0.5061
rolling_sharpe_min: -1.132
rolling_sharpe_max: 2.903
top_merge_partner: fn_accum_depr_depletion_and_amortization_ppne_a
redundancy_cluster: 56
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.04
n_negated_sims: 10
direction_gap: -0.59
---
# max_gross_income_guidance_2 (analyst4)

*The maximum guidance for Gross Income on an annual basis.*

## Signal Profile
- `rank(max_gross_income_guidance_2)`: S=0.80, F=0.64, T=1.9%, INFERIOR (TOP500)
- `rank(max_gross_income_guidance_2 / close)`: S=0.05, F=0.01, T=2.2%, INFERIOR (TOP500)
- `rank(ts_delta(max_gross_income_guidance_2, 5))`: S=0.47, F=0.17, T=33.7%, INFERIOR (TOP200)
- `-rank(max_gross_income_guidance_2)`: S=-0.57, F=-0.33, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_gross_income_guidance_2, 5))`: S=0.21, F=0.04, T=36.3%, INFERIOR (TOP3000)
- `-ts_zscore(max_gross_income_guidance_2, 63)`: S=0.28, F=0.08, T=21.6%, INFERIOR (TOP3000)
- `ts_mean(max_gross_income_guidance_2, 10)`: S=0.62, F=0.37, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(max_gross_income_guidance_2, 22))`: S=-0.13, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_gross_income_guidance_2)`: S=-0.80, F=-0.64, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * max_gross_income_guidance_2 / close)`: S=-0.05, F=-0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.80, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.23 (strong), ret=+18.5%
  - 2020: S=0.94 (moderate), ret=+9.0%
  - 2021: S=-0.21 (negative), ret=-2.1%
  - 2022: S=0.50 (weak), ret=+6.1%
  - 2023: S=0.91 (moderate), ret=+7.6%

## Risk & Drawdown
- Max drawdown: 17.24% over 505 days (recovered)
- Annualized: return +8.0%, volatility 10.0% (fraction of booksize)
- Hit rate: 50.6% positive days
- Tail shape: skew +0.34, excess kurtosis +2.36

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.13, max 2.90, latest 0.85

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +7.43%; worst month: -4.89%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.01
- Sideways: S=1.91
- Bear: S=0.76

## Negated Direction
Best negated: `rank(-1 * ts_delta(max_gross_income_guidance_2, 5))` S=0.21, F=0.04, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_gross_income_guidance_2)`: S=-0.80, F=-0.64, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * max_gross_income_guidance_2 / close)`: S=-0.05, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_gross_income_guidance_2, 5))`: S=0.21, F=0.04, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_gross_income_guidance_2)` | TOP500 | 0.80 | 0.64 | 17.2% | 80% | mixed |
| `rank(max_gross_income_guidance_2)` | TOP1000 | 0.57 | 0.33 | 13.7% | 60% | mixed |
| `rank(ts_delta(max_gross_income_guidance_2, 5))` | TOP200 | 0.48 | 0.17 | 14.9% | 80% | bear-only |
| `rank(max_gross_income_guidance_2)` | TOP3000 | 0.22 | 0.07 | 13.3% | 60% | bear-only |
| `rank(max_gross_income_guidance_2)` | TOP200 | 0.16 | 0.07 | 38.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- min_gross_income_guidance_2: 1.000 (strongly positively correlated)
- max_gross_income_guidance: 0.597 (moderately positively correlated)
- min_gross_income_guidance: 0.597 (moderately positively correlated)
- fnd6_cstkcvq: -0.425 (moderately negatively correlated)
- fnd6_cstkcv: -0.402 (moderately negatively correlated)

Redundancy cluster #56: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_accum_depr_depletion_and_amortization_ppne_a | fundamental2 | -0.37 | 1.46 | +0.61 | -0.52 | yes |
| fnd6_optprcex | fundamental6 | -0.35 | 1.49 | +0.59 | -0.72 | yes |
| sales_ps | fundamental_value | -0.34 | 1.63 | +0.57 | -0.89 | yes |
| fnd2_a_rvndm | fundamental2 | -0.35 | 1.47 | +0.57 | -0.81 | yes |
| fnd6_newa1v1300_dp | fundamental6 | -0.32 | 1.40 | +0.56 | -0.92 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
