---
field: fnd6_newa1v1300_intano
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.63
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1147
ann_vol: 0.0724
hit_rate: 0.4858
rolling_sharpe_min: -1.259
rolling_sharpe_max: 2.477
redundancy_cluster: 1
negated_best_sharpe: 0.63
negated_best_template: rank_neg_delta
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: 0.06
---
# fnd6_newa1v1300_intano (fundamental6)

*Other Intangibles*

## Signal Profile
- `rank(fnd6_newa1v1300_intano)`: S=0.40, F=0.22, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_intano / close)`: S=0.53, F=0.29, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa1v1300_intano, 5))`: S=0.15, F=0.03, T=34.9%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_intano)`: S=-0.20, F=-0.08, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_intano, 5))`: S=0.63, F=0.38, T=34.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_intano, 63)`: S=0.57, F=0.35, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_intano, 10)`: S=0.13, F=0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_intano, 22))`: S=0.43, F=0.20, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_intano)`: S=0.21, F=0.11, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_intano / close)`: S=0.12, F=0.04, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.53, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.37 (negative), ret=-1.4%
  - 2020: S=-0.50 (negative), ret=-3.6%
  - 2021: S=1.34 (moderate), ret=+13.1%
  - 2022: S=1.20 (moderate), ret=+10.3%
  - 2023: S=0.06 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 11.47% over 827 days (recovered)
- Annualized: return +3.8%, volatility 7.2% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew +0.18, excess kurtosis +2.50

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.26, max 2.48, latest -0.02

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.73%; worst month: -4.16%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.10
- Sideways: S=0.29
- Bear: S=-2.63

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_intano, 5))` S=0.63, F=0.38, INFERIOR
Direction gap: +0.06 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_intano)`: S=0.21, F=0.11, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_intano / close)`: S=0.12, F=0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_intano, 5))`: S=0.63, F=0.38, T=34.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_intano / close)` | TOP3000 | 0.53 | 0.29 | 11.5% | 60% | bull-only |
| `rank(fnd6_newa1v1300_intano)` | TOP3000 | 0.40 | 0.22 | 25.6% | 60% | bull-only |
| `rank(fnd6_newa1v1300_intano / close)` | TOP1000 | 0.37 | 0.19 | 14.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_intano)` | TOP1000 | 0.19 | 0.08 | 28.3% | 60% | bull-only |
| `rank(fnd6_newa1v1300_intano / close)` | TOP500 | 0.15 | 0.06 | 28.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa1v1300_intano, 5))` | TOP1000 | 0.15 | 0.03 | 21.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_intan: 0.988 (strongly positively correlated)
- fnd6_am: 0.980 (strongly positively correlated)
- fnd6_newqv1300_intanq: 0.976 (strongly positively correlated)
- fnd6_rectr: 0.951 (strongly positively correlated)
- fnd6_newa1v1300_gp: 0.950 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
