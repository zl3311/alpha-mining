---
field: fnd6_invfg
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 1.09
best_fitness: 0.94
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.137
ann_vol: 0.088
hit_rate: 0.5126
rolling_sharpe_min: -1.765
rolling_sharpe_max: 2.465
redundancy_cluster: 13
negated_best_sharpe: 0.55
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: -0.54
---
# fnd6_invfg (fundamental6)

*Inventories - Finished Goods*

## Signal Profile
- `rank(fnd6_invfg)`: S=0.43, F=0.26, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_invfg / close)`: S=0.55, F=0.34, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_invfg, 5))`: S=0.34, F=0.13, T=39.1%, INFERIOR (TOP3000)
- `-rank(fnd6_invfg)`: S=-0.36, F=-0.21, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_invfg, 5))`: S=0.32, F=0.14, T=24.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_invfg, 63)`: S=0.42, F=0.30, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_invfg, 10)`: S=0.05, F=0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_invfg, 22))`: S=1.09, F=0.94, T=19.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_invfg)`: S=0.38, F=0.25, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_invfg / close)`: S=0.55, F=0.41, T=3.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.54, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.94 (negative), ret=-4.9%
  - 2020: S=-0.54 (negative), ret=-4.1%
  - 2021: S=1.48 (moderate), ret=+17.1%
  - 2022: S=1.16 (moderate), ret=+12.5%
  - 2023: S=0.44 (weak), ret=+2.7%

## Risk & Drawdown
- Max drawdown: 13.70% over 807 days (recovered)
- Annualized: return +4.8%, volatility 8.8% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.03, excess kurtosis +1.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.76, max 2.46, latest 0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.75%; worst month: -5.75%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.23
- Sideways: S=-0.03
- Bear: S=-2.40

## Negated Direction
Best negated: `rank(-1 * fnd6_invfg / close)` S=0.55, F=0.41, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_invfg)`: S=0.38, F=0.25, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_invfg / close)`: S=0.55, F=0.41, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_invfg, 5))`: S=0.32, F=0.14, T=24.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_invfg / close)` | TOP3000 | 0.54 | 0.34 | 13.7% | 60% | bull-only |
| `rank(fnd6_invfg)` | TOP3000 | 0.43 | 0.26 | 25.9% | 60% | bull-only |
| `rank(fnd6_invfg / close)` | TOP1000 | 0.41 | 0.24 | 13.8% | 60% | bull-only |
| `rank(fnd6_invfg)` | TOP1000 | 0.35 | 0.21 | 23.2% | 60% | bull-only |
| `rank(fnd6_invfg / close)` | TOP500 | 0.32 | 0.17 | 19.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_invfg, 5))` | TOP3000 | 0.33 | 0.13 | 36.9% | 60% | mixed |
| `rank(fnd6_invfg)` | TOP500 | 0.20 | 0.10 | 34.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_invt: 0.937 (strongly positively correlated)
- fnd6_newqv1300_invtq: 0.923 (strongly positively correlated)
- inventory: 0.923 (strongly positively correlated)
- fnd6_newqv1300_invwipq: 0.884 (strongly positively correlated)
- gross_income_reported_value: 0.870 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
