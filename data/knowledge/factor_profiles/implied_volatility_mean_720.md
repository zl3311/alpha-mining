---
field: implied_volatility_mean_720
dataset: option8
best_template: ts_zscore
best_sharpe: 1.14
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0519
ann_vol: 0.0493
hit_rate: 0.5296
rolling_sharpe_min: -0.262
rolling_sharpe_max: 2.94
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: -0.05
negated_best_template: neg_rank_level
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -1.19
---
# implied_volatility_mean_720 (option8)

*The average of IvCall720 and IvPut720*

## Signal Profile
- `rank(implied_volatility_mean_720)`: S=0.25, F=0.17, T=5.9%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_720 / close)`: S=0.11, F=0.04, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_720, 5))`: S=1.49, F=0.52, T=59.8%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_720)`: S=-0.13, F=-0.06, T=6.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_720, 5))`: S=-1.49, F=-0.52, T=59.8%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_720, 22)`: S=1.14, F=0.53, T=31.6%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_720, 10)`: S=0.00, F=0.00, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_720, 22))`: S=1.06, F=0.44, T=33.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_720)`: S=-0.05, F=-0.01, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_720 / close)`: S=-0.03, F=-0.01, T=7.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.50, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.23 (weak), ret=+0.7%
  - 2020: S=2.19 (strong), ret=+9.5%
  - 2021: S=2.15 (strong), ret=+10.9%
  - 2022: S=2.21 (strong), ret=+15.7%
  - 2023: S=-0.19 (negative), ret=-0.7%

## Risk & Drawdown
- Max drawdown: 5.19% over 334 days (recovered)
- Annualized: return +7.4%, volatility 4.9% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +1.79, excess kurtosis +14.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.26, max 2.94, latest -0.17

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +5.83%; worst month: -2.47%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.05
- Sideways: S=0.61
- Bear: S=1.69

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_720)` S=-0.05, F=-0.01, INFERIOR
Direction gap: -1.19 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_720)`: S=-0.05, F=-0.01, T=10.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_720 / close)`: S=-0.03, F=-0.01, T=7.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_720, 5))`: S=-1.49, F=-0.52, T=59.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_720, 5))` | TOP3000 | 1.50 | 0.52 | 5.2% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_mean_720, 5))` | TOP1000 | 0.98 | 0.35 | 5.5% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_720, 5))` | TOP500 | 0.70 | 0.24 | 8.0% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_720, 5))` | TOP200 | 0.53 | 0.19 | 21.4% | 80% | mixed |
| `rank(implied_volatility_mean_720)` | TOP200 | 0.26 | 0.17 | 74.2% | 60% | bear-only |
| `rank(implied_volatility_mean_720)` | TOP500 | 0.19 | 0.11 | 72.8% | 40% | bear-only |
| `rank(implied_volatility_mean_720)` | TOP1000 | 0.14 | 0.06 | 67.4% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_1080: 0.998 (strongly positively correlated)
- implied_volatility_mean_360: 0.960 (strongly positively correlated)
- implied_volatility_mean_270: 0.941 (strongly positively correlated)
- implied_volatility_call_720: 0.916 (strongly positively correlated)
- implied_volatility_call_1080: 0.913 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.17 | 2.16 | +0.66 | +0.83 | yes |
| max_adjusted_net_income_guidance | company_guidance | -0.02 | 2.13 | +0.63 | +0.90 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.00 | 2.05 | +0.55 | -0.33 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.00 | 2.05 | +0.55 | -0.33 | yes |
| fnd6_acdo | fundamental_discontinued_ops | -0.08 | 2.04 | +0.55 | +0.59 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
