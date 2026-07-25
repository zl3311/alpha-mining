---
field: sales_estimate_count
dataset: analyst4
best_template: decay_linear
best_sharpe: 2.38
best_fitness: 1.62
best_universe: TOP3000
grade: GOOD
submittability: potentially_submittable
n_sims: 34
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0593
ann_vol: 0.0696
hit_rate: 0.5547
rolling_sharpe_min: -0.421
rolling_sharpe_max: 4.325
top_merge_partner: implied_volatility_put_90
negated_best_sharpe: 0.52
negated_best_template: neg_rank_level
negated_best_fitness: 0.28
n_negated_sims: 10
direction_gap: -1.86
---
# sales_estimate_count (analyst4)

*Sales - number of estimations*

## Signal Profile
- `rank(sales_estimate_count)`: S=1.59, F=0.88, T=3.0%, INFERIOR (TOP3000)
- `rank(sales_estimate_count / close)`: S=0.28, F=0.13, T=3.1%, INFERIOR (TOP1000)
- `rank(ts_delta(sales_estimate_count, 5))`: S=0.08, F=0.01, T=33.4%, INFERIOR (TOP3000)
- `ts_decay_linear(rank(sales_estimate_count) + rank(anl4_totassets_flag) + rank(fnd6_dlto / close) + rank(ts_mean(anl4_cfi_flag, 5) * (-1 * returns)), 3)`: S=2.38, F=1.62, T=35.6%, GOOD (TOP3000)
- `-rank(sales_estimate_count)`: S=-1.16, F=-0.63, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_count, 5))`: S=0.66, F=0.26, T=35.9%, INFERIOR (TOP3000)
- `ts_zscore(sales_estimate_count, 22)`: S=0.39, F=0.10, T=38.4%, INFERIOR (TOP3000)
- `ts_mean(sales_estimate_count, 10)`: S=1.01, F=0.57, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(sales_estimate_count, 22))`: S=0.43, F=0.15, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_count)`: S=0.52, F=0.28, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_count / close)`: S=-0.12, F=-0.04, T=3.9%, INFERIOR (TOP3000)

## Check Summary
- LOW_FITNESS: 32F/2P
- LOW_SHARPE: 31F/3P
- LOW_SUB_UNIVERSE_SHARPE: 7F/15P

## Temporal Behavior
Headline (decay_linear): Overall Sharpe 2.38, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.91 (moderate), ret=+4.2%
  - 2020: S=2.40 (strong), ret=+18.8%
  - 2021: S=2.55 (strong), ret=+21.4%
  - 2022: S=2.35 (strong), ret=+17.4%
  - 2023: S=3.97 (strong), ret=+19.4%

## Risk & Drawdown
- Max drawdown: 5.93% over 281 days (recovered)
- Annualized: return +16.6%, volatility 7.0% (fraction of booksize)
- Hit rate: 55.5% positive days
- Tail shape: skew +0.77, excess kurtosis +5.47

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.42, max 4.33, latest 4.00

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +6.80%; worst month: -3.34%
Positive months: 73%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=4.34
- Sideways: S=1.89
- Bear: S=1.06

## Negated Direction
Best negated: `rank(-1 * sales_estimate_count)` S=0.52, F=0.28, INFERIOR
Direction gap: -1.86 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * sales_estimate_count)`: S=0.52, F=0.28, T=4.9%, INFERIOR (TOP3000)
- `rank(-1 * sales_estimate_count / close)`: S=-0.12, F=-0.04, T=3.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sales_estimate_count, 5))`: S=0.66, F=0.26, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `ts_decay_linear(rank(sales_estimate_count) + rank(anl4_totassets_flag) + rank(fnd6_dlto / close) + rank(ts_mean(anl4_cfi_flag, 5) * (-1 * returns)), 3)` | TOP3000 | 2.38 | 1.62 | 5.9% | 100% | all-weather |
| `rank(sales_estimate_count)` | TOP3000 | 1.59 | 0.88 | 3.0% | 100% | all-weather |
| `rank(sales_estimate_count)` | TOP1000 | 1.17 | 0.63 | 4.3% | 100% | all-weather |
| `rank(sales_estimate_count / close)` | TOP1000 | 0.29 | 0.13 | 25.7% | 40% | bear-only |
| `rank(sales_estimate_count / close)` | TOP500 | 0.25 | 0.10 | 23.8% | 80% | bear-only |
| `rank(sales_estimate_count / close)` | TOP3000 | 0.15 | 0.06 | 39.5% | 40% | bear-only |
| `rank(sales_estimate_count)` | TOP500 | 0.21 | 0.05 | 11.8% | 80% | mixed |
| `rank(sales_estimate_count / close)` | TOP200 | 0.13 | 0.04 | 17.9% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_dlto: 0.578 (moderately positively correlated)
- fnd6_newa1v1300_dltt: 0.550 (moderately positively correlated)
- min_adjusted_net_income_guidance: 0.546 (moderately positively correlated)
- fnd6_txndbl: 0.546 (moderately positively correlated)
- fnd6_dltis: 0.543 (moderately positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_put_90 | option8 | +0.10 | 2.81 | +0.43 | -0.38 | yes |
| fnd6_itci | fundamental_tax_credit | +0.23 | 2.81 | +0.43 | +0.51 | yes |
| implied_volatility_call_270 - implied_volatility_put_270 | option8 | +0.16 | 2.78 | +0.40 | -0.11 | yes |
| implied_volatility_put_120 | option8 | +0.12 | 2.75 | +0.36 | -0.44 | yes |
| implied_volatility_mean_90 | option8 | +0.12 | 2.75 | +0.37 | -0.37 | yes |

## Actionability
Already in submitted book (alpha: unknown).
Passes all non-self-corr checks. Candidate for submission pending self-corr verification.
Untried templates: trade_when
