---
field: implied_volatility_mean_90
dataset: option8
best_template: rank_delta
best_sharpe: 1.65
best_fitness: 0.65
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0506
ann_vol: 0.0537
hit_rate: 0.5393
rolling_sharpe_min: -0.142
rolling_sharpe_max: 3.18
top_merge_partner: current_ratio
redundancy_cluster: 4
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.67
---
# implied_volatility_mean_90 (option8)

*The average of IvCall90 and IvPut90*

## Signal Profile
- `rank(implied_volatility_mean_90)`: S=0.30, F=0.23, T=6.6%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_90 / close)`: S=0.11, F=0.04, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_90, 5))`: S=1.65, F=0.65, T=56.1%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_90)`: S=-0.14, F=-0.07, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_90, 5))`: S=-1.65, F=-0.65, T=56.1%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_90, 22)`: S=0.99, F=0.48, T=30.2%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_90, 10)`: S=-0.01, F=0.00, T=3.5%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_90, 22))`: S=0.90, F=0.36, T=32.7%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_90)`: S=-0.06, F=-0.02, T=10.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_90 / close)`: S=-0.02, F=0.00, T=7.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.67, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.95 (moderate), ret=+3.5%
  - 2020: S=2.23 (strong), ret=+10.3%
  - 2021: S=2.26 (strong), ret=+13.9%
  - 2022: S=2.42 (strong), ret=+17.2%
  - 2023: S=-0.22 (negative), ret=-0.9%

## Risk & Drawdown
- Max drawdown: 5.06% over 108 days (recovered)
- Annualized: return +9.0%, volatility 5.4% (fraction of booksize)
- Hit rate: 53.9% positive days
- Tail shape: skew +0.96, excess kurtosis +6.66

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.14, max 3.18, latest -0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.34%; worst month: -1.89%
Positive months: 68%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.10
- Sideways: S=1.24
- Bear: S=1.60

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_90 / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.67 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_90)`: S=-0.06, F=-0.02, T=10.2%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_90 / close)`: S=-0.02, F=0.00, T=7.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_90, 5))`: S=-1.65, F=-0.65, T=56.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_90, 5))` | TOP3000 | 1.67 | 0.65 | 5.1% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_mean_90, 5))` | TOP1000 | 1.08 | 0.46 | 7.4% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_90, 5))` | TOP500 | 0.75 | 0.28 | 7.6% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_90, 5))` | TOP200 | 0.62 | 0.25 | 17.8% | 80% | mixed |
| `rank(implied_volatility_mean_90)` | TOP200 | 0.31 | 0.23 | 73.2% | 60% | bear-only |
| `rank(implied_volatility_mean_90)` | TOP500 | 0.22 | 0.13 | 74.4% | 40% | bear-only |
| `rank(implied_volatility_mean_90)` | TOP1000 | 0.14 | 0.07 | 69.3% | 40% | bear-only |
| `rank(implied_volatility_mean_90)` | TOP3000 | 0.06 | 0.02 | 73.8% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_60: 0.955 (strongly positively correlated)
- implied_volatility_call_90: 0.946 (strongly positively correlated)
- implied_volatility_mean_120: 0.944 (strongly positively correlated)
- implied_volatility_call_120: 0.927 (strongly positively correlated)
- implied_volatility_put_90: 0.912 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| current_ratio | fundamental6 | -0.03 | 2.27 | +0.60 | +0.21 | yes |
| max_adjusted_net_income_guidance | company_guidance | -0.01 | 2.25 | +0.58 | +0.84 | yes |
| fnd6_ivaco | fundamental_investment | -0.10 | 2.23 | +0.56 | +0.71 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.01 | 2.17 | +0.50 | -0.39 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.01 | 2.17 | +0.50 | -0.39 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
