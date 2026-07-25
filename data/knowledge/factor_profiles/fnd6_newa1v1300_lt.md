---
field: fnd6_newa1v1300_lt
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.01
best_fitness: 0.82
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0848
ann_vol: 0.0817
hit_rate: 0.4955
rolling_sharpe_min: -0.803
rolling_sharpe_max: 2.696
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.54
negated_best_template: rank_neg_delta
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.47
---
# fnd6_newa1v1300_lt (fundamental6)

*Liabilities - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_lt)`: S=0.75, F=0.61, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_lt / close)`: S=1.01, F=0.82, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_lt, 5))`: S=-0.39, F=-0.13, T=35.8%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_lt)`: S=-0.38, F=-0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_lt, 5))`: S=0.54, F=0.24, T=34.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_lt, 22)`: S=0.07, F=0.02, T=28.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_lt, 10)`: S=0.23, F=0.09, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_lt, 22))`: S=0.48, F=0.24, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lt)`: S=-0.38, F=-0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lt / close)`: S=-0.61, F=-0.44, T=1.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.01, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.14 (weak), ret=+0.7%
  - 2020: S=0.58 (moderate), ret=+5.6%
  - 2021: S=1.67 (strong), ret=+17.5%
  - 2022: S=1.64 (strong), ret=+12.9%
  - 2023: S=0.70 (moderate), ret=+3.8%

## Risk & Drawdown
- Max drawdown: 8.48% over 236 days (recovered)
- Annualized: return +8.2%, volatility 8.2% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.58, excess kurtosis +3.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.80, max 2.70, latest 0.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.64%; worst month: -3.29%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.93
- Sideways: S=0.45
- Bear: S=-0.82

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_lt, 5))` S=0.54, F=0.24, INFERIOR
Direction gap: -0.47 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_lt)`: S=-0.38, F=-0.24, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_lt / close)`: S=-0.61, F=-0.44, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_lt, 5))`: S=0.54, F=0.24, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_lt / close)` | TOP3000 | 1.01 | 0.82 | 8.5% | 100% | bull-only |
| `rank(fnd6_newa1v1300_lt)` | TOP3000 | 0.74 | 0.61 | 26.7% | 80% | bull-only |
| `rank(fnd6_newa1v1300_lt / close)` | TOP1000 | 0.61 | 0.44 | 14.1% | 80% | bull-only |
| `rank(fnd6_newa1v1300_lt)` | TOP1000 | 0.38 | 0.24 | 31.7% | 60% | bull-only |
| `rank(fnd6_newa1v1300_lt / close)` | TOP500 | 0.38 | 0.23 | 22.5% | 60% | bull-only |
| `rank(fnd6_newa1v1300_lt)` | TOP500 | 0.15 | 0.07 | 47.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_ltq: 0.993 (strongly positively correlated)
- liabilities: 0.993 (strongly positively correlated)
- fnd6_newqv1300_ltmibq: 0.992 (strongly positively correlated)
- fnd6_newa1v1300_dpc: 0.981 (strongly positively correlated)
- fnd6_mfma1_dpc: 0.981 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 1.93 | +0.76 | -0.61 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.64 | +0.63 | -0.65 | yes |
| anl4_rd_exp_flag | analyst4 | -0.26 | 1.65 | +0.63 | -0.30 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.20 | 1.54 | +0.53 | -0.62 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.29 | 1.49 | +0.48 | -0.90 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
