---
field: fnd6_fopox
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.93
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.094
ann_vol: 0.0482
hit_rate: 0.5352
rolling_sharpe_min: -1.111
rolling_sharpe_max: 3.151
top_merge_partner: fn_def_tax_assets_liab_net_a
redundancy_cluster: 32
negated_best_sharpe: 0.64
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.29
---
# fnd6_fopox (fundamental6)

*Funds from Operations - Other excluding Option Tax Benefit*

## Signal Profile
- `rank(fnd6_fopox)`: S=1.05, F=0.67, T=1.5%, INFERIOR (TOP3000)
- `rank(fnd6_fopox / close)`: S=0.92, F=0.61, T=2.4%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_fopox, 5))`: S=0.19, F=0.06, T=34.1%, INFERIOR (TOP500)
- `-rank(fnd6_fopox)`: S=-0.83, F=-0.49, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fopox, 5))`: S=0.64, F=0.31, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_fopox, 63)`: S=0.93, F=0.71, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_fopox, 10)`: S=0.74, F=0.45, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_fopox, 22))`: S=-0.25, F=-0.09, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fopox)`: S=-0.83, F=-0.49, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fopox / close)`: S=-0.93, F=-0.59, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.06, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.23 (moderate), ret=+3.2%
  - 2020: S=0.50 (moderate), ret=+2.0%
  - 2021: S=1.10 (moderate), ret=+8.5%
  - 2022: S=0.84 (moderate), ret=+3.6%
  - 2023: S=2.19 (strong), ret=+7.7%

## Risk & Drawdown
- Max drawdown: 9.40% over 165 days (recovered)
- Annualized: return +5.1%, volatility 4.8% (fraction of booksize)
- Hit rate: 53.5% positive days
- Tail shape: skew -0.01, excess kurtosis +3.89

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 3.15, latest 2.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2020
Best month: +4.14%; worst month: -1.95%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.38
- Sideways: S=1.98
- Bear: S=-1.18

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_fopox, 5))` S=0.64, F=0.31, INFERIOR
Direction gap: -0.29 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_fopox)`: S=-0.83, F=-0.49, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_fopox / close)`: S=-0.93, F=-0.59, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_fopox, 5))`: S=0.64, F=0.31, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_fopox)` | TOP3000 | 1.06 | 0.67 | 9.4% | 100% | bull-only |
| `rank(fnd6_fopox / close)` | TOP500 | 0.93 | 0.61 | 8.4% | 100% | mixed |
| `rank(fnd6_fopox)` | TOP500 | 0.91 | 0.60 | 13.0% | 80% | bull-only |
| `rank(fnd6_fopox / close)` | TOP1000 | 0.93 | 0.59 | 7.7% | 80% | all-weather |
| `rank(fnd6_fopox / close)` | TOP3000 | 0.83 | 0.52 | 10.9% | 80% | all-weather |
| `rank(fnd6_fopox)` | TOP1000 | 0.83 | 0.49 | 10.2% | 100% | bull-only |
| `rank(fnd6_fopox / close)` | TOP200 | 0.64 | 0.38 | 11.2% | 80% | mixed |
| `rank(fnd6_fopox)` | TOP200 | 0.47 | 0.25 | 17.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_fopox, 5))` | TOP500 | 0.19 | 0.06 | 39.1% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_caps: 0.853 (strongly positively correlated)
- fn_allocated_share_based_compensation_expense_q: 0.828 (strongly positively correlated)
- fnd6_newqv1300_capsq: 0.826 (strongly positively correlated)
- cash: 0.823 (strongly positively correlated)
- fnd6_newa2v1300_wcap: 0.819 (strongly positively correlated)

Redundancy cluster #32: 9 similar fields, mean |rho| 0.765 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.27 | 1.61 | +0.55 | +0.51 | yes |
| snt_value_fast_d1 | socialmedia12 | -0.19 | 1.53 | +0.47 | -0.50 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.12 | 1.62 | +0.48 | +0.34 | yes |
| anl4_tbvps_low | analyst4 | -0.04 | 1.50 | +0.45 | -0.33 | yes |
| anl4_tbvps_median | analyst4 | -0.04 | 1.50 | +0.44 | -0.35 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
