---
field: fnd6_newa1v1300_dvc
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.74
best_fitness: 0.62
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.2409
ann_vol: 0.1329
hit_rate: 0.5215
rolling_sharpe_min: -1.222
rolling_sharpe_max: 2.881
negated_best_sharpe: 0.33
negated_best_template: neg_rank_level
negated_best_fitness: 0.21
n_negated_sims: 10
direction_gap: -0.41
---
# fnd6_newa1v1300_dvc (fundamental6)

*Dividends Common/Ordinary*

## Signal Profile
- `rank(fnd6_newa1v1300_dvc)`: S=0.12, F=0.04, T=2.5%, INFERIOR (TOP1000)
- `rank(fnd6_newa1v1300_dvc / close)`: S=0.26, F=0.13, T=2.6%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newa1v1300_dvc, 5))`: S=0.41, F=0.15, T=40.6%, INFERIOR (TOP3000)
- `-rank(fnd6_newa1v1300_dvc)`: S=-0.12, F=-0.04, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dvc, 5))`: S=-0.08, F=-0.02, T=27.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_dvc, 63)`: S=0.74, F=0.62, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_dvc, 10)`: S=0.13, F=0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_dvc, 22))`: S=-0.04, F=-0.01, T=20.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dvc)`: S=0.33, F=0.21, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dvc / close)`: S=0.30, F=0.18, T=3.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.42, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.86 (moderate), ret=+9.6%
  - 2020: S=0.26 (weak), ret=+3.7%
  - 2021: S=0.11 (weak), ret=+1.5%
  - 2022: S=-0.72 (negative), ret=-9.7%
  - 2023: S=1.86 (strong), ret=+22.4%

## Risk & Drawdown
- Max drawdown: 24.09% over 727 days (recovered)
- Annualized: return +5.6%, volatility 13.3% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew -0.28, excess kurtosis +4.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.22, max 2.88, latest 1.84

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +10.51%; worst month: -5.81%
Positive months: 52%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=0.89
- Sideways: S=1.09
- Bear: S=-0.66

## Negated Direction
Best negated: `rank(-1 * fnd6_newa1v1300_dvc)` S=0.33, F=0.21, INFERIOR
Direction gap: -0.41 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_dvc)`: S=0.33, F=0.21, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_dvc / close)`: S=0.30, F=0.18, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_dvc, 5))`: S=-0.08, F=-0.02, T=27.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa1v1300_dvc, 5))` | TOP3000 | 0.42 | 0.15 | 24.1% | 80% | bull-only |
| `rank(fnd6_newa1v1300_dvc / close)` | TOP1000 | 0.25 | 0.13 | 24.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dvc, 5))` | TOP200 | 0.26 | 0.11 | 31.0% | 80% | mixed |
| `rank(fnd6_newa1v1300_dvc / close)` | TOP3000 | 0.21 | 0.10 | 28.3% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_dvc, 5))` | TOP1000 | 0.29 | 0.10 | 37.6% | 60% | weak |
| `rank(fnd6_newa1v1300_dvc)` | TOP1000 | 0.11 | 0.04 | 34.5% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dvc)` | TOP3000 | 0.08 | 0.03 | 36.7% | 60% | bull-only |
| `rank(fnd6_newa1v1300_dvc / close)` | TOP500 | 0.07 | 0.02 | 38.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_dvt: 0.902 (strongly positively correlated)
- min_capital_expenditure_guidance: 0.166 (weakly positively correlated)
- fnd6_newqv1300_cibegniq: 0.166 (weakly positively correlated)
- earnings_per_share_min_guidance: 0.164 (weakly positively correlated)
- max_capital_expenditure_guidance: 0.163 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
