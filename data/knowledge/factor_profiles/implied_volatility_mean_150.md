---
field: implied_volatility_mean_150
dataset: option8
best_template: rank_delta
best_sharpe: 1.61
best_fitness: 0.64
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0489
ann_vol: 0.0556
hit_rate: 0.5336
rolling_sharpe_min: -0.517
rolling_sharpe_max: 3.407
top_merge_partner: current_ratio
redundancy_cluster: 4
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.63
---
# implied_volatility_mean_150 (option8)

*The average of IvCall150 and IvPut150*

## Signal Profile
- `rank(implied_volatility_mean_150)`: S=0.29, F=0.21, T=6.1%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_150 / close)`: S=0.11, F=0.04, T=4.2%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_150, 5))`: S=1.61, F=0.64, T=56.2%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_150)`: S=-0.13, F=-0.06, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_150, 5))`: S=-1.61, F=-0.64, T=56.2%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_150, 22)`: S=1.11, F=0.57, T=30.2%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_150, 10)`: S=0.00, F=0.00, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_150, 22))`: S=1.13, F=0.51, T=32.9%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_150)`: S=-0.05, F=-0.01, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_150 / close)`: S=-0.02, F=0.00, T=7.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.62, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.77 (moderate), ret=+2.7%
  - 2020: S=2.43 (strong), ret=+12.0%
  - 2021: S=1.89 (strong), ret=+11.6%
  - 2022: S=2.62 (strong), ret=+20.1%
  - 2023: S=-0.54 (negative), ret=-2.1%

## Risk & Drawdown
- Max drawdown: 4.89% over 104 days (recovered)
- Annualized: return +9.0%, volatility 5.6% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew +1.28, excess kurtosis +9.38

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.52, max 3.41, latest -0.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +5.86%; worst month: -2.01%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.27
- Sideways: S=1.16
- Bear: S=1.28

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_150 / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.63 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_150)`: S=-0.05, F=-0.01, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_150 / close)`: S=-0.02, F=0.00, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_150, 5))`: S=-1.61, F=-0.64, T=56.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_150, 5))` | TOP3000 | 1.62 | 0.64 | 4.9% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_mean_150, 5))` | TOP1000 | 1.02 | 0.41 | 6.1% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_150, 5))` | TOP500 | 0.78 | 0.30 | 9.6% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_150, 5))` | TOP200 | 0.60 | 0.24 | 19.3% | 80% | mixed |
| `rank(implied_volatility_mean_150)` | TOP200 | 0.30 | 0.21 | 73.3% | 60% | bear-only |
| `rank(implied_volatility_mean_150)` | TOP500 | 0.21 | 0.12 | 74.2% | 40% | bear-only |
| `rank(implied_volatility_mean_150)` | TOP1000 | 0.14 | 0.06 | 69.3% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_180: 0.983 (strongly positively correlated)
- implied_volatility_mean_120: 0.976 (strongly positively correlated)
- implied_volatility_call_150: 0.944 (strongly positively correlated)
- implied_volatility_mean_270: 0.940 (strongly positively correlated)
- implied_volatility_put_150: 0.940 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| current_ratio | fundamental6 | -0.07 | 2.29 | +0.63 | +0.22 | yes |
| max_adjusted_net_income_guidance | company_guidance | +0.01 | 2.19 | +0.57 | +0.76 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.01 | 2.14 | +0.52 | -0.30 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.01 | 2.14 | +0.52 | -0.30 | yes |
| fnd6_ivaco | fundamental_investment | -0.09 | 2.17 | +0.54 | +0.64 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
