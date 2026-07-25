---
field: funds_from_operations_max_guidance
dataset: analyst4
best_template: rank_level
best_sharpe: 1.14
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.0472
ann_vol: 0.0546
hit_rate: 0.5296
rolling_sharpe_min: -0.114
rolling_sharpe_max: 2.627
top_merge_partner: fnd6_fopo
redundancy_cluster: 24
negated_best_sharpe: 0.22
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.92
---
# funds_from_operations_max_guidance (analyst4)

*The maximum guidance value for Funds from operation - annual*

## Signal Profile
- `rank(funds_from_operations_max_guidance)`: S=1.14, F=0.80, T=0.8%, INFERIOR (TOP3000)
- `rank(funds_from_operations_max_guidance / close)`: S=0.12, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(funds_from_operations_max_guidance, 5))`: S=0.54, F=0.21, T=33.7%, INFERIOR (TOP200)
- `-rank(funds_from_operations_max_guidance)`: S=0.19, F=0.08, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(funds_from_operations_max_guidance, 5))`: S=-0.54, F=-0.21, T=33.7%, INFERIOR (TOP3000)
- `-ts_zscore(funds_from_operations_max_guidance, 63)`: S=0.04, F=0.00, T=21.9%, INFERIOR (TOP3000)
- `ts_mean(funds_from_operations_max_guidance, 10)`: S=-0.22, F=-0.09, T=4.7%, INFERIOR (TOP3000)
- `rank(ts_rank(funds_from_operations_max_guidance, 22))`: S=-0.03, F=0.00, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * funds_from_operations_max_guidance)`: S=0.18, F=0.08, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * funds_from_operations_max_guidance / close)`: S=0.22, F=0.10, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.12, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.52 (moderate), ret=+2.1%
  - 2020: S=0.47 (weak), ret=+2.8%
  - 2021: S=1.97 (strong), ret=+9.5%
  - 2022: S=2.08 (strong), ret=+12.4%
  - 2023: S=0.57 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 4.72% over 280 days (recovered)
- Annualized: return +6.1%, volatility 5.5% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.08, excess kurtosis +2.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.11, max 2.63, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +5.11%; worst month: -3.32%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.89
- Sideways: S=2.42
- Bear: S=-0.67

## Negated Direction
Best negated: `rank(-1 * funds_from_operations_max_guidance / close)` S=0.22, F=0.10, INFERIOR
Direction gap: -0.92 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * funds_from_operations_max_guidance)`: S=0.18, F=0.08, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * funds_from_operations_max_guidance / close)`: S=0.22, F=0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(funds_from_operations_max_guidance, 5))`: S=-0.54, F=-0.21, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(funds_from_operations_max_guidance)` | TOP3000 | 1.12 | 0.80 | 4.7% | 100% | bull-only |
| `rank(ts_delta(funds_from_operations_max_guidance, 5))` | TOP200 | 0.56 | 0.21 | 16.2% | 40% | bear-only |
| `rank(funds_from_operations_max_guidance / close)` | TOP3000 | 0.12 | 0.04 | 51.0% | 60% | bull-only |

## Correlation Notes
Top correlates:
- min_funds_from_operations_guidance: 1.000 (strongly positively correlated)
- cap: 0.296 (weakly positively correlated)
- news_cap: 0.292 (weakly positively correlated)
- fnd6_cptmfmq_ceqq: 0.275 (weakly positively correlated)
- equity: 0.275 (weakly positively correlated)

Redundancy cluster #24: 2 similar fields, mean |rho| 1.0 (representative: min_funds_from_operations_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_fopo | fundamental6 | -0.07 | 1.61 | +0.49 | -0.96 | yes |
| fn_comp_options_forfeitures_and_expirations_a | fundamental2 | -0.06 | 1.66 | +0.49 | -0.46 | yes |
| fnd6_rank | fundamental6 | -0.16 | 1.69 | +0.53 | -0.01 | yes |
| fnd6_tlcf | fundamental6 | -0.03 | 1.59 | +0.47 | -0.42 | yes |
| news_close_vol | news12 | -0.08 | 1.69 | +0.50 | +0.95 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
