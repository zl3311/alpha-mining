---
field: fnd6_mfma1_apalch
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
max_drawdown: 0.1316
ann_vol: 0.0443
hit_rate: 0.5134
rolling_sharpe_min: -2.3
rolling_sharpe_max: 2.297
negated_best_sharpe: 0.6
negated_best_template: rank_neg_delta
negated_best_fitness: 0.3
n_negated_sims: 10
direction_gap: 0.29
---
# fnd6_mfma1_apalch (fundamental6)

*Accounts Payable and Accrued Liabilities - Increase/(Decrease)*

## Signal Profile
- `rank(fnd6_mfma1_apalch)`: S=0.25, F=0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(fnd6_mfma1_apalch / close)`: S=-0.21, F=-0.09, T=3.5%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_mfma1_apalch, 5))`: S=-0.05, F=-0.01, T=35.6%, INFERIOR (TOP1000)
- `-rank(fnd6_mfma1_apalch)`: S=-0.11, F=-0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_apalch, 5))`: S=0.60, F=0.30, T=34.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mfma1_apalch, 63)`: S=0.31, F=0.18, T=18.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mfma1_apalch, 10)`: S=0.09, F=0.02, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mfma1_apalch, 22))`: S=-0.85, F=-0.65, T=16.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_apalch)`: S=-0.25, F=-0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_apalch / close)`: S=0.44, F=0.16, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.26, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.11 (weak), ret=+0.3%
  - 2020: S=-0.93 (negative), ret=-3.9%
  - 2021: S=0.39 (weak), ret=+1.9%
  - 2022: S=1.53 (strong), ret=+8.4%
  - 2023: S=-0.30 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 13.16% over 1241 days (recovered)
- Annualized: return +1.2%, volatility 4.4% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew -0.23, excess kurtosis +1.15

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.30, max 2.30, latest -0.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +3.76%; worst month: -3.03%
Positive months: 48%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.01
- Sideways: S=0.35
- Bear: S=-1.65

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_mfma1_apalch, 5))` S=0.60, F=0.30, INFERIOR
Direction gap: +0.29 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_mfma1_apalch)`: S=-0.25, F=-0.07, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mfma1_apalch / close)`: S=0.44, F=0.16, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mfma1_apalch, 5))`: S=0.60, F=0.30, T=34.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mfma1_apalch)` | TOP3000 | 0.26 | 0.07 | 13.2% | 60% | bull-only |
| `rank(fnd6_mfma1_apalch)` | TOP1000 | 0.11 | 0.02 | 15.4% | 60% | bull-only |
| `rank(fnd6_mfma1_apalch)` | TOP500 | 0.10 | 0.02 | 11.7% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_apalch: 0.998 (strongly positively correlated)
- cap: 0.755 (strongly positively correlated)
- call_breakeven_720: 0.729 (strongly positively correlated)
- call_breakeven_120: 0.729 (strongly positively correlated)
- call_breakeven_180: 0.729 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
