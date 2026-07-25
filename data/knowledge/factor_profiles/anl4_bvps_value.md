---
field: anl4_bvps_value
dataset: analyst4
best_template: ts_zscore
best_sharpe: 1.18
best_fitness: 0.66
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 6
max_drawdown: 0.1962
ann_vol: 0.0763
hit_rate: 0.5312
rolling_sharpe_min: -2.352
rolling_sharpe_max: 2.78
top_merge_partner: news_open_vol
negated_best_sharpe: 0.41
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.27
n_negated_sims: 10
direction_gap: -0.77
---
# anl4_bvps_value (analyst4)

*Book value per share - announced financial value*

## Signal Profile
- `rank(anl4_bvps_value)`: S=0.15, F=0.04, T=2.1%, INFERIOR (TOP3000)
- `rank(anl4_bvps_value / close)`: S=0.46, F=0.26, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_bvps_value, 5))`: S=0.90, F=0.37, T=40.2%, INFERIOR (TOP1000)
- `-rank(anl4_bvps_value)`: S=-0.03, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_value, 5))`: S=-0.67, F=-0.32, T=38.7%, INFERIOR (TOP3000)
- `ts_zscore(anl4_bvps_value, 22)`: S=1.18, F=0.66, T=40.8%, INFERIOR (TOP3000)
- `ts_mean(anl4_bvps_value, 10)`: S=-0.44, F=-0.28, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_bvps_value, 22))`: S=0.98, F=0.51, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_value)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_value / close)`: S=0.41, F=0.27, T=3.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.90, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.19 (moderate), ret=+6.8%
  - 2020: S=1.07 (moderate), ret=+8.2%
  - 2021: S=2.11 (strong), ret=+16.8%
  - 2022: S=0.88 (moderate), ret=+7.8%
  - 2023: S=-0.87 (negative), ret=-5.9%

## Risk & Drawdown
- Max drawdown: 19.62% over 479 days (not yet recovered, ongoing at window end)
- Annualized: return +6.9%, volatility 7.6% (fraction of booksize)
- Hit rate: 53.1% positive days
- Tail shape: skew -0.00, excess kurtosis +2.90

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.35, max 2.78, latest -0.98

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +5.39%; worst month: -5.41%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.66
- Sideways: S=-1.20
- Bear: S=1.84

## Negated Direction
Best negated: `rank(-1 * anl4_bvps_value / close)` S=0.41, F=0.27, INFERIOR
Direction gap: -0.77 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_bvps_value)`: S=-0.04, F=-0.01, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_bvps_value / close)`: S=0.41, F=0.27, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_bvps_value, 5))`: S=-0.67, F=-0.32, T=38.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_bvps_value, 5))` | TOP1000 | 0.90 | 0.37 | 19.6% | 80% | all-weather |
| `rank(ts_delta(anl4_bvps_value, 5))` | TOP200 | 0.74 | 0.36 | 14.5% | 80% | all-weather |
| `rank(anl4_bvps_value / close)` | TOP3000 | 0.45 | 0.26 | 14.6% | 80% | mixed |
| `rank(ts_delta(anl4_bvps_value, 5))` | TOP500 | 0.63 | 0.24 | 10.0% | 60% | all-weather |
| `rank(anl4_bvps_value / close)` | TOP1000 | 0.14 | 0.05 | 16.7% | 60% | mixed |
| `rank(anl4_bvps_value)` | TOP3000 | 0.14 | 0.04 | 22.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- retained_earnings: 0.239 (weakly positively correlated)
- fnd6_cptnewqv1300_req: 0.239 (weakly positively correlated)
- fnd6_newqv1300_reunaq: 0.214 (weakly positively correlated)
- earnings_per_share_minimum: 0.206 (weakly positively correlated)
- fnd2_dfdtxasoprlcarryfwd: -0.188 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_open_vol | news12 | -0.16 | 1.41 | +0.48 | -0.37 | yes |
| fnd6_optex | fundamental6 | -0.11 | 1.33 | +0.43 | -0.22 | yes |
| fnd6_idesindq_curcd | fundamental6 | -0.01 | 1.26 | +0.36 | -0.81 | yes |
| fn_op_lease_min_pay_due_in_5y_a | fundamental2 | -0.10 | 1.33 | +0.43 | +0.64 | yes |
| fnd6_cshtr | fundamental6 | -0.16 | 1.44 | +0.43 | +0.62 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
