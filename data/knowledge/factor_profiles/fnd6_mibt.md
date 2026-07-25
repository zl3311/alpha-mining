---
field: fnd6_mibt
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.9
best_fitness: 0.55
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 8
max_drawdown: 0.1022
ann_vol: 0.0565
hit_rate: 0.4891
rolling_sharpe_min: -1.345
rolling_sharpe_max: 2.507
negated_best_sharpe: 0.9
negated_best_template: rank_neg_delta
negated_best_fitness: 0.55
n_negated_sims: 10
direction_gap: 0.54
---
# fnd6_mibt (fundamental6)

*Noncontrolling Interests - Total - Balance Sheet*

## Signal Profile
- `rank(fnd6_mibt)`: S=0.30, F=0.11, T=1.3%, INFERIOR (TOP1000)
- `rank(fnd6_mibt / close)`: S=0.36, F=0.14, T=1.4%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_mibt, 5))`: S=-0.28, F=-0.14, T=24.1%, INFERIOR (TOP200)
- `-rank(fnd6_mibt)`: S=-0.30, F=-0.11, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mibt, 5))`: S=0.90, F=0.55, T=34.7%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mibt, 63)`: S=0.06, F=0.02, T=16.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mibt, 10)`: S=-0.13, F=-0.04, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mibt, 22))`: S=-0.31, F=-0.14, T=15.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mibt)`: S=-0.23, F=-0.07, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mibt / close)`: S=-0.32, F=-0.11, T=0.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 8F/24P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.36, Consistency 40% positive years (2/5)
Yearly breakdown:
  - 2019: S=-0.48 (negative), ret=-1.5%
  - 2020: S=-0.33 (negative), ret=-1.7%
  - 2021: S=0.18 (weak), ret=+1.4%
  - 2022: S=2.26 (strong), ret=+14.5%
  - 2023: S=-0.74 (negative), ret=-2.8%

## Risk & Drawdown
- Max drawdown: 10.22% over 608 days (recovered)
- Annualized: return +2.0%, volatility 5.7% (fraction of booksize)
- Hit rate: 48.9% positive days
- Tail shape: skew +0.11, excess kurtosis +2.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.34, max 2.51, latest -0.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.47%; worst month: -4.52%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.52
- Sideways: S=0.02
- Bear: S=-2.03

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mibt, 5))` S=0.90, F=0.55, INFERIOR
Direction gap: +0.54 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_mibt)`: S=-0.23, F=-0.07, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mibt / close)`: S=-0.32, F=-0.11, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mibt, 5))`: S=0.90, F=0.55, T=34.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mibt / close)` | TOP1000 | 0.36 | 0.14 | 10.2% | 40% | bull-only |
| `rank(fnd6_mibt / close)` | TOP3000 | 0.32 | 0.11 | 13.3% | 40% | bull-only |
| `rank(fnd6_mibt)` | TOP1000 | 0.29 | 0.11 | 12.9% | 40% | bull-only |
| `rank(fnd6_mibt)` | TOP200 | 0.21 | 0.08 | 25.2% | 60% | bull-only |
| `rank(fnd6_mibt / close)` | TOP200 | 0.19 | 0.07 | 26.1% | 40% | bull-only |
| `rank(fnd6_mibt)` | TOP3000 | 0.23 | 0.07 | 16.2% | 40% | bull-only |
| `rank(fnd6_mibt / close)` | TOP500 | 0.20 | 0.06 | 11.7% | 60% | bull-only |
| `rank(fnd6_mibt)` | TOP500 | 0.17 | 0.05 | 12.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mibn: 0.982 (strongly positively correlated)
- fnd6_mfmq_mibtq: 0.963 (strongly positively correlated)
- fnd6_newqv1300_mibtq: 0.963 (strongly positively correlated)
- fnd6_newqv1300_mibnq: 0.950 (strongly positively correlated)
- anl4_ebitda_low: 0.766 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
