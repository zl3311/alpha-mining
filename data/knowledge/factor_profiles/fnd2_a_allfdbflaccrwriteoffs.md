---
field: fnd2_a_allfdbflaccrwriteoffs
dataset: fundamental2
best_template: ts_mean
best_sharpe: 0.78
best_fitness: 0.57
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1165
ann_vol: 0.0605
hit_rate: 0.4996
rolling_sharpe_min: -1.374
rolling_sharpe_max: 2.835
negated_best_sharpe: 0.02
negated_best_template: rank_neg_delta
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.76
---
# fnd2_a_allfdbflaccrwriteoffs (fundamental2)

*Amount of recoveries of receivables doubtful of collection that were previously charged off.*

## Signal Profile
- `rank(fnd2_a_allfdbflaccrwriteoffs)`: S=0.61, F=0.33, T=1.4%, INFERIOR (TOP1000)
- `rank(fnd2_a_allfdbflaccrwriteoffs / close)`: S=0.49, F=0.24, T=1.6%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd2_a_allfdbflaccrwriteoffs, 5))`: S=0.23, F=0.11, T=16.8%, INFERIOR (TOP200)
- `-rank(fnd2_a_allfdbflaccrwriteoffs)`: S=-0.61, F=-0.33, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_allfdbflaccrwriteoffs, 5))`: S=0.02, F=0.00, T=26.2%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_a_allfdbflaccrwriteoffs, 22)`: S=0.09, F=0.03, T=10.8%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_allfdbflaccrwriteoffs, 10)`: S=0.78, F=0.57, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_allfdbflaccrwriteoffs, 22))`: S=0.26, F=0.14, T=16.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_allfdbflaccrwriteoffs)`: S=-0.59, F=-0.32, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_allfdbflaccrwriteoffs / close)`: S=-0.40, F=-0.18, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/11P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.77 (moderate), ret=+3.5%
  - 2020: S=-0.52 (negative), ret=-3.1%
  - 2021: S=1.52 (strong), ret=+11.2%
  - 2022: S=0.68 (moderate), ret=+4.3%
  - 2023: S=0.33 (weak), ret=+1.7%

## Risk & Drawdown
- Max drawdown: 11.65% over 489 days (recovered)
- Annualized: return +3.6%, volatility 6.0% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.13, excess kurtosis +0.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.37, max 2.83, latest 0.25

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +3.49%; worst month: -3.46%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.02
- Sideways: S=0.73
- Bear: S=-2.21

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_allfdbflaccrwriteoffs, 5))` S=0.02, F=0.00, INFERIOR
Direction gap: -0.76 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_a_allfdbflaccrwriteoffs)`: S=-0.59, F=-0.32, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_allfdbflaccrwriteoffs / close)`: S=-0.40, F=-0.18, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_allfdbflaccrwriteoffs, 5))`: S=0.02, F=0.00, T=26.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_allfdbflaccrwriteoffs)` | TOP1000 | 0.59 | 0.33 | 11.7% | 80% | bull-only |
| `rank(fnd2_a_allfdbflaccrwriteoffs)` | TOP500 | 0.56 | 0.32 | 10.2% | 80% | bull-only |
| `rank(fnd2_a_allfdbflaccrwriteoffs / close)` | TOP1000 | 0.48 | 0.24 | 8.3% | 80% | bull-only |
| `rank(fnd2_a_allfdbflaccrwriteoffs)` | TOP3000 | 0.48 | 0.22 | 12.7% | 80% | bull-only |
| `rank(fnd2_a_allfdbflaccrwriteoffs / close)` | TOP3000 | 0.47 | 0.20 | 5.3% | 100% | bull-only |
| `rank(fnd2_a_allfdbflaccrwriteoffs / close)` | TOP500 | 0.38 | 0.18 | 14.3% | 60% | bull-only |
| `rank(fnd2_a_allfdbflaccrwriteoffs / close)` | TOP200 | 0.33 | 0.18 | 21.0% | 80% | bull-only |
| `rank(fnd2_a_allfdbflaccrwriteoffs)` | TOP200 | 0.30 | 0.16 | 20.3% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_allfdbflaccrwriteoffs, 5))` | TOP200 | 0.23 | 0.11 | 30.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_loxdr: 0.699 (moderately positively correlated)
- fnd6_newa1v1300_dv: 0.686 (moderately positively correlated)
- cashflow_dividends: 0.686 (moderately positively correlated)
- enterprise_value: 0.675 (moderately positively correlated)
- ebitda: 0.667 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
