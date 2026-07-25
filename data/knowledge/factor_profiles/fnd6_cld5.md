---
field: fnd6_cld5
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.96
best_fitness: 0.91
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.2
ann_vol: 0.1184
hit_rate: 0.5328
rolling_sharpe_min: -1.336
rolling_sharpe_max: 3.021
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 26
negated_best_sharpe: 0.27
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.69
---
# fnd6_cld5 (fundamental6)

*Capitalized Leases - Due in 5th Year*

## Signal Profile
- `rank(fnd6_cld5)`: S=0.96, F=0.91, T=3.8%, INFERIOR (TOP200)
- `rank(fnd6_cld5 / close)`: S=0.93, F=0.86, T=4.1%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_cld5, 5))`: S=0.06, F=0.01, T=38.7%, INFERIOR (TOP3000)
- `-rank(fnd6_cld5)`: S=-0.35, F=-0.16, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cld5, 5))`: S=0.27, F=0.13, T=20.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_cld5, 63)`: S=0.43, F=0.37, T=11.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cld5, 10)`: S=0.62, F=0.49, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cld5, 22))`: S=-0.56, F=-0.43, T=21.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld5)`: S=-0.71, F=-0.49, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld5 / close)`: S=-0.74, F=-0.51, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.96, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.21 (moderate), ret=+11.2%
  - 2020: S=-1.01 (negative), ret=-10.0%
  - 2021: S=2.16 (strong), ret=+30.6%
  - 2022: S=0.54 (moderate), ret=+7.4%
  - 2023: S=1.67 (strong), ret=+16.7%

## Risk & Drawdown
- Max drawdown: 20.00% over 413 days (recovered)
- Annualized: return +11.4%, volatility 11.8% (fraction of booksize)
- Hit rate: 53.3% positive days
- Tail shape: skew +0.14, excess kurtosis +1.99

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.34, max 3.02, latest 1.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +10.21%; worst month: -6.63%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.61
- Sideways: S=0.94
- Bear: S=0.29

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cld5, 5))` S=0.27, F=0.13, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cld5)`: S=-0.71, F=-0.49, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cld5 / close)`: S=-0.74, F=-0.51, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cld5, 5))`: S=0.27, F=0.13, T=20.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_cld5)` | TOP200 | 0.96 | 0.91 | 20.0% | 80% | mixed |
| `rank(fnd6_cld5 / close)` | TOP200 | 0.93 | 0.86 | 18.3% | 80% | all-weather |
| `rank(fnd6_cld5 / close)` | TOP3000 | 0.93 | 0.57 | 6.0% | 80% | bull-only |
| `rank(fnd6_cld5 / close)` | TOP500 | 0.74 | 0.51 | 10.8% | 80% | mixed |
| `rank(fnd6_cld5)` | TOP500 | 0.71 | 0.49 | 17.4% | 80% | bull-only |
| `rank(fnd6_cld5)` | TOP3000 | 0.69 | 0.41 | 11.0% | 60% | bull-only |
| `rank(fnd6_cld5)` | TOP1000 | 0.35 | 0.16 | 17.2% | 60% | bull-only |
| `rank(fnd6_cld5 / close)` | TOP1000 | 0.30 | 0.12 | 12.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cld4: 0.850 (strongly positively correlated)
- unsystematic_risk_last_30_days: -0.444 (moderately negatively correlated)
- fnd6_esopnr: 0.439 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.429 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.429 (moderately positively correlated)

Redundancy cluster #26: 2 similar fields, mean |rho| 0.85 (representative: fnd6_cld4). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.29 | 1.66 | +0.63 | -0.63 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.26 | 1.60 | +0.60 | -0.22 | yes |
| news_open_vol | news12 | -0.28 | 1.50 | +0.54 | -0.39 | yes |
| analyst_revision_rank_derivative | model16 | -0.22 | 1.45 | +0.48 | -0.88 | yes |
| relative_valuation_rank_derivative | model16 | -0.22 | 1.45 | +0.48 | -0.88 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
