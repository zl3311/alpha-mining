---
field: fnd6_newqv1300_altoq
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.83
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.0973
ann_vol: 0.0715
hit_rate: 0.5028
rolling_sharpe_min: -0.802
rolling_sharpe_max: 2.437
top_merge_partner: rp_ess_revenue
redundancy_cluster: 1
negated_best_sharpe: 0.02
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.81
---
# fnd6_newqv1300_altoq (fundamental6)

*Other Long-term Assets*

## Signal Profile
- `rank(fnd6_newqv1300_altoq)`: S=0.61, F=0.43, T=2.2%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_altoq / close)`: S=0.83, F=0.57, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_altoq, 5))`: S=0.92, F=0.32, T=39.1%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_altoq)`: S=-0.38, F=-0.23, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_altoq, 5))`: S=0.03, F=0.00, T=39.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_altoq, 63)`: S=-0.21, F=-0.04, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_altoq, 10)`: S=-0.05, F=-0.01, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_altoq, 22))`: S=-0.03, F=0.00, T=17.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_altoq)`: S=0.02, F=0.00, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_altoq / close)`: S=-0.15, F=-0.06, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/23P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/16P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.83, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.07 (negative), ret=-0.3%
  - 2020: S=-0.13 (negative), ret=-1.0%
  - 2021: S=1.19 (moderate), ret=+11.5%
  - 2022: S=1.94 (strong), ret=+14.3%
  - 2023: S=1.06 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 9.73% over 273 days (recovered)
- Annualized: return +5.9%, volatility 7.1% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.40, excess kurtosis +3.31

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.80, max 2.44, latest 1.04

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.50%; worst month: -2.89%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.74
- Sideways: S=1.01
- Bear: S=-1.72

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_altoq)` S=0.02, F=0.00, INFERIOR
Direction gap: -0.81 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_altoq)`: S=0.02, F=0.00, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_altoq / close)`: S=-0.15, F=-0.06, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_altoq, 5))`: S=0.03, F=0.00, T=39.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_altoq / close)` | TOP3000 | 0.83 | 0.57 | 9.7% | 60% | bull-only |
| `rank(fnd6_newqv1300_altoq / close)` | TOP1000 | 0.62 | 0.44 | 14.1% | 80% | bull-only |
| `rank(fnd6_newqv1300_altoq)` | TOP3000 | 0.60 | 0.43 | 29.3% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_altoq, 5))` | TOP3000 | 0.94 | 0.32 | 8.2% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_altoq, 5))` | TOP1000 | 0.72 | 0.25 | 10.4% | 60% | mixed |
| `rank(fnd6_newqv1300_altoq / close)` | TOP500 | 0.39 | 0.23 | 31.3% | 80% | bull-only |
| `rank(fnd6_newqv1300_altoq)` | TOP1000 | 0.37 | 0.23 | 32.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_altoq)` | TOP500 | 0.13 | 0.06 | 50.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_altoq, 5))` | TOP500 | 0.26 | 0.06 | 16.6% | 60% | mixed |
| `rank(fnd6_newqv1300_altoq / close)` | TOP200 | 0.15 | 0.06 | 36.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ao: 0.987 (strongly positively correlated)
- fnd6_aodo: 0.985 (strongly positively correlated)
- fnd6_aox: 0.984 (strongly positively correlated)
- fnd6_newqv1300_aoq: 0.961 (strongly positively correlated)
- fnd6_newqv1300_ancq: 0.954 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_ess_revenue | news18 | -0.35 | 1.47 | +0.58 | -0.58 | yes |
| anl4_rd_exp_flag | analyst4 | -0.34 | 1.59 | +0.56 | -0.59 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.31 | 1.35 | +0.52 | -0.66 | yes |
| anl4_epsr_flag | analyst4 | -0.31 | 1.71 | +0.54 | -0.34 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.25 | 1.32 | +0.49 | -0.67 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
