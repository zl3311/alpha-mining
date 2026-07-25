---
field: fn_intangible_assets_accum_amort_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.82
best_fitness: 0.66
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0774
ann_vol: 0.0708
hit_rate: 0.5101
rolling_sharpe_min: -0.59
rolling_sharpe_max: 2.312
redundancy_cluster: 1
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.24
---
# fn_intangible_assets_accum_amort_a (fundamental2)

*Accumulated amount of amortization of assets, excluding financial assets and goodwill, lacking physical substance with a finite life.*

## Signal Profile
- `rank(fn_intangible_assets_accum_amort_a)`: S=0.43, F=0.24, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_intangible_assets_accum_amort_a / close)`: S=0.75, F=0.49, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_intangible_assets_accum_amort_a, 5))`: S=-0.22, F=-0.06, T=34.3%, INFERIOR (TOP3000)
- `-rank(fn_intangible_assets_accum_amort_a)`: S=-0.17, F=-0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_intangible_assets_accum_amort_a, 5))`: S=0.58, F=0.31, T=34.3%, INFERIOR (TOP3000)
- `ts_zscore(fn_intangible_assets_accum_amort_a, 22)`: S=0.82, F=0.66, T=25.7%, INFERIOR (TOP3000)
- `ts_mean(fn_intangible_assets_accum_amort_a, 10)`: S=0.11, F=0.03, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_intangible_assets_accum_amort_a, 22))`: S=0.13, F=0.03, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_intangible_assets_accum_amort_a)`: S=0.28, F=0.16, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_intangible_assets_accum_amort_a / close)`: S=0.12, F=0.04, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.75, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.84 (moderate), ret=+3.6%
  - 2020: S=0.17 (weak), ret=+1.4%
  - 2021: S=1.07 (moderate), ret=+9.2%
  - 2022: S=1.41 (moderate), ret=+10.9%
  - 2023: S=0.23 (weak), ret=+0.9%

## Risk & Drawdown
- Max drawdown: 7.74% over 442 days (recovered)
- Annualized: return +5.3%, volatility 7.1% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.49, excess kurtosis +2.98

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.59, max 2.31, latest 0.34

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.55%; worst month: -3.07%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.86
- Sideways: S=0.26
- Bear: S=-1.37

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_intangible_assets_accum_amort_a, 5))` S=0.58, F=0.31, INFERIOR
Direction gap: -0.24 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_intangible_assets_accum_amort_a)`: S=0.28, F=0.16, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_intangible_assets_accum_amort_a / close)`: S=0.12, F=0.04, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_intangible_assets_accum_amort_a, 5))`: S=0.58, F=0.31, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_intangible_assets_accum_amort_a / close)` | TOP3000 | 0.75 | 0.49 | 7.7% | 100% | bull-only |
| `rank(fn_intangible_assets_accum_amort_a)` | TOP3000 | 0.42 | 0.24 | 24.3% | 80% | bull-only |
| `rank(fn_intangible_assets_accum_amort_a / close)` | TOP1000 | 0.31 | 0.16 | 17.5% | 60% | bull-only |
| `rank(fn_intangible_assets_accum_amort_a)` | TOP1000 | 0.16 | 0.07 | 30.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_intangible_assets_accum_amort_q: 0.966 (strongly positively correlated)
- fn_finite_lived_intangible_assets_gross_a: 0.954 (strongly positively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.938 (strongly positively correlated)
- fnd2_a_flintasacmamtzcsrld: 0.934 (strongly positively correlated)
- fn_mne_a: 0.924 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
