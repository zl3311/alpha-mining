---
field: fnd6_mibn
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.69
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1078
ann_vol: 0.055
hit_rate: 0.5004
rolling_sharpe_min: -1.286
rolling_sharpe_max: 2.425
negated_best_sharpe: 0.69
negated_best_template: rank_neg_delta
negated_best_fitness: 0.38
n_negated_sims: 10
direction_gap: 0.35
---
# fnd6_mibn (fundamental6)

*Noncontrolling Interests - Nonredeemable - Balance Sheet*

## Signal Profile
- `rank(fnd6_mibn)`: S=0.30, F=0.11, T=1.3%, INFERIOR (TOP1000)
- `rank(fnd6_mibn / close)`: S=0.34, F=0.13, T=1.4%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_mibn, 5))`: S=-0.07, F=-0.01, T=30.4%, INFERIOR (TOP500)
- `-rank(fnd6_mibn)`: S=-0.30, F=-0.11, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mibn, 5))`: S=0.69, F=0.38, T=34.2%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mibn, 63)`: S=-0.41, F=-0.30, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mibn, 10)`: S=-0.09, F=-0.02, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mibn, 22))`: S=0.04, F=0.01, T=15.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mibn)`: S=-0.23, F=-0.07, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mibn / close)`: S=-0.31, F=-0.11, T=0.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 8F/24P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.34, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.48 (negative), ret=-1.6%
  - 2020: S=-0.29 (negative), ret=-1.5%
  - 2021: S=0.12 (weak), ret=+0.9%
  - 2022: S=2.15 (strong), ret=+13.6%
  - 2023: S=-0.64 (negative), ret=-2.4%

## Risk & Drawdown
- Max drawdown: 10.78% over 808 days (recovered)
- Annualized: return +1.8%, volatility 5.5% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.15, excess kurtosis +1.97

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 2.42, latest -0.63

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.60%; worst month: -4.38%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.61
- Sideways: S=-0.14
- Bear: S=-2.04

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mibn, 5))` S=0.69, F=0.38, INFERIOR
Direction gap: +0.35 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_mibn)`: S=-0.23, F=-0.07, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mibn / close)`: S=-0.31, F=-0.11, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mibn, 5))`: S=0.69, F=0.38, T=34.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mibn / close)` | TOP1000 | 0.34 | 0.13 | 10.8% | 40% | bull-only |
| `rank(fnd6_mibn / close)` | TOP3000 | 0.31 | 0.11 | 14.1% | 40% | bull-only |
| `rank(fnd6_mibn)` | TOP1000 | 0.29 | 0.11 | 12.6% | 40% | bull-only |
| `rank(fnd6_mibn)` | TOP200 | 0.25 | 0.10 | 24.6% | 60% | bull-only |
| `rank(fnd6_mibn / close)` | TOP200 | 0.21 | 0.08 | 26.6% | 40% | bull-only |
| `rank(fnd6_mibn)` | TOP3000 | 0.23 | 0.07 | 16.8% | 40% | bull-only |
| `rank(fnd6_mibn / close)` | TOP500 | 0.15 | 0.04 | 11.8% | 60% | bull-only |
| `rank(fnd6_mibn)` | TOP500 | 0.13 | 0.04 | 12.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mibt: 0.982 (strongly positively correlated)
- fnd6_newqv1300_mibnq: 0.958 (strongly positively correlated)
- fnd6_mfmq_mibtq: 0.946 (strongly positively correlated)
- fnd6_newqv1300_mibtq: 0.945 (strongly positively correlated)
- anl4_ebitda_low: 0.761 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
