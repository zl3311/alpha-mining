---
field: total_assets_reported_value
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.72
best_fitness: 0.49
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.0942
ann_vol: 0.0802
hit_rate: 0.4834
rolling_sharpe_min: -0.752
rolling_sharpe_max: 2.323
redundancy_cluster: 1
negated_best_sharpe: 0.67
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: -0.05
---
# total_assets_reported_value (analyst4)

*Total Assets - actual value*

## Signal Profile
- `rank(total_assets_reported_value)`: S=0.49, F=0.31, T=2.4%, INFERIOR (TOP3000)
- `rank(total_assets_reported_value / close)`: S=0.72, F=0.49, T=2.8%, INFERIOR (TOP3000)
- `rank(ts_delta(total_assets_reported_value, 5))`: S=0.06, F=0.01, T=37.6%, INFERIOR (TOP3000)
- `-rank(total_assets_reported_value)`: S=-0.13, F=-0.05, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(total_assets_reported_value, 5))`: S=0.67, F=0.26, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(total_assets_reported_value, 63)`: S=0.38, F=0.13, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(total_assets_reported_value, 10)`: S=-0.33, F=-0.16, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(total_assets_reported_value, 22))`: S=-0.26, F=-0.07, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * total_assets_reported_value)`: S=0.29, F=0.18, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * total_assets_reported_value / close)`: S=0.18, F=0.08, T=2.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/6P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.71, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.29 (weak), ret=+1.6%
  - 2020: S=0.09 (weak), ret=+0.9%
  - 2021: S=1.37 (moderate), ret=+12.9%
  - 2022: S=0.99 (moderate), ret=+6.9%
  - 2023: S=0.96 (moderate), ret=+5.8%

## Risk & Drawdown
- Max drawdown: 9.42% over 239 days (recovered)
- Annualized: return +5.7%, volatility 8.0% (fraction of booksize)
- Hit rate: 48.3% positive days
- Tail shape: skew +0.71, excess kurtosis +3.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.75, max 2.32, latest 1.05

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.49%; worst month: -3.39%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.42
- Sideways: S=0.17
- Bear: S=-0.69

## Negated Direction
Best negated: `rank(-1 * ts_delta(total_assets_reported_value, 5))` S=0.67, F=0.26, INFERIOR
Direction gap: -0.05 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * total_assets_reported_value)`: S=0.29, F=0.18, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * total_assets_reported_value / close)`: S=0.18, F=0.08, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(total_assets_reported_value, 5))`: S=0.67, F=0.26, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(total_assets_reported_value / close)` | TOP3000 | 0.71 | 0.49 | 9.4% | 100% | bull-only |
| `rank(total_assets_reported_value)` | TOP3000 | 0.48 | 0.31 | 28.7% | 80% | bull-only |
| `rank(total_assets_reported_value / close)` | TOP1000 | 0.27 | 0.12 | 17.1% | 60% | bull-only |
| `rank(total_assets_reported_value)` | TOP1000 | 0.12 | 0.05 | 32.8% | 40% | bull-only |

## Correlation Notes
Top correlates:
- anl4_totassets_value: 1.000 (strongly positively correlated)
- anl4_totassets_mean: 0.971 (strongly positively correlated)
- anl4_totassets_median: 0.971 (strongly positively correlated)
- anl4_totassets_high: 0.971 (strongly positively correlated)
- anl4_totassets_low: 0.971 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
