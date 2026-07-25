---
field: anl4_dts_rspe
dataset: analyst4
best_template: rank_level
best_sharpe: 0.88
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0975
ann_vol: 0.0449
hit_rate: 0.5182
rolling_sharpe_min: -1.77
rolling_sharpe_max: 3.394
top_merge_partner: fn_def_tax_assets_liab_net_a
redundancy_cluster: 22
negated_best_sharpe: 0.41
negated_best_template: neg_rank
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: -0.47
---
# anl4_dts_rspe (analyst4)

*Reported Earnings per share - standard deviation of estimations*

## Signal Profile
- `rank(anl4_dts_rspe)`: S=0.88, F=0.49, T=4.8%, INFERIOR (TOP3000)
- `rank(anl4_dts_rspe / close)`: S=0.22, F=0.09, T=5.2%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_dts_rspe, 5))`: S=-0.04, F=0.00, T=39.4%, INFERIOR (TOP500)
- `-rank(anl4_dts_rspe)`: S=0.41, F=0.17, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_dts_rspe, 5))`: S=0.42, F=0.15, T=37.3%, INFERIOR (TOP3000)
- `ts_zscore(anl4_dts_rspe, 22)`: S=0.37, F=0.10, T=34.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_dts_rspe, 10)`: S=0.30, F=0.15, T=4.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_dts_rspe, 22))`: S=0.42, F=0.14, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_dts_rspe)`: S=-0.10, F=-0.03, T=6.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_dts_rspe / close)`: S=-0.10, F=-0.03, T=7.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.88, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+0.9%
  - 2020: S=0.29 (weak), ret=+1.3%
  - 2021: S=0.06 (weak), ret=+0.3%
  - 2022: S=2.23 (strong), ret=+10.4%
  - 2023: S=1.66 (strong), ret=+6.5%

## Risk & Drawdown
- Max drawdown: 9.75% over 627 days (recovered)
- Annualized: return +4.0%, volatility 4.5% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.34, excess kurtosis +2.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.77, max 3.39, latest 1.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +3.23%; worst month: -3.59%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.54
- Sideways: S=1.03
- Bear: S=-0.79

## Negated Direction
Best negated: `-rank(anl4_dts_rspe)` S=0.41, F=0.17, INFERIOR
Direction gap: -0.47 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_dts_rspe)`: S=-0.10, F=-0.03, T=6.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_dts_rspe / close)`: S=-0.10, F=-0.03, T=7.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_dts_rspe, 5))`: S=0.42, F=0.15, T=37.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_dts_rspe)` | TOP3000 | 0.88 | 0.49 | 9.8% | 100% | bull-only |
| `rank(anl4_dts_rspe / close)` | TOP3000 | 0.22 | 0.09 | 18.3% | 40% | mixed |
| `rank(anl4_dts_rspe / close)` | TOP500 | 0.09 | 0.03 | 24.5% | 80% | weak |
| `rank(anl4_dts_rspe)` | TOP200 | 0.08 | 0.03 | 19.4% | 60% | bull-only |
| `rank(anl4_dts_rspe / close)` | TOP200 | 0.10 | 0.03 | 27.0% | 80% | mixed |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_dts_spe: 0.715 (strongly positively correlated)
- anl4_qf_az_dts_spe: 0.715 (strongly positively correlated)
- anl4_dts_ptp: 0.627 (moderately positively correlated)
- anl4_netprofit_std: 0.608 (moderately positively correlated)
- anl4_ebit_std: 0.598 (moderately positively correlated)

Redundancy cluster #22: 3 similar fields, mean |rho| 0.81 (representative: anl4_qfd1_az_dts_spe). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.14 | 1.35 | +0.44 | -0.12 | yes |
| snt_value_fast_d1 | socialmedia12 | -0.05 | 1.28 | +0.40 | +0.06 | yes |
| news_low_exc_stddev | news12 | -0.06 | 1.30 | +0.36 | -0.34 | yes |
| fnd6_txtubadjust | fundamental6 | -0.02 | 1.18 | +0.30 | -0.89 | yes |
| fn_op_lease_min_pay_due_in_5y_a | fundamental2 | +0.12 | 1.17 | +0.28 | -0.94 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
