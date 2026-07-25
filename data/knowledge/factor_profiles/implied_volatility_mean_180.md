---
field: implied_volatility_mean_180
dataset: option8
best_template: rank_delta
best_sharpe: 1.52
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0534
ann_vol: 0.0548
hit_rate: 0.5287
rolling_sharpe_min: -0.742
rolling_sharpe_max: 3.346
top_merge_partner: max_adjusted_net_income_guidance
redundancy_cluster: 4
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.54
---
# implied_volatility_mean_180 (option8)

*The average of IvCall180 and IvPut180*

## Signal Profile
- `rank(implied_volatility_mean_180)`: S=0.29, F=0.21, T=6.0%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_180 / close)`: S=0.11, F=0.04, T=4.2%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_180, 5))`: S=1.52, F=0.58, T=56.7%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_180)`: S=-0.13, F=-0.06, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_180, 5))`: S=-1.52, F=-0.58, T=56.7%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_180, 22)`: S=1.08, F=0.54, T=30.4%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_180, 10)`: S=0.01, F=0.00, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_180, 22))`: S=1.06, F=0.46, T=33.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_180)`: S=-0.05, F=-0.01, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_180 / close)`: S=-0.02, F=0.00, T=7.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.53 (moderate), ret=+1.8%
  - 2020: S=2.55 (strong), ret=+12.5%
  - 2021: S=1.96 (strong), ret=+11.8%
  - 2022: S=2.36 (strong), ret=+17.8%
  - 2023: S=-0.73 (negative), ret=-2.8%

## Risk & Drawdown
- Max drawdown: 5.34% over 358 days (not yet recovered, ongoing at window end)
- Annualized: return +8.4%, volatility 5.5% (fraction of booksize)
- Hit rate: 52.9% positive days
- Tail shape: skew +1.32, excess kurtosis +9.86

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.74, max 3.35, latest -0.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +5.78%; worst month: -1.96%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.23
- Sideways: S=0.78
- Bear: S=1.39

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_180 / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_180)`: S=-0.05, F=-0.01, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_180 / close)`: S=-0.02, F=0.00, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_180, 5))`: S=-1.52, F=-0.58, T=56.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_180, 5))` | TOP3000 | 1.53 | 0.58 | 5.3% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_mean_180, 5))` | TOP1000 | 0.95 | 0.36 | 6.4% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_180, 5))` | TOP500 | 0.74 | 0.28 | 10.7% | 80% | mixed |
| `rank(implied_volatility_mean_180)` | TOP200 | 0.29 | 0.21 | 73.3% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_mean_180, 5))` | TOP200 | 0.54 | 0.20 | 18.0% | 80% | mixed |
| `rank(implied_volatility_mean_180)` | TOP500 | 0.21 | 0.13 | 73.8% | 40% | bear-only |
| `rank(implied_volatility_mean_180)` | TOP1000 | 0.14 | 0.06 | 69.1% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_150: 0.983 (strongly positively correlated)
- implied_volatility_mean_270: 0.966 (strongly positively correlated)
- implied_volatility_mean_360: 0.949 (strongly positively correlated)
- implied_volatility_mean_120: 0.947 (strongly positively correlated)
- implied_volatility_call_180: 0.944 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| max_adjusted_net_income_guidance | company_guidance | +0.01 | 2.12 | +0.59 | +0.80 | yes |
| current_ratio | fundamental6 | -0.07 | 2.25 | +0.59 | +0.16 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.00 | 2.09 | +0.56 | -0.24 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.00 | 2.09 | +0.56 | -0.24 | yes |
| fnd6_ivaco | fundamental_investment | -0.10 | 2.09 | +0.56 | +0.67 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
