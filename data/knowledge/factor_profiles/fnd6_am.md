---
field: fnd6_am
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.71
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1211
ann_vol: 0.0763
hit_rate: 0.4883
rolling_sharpe_min: -1.349
rolling_sharpe_max: 2.396
redundancy_cluster: 1
negated_best_sharpe: 0.71
negated_best_template: rank_neg_delta
negated_best_fitness: 0.53
n_negated_sims: 10
direction_gap: 0.05
---
# fnd6_am (fundamental6)

*Amortization of Intangibles*

## Signal Profile
- `rank(fnd6_am)`: S=0.39, F=0.22, T=1.6%, INFERIOR (TOP3000)
- `rank(fnd6_am / close)`: S=0.55, F=0.32, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_am, 5))`: S=-0.08, F=-0.01, T=37.4%, INFERIOR (TOP3000)
- `-rank(fnd6_am)`: S=-0.11, F=-0.04, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_am, 5))`: S=0.71, F=0.53, T=27.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_am, 63)`: S=0.66, F=0.47, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_am, 10)`: S=-0.06, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_am, 22))`: S=-0.12, F=-0.03, T=18.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_am)`: S=0.04, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_am / close)`: S=-0.08, F=-0.02, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.25 (negative), ret=-1.0%
  - 2020: S=-0.65 (negative), ret=-4.8%
  - 2021: S=1.33 (moderate), ret=+13.6%
  - 2022: S=1.19 (moderate), ret=+10.9%
  - 2023: S=0.40 (weak), ret=+1.8%

## Risk & Drawdown
- Max drawdown: 12.11% over 545 days (recovered)
- Annualized: return +4.2%, volatility 7.6% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.14, excess kurtosis +2.38

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.35, max 2.40, latest 0.33

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +7.68%; worst month: -4.91%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.16
- Sideways: S=0.23
- Bear: S=-2.66

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_am, 5))` S=0.71, F=0.53, INFERIOR
Direction gap: +0.05 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_am)`: S=0.04, F=0.01, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_am / close)`: S=-0.08, F=-0.02, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_am, 5))`: S=0.71, F=0.53, T=27.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_am / close)` | TOP3000 | 0.55 | 0.32 | 12.1% | 60% | bull-only |
| `rank(fnd6_am)` | TOP3000 | 0.39 | 0.22 | 28.2% | 80% | bull-only |
| `rank(fnd6_am / close)` | TOP1000 | 0.16 | 0.06 | 23.8% | 60% | bull-only |
| `rank(fnd6_am)` | TOP1000 | 0.10 | 0.04 | 36.2% | 60% | bull-only |
| `rank(fnd6_am / close)` | TOP500 | 0.07 | 0.02 | 36.9% | 40% | bull-only |
| `rank(fnd6_am / close)` | TOP200 | 0.08 | 0.02 | 45.1% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_intano: 0.980 (strongly positively correlated)
- fnd6_intan: 0.976 (strongly positively correlated)
- fnd6_newqv1300_intanq: 0.964 (strongly positively correlated)
- fnd6_rectr: 0.939 (strongly positively correlated)
- fnd6_newa1v1300_gp: 0.939 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
