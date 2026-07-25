---
field: implied_volatility_put_150
dataset: option8
best_template: rank_delta
best_sharpe: 1.57
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.0521
ann_vol: 0.0508
hit_rate: 0.5401
rolling_sharpe_min: -1.121
rolling_sharpe_max: 3.59
top_merge_partner: max_adjusted_net_income_guidance
redundancy_cluster: 4
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.57
---
# implied_volatility_put_150 (option8)

*At-the-money implied volatility of put options with 150 calendar days to expiration, annualized decimal*

## Signal Profile
- `rank(implied_volatility_put_150)`: S=0.27, F=0.19, T=7.0%, INFERIOR (TOP200)
- `rank(implied_volatility_put_150 / close)`: S=0.10, F=0.03, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_put_150, 5))`: S=1.57, F=0.58, T=57.5%, INFERIOR (TOP3000)
- `-rank(implied_volatility_put_150)`: S=-0.12, F=-0.05, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_150, 5))`: S=-1.57, F=-0.58, T=57.5%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_put_150, 22)`: S=1.11, F=0.54, T=29.9%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_put_150, 10)`: S=-0.08, F=-0.04, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_put_150, 22))`: S=1.04, F=0.44, T=32.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_150)`: S=-0.03, F=-0.01, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_150 / close)`: S=0.00, F=0.00, T=6.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 4F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.57, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.85 (moderate), ret=+3.0%
  - 2020: S=2.50 (strong), ret=+10.8%
  - 2021: S=1.75 (strong), ret=+10.3%
  - 2022: S=2.89 (strong), ret=+19.1%
  - 2023: S=-1.12 (negative), ret=-4.1%

## Risk & Drawdown
- Max drawdown: 5.21% over 360 days (not yet recovered, ongoing at window end)
- Annualized: return +8.0%, volatility 5.1% (fraction of booksize)
- Hit rate: 54.0% positive days
- Tail shape: skew +1.11, excess kurtosis +7.79

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 3.59, latest -1.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +5.33%; worst month: -2.14%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.46
- Sideways: S=0.84
- Bear: S=1.17

## Negated Direction
Best negated: `rank(-1 * implied_volatility_put_150 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.57 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_put_150)`: S=-0.03, F=-0.01, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_put_150 / close)`: S=0.00, F=0.00, T=6.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_put_150, 5))`: S=-1.57, F=-0.58, T=57.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_put_150, 5))` | TOP3000 | 1.57 | 0.58 | 5.2% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_put_150, 5))` | TOP1000 | 1.09 | 0.43 | 5.5% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_150, 5))` | TOP500 | 0.88 | 0.35 | 8.0% | 80% | mixed |
| `rank(ts_delta(implied_volatility_put_150, 5))` | TOP200 | 0.77 | 0.34 | 12.3% | 80% | mixed |
| `rank(implied_volatility_put_150)` | TOP200 | 0.28 | 0.19 | 74.1% | 60% | bear-only |
| `rank(implied_volatility_put_150)` | TOP500 | 0.19 | 0.10 | 74.9% | 40% | bear-only |
| `rank(implied_volatility_put_150)` | TOP1000 | 0.12 | 0.05 | 69.5% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_put_120: 0.978 (strongly positively correlated)
- implied_volatility_put_180: 0.978 (strongly positively correlated)
- implied_volatility_mean_150: 0.940 (strongly positively correlated)
- implied_volatility_put_270: 0.930 (strongly positively correlated)
- implied_volatility_mean_120: 0.927 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| max_adjusted_net_income_guidance | company_guidance | +0.02 | 2.14 | +0.57 | +0.70 | yes |
| current_ratio | fundamental6 | -0.05 | 2.23 | +0.57 | +0.19 | yes |
| fnd6_ivaco | fundamental_investment | -0.07 | 2.12 | +0.55 | +0.56 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.03 | 2.08 | +0.50 | -0.31 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.03 | 2.08 | +0.50 | -0.31 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
