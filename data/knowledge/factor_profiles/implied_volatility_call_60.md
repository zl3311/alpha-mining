---
field: implied_volatility_call_60
dataset: option8
best_template: rank_delta
best_sharpe: 0.96
best_fitness: 0.36
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.0695
ann_vol: 0.0687
hit_rate: 0.5101
rolling_sharpe_min: -0.389
rolling_sharpe_max: 2.141
top_merge_partner: anl4_afv4_dts_spe
redundancy_cluster: 20
negated_best_sharpe: 0.0
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 4
direction_gap: -0.96
---
# implied_volatility_call_60 (option8)

*Implied volatility of the at-the-money call for the stock with an expiration 60 calendar days from the measurement date*

## Signal Profile
- `rank(implied_volatility_call_60)`: S=0.31, F=0.24, T=7.6%, INFERIOR (TOP200)
- `rank(implied_volatility_call_60 / close)`: S=0.12, F=0.04, T=4.7%, INFERIOR (TOP3000)
- `rank(ts_delta(implied_volatility_call_60, 5))`: S=0.96, F=0.36, T=47.0%, INFERIOR (TOP1000)
- `-rank(implied_volatility_call_60)`: S=-0.16, F=-0.08, T=7.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_60, 5))`: S=-1.08, F=-0.33, T=58.2%, INFERIOR (TOP3000)
- `ts_zscore(implied_volatility_call_60, 22)`: S=0.81, F=0.34, T=30.6%, INFERIOR (TOP3000)
- `ts_mean(implied_volatility_call_60, 10)`: S=0.07, F=0.03, T=4.0%, INFERIOR (TOP3000)
- `rank(ts_rank(implied_volatility_call_60, 22))`: S=0.80, F=0.30, T=32.7%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_60)`: S=-0.08, F=-0.03, T=11.3%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_60 / close)`: S=0.00, F=0.00, T=7.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.96, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.67 (moderate), ret=+2.5%
  - 2020: S=1.31 (moderate), ret=+6.9%
  - 2021: S=1.59 (strong), ret=+13.4%
  - 2022: S=1.11 (moderate), ret=+10.4%
  - 2023: S=-0.14 (negative), ret=-0.8%

## Risk & Drawdown
- Max drawdown: 6.95% over 125 days (recovered)
- Annualized: return +6.6%, volatility 6.9% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.90, excess kurtosis +6.54

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.39, max 2.14, latest -0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +4.15%; worst month: -2.30%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.59
- Sideways: S=1.06
- Bear: S=0.07

## Negated Direction
Best negated: `rank(-1 * implied_volatility_call_60 / close)` S=0.00, F=0.00, INFERIOR
Direction gap: -0.96 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * implied_volatility_call_60)`: S=-0.08, F=-0.03, T=11.3%, INFERIOR (TOP3000)
- `rank(-1 * implied_volatility_call_60 / close)`: S=0.00, F=0.00, T=7.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(implied_volatility_call_60, 5))`: S=-1.08, F=-0.33, T=58.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(implied_volatility_call_60, 5))` | TOP1000 | 0.96 | 0.36 | 7.0% | 80% | mixed |
| `rank(ts_delta(implied_volatility_call_60, 5))` | TOP3000 | 1.11 | 0.33 | 4.6% | 80% | all-weather |
| `rank(implied_volatility_call_60)` | TOP200 | 0.32 | 0.24 | 73.7% | 60% | bear-only |
| `rank(ts_delta(implied_volatility_call_60, 5))` | TOP500 | 0.67 | 0.23 | 6.8% | 80% | mixed |
| `rank(ts_delta(implied_volatility_call_60, 5))` | TOP200 | 0.47 | 0.16 | 14.3% | 60% | mixed |
| `rank(implied_volatility_call_60)` | TOP500 | 0.22 | 0.13 | 74.9% | 60% | bear-only |
| `rank(implied_volatility_call_60)` | TOP1000 | 0.16 | 0.08 | 68.9% | 40% | bear-only |
| `rank(implied_volatility_call_60)` | TOP3000 | 0.08 | 0.03 | 72.5% | 40% | bear-only |

## Correlation Notes
Top correlates:
- implied_volatility_call_30: 0.882 (strongly positively correlated)
- implied_volatility_mean_30: 0.874 (strongly positively correlated)
- implied_volatility_put_30: 0.851 (strongly positively correlated)
- implied_volatility_call_20: 0.819 (strongly positively correlated)
- implied_volatility_mean_60: 0.787 (strongly positively correlated)

Redundancy cluster #20: 5 similar fields, mean |rho| 0.906 (representative: implied_volatility_call_20). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_afv4_dts_spe | analyst4 | -0.03 | 1.40 | +0.40 | -0.83 | yes |
| pcr_vol_60 | option9 | -0.02 | 1.32 | +0.36 | -0.84 | yes |
| fnd6_fopo | fundamental6 | -0.01 | 1.43 | +0.35 | -0.77 | yes |
| fnd6_txdbca | fundamental6 | -0.03 | 1.34 | +0.38 | -0.49 | yes |
| anl4_fcf_high | analyst4 | -0.05 | 1.44 | +0.42 | -0.10 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
