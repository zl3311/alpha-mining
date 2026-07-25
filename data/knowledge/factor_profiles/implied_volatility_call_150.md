---
field: implied_volatility_call_150
dataset: option8
best_template: rank_delta
best_sharpe: 1.5
best_fitness: 0.54
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0502
ann_vol: 0.05
hit_rate: 0.532
rolling_sharpe_min: -0.343
rolling_sharpe_max: 3.22
top_merge_partner: max_adjusted_net_income_guidance
redundancy_cluster: 4
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.5
---
# implied_volatility_call_150 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 150 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_150)`: S=0.29, F=0.22, T=6.5%, INFERIOR (TOP200)
- `rank(implied_volatility_call_150 / close)`: S=0.12, F=0.05, T=4.4%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_150, 5))`: S=1.50, F=0.54, T=58.6%, INFERIOR (TOP3000)
- `-rank(implied_volatility_call_150)`: S=-0.15, F=-0.08, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_150, 5))`: S=-1.50, F=-0.54, T=58.6%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_150, 22)`: S=0.86, F=0.37, T=30.7%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_150, 10)`: S=0.09, F=0.04, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_150, 22))`: S=0.93, F=0.37, T=33.0%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_150)`: S=-0.09, F=-0.03, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_150 / close)`: S=0.00, F=0.00, T=6.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.21 (moderate), ret=+3.9%
  - 2020: S=2.36 (strong), ret=+10.9%
  - 2021: S=1.74 (strong), ret=+9.9%
  - 2022: S=2.01 (strong), ret=+13.2%
  - 2023: S=-0.16 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 5.02% over 106 days (recovered)
- Annualized: return +7.6%, volatility 5.0% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew +0.82, excess kurtosis +6.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.34, max 3.22, latest -0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +4.51%; worst month: -1.74%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.06
- Sideways: S=1.12
- Bear: S=1.30

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_150 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -1.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_150)`: S=-0.09, F=-0.03, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_150 / close)`: S=0.00, F=0.00, T=6.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_150, 5))`: S=-1.50, F=-0.54, T=58.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_150, 5))` | TOP3000 | 1.53 | 0.54 | 5.0% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_call_150, 5))` | TOP1000 | 0.97 | 0.37 | 6.5% | 80% | mixed |
| `rank(ts_delta(implied_volatility_call_150, 5))` | TOP500 | 0.70 | 0.25 | 9.2% | 80% | mixed |
| `rank(implied_volatility_call_150)` | TOP200 | 0.31 | 0.22 | 73.3% | 60% | bear-only |
| `rank(implied_volatility_call_150)` | TOP500 | 0.23 | 0.14 | 73.3% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_150, 5))` | TOP200 | 0.44 | 0.14 | 20.8% | 60% | mixed |
| `rank(implied_volatility_call_150)` | TOP1000 | 0.16 | 0.08 | 68.5% | 40% | bear-only |
| `rank(implied_volatility_call_150)` | TOP3000 | 0.10 | 0.03 | 72.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_180: 0.981 (strongly positively correlated)
- implied_volatility_call_120: 0.948 (strongly positively correlated)
- implied_volatility_mean_150: 0.944 (strongly positively correlated)
- implied_volatility_mean_120: 0.936 (strongly positively correlated)
- implied_volatility_mean_180: 0.932 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| max_adjusted_net_income_guidance | company_guidance | -0.02 | 2.15 | +0.63 | +0.69 | yes |
| fnd6_ivaco | fundamental_investment | -0.11 | 2.12 | +0.59 | +0.50 | yes |
| anl4_qf_az_wol_spfc | analyst4 | -0.01 | 2.08 | +0.55 | -0.15 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | -0.01 | 2.08 | +0.55 | -0.15 | yes |
| current_ratio | fundamental6 | -0.07 | 2.22 | +0.56 | -0.02 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
