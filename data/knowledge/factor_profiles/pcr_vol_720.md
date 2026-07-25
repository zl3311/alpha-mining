---
field: pcr_vol_720
dataset: option9
best_template: rank_level
best_sharpe: 0.57
best_fitness: 0.11
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.0418
ann_vol: 0.0238
hit_rate: 0.5198
rolling_sharpe_min: -1.644
rolling_sharpe_max: 2.495
negated_best_sharpe: -0.25
negated_best_template: neg_rank
negated_best_fitness: -0.03
n_negated_sims: 4
direction_gap: -0.82
---
# pcr_vol_720 (option9)

*Ratio of put options volume to call options volume for contracts expiring in 720 days on a stock's options*

## Signal Profile
- `rank(pcr_vol_720)`: S=0.57, F=0.11, T=59.6%, INFERIOR (TOP3000)
- `rank(pcr_vol_720 / close)`: S=0.11, F=0.01, T=50.4%, INFERIOR (TOP3000)
- `rank(ts_delta(pcr_vol_720, 5))`: S=0.78, F=0.11, T=86.2%, INFERIOR (TOP3000)
- `-rank(pcr_vol_720)`: S=-0.25, F=-0.03, T=51.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_720, 5))`: S=-0.78, F=-0.11, T=86.2%, INFERIOR (TOP3000)
- `-ts_zscore(pcr_vol_720, 63)`: S=0.24, F=0.03, T=56.5%, INFERIOR (TOP3000)
- `ts_mean(pcr_vol_720, 10)`: S=0.27, F=0.09, T=18.7%, INFERIOR (TOP3000)
- `rank(ts_rank(pcr_vol_720, 22))`: S=-0.46, F=-0.07, T=66.1%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_720)`: S=-0.57, F=-0.11, T=59.6%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_720 / close)`: S=-0.47, F=-0.09, T=61.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/0P
- HIGH_TURNOVER: 7F/14P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.06 (moderate), ret=+2.5%
  - 2020: S=1.85 (strong), ret=+4.4%
  - 2021: S=0.06 (weak), ret=+0.1%
  - 2022: S=-0.15 (negative), ret=-0.4%
  - 2023: S=1.22 (moderate), ret=+2.6%

## Risk & Drawdown
- Max drawdown: 4.18% over 515 days (not yet recovered, ongoing at window end)
- Annualized: return +1.9%, volatility 2.4% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew -0.07, excess kurtosis +1.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.64, max 2.50, latest 1.39

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +2.15%; worst month: -1.95%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.24
- Sideways: S=0.55
- Bear: S=1.50

## Negated Direction
Best negated: `-rank(pcr_vol_720)` S=-0.25, F=-0.03, INFERIOR
Direction gap: -0.82 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pcr_vol_720)`: S=-0.57, F=-0.11, T=59.6%, INFERIOR (TOP3000)
- `rank(-1 * pcr_vol_720 / close)`: S=-0.47, F=-0.09, T=61.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pcr_vol_720, 5))`: S=-0.78, F=-0.11, T=86.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pcr_vol_720)` | TOP3000 | 0.57 | 0.11 | 4.5% | 80% | weak |
| `rank(ts_delta(pcr_vol_720, 5))` | TOP3000 | 0.79 | 0.11 | 4.2% | 80% | mixed |
| `rank(pcr_vol_720)` | TOP1000 | 0.24 | 0.03 | 6.1% | 40% | mixed |

## Correlation Notes
Top correlates:
- pcr_vol_120: 0.438 (moderately positively correlated)
- pcr_vol_1080: 0.206 (weakly positively correlated)
- pcr_vol_270: 0.137 (weakly positively correlated)
- pcr_vol_180: 0.101 (weakly positively correlated)
- news_mins_20_pct_up: -0.095 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
