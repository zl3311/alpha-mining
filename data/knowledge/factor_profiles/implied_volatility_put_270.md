---
field: implied_volatility_put_270
dataset: option8
best_template: ts_zscore
best_sharpe: 1.03
best_fitness: 0.47
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 23
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0594
ann_vol: 0.0476
hit_rate: 0.5101
rolling_sharpe_min: -1.099
rolling_sharpe_max: 3.36
top_merge_partner: rank(scl12_sentiment * (-1 * returns))
redundancy_cluster: 4
negated_best_sharpe: -0.02
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.05
---
# implied_volatility_put_270 (option8)

*Implied volatility of the at-the-money put for the stock with an expiration 270 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_put_270)`: S=0.26, F=0.18, T=7.1%, INFERIOR (TOP200)
- `rank(implied_volatility_put_270 / close)`: S=0.10, F=0.03, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_270, 5))`: S=1.19, F=0.37, T=58.6%, INFERIOR (TOP3000)
- `-rank(implied_volatility_put_270)`: S=-0.12, F=-0.05, T=6.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_270, 5))`: S=-1.19, F=-0.37, T=58.6%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_270, 22)`: S=1.03, F=0.47, T=29.8%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_270, 10)`: S=-0.07, F=-0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_270, 22))`: S=1.10, F=0.47, T=31.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_270)`: S=-0.02, F=0.00, T=10.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_270 / close)`: S=0.00, F=0.00, T=6.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 22F/1P
- LOW_FITNESS: 23F/0P
- LOW_SHARPE: 23F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/17P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.18, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.01 (negative), ret=-0.0%
  - 2020: S=1.61 (strong), ret=+6.5%
  - 2021: S=1.70 (strong), ret=+9.5%
  - 2022: S=2.43 (strong), ret=+15.1%
  - 2023: S=-1.04 (negative), ret=-3.5%

## Risk & Drawdown
- Max drawdown: 5.94% over 358 days (not yet recovered, ongoing at window end)
- Annualized: return +5.6%, volatility 4.8% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.98, excess kurtosis +6.62

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.10, max 3.36, latest -0.97

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.32%; worst month: -2.56%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.37
- Sideways: S=-0.19
- Bear: S=0.97

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_270)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.05 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_270)`: S=-0.02, F=0.00, T=10.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_270 / close)`: S=0.00, F=0.00, T=6.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_270, 5))`: S=-1.19, F=-0.37, T=58.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_270, 5))` | TOP3000 | 1.18 | 0.37 | 5.9% | 60% | all-weather |
| `rank(ts_delta(implied_volatility_put_270, 5))` | TOP1000 | 0.80 | 0.26 | 7.4% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_270, 5))` | TOP500 | 0.73 | 0.26 | 6.6% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_270, 5))` | TOP200 | 0.59 | 0.23 | 13.2% | 80% | mixed |
| `rank(implied_volatility_put_270)` | TOP200 | 0.27 | 0.18 | 73.1% | 60% | bear-only |
| `rank(implied_volatility_put_270)` | TOP500 | 0.18 | 0.09 | 74.4% | 40% | bear-only |
| `rank(implied_volatility_put_270)` | TOP1000 | 0.12 | 0.05 | 69.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_360: 0.986 (strongly positively correlated)
- implied_volatility_put_180: 0.963 (strongly positively correlated)
- implied_volatility_put_720: 0.934 (strongly positively correlated)
- implied_volatility_put_150: 0.930 (strongly positively correlated)
- implied_volatility_put_1080: 0.926 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.05 | 1.67 | +0.49 | -0.39 | yes |
| fnd6_rank | fundamental6 | +0.01 | 1.63 | +0.45 | -0.55 | yes |
| news_close_vol | news12 | -0.04 | 1.68 | +0.49 | +0.54 | yes |
| fnd6_dxd5 | fundamental6 | +0.02 | 1.66 | +0.47 | +0.38 | yes |
| pcr_vol_20 | option9 | +0.09 | 1.57 | +0.38 | -0.83 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
