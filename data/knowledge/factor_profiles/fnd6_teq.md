---
field: fnd6_teq
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.66
best_fitness: 0.44
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0876
ann_vol: 0.0699
hit_rate: 0.4785
rolling_sharpe_min: -0.968
rolling_sharpe_max: 1.933
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.28
---
# fnd6_teq (fundamental6)

*Stockholders' Equity - Total*

## Signal Profile
- `rank(fnd6_teq)`: S=0.41, F=0.23, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd6_teq / close)`: S=0.48, F=0.25, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_teq, 5))`: S=0.34, F=0.16, T=33.4%, INFERIOR (TOP200)
- `-rank(fnd6_teq)`: S=-0.15, F=-0.06, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_teq, 5))`: S=0.38, F=0.12, T=35.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_teq, 63)`: S=0.66, F=0.44, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_teq, 10)`: S=0.06, F=0.01, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_teq, 22))`: S=0.11, F=0.03, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_teq)`: S=-0.41, F=-0.23, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_teq / close)`: S=-0.48, F=-0.25, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.47, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.36 (negative), ret=-1.6%
  - 2020: S=-0.12 (negative), ret=-1.0%
  - 2021: S=0.90 (moderate), ret=+7.9%
  - 2022: S=0.84 (moderate), ret=+5.6%
  - 2023: S=0.98 (moderate), ret=+5.3%

## Risk & Drawdown
- Max drawdown: 8.76% over 270 days (recovered)
- Annualized: return +3.3%, volatility 7.0% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.79, excess kurtosis +4.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.97, max 1.93, latest 1.08

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +7.28%; worst month: -3.24%
Positive months: 49%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.16
- Sideways: S=0.16
- Bear: S=-1.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_teq, 5))` S=0.38, F=0.12, INFERIOR
Direction gap: -0.28 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_teq)`: S=-0.41, F=-0.23, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_teq / close)`: S=-0.48, F=-0.25, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_teq, 5))`: S=0.38, F=0.12, T=35.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_teq / close)` | TOP3000 | 0.47 | 0.25 | 8.8% | 60% | bull-only |
| `rank(fnd6_teq)` | TOP3000 | 0.41 | 0.23 | 31.6% | 80% | bull-only |
| `rank(fnd6_teq / close)` | TOP1000 | 0.33 | 0.16 | 12.6% | 60% | bull-only |
| `rank(ts_delta(fnd6_teq, 5))` | TOP200 | 0.34 | 0.16 | 76.0% | 60% | mixed |
| `rank(fnd6_teq)` | TOP1000 | 0.14 | 0.06 | 33.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_teq, 5))` | TOP1000 | 0.17 | 0.04 | 19.1% | 60% | bear-only |
| `rank(fnd6_teq / close)` | TOP500 | 0.11 | 0.04 | 26.4% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_seq: 0.999 (strongly positively correlated)
- fnd6_newa1v1300_ceq: 0.997 (strongly positively correlated)
- fnd6_ceql: 0.992 (strongly positively correlated)
- fnd6_newa1v1300_icapt: 0.968 (strongly positively correlated)
- fnd6_cptmfmq_atq: 0.959 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
