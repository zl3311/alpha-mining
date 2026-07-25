---
field: anl4_cfi_number
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.57
best_fitness: 0.37
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0651
ann_vol: 0.0435
hit_rate: 0.5198
rolling_sharpe_min: -0.651
rolling_sharpe_max: 2.599
negated_best_sharpe: 0.24
negated_best_template: rank_neg_delta
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.33
---
# anl4_cfi_number (analyst4)

*Cash Flow From Investing - number of estimations*

## Signal Profile
- `rank(anl4_cfi_number)`: S=0.67, F=0.37, T=3.8%, INFERIOR (TOP500)
- `rank(anl4_cfi_number / close)`: S=0.57, F=0.37, T=3.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cfi_number, 5))`: S=0.34, F=0.14, T=33.6%, INFERIOR (TOP200)
- `-rank(anl4_cfi_number)`: S=-0.73, F=-0.37, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_number, 5))`: S=0.24, F=0.06, T=37.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_cfi_number, 22)`: S=0.43, F=0.18, T=33.6%, INFERIOR (TOP3000)
- `ts_mean(anl4_cfi_number, 10)`: S=0.61, F=0.31, T=3.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cfi_number, 22))`: S=0.57, F=0.30, T=12.9%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_number)`: S=-0.63, F=-0.26, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_number / close)`: S=0.03, F=0.01, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.74, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.23 (moderate), ret=+4.5%
  - 2020: S=1.53 (strong), ret=+6.1%
  - 2021: S=0.19 (weak), ret=+0.9%
  - 2022: S=-0.06 (negative), ret=-0.3%
  - 2023: S=1.14 (moderate), ret=+4.5%

## Risk & Drawdown
- Max drawdown: 6.51% over 353 days (recovered)
- Annualized: return +3.2%, volatility 4.3% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew -0.24, excess kurtosis +3.03

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.65, max 2.60, latest 1.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +3.74%; worst month: -2.54%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.33
- Sideways: S=1.16
- Bear: S=0.76

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_cfi_number, 5))` S=0.24, F=0.06, INFERIOR
Direction gap: -0.33 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_cfi_number)`: S=-0.63, F=-0.26, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cfi_number / close)`: S=0.03, F=0.01, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cfi_number, 5))`: S=0.24, F=0.06, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cfi_number)` | TOP500 | 0.68 | 0.37 | 6.9% | 80% | all-weather |
| `rank(anl4_cfi_number)` | TOP1000 | 0.74 | 0.37 | 6.5% | 80% | mixed |
| `rank(anl4_cfi_number / close)` | TOP200 | 0.58 | 0.37 | 17.0% | 80% | mixed |
| `rank(anl4_cfi_number)` | TOP3000 | 0.64 | 0.26 | 5.4% | 80% | weak |
| `rank(anl4_cfi_number)` | TOP200 | 0.40 | 0.21 | 10.3% | 100% | bull-only |
| `rank(anl4_cfi_number / close)` | TOP500 | 0.32 | 0.15 | 27.3% | 80% | mixed |
| `rank(ts_delta(anl4_cfi_number, 5))` | TOP200 | 0.36 | 0.14 | 21.1% | 60% | weak |
| `rank(ts_delta(anl4_cfi_number, 5))` | TOP1000 | 0.40 | 0.13 | 13.4% | 60% | bear-only |
| `rank(anl4_cfi_number / close)` | TOP1000 | 0.23 | 0.10 | 27.2% | 40% | bear-only |

## Correlation Notes
Top correlates:
- anl4_totassets_number: 0.545 (moderately positively correlated)
- anl4_cff_number: 0.460 (moderately positively correlated)
- anl4_cfo_number: 0.411 (moderately positively correlated)
- anl4_totgw_number: 0.318 (weakly positively correlated)
- anl4_fcf_flag: 0.279 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
