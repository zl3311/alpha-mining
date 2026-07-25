---
field: fn_intangible_assets_accum_amort_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0822
ann_vol: 0.0741
hit_rate: 0.4907
rolling_sharpe_min: -0.482
rolling_sharpe_max: 2.179
redundancy_cluster: 1
negated_best_sharpe: 0.33
negated_best_template: neg_rank_level
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.44
---
# fn_intangible_assets_accum_amort_q (fundamental2)

*Accumulated amount of amortization of assets, excluding financial assets and goodwill, lacking physical substance with a finite life.*

## Signal Profile
- `rank(fn_intangible_assets_accum_amort_q)`: S=0.51, F=0.33, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_intangible_assets_accum_amort_q / close)`: S=0.77, F=0.52, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_intangible_assets_accum_amort_q, 5))`: S=0.26, F=0.09, T=38.5%, INFERIOR (TOP200)
- `-rank(fn_intangible_assets_accum_amort_q)`: S=-0.12, F=-0.04, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_intangible_assets_accum_amort_q, 5))`: S=-0.36, F=-0.13, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(fn_intangible_assets_accum_amort_q, 22)`: S=-0.10, F=-0.02, T=37.1%, INFERIOR (TOP3000)
- `ts_mean(fn_intangible_assets_accum_amort_q, 10)`: S=0.04, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_intangible_assets_accum_amort_q, 22))`: S=-0.12, F=-0.03, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fn_intangible_assets_accum_amort_q)`: S=0.33, F=0.21, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_intangible_assets_accum_amort_q / close)`: S=0.32, F=0.19, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.76, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.48 (weak), ret=+2.3%
  - 2020: S=0.25 (weak), ret=+2.1%
  - 2021: S=1.15 (moderate), ret=+10.6%
  - 2022: S=1.37 (moderate), ret=+11.3%
  - 2023: S=0.32 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 8.22% over 236 days (recovered)
- Annualized: return +5.6%, volatility 7.4% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.46, excess kurtosis +2.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.48, max 2.18, latest 0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.63%; worst month: -2.94%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.93
- Sideways: S=0.01
- Bear: S=-1.24

## Negated Direction
Best negated: `rank(-1 * fn_intangible_assets_accum_amort_q)` S=0.33, F=0.21, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_intangible_assets_accum_amort_q)`: S=0.33, F=0.21, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_intangible_assets_accum_amort_q / close)`: S=0.32, F=0.19, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_intangible_assets_accum_amort_q, 5))`: S=-0.36, F=-0.13, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_intangible_assets_accum_amort_q / close)` | TOP3000 | 0.76 | 0.52 | 8.2% | 100% | bull-only |
| `rank(fn_intangible_assets_accum_amort_q)` | TOP3000 | 0.50 | 0.33 | 24.8% | 60% | bull-only |
| `rank(ts_delta(fn_intangible_assets_accum_amort_q, 5))` | TOP500 | 0.29 | 0.09 | 20.2% | 80% | weak |
| `rank(ts_delta(fn_intangible_assets_accum_amort_q, 5))` | TOP200 | 0.26 | 0.09 | 25.3% | 80% | weak |
| `rank(fn_intangible_assets_accum_amort_q / close)` | TOP1000 | 0.21 | 0.09 | 20.7% | 60% | bull-only |
| `rank(fn_intangible_assets_accum_amort_q)` | TOP1000 | 0.11 | 0.04 | 34.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_intangible_assets_accum_amort_a: 0.966 (strongly positively correlated)
- fn_finite_lived_intangible_assets_gross_a: 0.926 (strongly positively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.923 (strongly positively correlated)
- fn_def_tax_liab_a: 0.914 (strongly positively correlated)
- fn_mne_a: 0.913 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
