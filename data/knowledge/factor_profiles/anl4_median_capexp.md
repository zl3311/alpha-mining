---
field: anl4_median_capexp
dataset: analyst4
best_template: neg_rank_level
best_sharpe: 0.33
best_fitness: 0.21
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0792
ann_vol: 0.0484
hit_rate: 0.5263
rolling_sharpe_min: -1.121
rolling_sharpe_max: 3.419
redundancy_cluster: 45
negated_best_sharpe: 0.33
negated_best_template: neg_rank_level
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.27
---
# anl4_median_capexp (analyst4)

*Capital Expenditures - median of estimations*

## Signal Profile
- `rank(anl4_median_capexp)`: S=0.29, F=0.14, T=1.3%, INFERIOR (TOP3000)
- `rank(anl4_median_capexp / close)`: S=0.36, F=0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_median_capexp, 5))`: S=0.60, F=0.17, T=36.8%, INFERIOR (TOP3000)
- `-rank(anl4_median_capexp)`: S=-0.10, F=-0.03, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_median_capexp, 5))`: S=-0.10, F=-0.02, T=34.4%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_median_capexp, 63)`: S=-0.26, F=-0.07, T=17.7%, INFERIOR (TOP3000)
- `ts_mean(anl4_median_capexp, 10)`: S=-0.08, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_median_capexp, 22))`: S=0.17, F=0.04, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_median_capexp)`: S=0.33, F=0.21, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_median_capexp / close)`: S=0.25, F=0.12, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 4F/28P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.82 (strong), ret=+11.1%
  - 2020: S=0.72 (moderate), ret=+3.6%
  - 2021: S=0.67 (moderate), ret=+3.3%
  - 2022: S=0.30 (weak), ret=+1.6%
  - 2023: S=-1.09 (negative), ret=-4.8%

## Risk & Drawdown
- Max drawdown: 7.92% over 828 days (not yet recovered, ongoing at window end)
- Annualized: return +3.0%, volatility 4.8% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew -0.12, excess kurtosis +1.18

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 3.42, latest -1.11

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +3.99%; worst month: -2.29%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.47
- Sideways: S=0.91
- Bear: S=0.51

## Negated Direction
Best negated: `rank(-1 * anl4_median_capexp)` S=0.33, F=0.21, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_median_capexp)`: S=0.33, F=0.21, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * anl4_median_capexp / close)`: S=0.25, F=0.12, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_median_capexp, 5))`: S=-0.10, F=-0.02, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_median_capexp, 5))` | TOP3000 | 0.63 | 0.17 | 7.9% | 80% | mixed |
| `rank(anl4_median_capexp / close)` | TOP3000 | 0.35 | 0.16 | 9.7% | 60% | bull-only |
| `rank(anl4_median_capexp)` | TOP3000 | 0.28 | 0.14 | 32.2% | 80% | bull-only |
| `rank(ts_delta(anl4_median_capexp, 5))` | TOP1000 | 0.35 | 0.08 | 10.2% | 60% | weak |
| `rank(anl4_median_capexp)` | TOP1000 | 0.10 | 0.03 | 33.3% | 60% | bull-only |
| `rank(anl4_median_capexp / close)` | TOP1000 | 0.09 | 0.03 | 12.9% | 40% | bull-only |
| `rank(ts_delta(anl4_median_capexp, 5))` | TOP200 | 0.09 | 0.02 | 37.0% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_capex_high: 0.831 (strongly positively correlated)
- fn_oth_comp_fair_value_a: -0.230 (weakly negatively correlated)
- fn_oth_comp_forfeitures_fair_value_a: -0.228 (weakly negatively correlated)
- fnd6_optprcey: -0.227 (weakly negatively correlated)
- fn_comp_options_out_weighted_avg_a: -0.226 (weakly negatively correlated)

Redundancy cluster #45: 2 similar fields, mean |rho| 0.831 (representative: anl4_capex_high). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
