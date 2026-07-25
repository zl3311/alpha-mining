---
field: fnd6_newa1v1300_gp
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.82
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1116
ann_vol: 0.0873
hit_rate: 0.498
rolling_sharpe_min: -0.936
rolling_sharpe_max: 2.752
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.17
negated_best_template: neg_rank_level
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.65
---
# fnd6_newa1v1300_gp (fundamental6)

*Gross Profit (Loss)*

## Signal Profile
- `rank(fnd6_newa1v1300_gp)`: S=0.51, F=0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_gp / close)`: S=0.82, F=0.62, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_gp, 5))`: S=0.67, F=0.41, T=35.2%, INFERIOR (TOP200)
- `-rank(fnd6_newa1v1300_gp)`: S=-0.24, F=-0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_gp, 5))`: S=-0.62, F=-0.36, T=35.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa1v1300_gp, 22)`: S=0.17, F=0.06, T=30.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_gp, 10)`: S=0.20, F=0.09, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_gp, 22))`: S=0.43, F=0.21, T=14.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_gp)`: S=0.17, F=0.09, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_gp / close)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.82, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.17 (negative), ret=-0.8%
  - 2020: S=-0.23 (negative), ret=-2.0%
  - 2021: S=1.22 (moderate), ret=+14.4%
  - 2022: S=1.79 (strong), ret=+18.0%
  - 2023: S=1.11 (moderate), ret=+5.4%

## Risk & Drawdown
- Max drawdown: 11.16% over 294 days (recovered)
- Annualized: return +7.1%, volatility 8.7% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +0.32, excess kurtosis +2.72

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.94, max 2.75, latest 1.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.32%; worst month: -4.03%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.31
- Sideways: S=0.39
- Bear: S=-2.07

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_gp)` S=0.17, F=0.09, INFERIOR
Direction gap: -0.65 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_gp)`: S=0.17, F=0.09, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_gp / close)`: S=0.04, F=0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_gp, 5))`: S=-0.62, F=-0.36, T=35.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_gp / close)` | TOP3000 | 0.82 | 0.62 | 11.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_gp, 5))` | TOP200 | 0.68 | 0.41 | 24.7% | 80% | all-weather |
| `rank(fnd6_newa1v1300_gp)` | TOP3000 | 0.51 | 0.36 | 33.1% | 80% | bull-only |
| `rank(fnd6_newa1v1300_gp / close)` | TOP1000 | 0.49 | 0.33 | 17.1% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_gp, 5))` | TOP1000 | 0.63 | 0.27 | 14.8% | 80% | all-weather |
| `rank(fnd6_newa1v1300_gp)` | TOP1000 | 0.23 | 0.12 | 38.8% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_gp, 5))` | TOP3000 | 0.33 | 0.09 | 12.9% | 60% | mixed |
| `rank(fnd6_newa1v1300_gp / close)` | TOP500 | 0.19 | 0.09 | 34.9% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_gp, 5))` | TOP500 | 0.22 | 0.07 | 20.3% | 40% | all-weather |

## Correlation Notes
Top correlates:
- fnd6_mfma2_revt: 0.972 (strongly positively correlated)
- fnd6_newa2v1300_sale: 0.972 (strongly positively correlated)
- fnd6_newa2v1300_revt: 0.972 (strongly positively correlated)
- gross_income_total: 0.969 (strongly positively correlated)
- fnd6_cptmfmq_saleq: 0.964 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.39 | 1.66 | +0.64 | -0.57 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.50 | +0.61 | -0.61 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.31 | 1.37 | +0.55 | -0.69 | yes |
| max_adjusted_net_profit_guidance | analyst4 | -0.30 | 1.37 | +0.55 | -0.68 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.27 | 1.46 | +0.51 | -0.64 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
