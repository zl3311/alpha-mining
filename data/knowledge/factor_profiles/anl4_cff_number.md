---
field: anl4_cff_number
dataset: analyst4
best_template: rank_level
best_sharpe: 0.72
best_fitness: 0.33
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0754
ann_vol: 0.0369
hit_rate: 0.5239
rolling_sharpe_min: -1.464
rolling_sharpe_max: 3.532
negated_best_sharpe: -0.03
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.75
---
# anl4_cff_number (analyst4)

*Cash Flow From Financing - number of estimations*

## Signal Profile
- `rank(anl4_cff_number)`: S=0.72, F=0.33, T=2.5%, INFERIOR (TOP3000)
- `rank(anl4_cff_number / close)`: S=0.43, F=0.25, T=3.5%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_cff_number, 5))`: S=0.30, F=0.11, T=33.8%, INFERIOR (TOP200)
- `-rank(anl4_cff_number)`: S=-0.59, F=-0.27, T=3.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_number, 5))`: S=0.03, F=0.00, T=37.0%, INFERIOR (TOP3000)
- `ts_zscore(anl4_cff_number, 22)`: S=0.12, F=0.03, T=33.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_cff_number, 10)`: S=0.61, F=0.30, T=3.1%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_cff_number, 22))`: S=0.20, F=0.06, T=12.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_number)`: S=-0.72, F=-0.33, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_number / close)`: S=-0.03, F=0.00, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.71, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.38 (strong), ret=+8.2%
  - 2020: S=-0.24 (negative), ret=-0.9%
  - 2021: S=0.57 (moderate), ret=+2.1%
  - 2022: S=0.10 (weak), ret=+0.3%
  - 2023: S=0.92 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 7.54% over 1195 days (recovered)
- Annualized: return +2.6%, volatility 3.7% (fraction of booksize)
- Hit rate: 52.4% positive days
- Tail shape: skew +0.28, excess kurtosis +2.35

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.46, max 3.53, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +2.89%; worst month: -1.88%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.53
- Sideways: S=2.07
- Bear: S=-0.44

## Negated Direction
Best negated: `rank(-1 * anl4_cff_number / close)` S=-0.03, F=0.00, INFERIOR
Direction gap: -0.75 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_cff_number)`: S=-0.72, F=-0.33, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_cff_number / close)`: S=-0.03, F=0.00, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_cff_number, 5))`: S=0.03, F=0.00, T=37.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_cff_number)` | TOP3000 | 0.71 | 0.33 | 7.5% | 80% | mixed |
| `rank(anl4_cff_number)` | TOP1000 | 0.58 | 0.27 | 4.9% | 100% | weak |
| `rank(anl4_cff_number / close)` | TOP200 | 0.43 | 0.25 | 16.2% | 80% | mixed |
| `rank(anl4_cff_number)` | TOP500 | 0.45 | 0.20 | 6.2% | 60% | mixed |
| `rank(anl4_cff_number / close)` | TOP1000 | 0.26 | 0.12 | 27.7% | 40% | bear-only |
| `rank(ts_delta(anl4_cff_number, 5))` | TOP200 | 0.31 | 0.11 | 18.7% | 60% | mixed |
| `rank(anl4_cff_number / close)` | TOP500 | 0.19 | 0.07 | 28.8% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_cfo_number: 0.630 (moderately positively correlated)
- anl4_cfi_number: 0.460 (moderately positively correlated)
- fn_allocated_share_based_compensation_expense_q: 0.434 (moderately positively correlated)
- pcr_vol_150: 0.424 (moderately positively correlated)
- news_atr14: 0.424 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
