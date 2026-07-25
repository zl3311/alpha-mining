---
field: implied_volatility_call_720
dataset: option8
best_template: rank_delta
best_sharpe: 1.57
best_fitness: 0.52
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0384
ann_vol: 0.0424
hit_rate: 0.5409
rolling_sharpe_min: 0.423
rolling_sharpe_max: 2.741
top_merge_partner: fnd6_ivaco
redundancy_cluster: 4
negated_best_sharpe: -0.01
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.58
---
# implied_volatility_call_720 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 720 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_720)`: S=0.24, F=0.16, T=7.1%, INFERIOR (TOP200)
- `rank(implied_volatility_call_720 / close)`: S=0.13, F=0.05, T=4.6%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_720, 5))`: S=1.57, F=0.52, T=61.1%, INFERIOR (TOP3000)
- `-rank(implied_volatility_call_720)`: S=-0.16, F=-0.08, T=7.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_720, 5))`: S=-1.57, F=-0.52, T=61.1%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_720, 22)`: S=0.96, F=0.38, T=31.2%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_720, 10)`: S=0.06, F=0.02, T=3.6%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_720, 22))`: S=0.87, F=0.31, T=33.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_720)`: S=-0.10, F=-0.04, T=10.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_720 / close)`: S=-0.01, F=0.00, T=6.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 9F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.58, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.55 (moderate), ret=+1.5%
  - 2020: S=2.00 (strong), ret=+7.9%
  - 2021: S=2.35 (strong), ret=+10.6%
  - 2022: S=1.83 (strong), ret=+10.5%
  - 2023: S=0.74 (moderate), ret=+2.3%

## Risk & Drawdown
- Max drawdown: 3.84% over 330 days (recovered)
- Annualized: return +6.7%, volatility 4.2% (fraction of booksize)
- Hit rate: 54.1% positive days
- Tail shape: skew +0.95, excess kurtosis +8.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min 0.42, max 2.74, latest 0.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +4.88%; worst month: -2.51%
Positive months: 63%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.03
- Sideways: S=1.17
- Bear: S=1.47

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_720 / close)` S=-0.01, F=0.00, INFERIOR
Direction gap: -1.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_720)`: S=-0.10, F=-0.04, T=10.1%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_720 / close)`: S=-0.01, F=0.00, T=6.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_720, 5))`: S=-1.57, F=-0.52, T=61.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_720, 5))` | TOP3000 | 1.58 | 0.52 | 3.8% | 100% | all-weather |
| `rank(ts_delta(implied_volatility_call_720, 5))` | TOP1000 | 1.12 | 0.40 | 4.5% | 100% | mixed |
| `rank(implied_volatility_call_720)` | TOP200 | 0.26 | 0.16 | 71.6% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_720, 5))` | TOP500 | 0.57 | 0.16 | 12.8% | 100% | bull-only |
| `rank(implied_volatility_call_720)` | TOP500 | 0.22 | 0.12 | 69.8% | 60% | bear-only |
| `rank(implied_volatility_call_720)` | TOP1000 | 0.17 | 0.08 | 65.0% | 40% | bear-only |
| `rank(ts_delta(implied_volatility_call_720, 5))` | TOP200 | 0.28 | 0.07 | 30.9% | 60% | bull-only |
| `rank(implied_volatility_call_720)` | TOP3000 | 0.10 | 0.04 | 69.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_1080: 0.998 (strongly positively correlated)
- implied_volatility_call_360: 0.953 (strongly positively correlated)
- implied_volatility_call_270: 0.930 (strongly positively correlated)
- implied_volatility_mean_720: 0.916 (strongly positively correlated)
- implied_volatility_mean_1080: 0.916 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_ivaco | fundamental_investment | -0.16 | 2.25 | +0.67 | +0.94 | yes |
| max_adjusted_net_income_guidance | company_guidance | -0.04 | 2.21 | +0.63 | +0.97 | yes |
| current_ratio | fundamental6 | -0.07 | 2.19 | +0.52 | +0.33 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.01 | 2.06 | +0.48 | -0.32 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.01 | 2.06 | +0.48 | -0.32 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
