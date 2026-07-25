---
field: fnd6_newa1v1300_apalch
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.6
best_fitness: 0.3
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 3
max_drawdown: 0.1329
ann_vol: 0.0445
hit_rate: 0.5142
rolling_sharpe_min: -2.311
rolling_sharpe_max: 2.401
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.3
---
# fnd6_newa1v1300_apalch (fundamental6)

*Accounts Payable and Accrued Liabilities - Increase/(Decrease)*

## Signal Profile
- `rank(fnd6_newa1v1300_apalch)`: S=0.27, F=0.08, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_newa1v1300_apalch / close)`: S=-0.27, F=-0.09, T=2.5%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_newa1v1300_apalch, 5))`: S=-0.11, F=-0.03, T=35.7%, INFERIOR (TOP1000)
- `-rank(fnd6_newa1v1300_apalch)`: S=-0.17, F=-0.05, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_apalch, 5))`: S=0.60, F=0.30, T=34.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newa1v1300_apalch, 63)`: S=0.30, F=0.17, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa1v1300_apalch, 10)`: S=0.09, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa1v1300_apalch, 22))`: S=-0.86, F=-0.66, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_apalch)`: S=-0.27, F=-0.08, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_apalch / close)`: S=0.40, F=0.14, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.28, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.06 (weak), ret=+0.2%
  - 2020: S=-0.95 (negative), ret=-4.0%
  - 2021: S=0.40 (weak), ret=+2.0%
  - 2022: S=1.57 (strong), ret=+8.6%
  - 2023: S=-0.18 (negative), ret=-0.6%

## Risk & Drawdown
- Max drawdown: 13.29% over 1241 days (recovered)
- Annualized: return +1.2%, volatility 4.5% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew -0.22, excess kurtosis +1.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.31, max 2.40, latest -0.35

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.90%; worst month: -3.04%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.09
- Sideways: S=0.34
- Bear: S=-1.65

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newa1v1300_apalch, 5))` S=0.60, F=0.30, INFERIOR
Direction gap: +0.30 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa1v1300_apalch)`: S=-0.27, F=-0.08, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa1v1300_apalch / close)`: S=0.40, F=0.14, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa1v1300_apalch, 5))`: S=0.60, F=0.30, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newa1v1300_apalch)` | TOP3000 | 0.28 | 0.08 | 13.3% | 60% | bull-only |
| `rank(fnd6_newa1v1300_apalch)` | TOP1000 | 0.17 | 0.05 | 14.8% | 60% | bull-only |
| `rank(fnd6_newa1v1300_apalch)` | TOP500 | 0.12 | 0.03 | 12.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_mfma1_apalch: 0.998 (strongly positively correlated)
- cap: 0.756 (strongly positively correlated)
- call_breakeven_720: 0.730 (strongly positively correlated)
- call_breakeven_120: 0.729 (strongly positively correlated)
- call_breakeven_180: 0.729 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
