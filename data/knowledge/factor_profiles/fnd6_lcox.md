---
field: fnd6_lcox
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.07
best_fitness: 0.69
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.054
ann_vol: 0.0495
hit_rate: 0.4988
rolling_sharpe_min: -0.976
rolling_sharpe_max: 3.122
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.24
negated_best_template: neg_rank_level
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.83
---
# fnd6_lcox (fundamental6)

*Current Liabilities - Other - Sundry*

## Signal Profile
- `rank(fnd6_lcox)`: S=0.73, F=0.47, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_lcox / close)`: S=1.07, F=0.69, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_lcox, 5))`: S=0.68, F=0.35, T=34.8%, INFERIOR (TOP500)
- `-rank(fnd6_lcox)`: S=-0.30, F=-0.13, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lcox, 5))`: S=-0.12, F=-0.03, T=36.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_lcox, 22)`: S=0.50, F=0.27, T=30.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_lcox, 10)`: S=-0.04, F=-0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_lcox, 22))`: S=0.01, F=0.00, T=15.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lcox)`: S=0.24, F=0.12, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lcox / close)`: S=0.19, F=0.07, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.07, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.47 (negative), ret=-1.6%
  - 2020: S=0.76 (moderate), ret=+3.7%
  - 2021: S=2.21 (strong), ret=+13.6%
  - 2022: S=1.79 (strong), ret=+9.8%
  - 2023: S=0.12 (weak), ret=+0.4%

## Risk & Drawdown
- Max drawdown: 5.40% over 427 days (recovered)
- Annualized: return +5.3%, volatility 5.0% (fraction of booksize)
- Hit rate: 49.9% positive days
- Tail shape: skew +0.46, excess kurtosis +2.16

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.98, max 3.12, latest 0.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.16%; worst month: -2.70%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.19
- Sideways: S=0.32
- Bear: S=-0.96

## Negated Direction
Best negated: `rank(-1 * fnd6_lcox)` S=0.24, F=0.12, INFERIOR
Direction gap: -0.83 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_lcox)`: S=0.24, F=0.12, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_lcox / close)`: S=0.19, F=0.07, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_lcox, 5))`: S=-0.12, F=-0.03, T=36.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_lcox / close)` | TOP3000 | 1.07 | 0.69 | 5.4% | 80% | bull-only |
| `rank(fnd6_lcox)` | TOP3000 | 0.73 | 0.47 | 16.1% | 80% | bull-only |
| `rank(ts_delta(fnd6_lcox, 5))` | TOP500 | 0.68 | 0.35 | 12.5% | 80% | all-weather |
| `rank(fnd6_lcox / close)` | TOP1000 | 0.45 | 0.22 | 8.8% | 40% | bull-only |
| `rank(fnd6_lcox)` | TOP1000 | 0.29 | 0.13 | 23.6% | 40% | bull-only |
| `rank(ts_delta(fnd6_lcox, 5))` | TOP1000 | 0.24 | 0.06 | 20.6% | 60% | mixed |
| `rank(ts_delta(fnd6_lcox, 5))` | TOP200 | 0.16 | 0.04 | 56.2% | 60% | weak |
| `rank(fnd6_lcox / close)` | TOP500 | 0.11 | 0.03 | 22.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_lco: 0.935 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.922 (strongly positively correlated)
- fnd6_cptmfmq_lctq: 0.917 (strongly positively correlated)
- liabilities_curr: 0.917 (strongly positively correlated)
- fnd6_cptnewqv1300_lctq: 0.917 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.26 | 1.72 | +0.55 | -0.64 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.25 | 1.77 | +0.61 | +0.47 | yes |
| anl4_cfo_flag | analyst4 | -0.11 | 1.62 | +0.51 | -0.90 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.22 | 1.57 | +0.50 | +0.07 | yes |
| anl4_capex_flag | analyst4 | -0.03 | 1.55 | +0.46 | -0.39 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
