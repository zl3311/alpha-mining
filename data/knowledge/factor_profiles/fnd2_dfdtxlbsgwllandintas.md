---
field: fnd2_dfdtxlbsgwllandintas
dataset: fundamental2
best_template: rank_ts_rank
best_sharpe: 0.61
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.0837
ann_vol: 0.0623
hit_rate: 0.5028
rolling_sharpe_min: -1.568
rolling_sharpe_max: 2.112
negated_best_sharpe: 0.61
negated_best_template: rank_neg_delta
negated_best_fitness: 0.35
n_negated_sims: 10
direction_gap: 0.0
---
# fnd2_dfdtxlbsgwllandintas (fundamental2)

*Amount of deferred tax liability attributable to taxable temporary differences from intangible assets including goodwill.*

## Signal Profile
- `rank(fnd2_dfdtxlbsgwllandintas)`: S=0.13, F=0.04, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd2_dfdtxlbsgwllandintas / close)`: S=0.41, F=0.19, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_dfdtxlbsgwllandintas, 5))`: S=0.21, F=0.07, T=34.4%, INFERIOR (TOP1000)
- `-rank(fnd2_dfdtxlbsgwllandintas)`: S=0.05, F=0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxlbsgwllandintas, 5))`: S=0.61, F=0.35, T=33.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_dfdtxlbsgwllandintas, 63)`: S=0.29, F=0.18, T=15.8%, INFERIOR (TOP3000)
- `ts_mean(fnd2_dfdtxlbsgwllandintas, 10)`: S=-0.18, F=-0.06, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_dfdtxlbsgwllandintas, 22))`: S=0.61, F=0.40, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxlbsgwllandintas)`: S=0.30, F=0.16, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxlbsgwllandintas / close)`: S=0.16, F=0.06, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.80 (moderate), ret=+3.2%
  - 2020: S=-0.01 (negative), ret=-0.1%
  - 2021: S=0.54 (moderate), ret=+3.9%
  - 2022: S=1.32 (moderate), ret=+7.8%
  - 2023: S=-0.62 (negative), ret=-2.3%

## Risk & Drawdown
- Max drawdown: 8.37% over 336 days (recovered)
- Annualized: return +2.5%, volatility 6.2% (fraction of booksize)
- Hit rate: 50.3% positive days
- Tail shape: skew +0.55, excess kurtosis +4.06

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.57, max 2.11, latest -0.45

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +6.02%; worst month: -3.87%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.38
- Sideways: S=0.41
- Bear: S=-1.72

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_dfdtxlbsgwllandintas, 5))` S=0.61, F=0.35, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_dfdtxlbsgwllandintas)`: S=0.30, F=0.16, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxlbsgwllandintas / close)`: S=0.16, F=0.06, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxlbsgwllandintas, 5))`: S=0.61, F=0.35, T=33.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_dfdtxlbsgwllandintas / close)` | TOP3000 | 0.41 | 0.19 | 8.4% | 60% | bull-only |
| `rank(ts_delta(fnd2_dfdtxlbsgwllandintas, 5))` | TOP1000 | 0.22 | 0.07 | 33.5% | 60% | mixed |
| `rank(fnd2_dfdtxlbsgwllandintas / close)` | TOP1000 | 0.14 | 0.05 | 12.2% | 60% | bull-only |
| `rank(fnd2_dfdtxlbsgwllandintas)` | TOP3000 | 0.13 | 0.04 | 23.9% | 60% | bull-only |
| `rank(ts_delta(fnd2_dfdtxlbsgwllandintas, 5))` | TOP3000 | 0.13 | 0.02 | 27.2% | 80% | mixed |

## Correlation Notes
Top correlates:
- fn_finite_lived_intangible_assets_gross_a: 0.887 (strongly positively correlated)
- fn_intangible_assets_accum_amort_a: 0.884 (strongly positively correlated)
- fnd2_a_flintasamt1expy5: 0.879 (strongly positively correlated)
- fn_def_tax_liab_a: 0.879 (strongly positively correlated)
- fnd2_a_flintasamt1expythree: 0.876 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
