---
field: implied_volatility_call_90
dataset: option8
best_template: rank_delta
best_sharpe: 1.44
best_fitness: 0.51
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0469
ann_vol: 0.0505
hit_rate: 0.5166
rolling_sharpe_min: 0.278
rolling_sharpe_max: 2.546
top_merge_partner: anl4_qf_az_wol_spfc
redundancy_cluster: 4
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.44
---
# implied_volatility_call_90 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 90 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_90)`: S=0.31, F=0.24, T=6.8%, INFERIOR (TOP200)
- `rank(implied_volatility_call_90 / close)`: S=0.12, F=0.05, T=4.5%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_90, 5))`: S=1.44, F=0.51, T=58.3%, INFERIOR (TOP3000)
- `-rank(implied_volatility_call_90)`: S=-0.16, F=-0.08, T=7.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_90, 5))`: S=-1.44, F=-0.51, T=58.3%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_90, 22)`: S=0.82, F=0.35, T=30.8%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_90, 10)`: S=0.09, F=0.04, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_90, 22))`: S=0.84, F=0.32, T=33.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_90)`: S=-0.08, F=-0.03, T=10.3%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_90 / close)`: S=0.00, F=0.00, T=6.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.46, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.93 (moderate), ret=+3.1%
  - 2020: S=1.57 (strong), ret=+7.2%
  - 2021: S=2.15 (strong), ret=+12.3%
  - 2022: S=1.84 (strong), ret=+12.2%
  - 2023: S=0.36 (weak), ret=+1.3%

## Risk & Drawdown
- Max drawdown: 4.69% over 111 days (recovered)
- Annualized: return +7.4%, volatility 5.1% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.74, excess kurtosis +5.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.28, max 2.55, latest 0.53

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.39%; worst month: -1.51%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.68
- Sideways: S=1.34
- Bear: S=1.35

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_90 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.44 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_90)`: S=-0.08, F=-0.03, T=10.3%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_90 / close)`: S=0.00, F=0.00, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_90, 5))`: S=-1.44, F=-0.51, T=58.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_90, 5))` | TOP3000 | 1.46 | 0.51 | 4.7% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_90, 5))` | TOP1000 | 1.04 | 0.41 | 7.2% | 80% | mixed |
| `rank(ts_delta(implied_volatility_call_90, 5))` | TOP500 | 0.76 | 0.28 | 7.3% | 80% | mixed |
| `rank(implied_volatility_call_90)` | TOP200 | 0.32 | 0.24 | 73.4% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_90, 5))` | TOP200 | 0.53 | 0.19 | 18.2% | 80% | mixed |
| `rank(implied_volatility_call_90)` | TOP500 | 0.23 | 0.14 | 74.0% | 60% | bear-only |
| `rank(implied_volatility_call_90)` | TOP1000 | 0.16 | 0.08 | 68.8% | 40% | bear-only |
| `rank(implied_volatility_call_90)` | TOP3000 | 0.09 | 0.03 | 72.8% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_120: 0.971 (strongly positively correlated)
- implied_volatility_mean_90: 0.946 (strongly positively correlated)
- implied_volatility_mean_60: 0.912 (strongly positively correlated)
- implied_volatility_call_150: 0.905 (strongly positively correlated)
- implied_volatility_mean_120: 0.896 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_qf_az_wol_spfc | analyst4 | +0.00 | 2.04 | +0.57 | -0.54 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.00 | 2.04 | +0.57 | -0.54 | yes |
| max_adjusted_net_income_guidance | company_guidance | -0.03 | 2.12 | +0.63 | +0.95 | yes |
| fnd6_ivaco | fundamental_investment | -0.13 | 2.08 | +0.62 | +0.83 | yes |
| fnd6_acdo | fundamental_discontinued_ops | -0.06 | 2.01 | +0.55 | +0.61 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
