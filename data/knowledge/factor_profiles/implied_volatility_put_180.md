---
field: implied_volatility_put_180
dataset: option8
best_template: ts_zscore
best_sharpe: 1.11
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0584
ann_vol: 0.0495
hit_rate: 0.5296
rolling_sharpe_min: -1.191
rolling_sharpe_max: 3.555
top_merge_partner: anl4_qf_az_wol_spfc
redundancy_cluster: 4
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.11
---
# implied_volatility_put_180 (option8)

*At-the-money implied volatility of put options with 180 calendar days to expiration, annualized decimal*

## Signal Profile
- `rank(implied_volatility_put_180)`: S=0.26, F=0.18, T=7.0%, INFERIOR (TOP200)
- `rank(implied_volatility_put_180 / close)`: S=0.10, F=0.03, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_180, 5))`: S=1.43, F=0.50, T=57.7%, INFERIOR (TOP3000)
- `-rank(implied_volatility_put_180)`: S=-0.12, F=-0.05, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_180, 5))`: S=-1.43, F=-0.50, T=57.7%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_180, 22)`: S=1.11, F=0.54, T=29.9%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_180, 10)`: S=-0.08, F=-0.03, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_180, 22))`: S=1.04, F=0.44, T=32.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_180)`: S=-0.03, F=-0.01, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_180 / close)`: S=0.00, F=0.00, T=6.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 4F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.43, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.58 (moderate), ret=+2.0%
  - 2020: S=2.16 (strong), ret=+9.4%
  - 2021: S=1.97 (strong), ret=+11.5%
  - 2022: S=2.49 (strong), ret=+15.9%
  - 2023: S=-1.12 (negative), ret=-4.0%

## Risk & Drawdown
- Max drawdown: 5.84% over 358 days (not yet recovered, ongoing at window end)
- Annualized: return +7.1%, volatility 5.0% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew +1.03, excess kurtosis +7.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.19, max 3.56, latest -1.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.97%; worst month: -2.14%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.37
- Sideways: S=0.46
- Bear: S=1.17

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_180 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.11 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_180)`: S=-0.03, F=-0.01, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_180 / close)`: S=0.00, F=0.00, T=6.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_180, 5))`: S=-1.43, F=-0.50, T=57.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_180, 5))` | TOP3000 | 1.43 | 0.50 | 5.8% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_put_180, 5))` | TOP1000 | 0.96 | 0.36 | 5.7% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_180, 5))` | TOP500 | 0.84 | 0.32 | 9.0% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_180, 5))` | TOP200 | 0.66 | 0.27 | 13.2% | 80% | mixed |
| `rank(implied_volatility_put_180)` | TOP200 | 0.27 | 0.18 | 73.9% | 60% | bear-only |
| `rank(implied_volatility_put_180)` | TOP500 | 0.18 | 0.10 | 74.6% | 40% | bear-only |
| `rank(implied_volatility_put_180)` | TOP1000 | 0.12 | 0.05 | 69.3% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_150: 0.978 (strongly positively correlated)
- implied_volatility_put_270: 0.963 (strongly positively correlated)
- implied_volatility_put_120: 0.945 (strongly positively correlated)
- implied_volatility_put_360: 0.943 (strongly positively correlated)
- implied_volatility_mean_180: 0.925 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_qf_az_wol_spfc | analyst4 | +0.02 | 2.00 | +0.55 | -0.37 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.02 | 2.00 | +0.55 | -0.37 | yes |
| fnd6_ivaco | fundamental_investment | -0.09 | 2.02 | +0.58 | +0.66 | yes |
| max_adjusted_net_income_guidance | company_guidance | +0.01 | 2.05 | +0.56 | +0.80 | yes |
| fnd6_acdo | fundamental_discontinued_ops | -0.06 | 1.99 | +0.55 | +0.36 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
