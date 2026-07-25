---
field: cashflow_per_share_minimum
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.78
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.0846
ann_vol: 0.046
hit_rate: 0.5247
rolling_sharpe_min: -1.394
rolling_sharpe_max: 2.866
top_merge_partner: fn_def_tax_assets_liab_net_a
redundancy_cluster: 9
negated_best_sharpe: 0.38
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.4
---
# cashflow_per_share_minimum (analyst4)

*Cash Flow Per Share - The lowest estimation, delay 1 quarter*

## Signal Profile
- `rank(cashflow_per_share_minimum)`: S=0.29, F=0.12, T=0.9%, INFERIOR (TOP3000)
- `rank(cashflow_per_share_minimum / close)`: S=0.78, F=0.55, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(cashflow_per_share_minimum, 5))`: S=0.85, F=0.28, T=35.8%, INFERIOR (TOP3000)
- `-rank(cashflow_per_share_minimum)`: S=-0.01, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_minimum, 5))`: S=0.37, F=0.12, T=33.8%, INFERIOR (TOP3000)
- `ts_zscore(cashflow_per_share_minimum, 22)`: S=0.51, F=0.19, T=33.0%, INFERIOR (TOP3000)
- `ts_mean(cashflow_per_share_minimum, 10)`: S=-0.05, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_per_share_minimum, 22))`: S=0.12, F=0.02, T=13.3%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_minimum)`: S=0.36, F=0.18, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_minimum / close)`: S=0.38, F=0.23, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.85, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.65 (strong), ret=+6.2%
  - 2020: S=0.91 (moderate), ret=+4.6%
  - 2021: S=0.42 (weak), ret=+2.0%
  - 2022: S=0.73 (moderate), ret=+3.6%
  - 2023: S=0.76 (moderate), ret=+2.9%

## Risk & Drawdown
- Max drawdown: 8.46% over 949 days (recovered)
- Annualized: return +3.9%, volatility 4.6% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +0.00, excess kurtosis +1.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.39, max 2.87, latest 0.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +5.72%; worst month: -3.18%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.65
- Sideways: S=1.08
- Bear: S=-0.10

## Negated Direction
Best negated: `rank(-1 * cashflow_per_share_minimum / close)` S=0.38, F=0.23, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cashflow_per_share_minimum)`: S=0.36, F=0.18, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_per_share_minimum / close)`: S=0.38, F=0.23, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_per_share_minimum, 5))`: S=0.37, F=0.12, T=33.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(cashflow_per_share_minimum, 5))` | TOP3000 | 0.85 | 0.28 | 8.5% | 100% | mixed |
| `rank(ts_delta(cashflow_per_share_minimum, 5))` | TOP1000 | 0.42 | 0.10 | 7.1% | 80% | mixed |

## Correlation Notes
Top correlates:
- cashflow_per_share_median_value: 0.902 (strongly positively correlated)
- cashflow_per_share_maximum: 0.817 (strongly positively correlated)
- anl4_qf_az_wol_spfc: 0.739 (strongly positively correlated)
- anl4_qfd1_az_wol_spfc: 0.739 (strongly positively correlated)
- est_cashflow_ps: 0.606 (moderately positively correlated)

Redundancy cluster #9: 4 similar fields, mean |rho| 0.783 (representative: anl4_qfd1_az_wol_spfc). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.26 | 1.42 | +0.51 | -0.57 | yes |
| parkinson_volatility_90 | option8 | -0.20 | 1.33 | +0.44 | -0.86 | yes |
| fn_comp_non_opt_forfeited_a | fundamental2 | -0.15 | 1.29 | +0.44 | -0.78 | yes |
| fnd6_dm | fundamental6 | -0.15 | 1.42 | +0.42 | -0.89 | yes |
| fnd2_a_ltrmdmrepopliny5 | fundamental2 | -0.12 | 1.30 | +0.43 | -0.71 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
