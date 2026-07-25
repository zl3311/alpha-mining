---
field: pcr_vol_all
dataset: option9
best_template: rank_level
best_sharpe: 0.69
best_fitness: 0.19
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.1107
ann_vol: 0.0514
hit_rate: 0.5304
rolling_sharpe_min: -1.111
rolling_sharpe_max: 2.563
redundancy_cluster: 23
negated_best_sharpe: -0.06
negated_best_template: neg_rank_value_norm
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -0.75
---
# pcr_vol_all (option9)

*Ratio of total put option volume to call option volume aggregated across all maturities, measuring short-term options flow sentiment*

## Signal Profile
- `rank(pcr_vol_all)`: S=0.69, F=0.19, T=48.6%, INFERIOR (TOP1000)
- `rank(ts_delta(pcr_vol_all, 5))`: S=0.51, F=0.12, T=67.7%, INFERIOR (TOP200)
- `-rank(pcr_vol_all)`: S=-0.69, F=-0.19, T=48.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_all, 5))`: S=-0.41, F=-0.05, T=88.3%, INFERIOR (TOP3000)
- `ts_zscore(pcr_vol_all, 22)`: S=0.76, F=0.18, T=58.1%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_all, 10)`: S=-0.23, F=-0.07, T=17.5%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_all, 22))`: S=0.63, F=0.13, T=61.5%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_all)`: S=-0.64, F=-0.13, T=64.0%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_all / close)`: S=-0.06, F=-0.01, T=60.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 19F/1P
- HIGH_TURNOVER: 6F/14P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.69, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.43 (weak), ret=+1.1%
  - 2020: S=0.10 (weak), ret=+0.5%
  - 2021: S=1.11 (moderate), ret=+8.8%
  - 2022: S=0.94 (moderate), ret=+4.7%
  - 2023: S=0.77 (moderate), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 11.07% over 287 days (recovered)
- Annualized: return +3.6%, volatility 5.1% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.14, excess kurtosis +4.11

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.11, max 2.56, latest 0.62

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +3.99%; worst month: -4.15%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.62
- Sideways: S=-0.11
- Bear: S=-0.89

## Negated Direction
Best negated: `rank(-1 * pcr_vol_all / close)` S=-0.06, F=-0.01, INFERIOR
Direction gap: -0.75 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_all)`: S=-0.64, F=-0.13, T=64.0%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_all / close)`: S=-0.06, F=-0.01, T=60.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_all, 5))`: S=-0.41, F=-0.05, T=88.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_vol_all)` | TOP1000 | 0.69 | 0.19 | 11.1% | 100% | bull-only |
| `rank(pcr_vol_all)` | TOP500 | 0.57 | 0.16 | 12.8% | 80% | mixed |
| `rank(pcr_vol_all)` | TOP3000 | 0.64 | 0.13 | 9.5% | 80% | bull-only |
| `rank(ts_delta(pcr_vol_all, 5))` | TOP200 | 0.53 | 0.12 | 5.9% | 80% | mixed |
| `rank(ts_delta(pcr_vol_all, 5))` | TOP1000 | 0.65 | 0.10 | 5.5% | 60% | mixed |
| `rank(ts_delta(pcr_vol_all, 5))` | TOP3000 | 0.42 | 0.05 | 4.6% | 40% | mixed |
| `rank(pcr_vol_all)` | TOP200 | 0.15 | 0.03 | 20.2% | 40% | weak |

## Correlation Notes
Top correlates:
- pcr_vol_20: 0.883 (strongly positively correlated)
- pcr_vol_30: 0.862 (strongly positively correlated)
- pcr_vol_10: 0.645 (moderately positively correlated)
- put_breakeven_720: 0.609 (moderately positively correlated)
- put_breakeven_1080: 0.609 (moderately positively correlated)

Redundancy cluster #23: 3 similar fields, mean |rho| 0.877 (representative: pcr_vol_20). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
