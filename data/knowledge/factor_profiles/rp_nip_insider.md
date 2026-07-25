---
field: rp_nip_insider
dataset: news18
best_template: rank_level
best_sharpe: 0.53
best_fitness: 0.11
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.1135
ann_vol: 0.1097
hit_rate: 0.5053
rolling_sharpe_min: -1.04
rolling_sharpe_max: 1.688
negated_best_sharpe: 0.61
negated_best_template: rank_neg_delta
negated_best_fitness: 0.11
n_negated_sims: 4
direction_gap: 0.08
---
# rp_nip_insider (news18)

*News impact projection of insider trading news*

## Signal Profile
- `rank(rp_nip_insider)`: S=0.53, F=0.11, T=131.9%, INFERIOR (TOP200)
- `rank(rp_nip_insider / close)`: S=-0.23, F=-0.03, T=140.7%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_insider, 5))`: S=-0.52, F=-0.10, T=166.2%, INFERIOR (TOP500)
- `-rank(rp_nip_insider)`: S=0.56, F=0.08, T=147.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_insider, 5))`: S=0.61, F=0.11, T=177.5%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_insider, 63)`: S=0.47, F=0.06, T=153.7%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_insider, 10)`: S=0.06, F=0.01, T=21.5%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_insider, 22))`: S=-0.41, F=-0.05, T=155.1%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_insider)`: S=-0.41, F=-0.05, T=156.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_insider / close)`: S=-0.55, F=-0.10, T=150.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 9F/12P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/7P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.53, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.50 (weak), ret=+4.6%
  - 2020: S=0.89 (moderate), ret=+11.5%
  - 2021: S=0.51 (moderate), ret=+5.9%
  - 2022: S=0.63 (moderate), ret=+7.6%
  - 2023: S=-0.17 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 11.35% over 148 days (recovered)
- Annualized: return +5.8%, volatility 11.0% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.67, excess kurtosis +7.91

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.04, max 1.69, latest -0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +7.61%; worst month: -7.11%
Positive months: 56%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.87
- Sideways: S=0.08
- Bear: S=0.58

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_nip_insider, 5))` S=0.61, F=0.11, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_nip_insider)`: S=-0.41, F=-0.05, T=156.2%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_insider / close)`: S=-0.55, F=-0.10, T=150.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_insider, 5))`: S=0.61, F=0.11, T=177.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_nip_insider)` | TOP200 | 0.53 | 0.11 | 11.3% | 80% | all-weather |
| `rank(rp_nip_insider)` | TOP500 | 0.36 | 0.05 | 11.8% | 60% | bear-only |
| `rank(rp_nip_insider)` | TOP3000 | 0.41 | 0.05 | 9.0% | 60% | bear-only |

## Correlation Notes
Top correlates:
- rp_nip_equity: 0.323 (weakly positively correlated)
- rp_nip_ptg: 0.298 (weakly positively correlated)
- anl4_cff_median: 0.265 (weakly positively correlated)
- anl4_cff_low: 0.263 (weakly positively correlated)
- fnd6_recta: 0.257 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
