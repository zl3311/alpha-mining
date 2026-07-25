---
field: implied_volatility_mean_1080
dataset: option8
best_template: ts_zscore
best_sharpe: 1.19
best_fitness: 0.56
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.052
ann_vol: 0.0491
hit_rate: 0.536
rolling_sharpe_min: -0.149
rolling_sharpe_max: 2.948
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: -0.05
negated_best_template: neg_rank_level
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -1.24
---
# implied_volatility_mean_1080 (option8)

*The average of IvCall1080 and IvPut1080*

## Signal Profile
- `rank(implied_volatility_mean_1080)`: S=0.25, F=0.17, T=6.0%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_1080 / close)`: S=0.11, F=0.04, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_1080, 5))`: S=1.52, F=0.53, T=59.9%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_1080)`: S=-0.13, F=-0.06, T=6.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_1080, 5))`: S=-1.52, F=-0.53, T=59.9%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_1080, 22)`: S=1.19, F=0.56, T=31.8%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_1080, 10)`: S=0.00, F=0.00, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_1080, 22))`: S=1.11, F=0.47, T=33.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_1080)`: S=-0.05, F=-0.01, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_1080 / close)`: S=-0.03, F=-0.01, T=7.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.52, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+0.9%
  - 2020: S=2.08 (strong), ret=+9.0%
  - 2021: S=2.22 (strong), ret=+11.2%
  - 2022: S=2.23 (strong), ret=+15.8%
  - 2023: S=-0.07 (negative), ret=-0.2%

## Risk & Drawdown
- Max drawdown: 5.20% over 334 days (recovered)
- Annualized: return +7.5%, volatility 4.9% (fraction of booksize)
- Hit rate: 53.6% positive days
- Tail shape: skew +1.83, excess kurtosis +15.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.15, max 2.95, latest -0.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +5.84%; worst month: -2.47%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.09
- Sideways: S=0.59
- Bear: S=1.75

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_1080)` S=-0.05, F=-0.01, INFERIOR
Direction gap: -1.24 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_1080)`: S=-0.05, F=-0.01, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_1080 / close)`: S=-0.03, F=-0.01, T=7.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_1080, 5))`: S=-1.52, F=-0.53, T=59.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_1080, 5))` | TOP3000 | 1.52 | 0.53 | 5.2% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_mean_1080, 5))` | TOP1000 | 1.04 | 0.37 | 5.5% | 100% | mixed |
| `rank(ts_delta(implied_volatility_mean_1080, 5))` | TOP500 | 0.78 | 0.27 | 8.7% | 100% | mixed |
| `rank(ts_delta(implied_volatility_mean_1080, 5))` | TOP200 | 0.54 | 0.19 | 22.3% | 80% | mixed |
| `rank(implied_volatility_mean_1080)` | TOP200 | 0.26 | 0.17 | 74.1% | 60% | bear-only |
| `rank(implied_volatility_mean_1080)` | TOP500 | 0.19 | 0.10 | 72.8% | 40% | bear-only |
| `rank(implied_volatility_mean_1080)` | TOP1000 | 0.14 | 0.06 | 67.3% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_720: 0.998 (strongly positively correlated)
- implied_volatility_mean_360: 0.954 (strongly positively correlated)
- implied_volatility_mean_270: 0.935 (strongly positively correlated)
- implied_volatility_call_720: 0.916 (strongly positively correlated)
- implied_volatility_call_1080: 0.915 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.17 | 2.18 | +0.66 | +0.85 | yes |
| max_adjusted_net_income_guidance | company_guidance | -0.02 | 2.15 | +0.62 | +0.92 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.01 | 2.06 | +0.54 | -0.38 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.01 | 2.06 | +0.54 | -0.38 | yes |
| current_ratio | fundamental6 | -0.06 | 2.20 | +0.54 | +0.35 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
