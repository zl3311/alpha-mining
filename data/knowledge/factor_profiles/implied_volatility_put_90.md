---
field: implied_volatility_put_90
dataset: option8
best_template: rank_delta
best_sharpe: 1.72
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0447
ann_vol: 0.051
hit_rate: 0.5336
rolling_sharpe_min: -0.639
rolling_sharpe_max: 3.644
top_merge_partner: fnd6_itci
redundancy_cluster: 4
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.72
---
# implied_volatility_put_90 (option8)

*Implied volatility of the at-the-money put for the stock with an expiration 90 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_put_90)`: S=0.28, F=0.20, T=7.2%, INFERIOR (TOP200)
- `rank(implied_volatility_put_90 / close)`: S=0.10, F=0.03, T=4.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_90, 5))`: S=1.72, F=0.67, T=57.7%, INFERIOR (TOP3000)
- `-rank(implied_volatility_put_90)`: S=-0.13, F=-0.06, T=7.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_90, 5))`: S=-1.72, F=-0.67, T=57.7%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_90, 22)`: S=0.94, F=0.43, T=30.3%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_90, 10)`: S=-0.10, F=-0.05, T=3.7%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_90, 22))`: S=0.87, F=0.34, T=32.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_90)`: S=-0.04, F=-0.01, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_90 / close)`: S=0.00, F=0.00, T=7.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.73, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.80 (moderate), ret=+2.9%
  - 2020: S=2.40 (strong), ret=+9.8%
  - 2021: S=2.04 (strong), ret=+12.3%
  - 2022: S=3.18 (strong), ret=+21.2%
  - 2023: S=-0.75 (negative), ret=-2.8%

## Risk & Drawdown
- Max drawdown: 4.47% over 226 days (recovered)
- Annualized: return +8.8%, volatility 5.1% (fraction of booksize)
- Hit rate: 53.4% positive days
- Tail shape: skew +1.14, excess kurtosis +7.90

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.64, max 3.64, latest -0.64

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.53%; worst month: -2.36%
Positive months: 68%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.51
- Sideways: S=1.05
- Bear: S=1.45

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_90 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.72 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_90)`: S=-0.04, F=-0.01, T=10.5%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_90 / close)`: S=0.00, F=0.00, T=7.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_90, 5))`: S=-1.72, F=-0.67, T=57.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_90, 5))` | TOP3000 | 1.73 | 0.67 | 4.5% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_put_90, 5))` | TOP1000 | 1.12 | 0.46 | 6.0% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_90, 5))` | TOP200 | 0.74 | 0.33 | 13.5% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_90, 5))` | TOP500 | 0.80 | 0.31 | 7.6% | 80% | mixed |
| `rank(implied_volatility_put_90)` | TOP200 | 0.29 | 0.20 | 73.5% | 60% | bear-only |
| `rank(implied_volatility_put_90)` | TOP500 | 0.19 | 0.11 | 74.9% | 40% | bear-only |
| `rank(implied_volatility_put_90)` | TOP1000 | 0.13 | 0.06 | 69.6% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_120: 0.961 (strongly positively correlated)
- implied_volatility_put_60: 0.949 (strongly positively correlated)
- implied_volatility_put_150: 0.926 (strongly positively correlated)
- implied_volatility_mean_120: 0.922 (strongly positively correlated)
- implied_volatility_mean_90: 0.912 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_itci | fundamental_tax_credit | +0.05 | 2.58 | +0.58 | -0.19 | yes |
| current_ratio | fundamental6 | -0.03 | 2.28 | +0.55 | +0.31 | yes |
| implied_volatility_call_30 - implied_volatility_put_30 | option8 | -0.01 | 2.46 | +0.69 | +0.86 | no |
| max_adjusted_net_income_guidance | company_guidance | +0.03 | 2.26 | +0.52 | +0.75 | yes |
| implied_volatility_call_270 - implied_volatility_put_270 | option8 | +0.01 | 2.48 | +0.67 | +0.88 | no |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
