---
field: fnd6_newqv1300_aocisecglq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.64
best_fitness: 0.46
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.204
ann_vol: 0.1302
hit_rate: 0.4745
rolling_sharpe_min: -0.904
rolling_sharpe_max: 2.374
negated_best_sharpe: 0.64
negated_best_template: rank_neg_delta
negated_best_fitness: 0.46
n_negated_sims: 10
direction_gap: 0.14
---
# fnd6_newqv1300_aocisecglq (fundamental6)

*Accum Other Comp Inc - Unreal G/L Ret Int in Sec Assets*

## Signal Profile
- `rank(fnd6_newqv1300_aocisecglq)`: S=0.50, F=0.35, T=13.9%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_aocisecglq / close)`: S=0.50, F=0.35, T=13.9%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newqv1300_aocisecglq, 5))`: S=0.06, F=0.01, T=12.4%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_aocisecglq)`: S=0.33, F=0.20, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aocisecglq, 5))`: S=0.64, F=0.46, T=9.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_aocisecglq, 22)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_newqv1300_aocisecglq, 10)`: S=-0.07, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_aocisecglq, 22))`: S=-0.38, F=-0.22, T=8.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aocisecglq)`: S=0.24, F=0.18, T=6.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aocisecglq / close)`: S=0.24, F=0.18, T=6.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/15P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.49, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.45 (weak), ret=+3.5%
  - 2020: S=1.31 (moderate), ret=+20.5%
  - 2021: S=0.78 (moderate), ret=+7.7%
  - 2022: S=-0.66 (negative), ret=-11.1%
  - 2023: S=0.99 (moderate), ret=+10.9%

## Risk & Drawdown
- Max drawdown: 20.40% over 763 days (not yet recovered, ongoing at window end)
- Annualized: return +6.4%, volatility 13.0% (fraction of booksize)
- Hit rate: 47.4% positive days
- Tail shape: skew +0.26, excess kurtosis +3.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.90, max 2.37, latest 1.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +10.58%; worst month: -6.49%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.44
- Sideways: S=0.52
- Bear: S=1.46

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_aocisecglq, 5))` S=0.64, F=0.46, INFERIOR
Direction gap: +0.14 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_aocisecglq)`: S=0.24, F=0.18, T=6.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_aocisecglq / close)`: S=0.24, F=0.18, T=6.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_aocisecglq, 5))`: S=0.64, F=0.46, T=9.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_aocisecglq / close)` | TOP500 | 0.49 | 0.35 | 20.4% | 80% | mixed |
| `rank(fnd6_newqv1300_aocisecglq)` | TOP500 | 0.49 | 0.35 | 20.4% | 80% | mixed |

## Correlation Notes
Top correlates:
- fnd6_cstkcvq: -0.409 (moderately negatively correlated)
- net_debt_amount: -0.398 (weakly negatively correlated)
- fnd6_cstkcv: -0.394 (weakly negatively correlated)
- anl4_af_div_value: -0.387 (weakly negatively correlated)
- fnd2_a_sbcpnargmtwfsptepddvdrt: -0.384 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
