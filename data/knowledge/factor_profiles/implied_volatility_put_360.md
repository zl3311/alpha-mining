---
field: implied_volatility_put_360
dataset: option8
best_template: ts_zscore
best_sharpe: 1.06
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0566
ann_vol: 0.0465
hit_rate: 0.519
rolling_sharpe_min: -1.029
rolling_sharpe_max: 3.16
top_merge_partner: rank(scl12_sentiment * (-1 * returns))
redundancy_cluster: 4
negated_best_sharpe: -0.02
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.08
---
# implied_volatility_put_360 (option8)

*Implied volatility of the at-the-money put for the stock with an expiration 360 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_put_360)`: S=0.25, F=0.17, T=7.2%, INFERIOR (TOP200)
- `rank(implied_volatility_put_360 / close)`: S=0.10, F=0.03, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_360, 5))`: S=1.16, F=0.35, T=59.0%, INFERIOR (TOP3000)
- `-rank(implied_volatility_put_360)`: S=-0.12, F=-0.05, T=7.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_360, 5))`: S=-1.16, F=-0.35, T=59.0%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_360, 22)`: S=1.06, F=0.48, T=29.8%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_360, 10)`: S=-0.07, F=-0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_360, 22))`: S=1.05, F=0.43, T=31.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_360)`: S=-0.02, F=0.00, T=10.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_360 / close)`: S=0.00, F=0.00, T=6.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.15, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-0.5%
  - 2020: S=1.48 (moderate), ret=+5.8%
  - 2021: S=1.73 (strong), ret=+9.4%
  - 2022: S=2.41 (strong), ret=+14.7%
  - 2023: S=-0.98 (negative), ret=-3.2%

## Risk & Drawdown
- Max drawdown: 5.66% over 344 days (not yet recovered, ongoing at window end)
- Annualized: return +5.4%, volatility 4.7% (fraction of booksize)
- Hit rate: 51.9% positive days
- Tail shape: skew +0.97, excess kurtosis +6.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.03, max 3.16, latest -0.93

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.42%; worst month: -2.45%
Positive months: 59%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.29
- Sideways: S=-0.25
- Bear: S=1.05

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_360)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.08 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_360)`: S=-0.02, F=0.00, T=10.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_360 / close)`: S=0.00, F=0.00, T=6.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_360, 5))`: S=-1.16, F=-0.35, T=59.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_360, 5))` | TOP3000 | 1.15 | 0.35 | 5.7% | 60% | all-weather |
| `rank(ts_delta(implied_volatility_put_360, 5))` | TOP1000 | 0.76 | 0.24 | 5.9% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_360, 5))` | TOP500 | 0.64 | 0.21 | 6.9% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_360, 5))` | TOP200 | 0.50 | 0.18 | 13.3% | 80% | mixed |
| `rank(implied_volatility_put_360)` | TOP200 | 0.26 | 0.17 | 73.2% | 60% | bear-only |
| `rank(implied_volatility_put_360)` | TOP500 | 0.17 | 0.08 | 74.1% | 40% | bear-only |
| `rank(implied_volatility_put_360)` | TOP1000 | 0.12 | 0.05 | 68.7% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_270: 0.986 (strongly positively correlated)
- implied_volatility_put_720: 0.955 (strongly positively correlated)
- implied_volatility_put_1080: 0.947 (strongly positively correlated)
- implied_volatility_put_180: 0.943 (strongly positively correlated)
- implied_volatility_put_150: 0.912 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.04 | 1.64 | +0.49 | -0.38 | yes |
| fnd6_rank | fundamental6 | +0.01 | 1.61 | +0.45 | -0.50 | yes |
| pcr_vol_20 | option9 | +0.07 | 1.56 | +0.41 | -0.81 | yes |
| fnd6_fopo | fundamental6 | +0.04 | 1.54 | +0.39 | -0.86 | yes |
| pcr_vol_30 | option9 | +0.10 | 1.54 | +0.39 | -0.76 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
