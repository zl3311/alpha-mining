---
field: anl4_ptpr_high
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.6
best_fitness: 0.24
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.1794
ann_vol: 0.0944
hit_rate: 0.5093
rolling_sharpe_min: -1.764
rolling_sharpe_max: 3.528
negated_best_sharpe: 0.33
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.18
n_negated_sims: 10
direction_gap: -0.27
---
# anl4_ptpr_high (analyst4)

*Reported pretax income - the highest estimation*

## Signal Profile
- `rank(anl4_ptpr_high)`: S=0.17, F=0.07, T=1.2%, INFERIOR (TOP3000)
- `rank(anl4_ptpr_high / close)`: S=0.35, F=0.19, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_ptpr_high, 5))`: S=0.60, F=0.24, T=34.4%, INFERIOR (TOP200)
- `-rank(anl4_ptpr_high)`: S=0.05, F=0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptpr_high, 5))`: S=0.12, F=0.02, T=36.5%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_ptpr_high, 63)`: S=-0.08, F=-0.01, T=17.0%, INFERIOR (TOP3000)
- `ts_mean(anl4_ptpr_high, 10)`: S=-0.08, F=-0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_ptpr_high, 22))`: S=-0.15, F=-0.03, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_high)`: S=0.30, F=0.16, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_high / close)`: S=0.33, F=0.18, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 21F/8P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.61, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.01 (negative), ret=-0.1%
  - 2020: S=2.41 (strong), ret=+23.6%
  - 2021: S=0.70 (moderate), ret=+6.9%
  - 2022: S=-0.26 (negative), ret=-2.6%
  - 2023: S=0.04 (weak), ret=+0.3%

## Risk & Drawdown
- Max drawdown: 17.94% over 449 days (not yet recovered, ongoing at window end)
- Annualized: return +5.7%, volatility 9.4% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.04, excess kurtosis +1.73

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.76, max 3.53, latest -0.03

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +8.51%; worst month: -6.64%
Positive months: 54%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.12
- Sideways: S=0.17
- Bear: S=0.51

## Negated Direction
Best negated: `rank(-1 * anl4_ptpr_high / close)` S=0.33, F=0.18, INFERIOR
Direction gap: -0.27 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_ptpr_high)`: S=0.30, F=0.16, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_ptpr_high / close)`: S=0.33, F=0.18, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_ptpr_high, 5))`: S=0.12, F=0.02, T=36.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(anl4_ptpr_high, 5))` | TOP200 | 0.61 | 0.24 | 17.9% | 60% | all-weather |
| `rank(anl4_ptpr_high / close)` | TOP3000 | 0.34 | 0.19 | 27.7% | 60% | bull-only |
| `rank(anl4_ptpr_high)` | TOP3000 | 0.16 | 0.07 | 42.3% | 60% | bull-only |
| `rank(ts_delta(anl4_ptpr_high, 5))` | TOP3000 | 0.31 | 0.06 | 9.0% | 60% | weak |
| `rank(ts_delta(anl4_ptpr_high, 5))` | TOP1000 | 0.28 | 0.06 | 15.7% | 40% | mixed |

## Correlation Notes
Top correlates:
- pv13_ustomergraphrank_hub_rank: 0.118 (weakly positively correlated)
- fnd6_newqv1300_aociderglq: 0.117 (weakly positively correlated)
- fnd6_np: 0.117 (weakly positively correlated)
- fnd6_cptnewqv1300_epsf12: 0.114 (weakly positively correlated)
- parkinson_volatility_60: 0.113 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
