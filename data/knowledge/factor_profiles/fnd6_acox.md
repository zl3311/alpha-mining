---
field: fnd6_acox
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 1.01
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.0523
ann_vol: 0.0609
hit_rate: 0.502
rolling_sharpe_min: -0.766
rolling_sharpe_max: 2.89
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.4
negated_best_template: neg_rank_level
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -0.61
---
# fnd6_acox (fundamental6)

*Current Assets - Other - Sundry*

## Signal Profile
- `rank(fnd6_acox)`: S=0.69, F=0.49, T=1.1%, INFERIOR (TOP3000)
- `rank(fnd6_acox / close)`: S=1.01, F=0.71, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_acox, 5))`: S=0.55, F=0.23, T=35.4%, INFERIOR (TOP1000)
- `-rank(fnd6_acox)`: S=-0.29, F=-0.14, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_acox, 5))`: S=-0.33, F=-0.15, T=34.9%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_acox, 63)`: S=0.73, F=0.48, T=19.0%, INFERIOR (TOP3000)
- `ts_mean(fnd6_acox, 10)`: S=-0.32, F=-0.16, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_acox, 22))`: S=0.63, F=0.34, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acox)`: S=0.40, F=0.28, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acox / close)`: S=0.30, F=0.16, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.00, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.45 (weak), ret=+1.7%
  - 2020: S=-0.15 (negative), ret=-1.0%
  - 2021: S=1.92 (strong), ret=+15.8%
  - 2022: S=1.96 (strong), ret=+11.7%
  - 2023: S=0.41 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 5.23% over 207 days (recovered)
- Annualized: return +6.1%, volatility 6.1% (fraction of booksize)
- Hit rate: 50.2% positive days
- Tail shape: skew +0.47, excess kurtosis +3.32

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.77, max 2.89, latest 0.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.64%; worst month: -2.62%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.92
- Sideways: S=0.21
- Bear: S=-0.67

## Negated Direction
Best negated: `rank(-1 * fnd6_acox)` S=0.40, F=0.28, INFERIOR
Direction gap: -0.61 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_acox)`: S=0.40, F=0.28, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_acox / close)`: S=0.30, F=0.16, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_acox, 5))`: S=-0.33, F=-0.15, T=34.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_acox / close)` | TOP3000 | 1.00 | 0.71 | 5.2% | 80% | bull-only |
| `rank(fnd6_acox)` | TOP3000 | 0.68 | 0.49 | 26.9% | 80% | bull-only |
| `rank(fnd6_acox / close)` | TOP1000 | 0.50 | 0.28 | 11.8% | 80% | bull-only |
| `rank(ts_delta(fnd6_acox, 5))` | TOP1000 | 0.57 | 0.23 | 15.1% | 60% | bear-only |
| `rank(fnd6_acox / close)` | TOP500 | 0.40 | 0.22 | 24.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_acox, 5))` | TOP200 | 0.38 | 0.18 | 53.0% | 80% | mixed |
| `rank(fnd6_acox)` | TOP1000 | 0.28 | 0.14 | 30.7% | 60% | bull-only |
| `rank(fnd6_acox)` | TOP500 | 0.09 | 0.03 | 45.9% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_acodo: 0.999 (strongly positively correlated)
- fnd6_newa1v1300_aco: 0.953 (strongly positively correlated)
- fnd6_newa1v1300_lct: 0.943 (strongly positively correlated)
- fnd6_cptmfmq_lctq: 0.938 (strongly positively correlated)
- fnd6_cptnewqv1300_lctq: 0.938 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.32 | 1.81 | +0.63 | -0.77 | yes |
| rp_ess_revenue | news18 | -0.33 | 1.52 | +0.52 | -0.83 | yes |
| anl4_rd_exp_flag | analyst4 | -0.22 | 1.55 | +0.53 | -0.66 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.17 | 1.48 | +0.47 | -0.88 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.16 | 2.07 | +0.44 | -0.58 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
