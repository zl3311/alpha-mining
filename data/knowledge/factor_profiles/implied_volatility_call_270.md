---
field: implied_volatility_call_270
dataset: option8
cluster: option8_ratio
coverage: 0.9729
community_alphas: 12883
best_template: rank_delta
best_sharpe: 1.42
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 24
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.0392
ann_vol: 0.0467
hit_rate: 0.532
rolling_sharpe_min: 0.113
rolling_sharpe_max: 2.552
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: -0.01
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.43
---
# implied_volatility_call_270 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 270 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_270)`: S=0.29, F=0.21, T=6.5%, INFERIOR (TOP200)
- `rank(implied_volatility_call_270 / close)`: S=0.12, F=0.05, T=4.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_270, 5))`: S=1.42, F=0.47, T=59.8%, INFERIOR (TOP3000)
- `ts_decay_linear(rank(implied_volatility_call_270), 5)`: S=0.08, F=0.03, T=8.0%, INFERIOR (TOP3000)
- `-rank(implied_volatility_call_270)`: S=-0.15, F=-0.08, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_270, 5))`: S=-1.42, F=-0.47, T=59.8%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_270, 22)`: S=0.84, F=0.34, T=30.6%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_270, 10)`: S=0.09, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_270, 22))`: S=0.73, F=0.25, T=32.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_270)`: S=-0.09, F=-0.03, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_270 / close)`: S=-0.01, F=0.00, T=6.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 23F/1P
- LOW_FITNESS: 24F/0P
- LOW_SHARPE: 22F/2P
- LOW_SUB_UNIVERSE_SHARPE: 4F/18P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.44, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.16 (weak), ret=+0.5%
  - 2020: S=2.10 (strong), ret=+8.9%
  - 2021: S=1.80 (strong), ret=+9.3%
  - 2022: S=1.80 (strong), ret=+11.4%
  - 2023: S=0.86 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 3.92% over 330 days (recovered)
- Annualized: return +6.7%, volatility 4.7% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew +1.02, excess kurtosis +8.34

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.11, max 2.55, latest 0.98

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +4.63%; worst month: -2.69%
Positive months: 68%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.19
- Sideways: S=0.75
- Bear: S=1.18

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_270 / close)` S=-0.01, F=0.00, INFERIOR
Direction gap: -1.43 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_270)`: S=-0.09, F=-0.03, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_270 / close)`: S=-0.01, F=0.00, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_270, 5))`: S=-1.42, F=-0.47, T=59.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_270, 5))` | TOP3000 | 1.44 | 0.47 | 3.9% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_270, 5))` | TOP1000 | 0.86 | 0.30 | 6.4% | 60% | mixed |
| `rank(implied_volatility_call_270)` | TOP200 | 0.30 | 0.21 | 72.8% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_270, 5))` | TOP500 | 0.60 | 0.19 | 8.7% | 80% | bull-only |
| `rank(implied_volatility_call_270)` | TOP500 | 0.24 | 0.14 | 72.4% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_270, 5))` | TOP200 | 0.36 | 0.11 | 21.4% | 60% | bull-only |
| `rank(implied_volatility_call_270)` | TOP1000 | 0.16 | 0.08 | 67.5% | 40% | bear-only |
| `rank(implied_volatility_call_270)` | TOP3000 | 0.09 | 0.03 | 71.2% | 40% | bear-only |
| `ts_decay_linear(rank(implied_volatility_call_270), 5)` | TOP3000 | 0.09 | 0.03 | 71.7% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_360: 0.986 (strongly positively correlated)
- implied_volatility_call_180: 0.958 (strongly positively correlated)
- implied_volatility_mean_270: 0.932 (strongly positively correlated)
- implied_volatility_call_720: 0.930 (strongly positively correlated)
- implied_volatility_call_150: 0.924 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.13 | 2.08 | +0.64 | +0.86 | yes |
| max_adjusted_net_income_guidance | company_guidance | -0.02 | 2.10 | +0.61 | +0.83 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.01 | 2.00 | +0.55 | -0.12 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.01 | 2.00 | +0.55 | -0.12 | yes |
| fnd6_acdo | fundamental_discontinued_ops | -0.08 | 1.99 | +0.55 | +0.74 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: trade_when
