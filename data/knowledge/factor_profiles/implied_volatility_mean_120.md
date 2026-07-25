---
field: implied_volatility_mean_120
dataset: option8
best_template: rank_delta
best_sharpe: 1.58
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 8
max_drawdown: 0.0533
ann_vol: 0.055
hit_rate: 0.5385
rolling_sharpe_min: -0.616
rolling_sharpe_max: 3.202
top_merge_partner: current_ratio
redundancy_cluster: 4
negated_best_sharpe: -0.02
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -1.6
---
# implied_volatility_mean_120 (option8)

*The average of IvCall120 and IvPut120*

## Signal Profile
- `rank(implied_volatility_mean_120)`: S=0.28, F=0.21, T=6.2%, INFERIOR (TOP200)
- `rank(implied_volatility_mean_120 / close)`: S=0.11, F=0.04, T=4.3%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_mean_120, 5))`: S=1.58, F=0.62, T=56.1%, INFERIOR (TOP3000)
- `-rank(implied_volatility_mean_120)`: S=-0.13, F=-0.06, T=6.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_120, 5))`: S=-1.58, F=-0.62, T=56.1%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_mean_120, 22)`: S=1.02, F=0.51, T=30.2%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_mean_120, 10)`: S=0.00, F=0.00, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_mean_120, 22))`: S=1.06, F=0.47, T=32.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_120)`: S=-0.05, F=-0.02, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_120 / close)`: S=-0.02, F=0.00, T=7.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 20F/1P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.60, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.80 (moderate), ret=+2.9%
  - 2020: S=2.15 (strong), ret=+10.7%
  - 2021: S=1.94 (strong), ret=+12.1%
  - 2022: S=2.79 (strong), ret=+20.2%
  - 2023: S=-0.73 (negative), ret=-2.9%

## Risk & Drawdown
- Max drawdown: 5.33% over 106 days (recovered)
- Annualized: return +8.8%, volatility 5.5% (fraction of booksize)
- Hit rate: 53.8% positive days
- Tail shape: skew +0.97, excess kurtosis +6.63

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.62, max 3.20, latest -0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.69%; worst month: -1.93%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=2.07
- Sideways: S=1.30
- Bear: S=1.33

## Negated Direction
Best negated: `rank(-1 * implied_volatility_mean_120 / close)` S=-0.02, F=0.00, INFERIOR
Direction gap: -1.60 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_mean_120)`: S=-0.05, F=-0.02, T=9.8%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_mean_120 / close)`: S=-0.02, F=0.00, T=7.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_mean_120, 5))`: S=-1.58, F=-0.62, T=56.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_mean_120, 5))` | TOP3000 | 1.60 | 0.62 | 5.3% | 80% | all-weather |
| `rank(ts_delta(implied_volatility_mean_120, 5))` | TOP1000 | 1.07 | 0.44 | 6.2% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_120, 5))` | TOP500 | 0.88 | 0.37 | 7.4% | 80% | mixed |
| `rank(ts_delta(implied_volatility_mean_120, 5))` | TOP200 | 0.59 | 0.24 | 19.5% | 60% | mixed |
| `rank(implied_volatility_mean_120)` | TOP200 | 0.29 | 0.21 | 73.2% | 60% | bear-only |
| `rank(implied_volatility_mean_120)` | TOP500 | 0.21 | 0.13 | 74.3% | 40% | bear-only |
| `rank(implied_volatility_mean_120)` | TOP1000 | 0.14 | 0.06 | 69.5% | 40% | bear-only |
| `rank(implied_volatility_mean_120)` | TOP3000 | 0.06 | 0.02 | 74.4% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_mean_150: 0.976 (strongly positively correlated)
- implied_volatility_mean_180: 0.947 (strongly positively correlated)
- implied_volatility_mean_90: 0.944 (strongly positively correlated)
- implied_volatility_put_120: 0.938 (strongly positively correlated)
- implied_volatility_call_150: 0.936 (strongly positively correlated)

Redundancy cluster #4: 26 similar fields, mean |rho| 0.836 (representative: implied_volatility_put_90). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| current_ratio | fundamental6 | -0.05 | 2.26 | +0.60 | +0.28 | yes |
| max_adjusted_net_income_guidance | company_guidance | +0.01 | 2.17 | +0.57 | +0.77 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | +0.01 | 2.12 | +0.53 | -0.41 | yes |
| anl4_qf_az_wol_spfc | analyst4 | +0.01 | 2.12 | +0.53 | -0.41 | yes |
| fnd6_ivaco | fundamental_investment | -0.10 | 2.15 | +0.55 | +0.64 | yes |

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
