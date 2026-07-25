---
field: fnd6_dd1q
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.12
best_fitness: 0.91
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.0897
ann_vol: 0.0746
hit_rate: 0.4972
rolling_sharpe_min: -1.018
rolling_sharpe_max: 2.841
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.93
negated_best_template: rank_neg_delta
negated_best_fitness: 0.36
n_negated_sims: 10
direction_gap: -0.19
---
# fnd6_dd1q (fundamental6)

*Long-Term Debt Due in 1 Year*

## Signal Profile
- `rank(fnd6_dd1q)`: S=0.90, F=0.76, T=3.1%, INFERIOR (TOP3000)
- `rank(fnd6_dd1q / close)`: S=1.12, F=0.91, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dd1q, 5))`: S=-0.42, F=-0.12, T=39.5%, INFERIOR (TOP1000)
- `-rank(fnd6_dd1q)`: S=-0.37, F=-0.22, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd1q, 5))`: S=0.93, F=0.36, T=39.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dd1q, 63)`: S=0.24, F=0.06, T=19.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dd1q, 10)`: S=-0.03, F=0.00, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dd1q, 22))`: S=0.03, F=0.00, T=17.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd1q)`: S=-0.90, F=-0.76, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd1q / close)`: S=-1.12, F=-0.91, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.12, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.42 (moderate), ret=+6.0%
  - 2020: S=0.34 (weak), ret=+2.9%
  - 2021: S=2.02 (strong), ret=+19.5%
  - 2022: S=1.23 (moderate), ret=+9.1%
  - 2023: S=0.66 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 8.97% over 217 days (recovered)
- Annualized: return +8.3%, volatility 7.5% (fraction of booksize)
- Hit rate: 49.7% positive days
- Tail shape: skew +0.48, excess kurtosis +2.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.02, max 2.84, latest 0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.96%; worst month: -3.28%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.82
- Sideways: S=0.61
- Bear: S=-0.44

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dd1q, 5))` S=0.93, F=0.36, INFERIOR
Direction gap: -0.19 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_dd1q)`: S=-0.90, F=-0.76, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dd1q / close)`: S=-1.12, F=-0.91, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dd1q, 5))`: S=0.93, F=0.36, T=39.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dd1q / close)` | TOP3000 | 1.12 | 0.91 | 9.0% | 100% | mixed |
| `rank(fnd6_dd1q)` | TOP3000 | 0.89 | 0.76 | 21.5% | 80% | bull-only |
| `rank(fnd6_dd1q / close)` | TOP1000 | 0.57 | 0.38 | 13.2% | 60% | bull-only |
| `rank(fnd6_dd1q)` | TOP1000 | 0.36 | 0.22 | 28.4% | 60% | bull-only |
| `rank(fnd6_dd1q / close)` | TOP500 | 0.16 | 0.06 | 19.8% | 60% | bull-only |
| `rank(fnd6_dd1q)` | TOP500 | 0.07 | 0.02 | 38.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_dlcq: 0.965 (strongly positively correlated)
- debt_st: 0.965 (strongly positively correlated)
- fnd6_mfmq_dlcq: 0.965 (strongly positively correlated)
- fnd6_dd1: 0.950 (strongly positively correlated)
- fnd6_newqv1300_ppentq: 0.949 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.35 | 1.98 | +0.81 | -0.96 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.69 | +0.58 | -0.93 | yes |
| anl4_rd_exp_flag | analyst4 | -0.27 | 1.72 | +0.61 | -0.63 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.19 | 1.61 | +0.49 | -0.93 | yes |
| implied_volatility_mean_10 | option8 | -0.08 | 1.69 | +0.47 | -0.82 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
