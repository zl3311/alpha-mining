---
field: rp_nip_ptg
dataset: news18
best_template: rank_level
best_sharpe: 0.77
best_fitness: 0.2
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1381
ann_vol: 0.0958
hit_rate: 0.5255
rolling_sharpe_min: -1.19
rolling_sharpe_max: 2.192
negated_best_sharpe: -0.16
negated_best_template: neg_rank_level
negated_best_fitness: -0.01
n_negated_sims: 4
direction_gap: -0.93
---
# rp_nip_ptg (news18)

*News impact projection of price target news*

## Signal Profile
- `rank(rp_nip_ptg)`: S=0.77, F=0.20, T=113.3%, INFERIOR (TOP200)
- `rank(rp_nip_ptg / close)`: S=0.19, F=0.02, T=121.1%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_ptg, 5))`: S=0.79, F=0.14, T=157.4%, INFERIOR (TOP1000)
- `-rank(rp_nip_ptg)`: S=-0.52, F=-0.07, T=128.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_ptg, 5))`: S=-0.38, F=-0.04, T=165.2%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_ptg, 63)`: S=0.03, F=0.00, T=136.2%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_ptg, 10)`: S=0.27, F=0.06, T=17.9%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_ptg, 22))`: S=0.04, F=0.00, T=138.6%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_ptg)`: S=-0.16, F=-0.01, T=142.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_ptg / close)`: S=-0.13, F=-0.01, T=136.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/14P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.76, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.26 (weak), ret=+2.9%
  - 2020: S=1.54 (strong), ret=+14.1%
  - 2021: S=0.60 (moderate), ret=+6.3%
  - 2022: S=1.28 (moderate), ret=+12.6%
  - 2023: S=-0.02 (negative), ret=-0.1%

## Risk & Drawdown
- Max drawdown: 13.81% over 547 days (recovered)
- Annualized: return +7.3%, volatility 9.6% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew +2.26, excess kurtosis +28.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.19, max 2.19, latest -0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +11.48%; worst month: -5.34%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.35
- Sideways: S=0.38
- Bear: S=1.72

## Negated Direction
Best negated: `rank(-1 * rp_nip_ptg)` S=-0.16, F=-0.01, INFERIOR
Direction gap: -0.93 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_nip_ptg)`: S=-0.16, F=-0.01, T=142.5%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_ptg / close)`: S=-0.13, F=-0.01, T=136.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_ptg, 5))`: S=-0.38, F=-0.04, T=165.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_nip_ptg)` | TOP200 | 0.76 | 0.20 | 13.8% | 80% | mixed |
| `rank(ts_delta(rp_nip_ptg, 5))` | TOP1000 | 0.79 | 0.14 | 9.1% | 80% | all-weather |
| `rank(rp_nip_ptg)` | TOP500 | 0.66 | 0.12 | 8.5% | 80% | mixed |
| `rank(ts_delta(rp_nip_ptg, 5))` | TOP500 | 0.63 | 0.11 | 14.6% | 60% | all-weather |
| `rank(rp_nip_ptg)` | TOP1000 | 0.54 | 0.07 | 6.9% | 60% | bear-only |
| `rank(ts_delta(rp_nip_ptg, 5))` | TOP3000 | 0.38 | 0.04 | 8.0% | 60% | all-weather |

## Correlation Notes
Top correlates:
- rp_nip_equity: 0.602 (moderately positively correlated)
- rp_nip_price: 0.320 (weakly positively correlated)
- rp_nip_insider: 0.298 (weakly positively correlated)
- anl4_cfi_low: 0.251 (weakly positively correlated)
- anl4_cfi_mean: 0.248 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
