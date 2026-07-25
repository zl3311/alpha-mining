---
field: fnd6_newqv1300_cisecglq
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 0.71
best_fitness: 0.43
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.384
ann_vol: 0.2256
hit_rate: 0.5045
rolling_sharpe_min: -0.892
rolling_sharpe_max: 2.976
negated_best_sharpe: 0.71
negated_best_template: neg_rank_level
negated_best_fitness: 0.43
n_negated_sims: 10
direction_gap: 0.25
---
# fnd6_newqv1300_cisecglq (fundamental6)

*Comp Inc - Securities Gains/Losses*

## Signal Profile
- `rank(fnd6_newqv1300_cisecglq)`: S=0.19, F=0.05, T=6.1%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_cisecglq / close)`: S=0.25, F=0.07, T=6.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_cisecglq, 5))`: S=0.46, F=0.19, T=58.5%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_cisecglq)`: S=0.69, F=0.36, T=7.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cisecglq, 5))`: S=-0.38, F=-0.14, T=56.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_cisecglq, 22)`: S=0.31, F=0.12, T=38.1%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_cisecglq, 10)`: S=-0.23, F=-0.09, T=6.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_cisecglq, 22))`: S=-0.11, F=-0.02, T=22.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cisecglq)`: S=0.71, F=0.43, T=8.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cisecglq / close)`: S=0.69, F=0.41, T=8.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.46, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.28 (weak), ret=+4.7%
  - 2020: S=2.60 (strong), ret=+44.8%
  - 2021: S=-0.11 (negative), ret=-2.7%
  - 2022: S=0.07 (weak), ret=+1.9%
  - 2023: S=0.11 (weak), ret=+2.5%

## Risk & Drawdown
- Max drawdown: 38.40% over 816 days (recovered)
- Annualized: return +10.5%, volatility 22.6% (fraction of booksize)
- Hit rate: 50.4% positive days
- Tail shape: skew +0.51, excess kurtosis +4.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.89, max 2.98, latest 0.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +23.40%; worst month: -10.77%
Positive months: 51%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.74
- Sideways: S=0.87
- Bear: S=1.29

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_cisecglq)` S=0.71, F=0.43, INFERIOR
Direction gap: +0.25 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_cisecglq)`: S=0.71, F=0.43, T=8.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_cisecglq / close)`: S=0.69, F=0.41, T=8.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_cisecglq, 5))`: S=-0.38, F=-0.14, T=56.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_cisecglq, 5))` | TOP200 | 0.46 | 0.19 | 38.4% | 80% | bear-only |
| `rank(ts_delta(fnd6_newqv1300_cisecglq, 5))` | TOP500 | 0.43 | 0.17 | 27.9% | 40% | bear-only |
| `rank(fnd6_newqv1300_cisecglq / close)` | TOP3000 | 0.26 | 0.07 | 11.5% | 60% | mixed |
| `rank(fnd6_newqv1300_cisecglq)` | TOP3000 | 0.20 | 0.05 | 12.8% | 60% | mixed |

## Correlation Notes
Top correlates:
- historical_volatility_120: -0.129 (weakly negatively correlated)
- historical_volatility_10 - historical_volatility_180: -0.121 (weakly negatively correlated)
- anl4_netprofit_flag: 0.113 (weakly positively correlated)
- news_mins_2_chg: 0.110 (weakly positively correlated)
- parkinson_volatility_120: -0.109 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
