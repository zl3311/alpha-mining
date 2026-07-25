---
field: implied_volatility_call_180
dataset: option8
best_template: rank_delta
best_sharpe: 1.47
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0413
ann_vol: 0.049
hit_rate: 0.5385
rolling_sharpe_min: -0.507
rolling_sharpe_max: 3.091
top_merge_partner: max_adjusted_net_income_guidance
redundancy_cluster: 4
negated_best_sharpe: -0.01
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.48
---
# implied_volatility_call_180 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 180 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_180)`: S=0.29, F=0.21, T=6.4%, INFERIOR (TOP200)
- `rank(implied_volatility_call_180 / close)`: S=0.12, F=0.05, T=4.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_180, 5))`: S=1.47, F=0.51, T=58.9%, INFERIOR (TOP3000)
- `-rank(implied_volatility_call_180)`: S=-0.15, F=-0.08, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_180, 5))`: S=-1.47, F=-0.51, T=58.9%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_180, 22)`: S=0.84, F=0.35, T=30.8%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_180, 10)`: S=0.09, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_180, 22))`: S=0.78, F=0.28, T=33.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_180)`: S=-0.09, F=-0.04, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_180 / close)`: S=-0.01, F=0.00, T=6.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.49, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.88 (moderate), ret=+2.7%
  - 2020: S=2.30 (strong), ret=+10.2%
  - 2021: S=1.92 (strong), ret=+10.6%
  - 2022: S=1.99 (strong), ret=+13.1%
  - 2023: S=-0.25 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 4.13% over 98 days (recovered)
- Annualized: return +7.3%, volatility 4.9% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew +0.96, excess kurtosis +7.38

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.51, max 3.09, latest -0.15

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +4.92%; worst month: -1.98%
Positive months: 66%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.17
- Sideways: S=0.92
- Bear: S=1.22

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_180 / close)` S=-0.01, F=0.00, INFERIOR
Direction gap: -1.48 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_180)`: S=-0.09, F=-0.04, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_180 / close)`: S=-0.01, F=0.00, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_180, 5))`: S=-1.47, F=-0.51, T=58.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_180, 5))` | TOP3000 | 1.49 | 0.51 | 4.1% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_call_180, 5))` | TOP1000 | 0.97 | 0.36 | 6.8% | 80% | mixed |
| `rank(ts_delta(implied_volatility_call_180, 5))` | TOP500 | 0.65 | 0.22 | 10.4% | 80% | bull-only |
| `rank(implied_volatility_call_180)` | TOP200 | 0.30 | 0.21 | 73.0% | 60% | bear-only |
| `rank(implied_volatility_call_180)` | TOP500 | 0.23 | 0.14 | 72.9% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_180, 5))` | TOP200 | 0.40 | 0.12 | 17.8% | 60% | mixed |
| `rank(implied_volatility_call_180)` | TOP1000 | 0.16 | 0.08 | 68.1% | 40% | bear-only |
| `rank(implied_volatility_call_180)` | TOP3000 | 0.10 | 0.04 | 71.7% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_150: 0.981 (strongly positively correlated)
- implied_volatility_call_270: 0.958 (strongly positively correlated)
- implied_volatility_mean_180: 0.944 (strongly positively correlated)
- implied_volatility_call_360: 0.938 (strongly positively correlated)
- implied_volatility_mean_150: 0.934 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| max_adjusted_net_income_guidance | company_guidance | -0.02 | 2.12 | +0.63 | +0.80 | yes |
| fnd6_ivaco | fundamental_investment | -0.11 | 2.09 | +0.60 | +0.64 | yes |
| anl4_qf_az_wol_spfc | analyst4 | -0.00 | 2.05 | +0.56 | -0.22 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | -0.00 | 2.05 | +0.56 | -0.22 | yes |
| fnd6_acdo | fundamental_discontinued_ops | -0.07 | 2.03 | +0.54 | +0.40 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
