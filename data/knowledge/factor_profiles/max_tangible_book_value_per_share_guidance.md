---
field: max_tangible_book_value_per_share_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 0.82
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2048
ann_vol: 0.154
hit_rate: 0.515
rolling_sharpe_min: -0.436
rolling_sharpe_max: 3.329
top_merge_partner: multi_factor_static_score_derivative
redundancy_cluster: 54
negated_best_sharpe: 0.36
negated_best_template: neg_rank_level
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.46
---
# max_tangible_book_value_per_share_guidance (analyst4)

*Tangible Book Value per Share - maximum guidance value*

## Signal Profile
- `rank(max_tangible_book_value_per_share_guidance)`: S=0.82, F=0.82, T=1.9%, INFERIOR (TOP3000)
- `rank(max_tangible_book_value_per_share_guidance / close)`: S=0.07, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_tangible_book_value_per_share_guidance, 5))`: S=0.54, F=0.20, T=33.7%, INFERIOR (TOP200)
- `-rank(max_tangible_book_value_per_share_guidance)`: S=-0.23, F=-0.11, T=3.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_tangible_book_value_per_share_guidance, 5))`: S=0.23, F=0.05, T=36.2%, INFERIOR (TOP3000)
- `-ts_zscore(max_tangible_book_value_per_share_guidance, 63)`: S=0.08, F=0.01, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(max_tangible_book_value_per_share_guidance, 10)`: S=0.02, F=0.00, T=24.1%, INFERIOR (TOP3000)
- `rank(ts_rank(max_tangible_book_value_per_share_guidance, 22))`: S=-0.12, F=-0.03, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * max_tangible_book_value_per_share_guidance)`: S=0.36, F=0.20, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * max_tangible_book_value_per_share_guidance / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.83, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.23 (negative), ret=-3.4%
  - 2020: S=0.46 (weak), ret=+9.6%
  - 2021: S=1.50 (moderate), ret=+25.3%
  - 2022: S=3.24 (strong), ret=+34.0%
  - 2023: S=-0.30 (negative), ret=-2.5%

## Risk & Drawdown
- Max drawdown: 20.48% over 571 days (recovered)
- Annualized: return +12.8%, volatility 15.4% (fraction of booksize)
- Hit rate: 51.5% positive days
- Tail shape: skew +0.30, excess kurtosis +4.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.44, max 3.33, latest -0.41

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +12.51%; worst month: -9.46%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.13
- Sideways: S=0.95
- Bear: S=-0.30

## Negated Direction
Best negated: `rank(-1 * max_tangible_book_value_per_share_guidance)` S=0.36, F=0.20, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * max_tangible_book_value_per_share_guidance)`: S=0.36, F=0.20, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * max_tangible_book_value_per_share_guidance / close)`: S=0.06, F=0.01, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_tangible_book_value_per_share_guidance, 5))`: S=0.23, F=0.05, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(max_tangible_book_value_per_share_guidance)` | TOP3000 | 0.83 | 0.82 | 20.5% | 60% | mixed |
| `rank(max_tangible_book_value_per_share_guidance)` | TOP500 | 0.54 | 0.41 | 32.4% | 80% | bull-only |
| `rank(ts_delta(max_tangible_book_value_per_share_guidance, 5))` | TOP200 | 0.56 | 0.20 | 15.4% | 60% | bear-only |
| `rank(max_tangible_book_value_per_share_guidance)` | TOP1000 | 0.23 | 0.11 | 37.5% | 60% | bull-only |
| `rank(max_tangible_book_value_per_share_guidance)` | TOP200 | 0.15 | 0.07 | 30.7% | 60% | bull-only |
| `rank(max_tangible_book_value_per_share_guidance / close)` | TOP3000 | 0.07 | 0.02 | 53.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_tangible_book_value_per_share_guidance: 1.000 (strongly positively correlated)
- rel_num_part: 0.418 (moderately positively correlated)
- rel_num_comp: 0.411 (moderately positively correlated)
- rel_num_all: 0.411 (moderately positively correlated)
- anl4_bvps_flag: 0.408 (moderately positively correlated)

Redundancy cluster #54: 2 similar fields, mean |rho| 1.0 (representative: min_tangible_book_value_per_share_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| multi_factor_static_score_derivative | model16 | -0.12 | 1.25 | +0.41 | -0.21 | yes |
| growth_potential_rank_derivative | model16 | -0.12 | 1.29 | +0.41 | -0.25 | yes |
| fnd6_txtubposdec | fundamental6 | -0.12 | 1.24 | +0.41 | -0.26 | yes |
| relative_valuation_rank_derivative | model16 | -0.12 | 1.33 | +0.40 | -0.29 | yes |
| earnings_certainty_rank_derivative | model16 | -0.12 | 1.33 | +0.40 | -0.29 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
