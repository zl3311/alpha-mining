---
field: news_open_gap
dataset: news12
best_template: rank_delta
best_sharpe: 1.19
best_fitness: 0.44
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.2708
ann_vol: 0.1574
hit_rate: 0.5255
rolling_sharpe_min: -1.424
rolling_sharpe_max: 3.596
top_merge_partner: rp_css_technical
negated_best_sharpe: 0.76
negated_best_template: neg_rank_level
negated_best_fitness: 0.18
n_negated_sims: 4
direction_gap: -0.43
---
# news_open_gap (news12)

*Percent difference between current day's open and previous day's close*

## Signal Profile
- `rank(news_open_gap)`: S=0.36, F=0.07, T=112.6%, INFERIOR (TOP500)
- `rank(news_open_gap / close)`: S=-0.11, F=-0.01, T=116.5%, INFERIOR (TOP3000)
- `rank(ts_delta(news_open_gap, 5))`: S=1.19, F=0.44, T=135.8%, INFERIOR (TOP1000)
- `-rank(news_open_gap)`: S=0.02, F=0.00, T=116.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_open_gap, 5))`: S=-1.10, F=-0.42, T=145.0%, INFERIOR (TOP3000)
- `ts_zscore(news_open_gap, 22)`: S=0.61, F=0.13, T=121.7%, INFERIOR (TOP3000)
- `ts_mean(news_open_gap, 10)`: S=0.30, F=0.09, T=30.3%, INFERIOR (TOP3000)
- `rank(ts_rank(news_open_gap, 22))`: S=0.29, F=0.04, T=123.2%, INFERIOR (TOP3000)
- `rank(-1 * news_open_gap)`: S=0.76, F=0.18, T=119.7%, INFERIOR (TOP3000)
- `rank(-1 * news_open_gap / close)`: S=0.76, F=0.18, T=119.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 6F/13P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.18, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.52 (moderate), ret=+8.3%
  - 2020: S=1.56 (strong), ret=+26.4%
  - 2021: S=0.02 (weak), ret=+0.3%
  - 2022: S=2.13 (strong), ret=+35.1%
  - 2023: S=1.86 (strong), ret=+21.0%

## Risk & Drawdown
- Max drawdown: 27.08% over 732 days (recovered)
- Annualized: return +18.6%, volatility 15.7% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew -0.44, excess kurtosis +6.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.42, max 3.60, latest 1.88

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +17.10%; worst month: -17.10%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.25
- Sideways: S=1.24
- Bear: S=1.05

## Negated Direction
Best negated: `rank(-1 * news_open_gap)` S=0.76, F=0.18, INFERIOR
Direction gap: -0.43 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * news_open_gap)`: S=0.76, F=0.18, T=119.7%, INFERIOR (TOP3000)
- `rank(-1 * news_open_gap / close)`: S=0.76, F=0.18, T=119.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(news_open_gap, 5))`: S=-1.10, F=-0.42, T=145.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(news_open_gap, 5))` | TOP1000 | 1.18 | 0.44 | 27.1% | 100% | all-weather |
| `rank(ts_delta(news_open_gap, 5))` | TOP3000 | 1.10 | 0.42 | 28.2% | 80% | mixed |
| `rank(ts_delta(news_open_gap, 5))` | TOP200 | 1.10 | 0.42 | 21.7% | 60% | mixed |
| `rank(ts_delta(news_open_gap, 5))` | TOP500 | 0.75 | 0.23 | 35.6% | 80% | mixed |
| `rank(news_open_gap)` | TOP500 | 0.35 | 0.07 | 23.1% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_txdbcl: 0.118 (weakly positively correlated)
- fn_derivative_notional_amount_a: 0.113 (weakly positively correlated)
- fn_derivative_notional_amount_q: 0.112 (weakly positively correlated)
- fnd2_a_ltrmdmrepoplay5: 0.110 (weakly positively correlated)
- fn_unrecognized_tax_benefits_a: 0.109 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| rp_css_technical | news18 | -0.06 | 1.73 | +0.54 | +0.22 | yes |
| fnd6_mrc1 | fundamental6 | -0.01 | 1.73 | +0.46 | -0.73 | yes |
| fn_incremental_shares_attributable_to_share_based_payment_q | fundamental2 | +0.02 | 1.61 | +0.43 | -0.97 | yes |
| fnd6_cld4 | fundamental6 | -0.01 | 1.62 | +0.44 | -0.81 | yes |
| fnd6_idit | fundamental6 | -0.07 | 1.65 | +0.47 | -0.37 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
