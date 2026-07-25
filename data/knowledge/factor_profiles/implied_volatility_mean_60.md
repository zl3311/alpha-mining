---
field: implied_volatility_mean_60
dataset: option8
best_template: rank_delta
best_sharpe: 1.3
best_fitness: 0.45
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0529
ann_vol: 0.0513
hit_rate: 0.5174
rolling_sharpe_min: -0.553
rolling_sharpe_max: 2.744
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.32
---
# implied_volatility_mean_60 (option8)

*The average of IvCall60 and IvPut60*

## Signal Profile
- `rank(implied_volatility_mean_60)`: S=0.31, F=0.24, T=7.3%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_60 / close)`: S=0.11, F=0.04, T=4.5%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_60, 5))`: S=1.30, F=0.45, T=56.2%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_60)`: S=-0.14, F=-0.07, T=7.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_60, 5))`: S=-1.30, F=-0.45, T=56.2%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_60, 22)`: S=0.88, F=0.40, T=30.1%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_60, 10)`: S=-0.03, F=-0.01, T=3.9%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_60, 22))`: S=0.85, F=0.33, T=32.5%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_60)`: S=-0.05, F=-0.01, T=11.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_60 / close)`: S=-0.02, F=0.00, T=7.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.33, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.13 (weak), ret=+0.5%
  - 2020: S=1.95 (strong), ret=+8.5%
  - 2021: S=2.42 (strong), ret=+14.2%
  - 2022: S=1.93 (strong), ret=+13.1%
  - 2023: S=-0.72 (negative), ret=-2.8%

## Risk & Drawdown
- Max drawdown: 5.29% over 169 days (recovered)
- Annualized: return +6.8%, volatility 5.1% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.90, excess kurtosis +6.17

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.55, max 2.74, latest -0.55

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +3.97%; worst month: -2.12%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.86
- Sideways: S=0.65
- Bear: S=1.37

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_60 / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.32 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_60)`: S=-0.05, F=-0.01, T=11.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_60 / close)`: S=-0.02, F=0.00, T=7.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_60, 5))`: S=-1.30, F=-0.45, T=56.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_60, 5))` | TOP3000 | 1.33 | 0.45 | 5.3% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_mean_60, 5))` | TOP1000 | 1.07 | 0.44 | 7.3% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_60, 5))` | TOP200 | 0.70 | 0.29 | 13.3% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_60, 5))` | TOP500 | 0.71 | 0.26 | 6.9% | 80% | mixed |
| `rank(implied_volatility_mean_60)` | TOP200 | 0.32 | 0.24 | 73.1% | 60% | bear-only |
| `rank(implied_volatility_mean_60)` | TOP500 | 0.22 | 0.13 | 74.8% | 40% | bear-only |
| `rank(implied_volatility_mean_60)` | TOP1000 | 0.15 | 0.07 | 69.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_90: 0.955 (strongly positively correlated)
- implied_volatility_put_60: 0.922 (strongly positively correlated)
- implied_volatility_call_90: 0.912 (strongly positively correlated)
- implied_volatility_mean_120: 0.879 (strongly positively correlated)
- implied_volatility_put_90: 0.876 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.10 | 1.93 | +0.57 | +0.83 | yes |
| fnd6_cld3 | fundamental6 | -0.05 | 1.88 | +0.55 | +0.91 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.00 | 1.96 | +0.51 | -0.39 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.00 | 1.96 | +0.51 | -0.39 | yes |
| fnd6_cld2 | fundamental6 | -0.02 | 1.88 | +0.55 | +0.48 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
