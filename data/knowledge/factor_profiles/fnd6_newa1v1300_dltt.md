---
field: fnd6_newa1v1300_dltt
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.2
best_fitness: 1.06
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.0735
ann_vol: 0.0813
hit_rate: 0.5109
rolling_sharpe_min: -0.521
rolling_sharpe_max: 2.906
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.91
negated_best_template: rank_neg_delta
negated_best_fitness: 0.63
n_negated_sims: 10
direction_gap: -0.29
---
# fnd6_newa1v1300_dltt (fundamental6)

*Long-Term Debt - Total*

## Signal Profile
- `rank(fnd6_newa1v1300_dltt)`: S=0.83, F=0.68, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_dltt / close)`: S=1.20, F=1.06, T=1.3%, AVERAGE (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_dltt, 5))`: S=-0.22, F=-0.05, T=36.0%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_dltt)`: S=-0.35, F=-0.21, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dltt, 5))`: S=0.91, F=0.63, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_dltt, 63)`: S=0.51, F=0.30, T=18.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_dltt, 10)`: S=0.26, F=0.11, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_dltt, 22))`: S=0.14, F=0.04, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dltt)`: S=0.12, F=0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dltt / close)`: S=0.00, F=0.00, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.20, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.68 (moderate), ret=+2.8%
  - 2020: S=0.78 (moderate), ret=+7.5%
  - 2021: S=1.76 (strong), ret=+19.0%
  - 2022: S=1.74 (strong), ret=+14.3%
  - 2023: S=0.89 (moderate), ret=+4.2%

## Risk & Drawdown
- Max drawdown: 7.35% over 260 days (recovered)
- Annualized: return +9.8%, volatility 8.1% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.46, excess kurtosis +3.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.52, max 2.91, latest 0.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +9.60%; worst month: -2.56%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.04
- Sideways: S=0.79
- Bear: S=-0.66

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_dltt, 5))` S=0.91, F=0.63, INFERIOR
Direction gap: -0.29 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_dltt)`: S=0.12, F=0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dltt / close)`: S=0.00, F=0.00, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dltt, 5))`: S=0.91, F=0.63, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_dltt / close)` | TOP3000 | 1.20 | 1.06 | 7.3% | 100% | bull-only |
| `rank(fnd6_newa1v1300_dltt)` | TOP3000 | 0.82 | 0.68 | 20.9% | 80% | bull-only |
| `rank(fnd6_newa1v1300_dltt / close)` | TOP1000 | 0.62 | 0.44 | 12.2% | 80% | bull-only |
| `rank(fnd6_newa1v1300_dltt / close)` | TOP500 | 0.36 | 0.21 | 21.6% | 40% | bull-only |
| `rank(fnd6_newa1v1300_dltt)` | TOP1000 | 0.34 | 0.21 | 28.2% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dltt)` | TOP500 | 0.11 | 0.04 | 43.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptmfmq_dlttq: 0.990 (strongly positively correlated)
- debt_lt: 0.990 (strongly positively correlated)
- fnd6_cptnewqv1300_dlttq: 0.990 (strongly positively correlated)
- debt: 0.980 (strongly positively correlated)
- fnd6_newqv1300_lltq: 0.968 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.36 | 2.07 | +0.87 | -0.71 | yes |
| anl4_rd_exp_flag | analyst4 | -0.34 | 1.89 | +0.69 | -0.43 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.79 | +0.59 | -0.73 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.25 | 1.74 | +0.54 | -0.73 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.15 | 2.18 | +0.56 | -0.40 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
