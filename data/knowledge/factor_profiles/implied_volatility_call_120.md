---
field: implied_volatility_call_120
dataset: option8
best_template: rank_delta
best_sharpe: 1.38
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0508
ann_vol: 0.0512
hit_rate: 0.532
rolling_sharpe_min: -0.185
rolling_sharpe_max: 2.987
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.38
---
# implied_volatility_call_120 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 120 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_120)`: S=0.30, F=0.22, T=6.5%, INFERIOR (TOP200)
- `rank(implied_volatility_call_120 / close)`: S=0.12, F=0.05, T=4.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_120, 5))`: S=1.38, F=0.48, T=58.5%, INFERIOR (TOP3000)
- `-rank(implied_volatility_call_120)`: S=-0.15, F=-0.08, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_120, 5))`: S=-1.38, F=-0.48, T=58.5%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_120, 22)`: S=0.78, F=0.32, T=30.8%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_120, 10)`: S=0.09, F=0.04, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_120, 22))`: S=0.84, F=0.32, T=33.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_120)`: S=-0.08, F=-0.03, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_120 / close)`: S=0.00, F=0.00, T=6.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.40, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.21 (moderate), ret=+4.0%
  - 2020: S=1.97 (strong), ret=+9.5%
  - 2021: S=1.76 (strong), ret=+10.3%
  - 2022: S=1.71 (strong), ret=+11.3%
  - 2023: S=-0.00 (negative), ret=-0.0%

## Risk & Drawdown
- Max drawdown: 5.08% over 111 days (recovered)
- Annualized: return +7.2%, volatility 5.1% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew +0.72, excess kurtosis +5.68

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.18, max 2.99, latest 0.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +4.37%; worst month: -1.56%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.47
- Sideways: S=1.39
- Bear: S=1.38

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_120 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.38 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_120)`: S=-0.08, F=-0.03, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_120 / close)`: S=0.00, F=0.00, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_120, 5))`: S=-1.38, F=-0.48, T=58.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_120, 5))` | TOP3000 | 1.40 | 0.48 | 5.1% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_call_120, 5))` | TOP1000 | 0.96 | 0.36 | 6.2% | 80% | mixed |
| `rank(ts_delta(implied_volatility_call_120, 5))` | TOP500 | 0.80 | 0.31 | 7.2% | 80% | mixed |
| `rank(implied_volatility_call_120)` | TOP200 | 0.31 | 0.22 | 73.5% | 60% | bear-only |
| `rank(implied_volatility_call_120)` | TOP500 | 0.23 | 0.14 | 73.7% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_120, 5))` | TOP200 | 0.41 | 0.13 | 22.4% | 60% | mixed |
| `rank(implied_volatility_call_120)` | TOP1000 | 0.16 | 0.08 | 68.8% | 40% | bear-only |
| `rank(implied_volatility_call_120)` | TOP3000 | 0.09 | 0.03 | 72.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_90: 0.971 (strongly positively correlated)
- implied_volatility_call_150: 0.948 (strongly positively correlated)
- implied_volatility_mean_90: 0.927 (strongly positively correlated)
- implied_volatility_call_180: 0.914 (strongly positively correlated)
- implied_volatility_mean_120: 0.912 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.12 | 2.01 | +0.61 | +0.54 | yes |
| max_adjusted_net_income_guidance | company_guidance | -0.03 | 2.07 | +0.58 | +0.74 | yes |
| fnd6_acdo | fundamental_discontinued_ops | -0.07 | 1.99 | +0.58 | +0.30 | yes |
| anl4_qf_az_wol_spfc | analyst4 | -0.00 | 2.00 | +0.56 | -0.22 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | -0.00 | 2.00 | +0.56 | -0.22 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
