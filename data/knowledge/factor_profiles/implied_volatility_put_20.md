---
field: implied_volatility_put_20
dataset: option8
best_template: rank_delta
best_sharpe: 1.1
best_fitness: 0.58
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.1431
ann_vol: 0.1072
hit_rate: 0.5215
rolling_sharpe_min: -0.048
rolling_sharpe_max: 2.855
top_merge_partner: sharesout
redundancy_cluster: 15
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.1
---
# implied_volatility_put_20 (option8)

*At-the-money implied volatility of put options with 20 calendar days to expiration, annualized decimal*

## Signal Profile
- `rank(implied_volatility_put_20)`: S=0.36, F=0.30, T=10.9%, INFERIOR (TOP200)
- `rank(implied_volatility_put_20 / close)`: S=0.11, F=0.04, T=5.3%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_20, 5))`: S=1.10, F=0.58, T=41.8%, INFERIOR (TOP200)
- `-rank(implied_volatility_put_20)`: S=-0.17, F=-0.09, T=10.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_20, 5))`: S=-1.16, F=-0.36, T=57.7%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_20, 22)`: S=0.92, F=0.41, T=31.1%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_20, 10)`: S=-0.17, F=-0.11, T=5.6%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_20, 22))`: S=0.80, F=0.30, T=33.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_20)`: S=-0.04, F=-0.01, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_20 / close)`: S=0.00, F=0.00, T=7.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.10, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.24 (weak), ret=+1.5%
  - 2020: S=1.10 (moderate), ret=+9.8%
  - 2021: S=0.76 (moderate), ret=+9.7%
  - 2022: S=2.42 (strong), ret=+34.2%
  - 2023: S=0.33 (weak), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 14.31% over 214 days (recovered)
- Annualized: return +11.8%, volatility 10.7% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.95, excess kurtosis +7.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.05, max 2.85, latest 0.46

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +8.99%; worst month: -6.37%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.62
- Sideways: S=0.99
- Bear: S=0.60

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_20 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.10 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_20)`: S=-0.04, F=-0.01, T=14.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_20 / close)`: S=0.00, F=0.00, T=7.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_20, 5))`: S=-1.16, F=-0.36, T=57.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_20, 5))` | TOP200 | 1.10 | 0.58 | 14.3% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_put_20, 5))` | TOP1000 | 1.22 | 0.52 | 7.9% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_put_20, 5))` | TOP500 | 0.89 | 0.36 | 10.7% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_20, 5))` | TOP3000 | 1.16 | 0.36 | 4.6% | 80% | all-weather |
| `rank(implied_volatility_put_20)` | TOP200 | 0.37 | 0.30 | 72.1% | 60% | bear-only |
| `rank(implied_volatility_put_20)` | TOP500 | 0.24 | 0.14 | 73.7% | 60% | bear-only |
| `rank(implied_volatility_put_20)` | TOP1000 | 0.18 | 0.09 | 67.7% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_20: 0.985 (strongly positively correlated)
- implied_volatility_put_10: 0.784 (strongly positively correlated)
- implied_volatility_mean_10: 0.771 (strongly positively correlated)
- implied_volatility_call_10: 0.743 (strongly positively correlated)
- implied_volatility_call_20: 0.648 (moderately positively correlated)

Redundancy cluster #15: 5 similar fields, mean |rho| 0.853 (representative: implied_volatility_put_10). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| sharesout | pv1 | -0.06 | 1.55 | +0.45 | -0.84 | yes |
| news_mins_4_chg | news12 | -0.05 | 1.59 | +0.48 | -0.36 | yes |
| fnd6_cld4 | fundamental6 | -0.02 | 1.58 | +0.47 | -0.43 | yes |
| anl4_cff_flag | analyst4 | -0.06 | 1.61 | +0.48 | -0.22 | yes |
| fn_oth_income_loss_derivatives_qualifying_as_hedges_of_tax_q | fundamental2 | -0.07 | 1.64 | +0.49 | -0.13 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
