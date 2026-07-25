---
field: fnd6_cld2
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.29
best_fitness: 0.96
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0706
ann_vol: 0.0537
hit_rate: 0.5158
rolling_sharpe_min: -0.537
rolling_sharpe_max: 3.042
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 14
negated_best_sharpe: 0.84
negated_best_template: rank_neg_delta
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: -0.45
---
# fnd6_cld2 (fundamental6)

*Capitalized Leases - Due in 2nd Year*

## Signal Profile
- `rank(fnd6_cld2)`: S=0.92, F=0.66, T=2.1%, INFERIOR (TOP3000)
- `rank(fnd6_cld2 / close)`: S=1.29, F=0.96, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_cld2, 5))`: S=0.29, F=0.11, T=33.0%, INFERIOR (TOP1000)
- `-rank(fnd6_cld2)`: S=-0.53, F=-0.30, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cld2, 5))`: S=0.84, F=0.58, T=41.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cld2, 63)`: S=0.44, F=0.36, T=13.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cld2, 10)`: S=0.53, F=0.41, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cld2, 22))`: S=0.21, F=0.10, T=20.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld2)`: S=-0.92, F=-0.66, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld2 / close)`: S=-1.29, F=-0.96, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.29, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.57 (strong), ret=+3.9%
  - 2020: S=1.27 (moderate), ret=+7.4%
  - 2021: S=1.88 (strong), ret=+11.6%
  - 2022: S=1.10 (moderate), ret=+6.6%
  - 2023: S=0.92 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 7.06% over 435 days (recovered)
- Annualized: return +6.9%, volatility 5.4% (fraction of booksize)
- Hit rate: 51.6% positive days
- Tail shape: skew +0.42, excess kurtosis +2.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.54, max 3.04, latest 0.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +5.89%; worst month: -2.32%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.44
- Sideways: S=1.45
- Bear: S=-0.04

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cld2, 5))` S=0.84, F=0.58, INFERIOR
Direction gap: -0.45 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cld2)`: S=-0.92, F=-0.66, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld2 / close)`: S=-1.29, F=-0.96, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cld2, 5))`: S=0.84, F=0.58, T=41.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cld2 / close)` | TOP3000 | 1.29 | 0.96 | 7.1% | 100% | mixed |
| `rank(fnd6_cld2)` | TOP3000 | 0.90 | 0.66 | 11.3% | 80% | bull-only |
| `rank(fnd6_cld2)` | TOP500 | 0.60 | 0.40 | 28.4% | 80% | bull-only |
| `rank(fnd6_cld2 / close)` | TOP500 | 0.59 | 0.36 | 14.1% | 60% | mixed |
| `rank(fnd6_cld2)` | TOP1000 | 0.53 | 0.30 | 20.8% | 80% | bull-only |
| `rank(fnd6_cld2 / close)` | TOP1000 | 0.51 | 0.27 | 12.2% | 100% | bull-only |
| `rank(fnd6_cld2 / close)` | TOP200 | 0.37 | 0.24 | 27.2% | 80% | bull-only |
| `rank(fnd6_cld2)` | TOP200 | 0.36 | 0.22 | 38.4% | 80% | bull-only |
| `rank(ts_delta(fnd6_cld2, 5))` | TOP1000 | 0.29 | 0.11 | 45.7% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_cld3: 0.953 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.707 (strongly positively correlated)
- fnd6_newa2v1300_ppent: 0.706 (strongly positively correlated)
- fnd6_newqv1300_ltmibq: 0.704 (strongly positively correlated)
- fnd6_cptnewqv1300_ltq: 0.703 (strongly positively correlated)

Redundancy cluster #14: 2 similar fields, mean |rho| 0.953 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.22 | 1.83 | +0.54 | -0.84 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.08 | 2.13 | +0.51 | -0.76 | yes |
| implied_volatility_call_120 | option8 | -0.05 | 1.95 | +0.55 | +0.52 | yes |
| implied_volatility_mean_60 | option8 | -0.02 | 1.88 | +0.55 | +0.48 | yes |
| implied_volatility_call_20 | option8 | -0.05 | 1.83 | +0.54 | +0.12 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
