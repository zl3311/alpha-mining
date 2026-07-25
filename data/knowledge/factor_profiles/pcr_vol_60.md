---
field: pcr_vol_60
dataset: option9
best_template: rank_delta
best_sharpe: 0.87
best_fitness: 0.24
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0991
ann_vol: 0.0632
hit_rate: 0.5263
rolling_sharpe_min: -1.17
rolling_sharpe_max: 3.276
top_merge_partner: fnd2_a_ltrmdmrepoplay5
negated_best_sharpe: -0.1
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -0.97
---
# pcr_vol_60 (option9)

*Ratio of total put options volume to call options volume for contracts expiring 60 days in the future, indicating short-term options flow sentiment*

## Signal Profile
- `rank(pcr_vol_60)`: S=0.48, F=0.10, T=51.8%, INFERIOR (TOP1000)
- `rank(ts_delta(pcr_vol_60, 5))`: S=0.87, F=0.24, T=70.6%, INFERIOR (TOP200)
- `-rank(pcr_vol_60)`: S=-0.48, F=-0.10, T=51.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_60, 5))`: S=-0.66, F=-0.09, T=85.4%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_vol_60, 63)`: S=-0.01, F=0.00, T=55.8%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_60, 10)`: S=-0.19, F=-0.05, T=18.5%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_60, 22))`: S=-0.17, F=-0.02, T=63.7%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_60)`: S=-0.46, F=-0.08, T=60.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_60 / close)`: S=-0.10, F=-0.01, T=60.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 7F/13P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/6P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.89, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.01 (moderate), ret=+4.7%
  - 2020: S=0.54 (moderate), ret=+3.6%
  - 2021: S=-0.68 (negative), ret=-4.8%
  - 2022: S=1.68 (strong), ret=+11.6%
  - 2023: S=2.40 (strong), ret=+12.3%

## Risk & Drawdown
- Max drawdown: 9.91% over 575 days (recovered)
- Annualized: return +5.6%, volatility 6.3% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew +0.11, excess kurtosis +2.08

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.17, max 3.28, latest 2.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2021
Best month: +5.57%; worst month: -3.57%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.41
- Sideways: S=1.41
- Bear: S=-0.15

## Negated Direction
Best negated: `rank(-1 * pcr_vol_60 / close)` S=-0.10, F=-0.01, INFERIOR
Direction gap: -0.97 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_60)`: S=-0.46, F=-0.08, T=60.2%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_60 / close)`: S=-0.10, F=-0.01, T=60.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_60, 5))`: S=-0.66, F=-0.09, T=85.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pcr_vol_60, 5))` | TOP200 | 0.89 | 0.24 | 9.9% | 80% | mixed |
| `rank(pcr_vol_60)` | TOP1000 | 0.47 | 0.10 | 8.7% | 60% | bull-only |
| `rank(ts_delta(pcr_vol_60, 5))` | TOP3000 | 0.67 | 0.09 | 5.0% | 40% | mixed |
| `rank(pcr_vol_60)` | TOP3000 | 0.46 | 0.08 | 6.2% | 60% | mixed |
| `rank(pcr_vol_60)` | TOP200 | 0.32 | 0.07 | 15.5% | 80% | mixed |
| `rank(pcr_vol_60)` | TOP500 | 0.27 | 0.05 | 8.4% | 60% | bull-only |
| `rank(ts_delta(pcr_vol_60, 5))` | TOP1000 | 0.29 | 0.03 | 8.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pcr_vol_90: 0.542 (moderately positively correlated)
- news_vol_stddev: -0.109 (weakly negatively correlated)
- snt_buzz_bfl_fast_d1: 0.106 (weakly positively correlated)
- fn_profit_loss_a: -0.103 (weakly negatively correlated)
- scl12_buzz_fast_d1: -0.097 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd2_a_ltrmdmrepoplay5 | fundamental2 | -0.06 | 1.30 | +0.38 | -0.91 | yes |
| fnd2_dfdtxastxdfdexpcompbnf | fundamental2 | -0.03 | 1.28 | +0.38 | -0.84 | yes |
| fn_op_lease_min_pay_due_in_5y_a | fundamental2 | -0.01 | 1.27 | +0.37 | -0.85 | yes |
| fnd2_a_ltrmdmrepoplinyfour | fundamental2 | -0.04 | 1.27 | +0.37 | -0.77 | yes |
| implied_volatility_call_60 | option8 | -0.02 | 1.32 | +0.36 | -0.84 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
