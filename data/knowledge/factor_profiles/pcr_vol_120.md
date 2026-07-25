---
field: pcr_vol_120
dataset: option9
best_template: rank_delta
best_sharpe: 0.68
best_fitness: 0.1
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.0543
ann_vol: 0.0251
hit_rate: 0.5182
rolling_sharpe_min: -1.578
rolling_sharpe_max: 3.47
negated_best_sharpe: -0.19
negated_best_template: neg_rank
negated_best_fitness: -0.02
n_negated_sims: 4
direction_gap: -0.87
---
# pcr_vol_120 (option9)

*Ratio of put options volume to call options volume for contracts expiring in 120 days on a stock's options*

## Signal Profile
- `rank(pcr_vol_120)`: S=0.42, F=0.07, T=58.8%, INFERIOR (TOP3000)
- `rank(pcr_vol_120 / close)`: S=0.05, F=0.01, T=44.4%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_vol_120, 5))`: S=0.68, F=0.10, T=85.9%, INFERIOR (TOP3000)
- `-rank(pcr_vol_120)`: S=-0.19, F=-0.02, T=50.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_120, 5))`: S=-0.68, F=-0.10, T=85.9%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_vol_120, 63)`: S=0.49, F=0.09, T=56.1%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_120, 10)`: S=-0.22, F=-0.06, T=18.3%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_120, 22))`: S=-0.35, F=-0.05, T=64.6%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_120)`: S=-0.42, F=-0.07, T=58.8%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_120 / close)`: S=-0.16, F=-0.02, T=60.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 7F/14P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.69, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.60 (moderate), ret=+1.4%
  - 2020: S=1.34 (moderate), ret=+3.4%
  - 2021: S=0.24 (weak), ret=+0.6%
  - 2022: S=-1.45 (negative), ret=-3.9%
  - 2023: S=3.29 (strong), ret=+7.0%

## Risk & Drawdown
- Max drawdown: 5.43% over 649 days (recovered)
- Annualized: return +1.7%, volatility 2.5% (fraction of booksize)
- Hit rate: 51.8% positive days
- Tail shape: skew +0.01, excess kurtosis +1.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.58, max 3.47, latest 3.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +1.61%; worst month: -1.88%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.85
- Sideways: S=1.79
- Bear: S=-0.48

## Negated Direction
Best negated: `-rank(pcr_vol_120)` S=-0.19, F=-0.02, INFERIOR
Direction gap: -0.87 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_120)`: S=-0.42, F=-0.07, T=58.8%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_120 / close)`: S=-0.16, F=-0.02, T=60.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_120, 5))`: S=-0.68, F=-0.10, T=85.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(pcr_vol_120, 5))` | TOP3000 | 0.69 | 0.10 | 5.4% | 80% | mixed |
| `rank(pcr_vol_120)` | TOP3000 | 0.42 | 0.07 | 6.1% | 60% | mixed |
| `rank(pcr_vol_120)` | TOP500 | 0.23 | 0.04 | 13.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- pcr_vol_720: 0.438 (moderately positively correlated)
- pcr_vol_150: 0.172 (weakly positively correlated)
- pcr_vol_180: 0.148 (weakly positively correlated)
- pcr_vol_90: 0.147 (weakly positively correlated)
- pcr_vol_1080: 0.125 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
