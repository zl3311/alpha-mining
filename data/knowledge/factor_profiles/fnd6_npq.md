---
field: fnd6_npq
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.78
best_fitness: 0.41
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.319
ann_vol: 0.18
hit_rate: 0.4996
rolling_sharpe_min: -1.573
rolling_sharpe_max: 1.809
negated_best_sharpe: 0.78
negated_best_template: rank_neg_delta
negated_best_fitness: 0.41
n_negated_sims: 10
direction_gap: 0.48
---
# fnd6_npq (fundamental6)

*Notes Payable*

## Signal Profile
- `rank(fnd6_npq)`: S=0.12, F=0.03, T=2.7%, INFERIOR (TOP1000)
- `rank(fnd6_npq / close)`: S=0.16, F=0.04, T=2.8%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_npq, 5))`: S=0.26, F=0.09, T=37.8%, INFERIOR (TOP200)
- `-rank(fnd6_npq)`: S=-0.12, F=-0.03, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_npq, 5))`: S=0.78, F=0.41, T=37.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_npq, 22)`: S=0.14, F=0.03, T=34.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_npq, 10)`: S=0.08, F=0.02, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_npq, 22))`: S=0.30, F=0.10, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_npq)`: S=0.17, F=0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_npq / close)`: S=0.11, F=0.03, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.26, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.38 (weak), ret=+4.6%
  - 2020: S=0.80 (moderate), ret=+16.1%
  - 2021: S=-0.06 (negative), ret=-1.2%
  - 2022: S=0.61 (moderate), ret=+11.6%
  - 2023: S=-0.49 (negative), ret=-8.1%

## Risk & Drawdown
- Max drawdown: 31.90% over 547 days (not yet recovered, ongoing at window end)
- Annualized: return +4.7%, volatility 18.0% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.12, excess kurtosis +4.44

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.57, max 1.81, latest -0.60

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +15.08%; worst month: -7.34%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.74
- Sideways: S=-0.11
- Bear: S=0.13

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_npq, 5))` S=0.78, F=0.41, INFERIOR
Direction gap: +0.48 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_npq)`: S=0.17, F=0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_npq / close)`: S=0.11, F=0.03, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_npq, 5))`: S=0.78, F=0.41, T=37.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_npq, 5))` | TOP200 | 0.26 | 0.09 | 31.9% | 60% | mixed |
| `rank(fnd6_npq / close)` | TOP1000 | 0.15 | 0.04 | 10.4% | 60% | bull-only |
| `rank(fnd6_npq)` | TOP1000 | 0.11 | 0.03 | 11.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_npq, 5))` | TOP3000 | 0.16 | 0.03 | 13.3% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_tfvl: 0.162 (weakly positively correlated)
- implied_volatility_mean_720: 0.139 (weakly positively correlated)
- fnd2_propplteqmuflmameqmt: 0.139 (weakly positively correlated)
- implied_volatility_call_720: 0.138 (weakly positively correlated)
- implied_volatility_mean_1080: 0.138 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
