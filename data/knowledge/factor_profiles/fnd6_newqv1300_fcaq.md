---
field: fnd6_newqv1300_fcaq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.52
best_fitness: 0.29
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 1
max_drawdown: 0.0887
ann_vol: 0.043
hit_rate: 0.5085
rolling_sharpe_min: -1.58
rolling_sharpe_max: 1.749
negated_best_sharpe: 0.32
negated_best_template: neg_rank_level
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.2
---
# fnd6_newqv1300_fcaq (fundamental6)

*Foreign Exchange Income (Loss)*

## Signal Profile
- `rank(fnd6_newqv1300_fcaq)`: S=0.05, F=0.01, T=8.0%, INFERIOR (TOP500)
- `rank(fnd6_newqv1300_fcaq / close)`: S=0.25, F=0.07, T=5.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_fcaq, 5))`: S=0.04, F=0.00, T=40.6%, INFERIOR (TOP3000)
- `-rank(fnd6_newqv1300_fcaq)`: S=0.26, F=0.10, T=7.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_fcaq, 5))`: S=0.37, F=0.18, T=43.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_fcaq, 22)`: S=0.52, F=0.29, T=35.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_fcaq, 10)`: S=0.27, F=0.14, T=5.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_fcaq, 22))`: S=-0.36, F=-0.15, T=19.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_fcaq)`: S=0.32, F=0.21, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_fcaq / close)`: S=0.27, F=0.16, T=9.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/12P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/9P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.25, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.27 (moderate), ret=+5.2%
  - 2020: S=0.38 (weak), ret=+1.6%
  - 2021: S=0.47 (weak), ret=+2.1%
  - 2022: S=-0.32 (negative), ret=-1.4%
  - 2023: S=-0.56 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 8.87% over 833 days (not yet recovered, ongoing at window end)
- Annualized: return +1.1%, volatility 4.3% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.14, excess kurtosis +2.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.58, max 1.75, latest -0.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +2.78%; worst month: -2.84%
Positive months: 56%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.87
- Sideways: S=0.23
- Bear: S=1.32

## Negated Direction
Best negated: `rank(-1 * fnd6_newqv1300_fcaq)` S=0.32, F=0.21, INFERIOR
Direction gap: -0.20 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_fcaq)`: S=0.32, F=0.21, T=9.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_fcaq / close)`: S=0.27, F=0.16, T=9.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_fcaq, 5))`: S=0.37, F=0.18, T=43.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_fcaq / close)` | TOP3000 | 0.25 | 0.07 | 8.9% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_prcl: -0.225 (weakly negatively correlated)
- fnd6_fopox: -0.204 (weakly negatively correlated)
- fnd6_mfmq_cheq: -0.204 (weakly negatively correlated)
- cash_st: -0.204 (weakly negatively correlated)
- fn_comp_not_rec_q: -0.199 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
