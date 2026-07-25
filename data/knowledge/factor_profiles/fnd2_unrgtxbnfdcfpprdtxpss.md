---
field: fnd2_unrgtxbnfdcfpprdtxpss
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.36
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0499
ann_vol: 0.0367
hit_rate: 0.5206
rolling_sharpe_min: -0.771
rolling_sharpe_max: 1.823
negated_best_sharpe: 0.18
negated_best_template: neg_rank_level
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.59
---
# fnd2_unrgtxbnfdcfpprdtxpss (fundamental2)

*Amount of decrease in unrecognized tax benefits resulting from tax positions that have been or will be taken in current period tax return.*

## Signal Profile
- `rank(fnd2_unrgtxbnfdcfpprdtxpss)`: S=0.34, F=0.13, T=1.3%, INFERIOR (TOP1000)
- `rank(fnd2_unrgtxbnfdcfpprdtxpss / close)`: S=0.77, F=0.36, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_unrgtxbnfdcfpprdtxpss, 5))`: S=0.32, F=0.11, T=33.9%, INFERIOR (TOP3000)
- `-rank(fnd2_unrgtxbnfdcfpprdtxpss)`: S=-0.34, F=-0.13, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unrgtxbnfdcfpprdtxpss, 5))`: S=-0.04, F=-0.01, T=28.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_unrgtxbnfdcfpprdtxpss, 22)`: S=0.10, F=0.03, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd2_unrgtxbnfdcfpprdtxpss, 10)`: S=0.25, F=0.09, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_unrgtxbnfdcfpprdtxpss, 22))`: S=-0.59, F=-0.34, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfdcfpprdtxpss)`: S=0.18, F=0.07, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfdcfpprdtxpss / close)`: S=0.06, F=0.01, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.76, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.75 (moderate), ret=+2.1%
  - 2020: S=0.56 (moderate), ret=+2.1%
  - 2021: S=0.98 (moderate), ret=+4.0%
  - 2022: S=0.62 (moderate), ret=+2.6%
  - 2023: S=0.95 (moderate), ret=+2.8%

## Risk & Drawdown
- Max drawdown: 4.99% over 548 days (recovered)
- Annualized: return +2.8%, volatility 3.7% (fraction of booksize)
- Hit rate: 52.1% positive days
- Tail shape: skew +0.19, excess kurtosis +1.23

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.77, max 1.82, latest 0.95

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +2.24%; worst month: -1.93%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.27
- Sideways: S=0.15
- Bear: S=-0.52

## Negated Direction
Best negated: `rank(-1 * fnd2_unrgtxbnfdcfpprdtxpss)` S=0.18, F=0.07, INFERIOR
Direction gap: -0.59 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_unrgtxbnfdcfpprdtxpss)`: S=0.18, F=0.07, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_unrgtxbnfdcfpprdtxpss / close)`: S=0.06, F=0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_unrgtxbnfdcfpprdtxpss, 5))`: S=-0.04, F=-0.01, T=28.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_unrgtxbnfdcfpprdtxpss / close)` | TOP3000 | 0.76 | 0.36 | 5.0% | 100% | bull-only |
| `rank(fnd2_unrgtxbnfdcfpprdtxpss / close)` | TOP1000 | 0.53 | 0.25 | 6.3% | 60% | bull-only |
| `rank(fnd2_unrgtxbnfdcfpprdtxpss / close)` | TOP500 | 0.31 | 0.13 | 11.5% | 60% | bull-only |
| `rank(fnd2_unrgtxbnfdcfpprdtxpss)` | TOP1000 | 0.33 | 0.13 | 12.1% | 80% | bull-only |
| `rank(ts_delta(fnd2_unrgtxbnfdcfpprdtxpss, 5))` | TOP3000 | 0.33 | 0.11 | 29.1% | 60% | weak |
| `rank(fnd2_unrgtxbnfdcfpprdtxpss)` | TOP3000 | 0.31 | 0.11 | 11.0% | 80% | bull-only |
| `rank(fnd2_unrgtxbnfdcfpprdtxpss)` | TOP500 | 0.12 | 0.04 | 18.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_unrecognized_tax_benefits_a: 0.702 (strongly positively correlated)
- fnd2_a_rvndm: 0.690 (moderately positively correlated)
- anl4_ebitda_high: 0.688 (moderately positively correlated)
- fnd6_newa1v1300_lo: 0.686 (moderately positively correlated)
- anl4_medianepsbfam: 0.682 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
