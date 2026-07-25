---
field: fnd6_dltis
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.29
best_fitness: 0.93
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0533
ann_vol: 0.0507
hit_rate: 0.5198
rolling_sharpe_min: -0.726
rolling_sharpe_max: 3.132
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 12
negated_best_sharpe: 0.94
negated_best_template: rank_neg_delta
negated_best_fitness: 0.57
n_negated_sims: 10
direction_gap: -0.35
---
# fnd6_dltis (fundamental6)

*Long-Term Debt - Issuance*

## Signal Profile
- `rank(fnd6_dltis)`: S=0.99, F=0.67, T=1.4%, INFERIOR (TOP3000)
- `rank(fnd6_dltis / close)`: S=1.29, F=0.93, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dltis, 5))`: S=0.20, F=0.05, T=35.0%, INFERIOR (TOP3000)
- `-rank(fnd6_dltis)`: S=-0.52, F=-0.27, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dltis, 5))`: S=0.94, F=0.57, T=34.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dltis, 63)`: S=-0.24, F=-0.10, T=17.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dltis, 10)`: S=-0.18, F=-0.07, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dltis, 22))`: S=0.39, F=0.18, T=15.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dltis)`: S=-0.52, F=-0.27, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dltis / close)`: S=-0.63, F=-0.35, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.28, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.02 (moderate), ret=+3.0%
  - 2020: S=0.94 (moderate), ret=+5.8%
  - 2021: S=2.15 (strong), ret=+13.9%
  - 2022: S=1.08 (moderate), ret=+5.4%
  - 2023: S=1.23 (moderate), ret=+3.8%

## Risk & Drawdown
- Max drawdown: 5.33% over 582 days (not yet recovered, ongoing at window end)
- Annualized: return +6.5%, volatility 5.1% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.38, excess kurtosis +2.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.73, max 3.13, latest 1.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.15%; worst month: -3.23%
Positive months: 66%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.97
- Sideways: S=0.60
- Bear: S=-0.08

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dltis, 5))` S=0.94, F=0.57, INFERIOR
Direction gap: -0.35 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_dltis)`: S=-0.52, F=-0.27, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dltis / close)`: S=-0.63, F=-0.35, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dltis, 5))`: S=0.94, F=0.57, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dltis / close)` | TOP3000 | 1.28 | 0.93 | 5.3% | 100% | mixed |
| `rank(fnd6_dltis)` | TOP3000 | 0.99 | 0.67 | 8.3% | 80% | bull-only |
| `rank(fnd6_dltis / close)` | TOP1000 | 0.62 | 0.35 | 7.1% | 80% | mixed |
| `rank(fnd6_dltis)` | TOP1000 | 0.52 | 0.27 | 9.7% | 60% | bull-only |
| `rank(fnd6_dltis / close)` | TOP500 | 0.34 | 0.15 | 14.2% | 80% | bull-only |
| `rank(fnd6_dltis)` | TOP200 | 0.19 | 0.09 | 21.8% | 40% | bull-only |
| `rank(fnd6_dltis)` | TOP500 | 0.22 | 0.09 | 16.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_dltis, 5))` | TOP3000 | 0.18 | 0.05 | 17.1% | 40% | mixed |
| `rank(fnd6_dltis / close)` | TOP200 | 0.13 | 0.05 | 24.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dltt: 0.929 (strongly positively correlated)
- fnd6_cptmfmq_dlttq: 0.924 (strongly positively correlated)
- debt_lt: 0.924 (strongly positively correlated)
- fnd6_cptnewqv1300_dlttq: 0.924 (strongly positively correlated)
- fnd6_dltr: 0.918 (strongly positively correlated)

Redundancy cluster #12: 12 similar fields, mean |rho| 0.749 (representative: fnd6_dlto). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.32 | 1.90 | +0.62 | -0.84 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.18 | 1.88 | +0.60 | +0.45 | yes |
| implied_volatility_call_20 | option8 | -0.03 | 1.80 | +0.52 | -0.42 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | -0.02 | 1.95 | +0.50 | -0.53 | yes |
| anl4_qf_az_wol_spfc | analyst4 | -0.02 | 1.95 | +0.50 | -0.53 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
