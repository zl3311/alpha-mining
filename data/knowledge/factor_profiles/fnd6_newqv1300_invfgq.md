---
field: fnd6_newqv1300_invfgq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 1.25
best_fitness: 0.84
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_FITNESS
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1459
ann_vol: 0.1277
hit_rate: 0.5085
rolling_sharpe_min: -0.719
rolling_sharpe_max: 2.451
redundancy_cluster: 55
negated_best_sharpe: 1.25
negated_best_template: rank_neg_delta
negated_best_fitness: 0.84
n_negated_sims: 10
direction_gap: 0.68
---
# fnd6_newqv1300_invfgq (fundamental6)

*Inventory - Finished Goods*

## Signal Profile
- `rank(fnd6_newqv1300_invfgq)`: S=0.49, F=0.36, T=8.0%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_invfgq / close)`: S=0.57, F=0.44, T=8.1%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_invfgq, 5))`: S=0.03, F=0.00, T=52.3%, INFERIOR (TOP1000)
- `-rank(fnd6_newqv1300_invfgq)`: S=-0.37, F=-0.23, T=7.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_invfgq, 5))`: S=1.25, F=0.84, T=56.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_invfgq, 63)`: S=0.54, F=0.21, T=21.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_invfgq, 10)`: S=0.07, F=0.02, T=2.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_invfgq, 22))`: S=-0.11, F=-0.02, T=21.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invfgq)`: S=0.36, F=0.24, T=9.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invfgq / close)`: S=0.55, F=0.43, T=9.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 29F/3P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.57, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.06 (strong), ret=+15.1%
  - 2020: S=-0.20 (negative), ret=-2.5%
  - 2021: S=0.99 (moderate), ret=+19.1%
  - 2022: S=0.76 (moderate), ret=+8.9%
  - 2023: S=-0.65 (negative), ret=-5.0%

## Risk & Drawdown
- Max drawdown: 14.59% over 148 days (recovered)
- Annualized: return +7.3%, volatility 12.8% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.02, excess kurtosis +1.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.72, max 2.45, latest -0.68

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +11.02%; worst month: -8.41%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.31
- Sideways: S=1.30
- Bear: S=-2.08

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_invfgq, 5))` S=1.25, F=0.84, INFERIOR
Direction gap: +0.68 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_invfgq)`: S=0.36, F=0.24, T=9.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_invfgq / close)`: S=0.55, F=0.43, T=9.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_invfgq, 5))`: S=1.25, F=0.84, T=56.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_invfgq / close)` | TOP500 | 0.57 | 0.44 | 14.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_invfgq)` | TOP500 | 0.49 | 0.36 | 22.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_invfgq / close)` | TOP3000 | 0.40 | 0.23 | 15.6% | 40% | bull-only |
| `rank(fnd6_newqv1300_invfgq)` | TOP1000 | 0.36 | 0.23 | 22.9% | 60% | bull-only |
| `rank(fnd6_newqv1300_invfgq)` | TOP3000 | 0.38 | 0.23 | 26.2% | 40% | bull-only |
| `rank(fnd6_newqv1300_invfgq / close)` | TOP1000 | 0.35 | 0.21 | 15.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_invrmq: 0.816 (strongly positively correlated)
- fnd6_loxdr: 0.719 (strongly positively correlated)
- pv13_revere_term_sector_total: 0.704 (strongly positively correlated)
- fnd6_invwip: 0.703 (strongly positively correlated)
- min_free_cashflow_per_share_guidance: 0.696 (moderately positively correlated)

Redundancy cluster #55: 2 similar fields, mean |rho| 0.816 (representative: fnd6_newqv1300_invrmq). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_FITNESS. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
