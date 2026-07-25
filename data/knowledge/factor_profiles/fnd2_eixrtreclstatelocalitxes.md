---
field: fnd2_eixrtreclstatelocalitxes
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.67
best_fitness: 0.49
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.251
ann_vol: 0.1748
hit_rate: 0.4874
rolling_sharpe_min: -1.141
rolling_sharpe_max: 2.538
negated_best_sharpe: 0.53
negated_best_template: neg_rank
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.14
---
# fnd2_eixrtreclstatelocalitxes (fundamental2)

*Percentage of the difference between reported income tax expense (benefit) and expected income tax expense (benefit) computed by applying the domestic federal statutory income tax rates to pretax income (loss) from continuing operations applicable to state and local income tax expense (benefit), net of federal tax expense (benefit).*

## Signal Profile
- `rank(fnd2_eixrtreclstatelocalitxes)`: S=0.08, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd2_eixrtreclstatelocalitxes / close)`: S=0.28, F=0.11, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_eixrtreclstatelocalitxes, 5))`: S=0.67, F=0.49, T=21.7%, INFERIOR (TOP200)
- `-rank(fnd2_eixrtreclstatelocalitxes)`: S=0.53, F=0.24, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_eixrtreclstatelocalitxes, 5))`: S=-0.10, F=-0.02, T=34.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_eixrtreclstatelocalitxes, 63)`: S=-0.37, F=-0.31, T=13.7%, INFERIOR (TOP3000)
- `ts_mean(fnd2_eixrtreclstatelocalitxes, 10)`: S=-0.25, F=-0.14, T=2.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_eixrtreclstatelocalitxes, 22))`: S=0.31, F=0.16, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_eixrtreclstatelocalitxes)`: S=0.53, F=0.24, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_eixrtreclstatelocalitxes / close)`: S=0.17, F=0.05, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.67, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.49 (strong), ret=+33.4%
  - 2020: S=0.08 (weak), ret=+1.1%
  - 2021: S=0.61 (moderate), ret=+16.0%
  - 2022: S=1.30 (moderate), ret=+20.4%
  - 2023: S=-1.09 (negative), ret=-13.2%

## Risk & Drawdown
- Max drawdown: 25.10% over 893 days (recovered)
- Annualized: return +11.8%, volatility 17.5% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +2.71, excess kurtosis +37.77

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.14, max 2.54, latest -1.12

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +26.24%; worst month: -12.48%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.83
- Sideways: S=1.23
- Bear: S=0.18

## Negated Direction
Best negated: `-rank(fnd2_eixrtreclstatelocalitxes)` S=0.53, F=0.24, INFERIOR
Direction gap: -0.14 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_eixrtreclstatelocalitxes)`: S=0.53, F=0.24, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_eixrtreclstatelocalitxes / close)`: S=0.17, F=0.05, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_eixrtreclstatelocalitxes, 5))`: S=-0.10, F=-0.02, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_eixrtreclstatelocalitxes, 5))` | TOP200 | 0.67 | 0.49 | 25.1% | 80% | mixed |
| `rank(ts_delta(fnd2_eixrtreclstatelocalitxes, 5))` | TOP3000 | 0.71 | 0.42 | 19.9% | 80% | all-weather |
| `rank(ts_delta(fnd2_eixrtreclstatelocalitxes, 5))` | TOP500 | 0.33 | 0.15 | 48.4% | 60% | mixed |
| `rank(fnd2_eixrtreclstatelocalitxes / close)` | TOP3000 | 0.28 | 0.11 | 13.1% | 80% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_itcb: 0.271 (weakly positively correlated)
- fn_comp_fair_value_assumptions_weighted_avg_vol_rate_a: -0.269 (weakly negatively correlated)
- fn_accum_oth_income_loss_net_of_tax_a: -0.263 (weakly negatively correlated)
- parkinson_volatility_180: -0.262 (weakly negatively correlated)
- parkinson_volatility_150: -0.261 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
