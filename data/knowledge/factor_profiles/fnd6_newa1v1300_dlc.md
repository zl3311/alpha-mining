---
field: fnd6_newa1v1300_dlc
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.98
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0738
ann_vol: 0.0566
hit_rate: 0.4955
rolling_sharpe_min: -1.088
rolling_sharpe_max: 2.461
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.35
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.63
---
# fnd6_newa1v1300_dlc (fundamental6)

*Debt in Current Liabilities - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_dlc)`: S=0.69, F=0.46, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_dlc / close)`: S=0.98, F=0.65, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_dlc, 5))`: S=-0.19, F=-0.04, T=36.1%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_dlc)`: S=-0.35, F=-0.18, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dlc, 5))`: S=0.35, F=0.13, T=33.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_dlc, 63)`: S=0.44, F=0.23, T=18.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_dlc, 10)`: S=0.24, F=0.11, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_dlc, 22))`: S=-0.05, F=-0.01, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dlc)`: S=-0.13, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dlc / close)`: S=-0.27, F=-0.12, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.98, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.03 (moderate), ret=+2.9%
  - 2020: S=0.42 (weak), ret=+2.6%
  - 2021: S=1.42 (moderate), ret=+10.2%
  - 2022: S=1.53 (strong), ret=+9.5%
  - 2023: S=0.48 (weak), ret=+1.9%

## Risk & Drawdown
- Max drawdown: 7.38% over 237 days (recovered)
- Annualized: return +5.5%, volatility 5.7% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.48, excess kurtosis +2.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 2.46, latest 0.48

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.31%; worst month: -3.43%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.05
- Sideways: S=0.77
- Bear: S=-1.33

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_dlc, 5))` S=0.35, F=0.13, INFERIOR
Direction gap: -0.63 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_dlc)`: S=-0.13, F=-0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dlc / close)`: S=-0.27, F=-0.12, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dlc, 5))`: S=0.35, F=0.13, T=33.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_dlc / close)` | TOP3000 | 0.98 | 0.65 | 7.4% | 100% | bull-only |
| `rank(fnd6_newa1v1300_dlc)` | TOP3000 | 0.68 | 0.46 | 17.7% | 80% | bull-only |
| `rank(fnd6_newa1v1300_dlc / close)` | TOP1000 | 0.54 | 0.32 | 13.6% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dlc)` | TOP1000 | 0.35 | 0.18 | 21.5% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dlc / close)` | TOP500 | 0.26 | 0.12 | 17.9% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dlc)` | TOP500 | 0.12 | 0.04 | 32.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dd1: 0.970 (strongly positively correlated)
- fnd6_mfmq_dlcq: 0.957 (strongly positively correlated)
- fnd6_newqv1300_dlcq: 0.957 (strongly positively correlated)
- debt_st: 0.957 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.937 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.34 | 1.79 | +0.61 | -0.81 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.50 | +0.53 | -0.76 | yes |
| anl4_rd_exp_flag | analyst4 | -0.25 | 1.54 | +0.51 | -0.74 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.27 | 1.50 | +0.52 | -0.53 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.18 | 1.45 | +0.47 | -0.87 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
