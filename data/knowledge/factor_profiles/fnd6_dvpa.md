---
field: fnd6_dvpa
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.64
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.216
ann_vol: 0.0736
hit_rate: 0.4607
rolling_sharpe_min: -2.84
rolling_sharpe_max: 2.443
negated_best_sharpe: 0.24
negated_best_template: neg_rank_level
negated_best_fitness: 0.15
n_negated_sims: 10
direction_gap: -0.4
---
# fnd6_dvpa (fundamental6)

*Preferred Dividends in Arrears*

## Signal Profile
- `rank(fnd6_dvpa)`: S=0.34, F=0.23, T=3.9%, INFERIOR (TOP200)
- `rank(fnd6_dvpa / close)`: S=0.34, F=0.23, T=3.9%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_dvpa, 5))`: S=0.64, F=0.55, T=6.5%, INFERIOR (TOP3000)
- `-rank(fnd6_dvpa)`: S=0.18, F=0.10, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dvpa, 5))`: S=-0.16, F=-0.05, T=4.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_dvpa, 22)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_dvpa, 10)`: S=0.04, F=0.01, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dvpa, 22))`: S=0.11, F=0.04, T=5.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dvpa)`: S=0.24, F=0.15, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dvpa / close)`: S=0.24, F=0.15, T=4.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/18P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.67 (strong), ret=+7.5%
  - 2020: S=-1.20 (negative), ret=-6.2%
  - 2021: S=1.31 (moderate), ret=+16.2%
  - 2022: S=1.29 (moderate), ret=+8.4%
  - 2023: S=0.17 (weak), ret=+0.8%

## Risk & Drawdown
- Max drawdown: 21.60% over 518 days (recovered)
- Annualized: return +5.4%, volatility 7.4% (fraction of booksize)
- Hit rate: 46.1% positive days
- Tail shape: skew +0.83, excess kurtosis +10.61

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.84, max 2.44, latest 0.18

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +9.39%; worst month: -6.68%
Positive months: 64%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.22
- Sideways: S=1.32
- Bear: S=-1.57

## Negated Direction
Best negated: `rank(-1 * fnd6_dvpa)` S=0.24, F=0.15, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_dvpa)`: S=0.24, F=0.15, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dvpa / close)`: S=0.24, F=0.15, T=4.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dvpa, 5))`: S=-0.16, F=-0.05, T=4.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_dvpa, 5))` | TOP500 | 0.74 | 0.55 | 21.6% | 80% | bull-only |
| `rank(ts_delta(fnd6_dvpa, 5))` | TOP3000 | 0.63 | 0.55 | 16.5% | 80% | mixed |
| `rank(fnd6_dvpa)` | TOP200 | 0.32 | 0.23 | 14.2% | 40% | bull-only |
| `rank(fnd6_dvpa / close)` | TOP200 | 0.32 | 0.23 | 14.2% | 40% | bull-only |
| `rank(fnd6_dvpa)` | TOP500 | 0.32 | 0.22 | 27.3% | 60% | bull-only |
| `rank(fnd6_dvpa / close)` | TOP500 | 0.32 | 0.22 | 27.3% | 60% | bull-only |
| `rank(fnd6_dvpa)` | TOP3000 | 0.25 | 0.16 | 52.4% | 40% | bear-only |
| `rank(fnd6_dvpa / close)` | TOP3000 | 0.25 | 0.16 | 52.4% | 40% | bear-only |
| `rank(ts_delta(fnd6_dvpa, 5))` | TOP200 | 0.10 | 0.04 | 24.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_esopnr: 0.672 (moderately positively correlated)
- min_free_cashflow_per_share_guidance: 0.668 (moderately positively correlated)
- shareholders_equity_min_guidance: 0.668 (moderately positively correlated)
- min_total_assets_guidance: 0.668 (moderately positively correlated)
- max_free_cashflow_per_share_guidance: 0.668 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
