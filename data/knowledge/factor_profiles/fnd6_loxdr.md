---
field: fnd6_loxdr
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.42
best_fitness: 0.26
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1713
ann_vol: 0.1115
hit_rate: 0.4939
rolling_sharpe_min: -1.154
rolling_sharpe_max: 2.089
negated_best_sharpe: 0.5
negated_best_template: rank_neg_delta
negated_best_fitness: 0.25
n_negated_sims: 10
direction_gap: 0.08
---
# fnd6_loxdr (fundamental6)

*Liabilities - Other - Excluding Deferred Revenue*

## Signal Profile
- `rank(fnd6_loxdr)`: S=0.41, F=0.24, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_loxdr / close)`: S=0.42, F=0.26, T=1.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_loxdr, 5))`: S=0.35, F=0.11, T=34.8%, INFERIOR (TOP1000)
- `-rank(fnd6_loxdr)`: S=-0.29, F=-0.16, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_loxdr, 5))`: S=0.50, F=0.25, T=36.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_loxdr, 63)`: S=0.13, F=0.04, T=19.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_loxdr, 10)`: S=0.18, F=0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_loxdr, 22))`: S=0.30, F=0.11, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_loxdr)`: S=0.20, F=0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_loxdr / close)`: S=0.21, F=0.11, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.41, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.07 (weak), ret=+0.4%
  - 2020: S=-0.56 (negative), ret=-6.1%
  - 2021: S=0.99 (moderate), ret=+16.0%
  - 2022: S=1.33 (moderate), ret=+16.9%
  - 2023: S=-0.80 (negative), ret=-4.5%

## Risk & Drawdown
- Max drawdown: 17.13% over 509 days (recovered)
- Annualized: return +4.6%, volatility 11.2% (fraction of booksize)
- Hit rate: 49.4% positive days
- Tail shape: skew +0.14, excess kurtosis +3.55

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 2.09, latest -0.77

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +8.54%; worst month: -5.51%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.60
- Sideways: S=-0.14
- Bear: S=-2.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_loxdr, 5))` S=0.50, F=0.25, INFERIOR
Direction gap: +0.08 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_loxdr)`: S=0.20, F=0.11, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_loxdr / close)`: S=0.21, F=0.11, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_loxdr, 5))`: S=0.50, F=0.25, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_loxdr / close)` | TOP1000 | 0.41 | 0.26 | 17.1% | 60% | bull-only |
| `rank(fnd6_loxdr / close)` | TOP3000 | 0.44 | 0.24 | 13.0% | 60% | bull-only |
| `rank(fnd6_loxdr)` | TOP3000 | 0.40 | 0.24 | 31.1% | 80% | bull-only |
| `rank(fnd6_loxdr)` | TOP1000 | 0.28 | 0.16 | 33.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_loxdr, 5))` | TOP1000 | 0.35 | 0.11 | 29.7% | 60% | mixed |
| `rank(ts_delta(fnd6_loxdr, 5))` | TOP3000 | 0.34 | 0.10 | 12.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_loxdrq: 0.886 (strongly positively correlated)
- fnd2_a_sbcpnargmtwfsptepddvdrt: 0.880 (strongly positively correlated)
- fnd6_newa1v1300_dv: 0.879 (strongly positively correlated)
- cashflow_dividends: 0.878 (strongly positively correlated)
- fn_accum_depr_depletion_and_amortization_ppne_a: 0.873 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
