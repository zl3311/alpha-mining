---
field: fnd6_newa1v1300_lco
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0782
ann_vol: 0.0658
hit_rate: 0.4866
rolling_sharpe_min: -1.037
rolling_sharpe_max: 2.711
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.29
negated_best_template: neg_rank_level
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.61
---
# fnd6_newa1v1300_lco (fundamental6)

*Current Liabilities - Other - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_lco)`: S=0.69, F=0.50, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_lco / close)`: S=0.90, F=0.62, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_lco, 5))`: S=0.07, F=0.01, T=35.7%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_lco)`: S=-0.31, F=-0.16, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_lco, 5))`: S=-0.21, F=-0.07, T=35.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_lco, 63)`: S=0.21, F=0.07, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_lco, 10)`: S=-0.02, F=0.00, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_lco, 22))`: S=0.08, F=0.02, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lco)`: S=0.29, F=0.17, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lco / close)`: S=0.17, F=0.07, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.90, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.20 (negative), ret=-0.9%
  - 2020: S=0.76 (moderate), ret=+5.5%
  - 2021: S=1.67 (strong), ret=+13.4%
  - 2022: S=1.32 (moderate), ret=+8.9%
  - 2023: S=0.41 (weak), ret=+2.0%

## Risk & Drawdown
- Max drawdown: 7.82% over 490 days (recovered)
- Annualized: return +5.9%, volatility 6.6% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.58, excess kurtosis +2.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.04, max 2.71, latest 0.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.47%; worst month: -3.42%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.83
- Sideways: S=0.08
- Bear: S=-0.83

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_lco)` S=0.29, F=0.17, INFERIOR
Direction gap: -0.61 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_lco)`: S=0.29, F=0.17, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lco / close)`: S=0.17, F=0.07, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_lco, 5))`: S=-0.21, F=-0.07, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_lco / close)` | TOP3000 | 0.90 | 0.62 | 7.8% | 80% | bull-only |
| `rank(fnd6_newa1v1300_lco)` | TOP3000 | 0.69 | 0.50 | 23.8% | 80% | bull-only |
| `rank(fnd6_newa1v1300_lco / close)` | TOP1000 | 0.47 | 0.27 | 11.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_lco)` | TOP1000 | 0.30 | 0.16 | 29.4% | 60% | bull-only |
| `rank(fnd6_newa1v1300_lco / close)` | TOP500 | 0.20 | 0.08 | 25.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_lct: 0.981 (strongly positively correlated)
- fnd6_newqv1300_lcoq: 0.978 (strongly positively correlated)
- fnd6_cptmfmq_lctq: 0.974 (strongly positively correlated)
- fnd6_cptnewqv1300_lctq: 0.974 (strongly positively correlated)
- liabilities_curr: 0.974 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.33 | 1.78 | +0.60 | -0.58 | yes |
| rp_ess_revenue | news18 | -0.33 | 1.48 | +0.58 | -0.53 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.25 | 1.32 | +0.43 | -0.96 | yes |
| max_gross_income_guidance | analyst4 | -0.18 | 1.34 | +0.44 | -0.66 | yes |
| anl4_capex_high | analyst4 | -0.16 | 1.39 | +0.47 | -0.36 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
