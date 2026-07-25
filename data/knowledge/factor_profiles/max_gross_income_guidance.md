---
field: max_gross_income_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.87
best_fitness: 0.74
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.1482
ann_vol: 0.105
hit_rate: 0.5182
rolling_sharpe_min: -0.868
rolling_sharpe_max: 3.33
top_merge_partner: fnd6_optprcex
redundancy_cluster: 49
negated_best_sharpe: 0.28
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.59
---
# max_gross_income_guidance (analyst4)

*The maximum guidance value for Gross Income.*

## Signal Profile
- `rank(max_gross_income_guidance)`: S=0.87, F=0.74, T=2.1%, INFERIOR (TOP500)
- `rank(max_gross_income_guidance / close)`: S=0.09, F=0.02, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(max_gross_income_guidance, 5))`: S=0.45, F=0.16, T=33.5%, INFERIOR (TOP200)
- `-rank(max_gross_income_guidance)`: S=-0.73, F=-0.50, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_gross_income_guidance, 5))`: S=0.28, F=0.06, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(max_gross_income_guidance, 63)`: S=0.26, F=0.07, T=21.7%, INFERIOR (TOP3000)
- `ts_mean(max_gross_income_guidance, 10)`: S=0.81, F=0.58, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(max_gross_income_guidance, 22))`: S=-0.14, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_gross_income_guidance)`: S=-0.87, F=-0.74, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * max_gross_income_guidance / close)`: S=-0.09, F=-0.02, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.88, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.16 (strong), ret=+21.1%
  - 2020: S=1.18 (moderate), ret=+12.8%
  - 2021: S=0.95 (moderate), ret=+10.0%
  - 2022: S=-0.42 (negative), ret=-4.5%
  - 2023: S=0.65 (moderate), ret=+6.1%

## Risk & Drawdown
- Max drawdown: 14.82% over 295 days (recovered)
- Annualized: return +9.3%, volatility 10.5% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.06, excess kurtosis +1.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.87, max 3.33, latest 0.66

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +7.33%; worst month: -7.45%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.01
- Sideways: S=1.48
- Bear: S=1.19

## Negated Direction
Best negated: `rank(-1 * ts_delta(max_gross_income_guidance, 5))` S=0.28, F=0.06, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_gross_income_guidance)`: S=-0.87, F=-0.74, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * max_gross_income_guidance / close)`: S=-0.09, F=-0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_gross_income_guidance, 5))`: S=0.28, F=0.06, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_gross_income_guidance)` | TOP500 | 0.88 | 0.74 | 14.8% | 80% | mixed |
| `rank(max_gross_income_guidance)` | TOP1000 | 0.76 | 0.50 | 14.8% | 60% | mixed |
| `rank(ts_delta(max_gross_income_guidance, 5))` | TOP200 | 0.46 | 0.16 | 21.9% | 60% | bear-only |
| `rank(max_gross_income_guidance / close)` | TOP500 | 0.09 | 0.02 | 32.4% | 40% | bull-only |
| `rank(max_gross_income_guidance)` | TOP3000 | 0.09 | 0.02 | 10.1% | 80% | weak |

## Correlation Notes
Top correlates:
- min_gross_income_guidance: 1.000 (strongly positively correlated)
- min_gross_income_guidance_2: 0.599 (moderately positively correlated)
- max_gross_income_guidance_2: 0.597 (moderately positively correlated)
- fnd6_cstkcvq: -0.380 (weakly negatively correlated)
- fnd6_cstkcv: -0.363 (weakly negatively correlated)

Redundancy cluster #49: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_optprcex | fundamental6 | -0.30 | 1.51 | +0.61 | -0.85 | yes |
| fnd6_optprcwa | fundamental6 | -0.28 | 1.48 | +0.59 | -0.72 | yes |
| fnd6_optprcby | fundamental6 | -0.29 | 1.58 | +0.58 | -0.81 | yes |
| fnd2_a_rvndm | fundamental2 | -0.28 | 1.47 | +0.57 | -0.90 | yes |
| fn_accum_depr_depletion_and_amortization_ppne_a | fundamental2 | -0.29 | 1.45 | +0.56 | -0.62 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
