---
field: fnd6_newqv1300_intanoq
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.69
best_fitness: 0.22
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 7
max_drawdown: 0.0958
ann_vol: 0.0586
hit_rate: 0.5263
rolling_sharpe_min: -1.497
rolling_sharpe_max: 3.349
negated_best_sharpe: 0.43
negated_best_template: rank_neg_delta
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.26
---
# fnd6_newqv1300_intanoq (fundamental6)

*Other Intangibles*

## Signal Profile
- `rank(fnd6_newqv1300_intanoq)`: S=0.36, F=0.19, T=2.0%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_intanoq / close)`: S=0.39, F=0.19, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_intanoq, 5))`: S=0.69, F=0.22, T=38.1%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_intanoq)`: S=-0.10, F=-0.03, T=2.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_intanoq, 5))`: S=0.43, F=0.18, T=39.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_intanoq, 63)`: S=0.13, F=0.02, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_intanoq, 10)`: S=0.02, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_intanoq, 22))`: S=0.06, F=0.01, T=17.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_intanoq)`: S=0.27, F=0.16, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_intanoq / close)`: S=0.25, F=0.13, T=4.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/2P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.68, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.46 (negative), ret=-1.9%
  - 2020: S=2.96 (strong), ret=+19.3%
  - 2021: S=0.72 (moderate), ret=+4.1%
  - 2022: S=-1.43 (negative), ret=-8.0%
  - 2023: S=0.99 (moderate), ret=+6.2%

## Risk & Drawdown
- Max drawdown: 9.58% over 551 days (recovered)
- Annualized: return +4.0%, volatility 5.9% (fraction of booksize)
- Hit rate: 52.6% positive days
- Tail shape: skew +0.04, excess kurtosis +5.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.50, max 3.35, latest 0.95

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +6.14%; worst month: -5.12%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-1.08
- Sideways: S=0.39
- Bear: S=2.67

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_intanoq, 5))` S=0.43, F=0.18, INFERIOR
Direction gap: -0.26 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_intanoq)`: S=0.27, F=0.16, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_intanoq / close)`: S=0.25, F=0.13, T=4.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_intanoq, 5))`: S=0.43, F=0.18, T=39.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newqv1300_intanoq, 5))` | TOP3000 | 0.68 | 0.22 | 9.6% | 60% | bear-only |
| `rank(fnd6_newqv1300_intanoq)` | TOP3000 | 0.35 | 0.19 | 28.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_intanoq / close)` | TOP3000 | 0.39 | 0.19 | 14.8% | 40% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_intanoq, 5))` | TOP1000 | 0.35 | 0.10 | 14.4% | 60% | mixed |
| `rank(fnd6_newqv1300_intanoq / close)` | TOP1000 | 0.18 | 0.07 | 20.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_intanoq)` | TOP1000 | 0.09 | 0.03 | 32.6% | 60% | bull-only |
| `rank(fnd6_newqv1300_intanoq / close)` | TOP500 | 0.07 | 0.02 | 33.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_txtubxintbs: -0.227 (weakly negatively correlated)
- fnd6_txtubsettle: -0.227 (weakly negatively correlated)
- anl4_cfo_mean: -0.221 (weakly negatively correlated)
- fnd6_loxdr: -0.220 (weakly negatively correlated)
- fnd6_txtubtxtr: -0.220 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
