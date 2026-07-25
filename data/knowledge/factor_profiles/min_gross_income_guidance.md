---
field: min_gross_income_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.86
best_fitness: 0.73
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1473
ann_vol: 0.1056
hit_rate: 0.519
rolling_sharpe_min: -0.945
rolling_sharpe_max: 3.315
top_merge_partner: fnd6_optprcex
redundancy_cluster: 49
negated_best_sharpe: 0.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.43
---
# min_gross_income_guidance (analyst4)

*The minimum guidance value for Gross Income.*

## Signal Profile
- `rank(min_gross_income_guidance)`: S=0.86, F=0.73, T=2.1%, INFERIOR (TOP500)
- `rank(min_gross_income_guidance / close)`: S=0.09, F=0.02, T=2.3%, INFERIOR (TOP500)
- `rank(ts_delta(min_gross_income_guidance, 5))`: S=0.24, F=0.06, T=33.7%, INFERIOR (TOP200)
- `-rank(min_gross_income_guidance)`: S=-0.73, F=-0.50, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_gross_income_guidance, 5))`: S=0.43, F=0.12, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(min_gross_income_guidance, 63)`: S=0.44, F=0.16, T=21.6%, INFERIOR (TOP3000)
- `ts_mean(min_gross_income_guidance, 10)`: S=0.74, F=0.52, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(min_gross_income_guidance, 22))`: S=-0.19, F=-0.05, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * min_gross_income_guidance)`: S=-0.86, F=-0.73, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * min_gross_income_guidance / close)`: S=-0.09, F=-0.02, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.87, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.15 (strong), ret=+21.1%
  - 2020: S=1.17 (moderate), ret=+12.8%
  - 2021: S=0.94 (moderate), ret=+9.8%
  - 2022: S=-0.47 (negative), ret=-5.1%
  - 2023: S=0.67 (moderate), ret=+6.4%

## Risk & Drawdown
- Max drawdown: 14.73% over 295 days (recovered)
- Annualized: return +9.2%, volatility 10.6% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.05, excess kurtosis +1.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.94, max 3.31, latest 0.68

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2022
Best month: +7.32%; worst month: -7.39%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.02
- Sideways: S=1.46
- Bear: S=1.19

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_gross_income_guidance, 5))` S=0.43, F=0.12, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * min_gross_income_guidance)`: S=-0.86, F=-0.73, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * min_gross_income_guidance / close)`: S=-0.09, F=-0.02, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_gross_income_guidance, 5))`: S=0.43, F=0.12, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_gross_income_guidance)` | TOP500 | 0.87 | 0.73 | 14.7% | 80% | mixed |
| `rank(min_gross_income_guidance)` | TOP1000 | 0.75 | 0.50 | 14.7% | 60% | mixed |
| `rank(ts_delta(min_gross_income_guidance, 5))` | TOP200 | 0.26 | 0.06 | 24.1% | 40% | bear-only |
| `rank(min_gross_income_guidance / close)` | TOP500 | 0.09 | 0.02 | 32.3% | 40% | bull-only |

## Correlation Notes
Top correlates:
- max_gross_income_guidance: 1.000 (strongly positively correlated)
- min_gross_income_guidance_2: 0.598 (moderately positively correlated)
- max_gross_income_guidance_2: 0.597 (moderately positively correlated)
- fnd6_cstkcvq: -0.383 (weakly negatively correlated)
- fnd6_cstkcv: -0.366 (weakly negatively correlated)

Redundancy cluster #49: 2 similar fields, mean |rho| 1.0 (representative: max_gross_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_optprcex | fundamental6 | -0.30 | 1.50 | +0.60 | -0.86 | yes |
| fnd6_optprcwa | fundamental6 | -0.28 | 1.47 | +0.58 | -0.73 | yes |
| fnd6_optprcby | fundamental6 | -0.29 | 1.56 | +0.57 | -0.82 | yes |
| fnd2_a_rvndm | fundamental2 | -0.28 | 1.45 | +0.56 | -0.89 | yes |
| fn_accum_depr_depletion_and_amortization_ppne_a | fundamental2 | -0.29 | 1.43 | +0.56 | -0.64 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
