---
field: implied_volatility_put_60
dataset: option8
best_template: rank_delta
best_sharpe: 1.5
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0485
ann_vol: 0.049
hit_rate: 0.5231
rolling_sharpe_min: -0.535
rolling_sharpe_max: 3.479
top_merge_partner: max_adjusted_net_income_guidance
redundancy_cluster: 4
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.5
---
# implied_volatility_put_60 (option8)

*Implied volatility of the at-the-money put for the stock with an expiration 60 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_put_60)`: S=0.30, F=0.23, T=7.9%, INFERIOR (TOP200)
- `rank(implied_volatility_put_60 / close)`: S=0.10, F=0.03, T=4.5%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_60, 5))`: S=1.50, F=0.53, T=57.8%, INFERIOR (TOP3000)
- `-rank(implied_volatility_put_60)`: S=-0.14, F=-0.07, T=8.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_60, 5))`: S=-1.50, F=-0.53, T=57.8%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_60, 22)`: S=0.79, F=0.33, T=30.2%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_60, 10)`: S=-0.11, F=-0.06, T=4.1%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_60, 22))`: S=0.80, F=0.30, T=32.5%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_60)`: S=-0.04, F=-0.01, T=11.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_60 / close)`: S=0.00, F=0.00, T=7.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.51, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+1.0%
  - 2020: S=2.18 (strong), ret=+8.7%
  - 2021: S=2.21 (strong), ret=+13.0%
  - 2022: S=2.58 (strong), ret=+16.1%
  - 2023: S=-0.63 (negative), ret=-2.4%

## Risk & Drawdown
- Max drawdown: 4.85% over 344 days (recovered)
- Annualized: return +7.4%, volatility 4.9% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew +0.94, excess kurtosis +6.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.54, max 3.48, latest -0.54

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.01%; worst month: -2.58%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.31
- Sideways: S=0.66
- Bear: S=1.38

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_60 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_60)`: S=-0.04, F=-0.01, T=11.4%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_60 / close)`: S=0.00, F=0.00, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_60, 5))`: S=-1.50, F=-0.53, T=57.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_60, 5))` | TOP3000 | 1.51 | 0.53 | 4.9% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_put_60, 5))` | TOP1000 | 1.10 | 0.44 | 6.5% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_60, 5))` | TOP200 | 0.79 | 0.35 | 13.0% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_put_60, 5))` | TOP500 | 0.71 | 0.25 | 8.4% | 60% | mixed |
| `rank(implied_volatility_put_60)` | TOP200 | 0.30 | 0.23 | 73.5% | 60% | bear-only |
| `rank(implied_volatility_put_60)` | TOP500 | 0.20 | 0.12 | 74.8% | 40% | bear-only |
| `rank(implied_volatility_put_60)` | TOP1000 | 0.14 | 0.07 | 69.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_90: 0.949 (strongly positively correlated)
- implied_volatility_mean_60: 0.922 (strongly positively correlated)
- implied_volatility_mean_90: 0.885 (strongly positively correlated)
- implied_volatility_put_120: 0.884 (strongly positively correlated)
- implied_volatility_mean_120: 0.863 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| max_adjusted_net_income_guidance | company_guidance | +0.03 | 2.10 | +0.58 | +0.87 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.02 | 2.05 | +0.53 | -0.40 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.02 | 2.05 | +0.53 | -0.40 | yes |
| fnd6_ivaco | fundamental_investment | -0.06 | 2.07 | +0.55 | +0.78 | yes |
| fn_liab_fair_val_l2_q | fundamental2 | +0.09 | 1.96 | +0.45 | -0.71 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
