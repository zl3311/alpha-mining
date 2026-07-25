---
field: min_adjusted_funds_from_operations_guidance
dataset: analyst4
best_template: ts_mean
best_sharpe: 0.75
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0773
ann_vol: 0.0705
hit_rate: 0.5166
rolling_sharpe_min: -0.571
rolling_sharpe_max: 3.064
redundancy_cluster: 70
negated_best_sharpe: 0.23
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.1
n_negated_sims: 10
direction_gap: -0.52
---
# min_adjusted_funds_from_operations_guidance (analyst4)

*Funds from operation - minimum guidance value*

## Signal Profile
- `rank(min_adjusted_funds_from_operations_guidance)`: S=0.73, F=0.47, T=1.5%, INFERIOR (TOP1000)
- `rank(min_adjusted_funds_from_operations_guidance / close)`: S=0.08, F=0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_adjusted_funds_from_operations_guidance, 5))`: S=0.54, F=0.20, T=33.7%, INFERIOR (TOP200)
- `-rank(min_adjusted_funds_from_operations_guidance)`: S=-0.73, F=-0.47, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_adjusted_funds_from_operations_guidance, 5))`: S=-0.54, F=-0.20, T=33.7%, INFERIOR (TOP3000)
- `ts_zscore(min_adjusted_funds_from_operations_guidance, 22)`: S=0.03, F=0.00, T=42.8%, INFERIOR (TOP3000)
- `ts_mean(min_adjusted_funds_from_operations_guidance, 10)`: S=0.75, F=0.48, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(min_adjusted_funds_from_operations_guidance, 22))`: S=-0.05, F=-0.01, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * min_adjusted_funds_from_operations_guidance)`: S=-0.48, F=-0.38, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * min_adjusted_funds_from_operations_guidance / close)`: S=0.23, F=0.10, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.12 (weak), ret=+0.5%
  - 2020: S=-0.07 (negative), ret=-0.5%
  - 2021: S=2.21 (strong), ret=+15.4%
  - 2022: S=0.91 (moderate), ret=+5.8%
  - 2023: S=0.55 (moderate), ret=+4.4%

## Risk & Drawdown
- Max drawdown: 7.73% over 213 days (recovered)
- Annualized: return +5.2%, volatility 7.0% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.39, excess kurtosis +6.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.57, max 3.06, latest 0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +6.39%; worst month: -3.39%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.48
- Sideways: S=0.70
- Bear: S=-0.03

## Negated Direction
Best negated: `rank(-1 * min_adjusted_funds_from_operations_guidance / close)` S=0.23, F=0.10, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * min_adjusted_funds_from_operations_guidance)`: S=-0.48, F=-0.38, T=6.1%, INFERIOR (TOP3000)
- `rank(-1 * min_adjusted_funds_from_operations_guidance / close)`: S=0.23, F=0.10, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_adjusted_funds_from_operations_guidance, 5))`: S=-0.54, F=-0.20, T=33.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(min_adjusted_funds_from_operations_guidance)` | TOP1000 | 0.74 | 0.47 | 7.7% | 80% | mixed |
| `rank(ts_delta(min_adjusted_funds_from_operations_guidance, 5))` | TOP200 | 0.56 | 0.20 | 15.2% | 60% | bear-only |
| `rank(min_adjusted_funds_from_operations_guidance)` | TOP3000 | 0.32 | 0.11 | 9.2% | 60% | mixed |
| `rank(min_adjusted_funds_from_operations_guidance / close)` | TOP3000 | 0.08 | 0.02 | 52.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_adjusted_funds_from_operations_guidance: 1.000 (strongly positively correlated)
- free_cash_flow_per_share: 0.294 (weakly positively correlated)
- fnd6_oprepsx: 0.281 (weakly positively correlated)
- fnd6_newa2v1300_opeps: 0.281 (weakly positively correlated)
- fnd6_mfma2_opeps: 0.280 (weakly positively correlated)

Redundancy cluster #70: 2 similar fields, mean |rho| 1.0 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
