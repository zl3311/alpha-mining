---
field: fnd6_esubc
dataset: fundamental6
best_template: rank_neg_delta
best_sharpe: 0.7
best_fitness: 0.53
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: weak
n_variations_with_pnl: 3
max_drawdown: 0.3071
ann_vol: 0.1363
hit_rate: 0.5093
rolling_sharpe_min: -2.149
rolling_sharpe_max: 2.725
negated_best_sharpe: 0.7
negated_best_template: rank_neg_delta
negated_best_fitness: 0.53
n_negated_sims: 10
direction_gap: 0.45
---
# fnd6_esubc (fundamental6)

*Equity in Net Loss - Earnings*

## Signal Profile
- `rank(fnd6_esubc)`: S=0.25, F=0.13, T=3.5%, INFERIOR (TOP200)
- `rank(fnd6_esubc / close)`: S=0.23, F=0.12, T=3.6%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_esubc, 5))`: S=0.09, F=0.02, T=32.5%, INFERIOR (TOP3000)
- `-rank(fnd6_esubc)`: S=0.14, F=0.03, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_esubc, 5))`: S=0.70, F=0.53, T=24.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_esubc, 22)`: S=-0.28, F=-0.16, T=15.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_esubc, 10)`: S=-0.15, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_esubc, 22))`: S=-0.13, F=-0.05, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esubc)`: S=0.50, F=0.23, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esubc / close)`: S=0.48, F=0.22, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 14F/18P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.23, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=2.57 (strong), ret=+33.5%
  - 2020: S=-2.12 (negative), ret=-25.9%
  - 2021: S=0.32 (weak), ret=+5.4%
  - 2022: S=0.28 (weak), ret=+3.8%
  - 2023: S=-0.12 (negative), ret=-1.2%

## Risk & Drawdown
- Max drawdown: 30.71% over 1473 days (not yet recovered, ongoing at window end)
- Annualized: return +3.2%, volatility 13.6% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.36, excess kurtosis +3.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.15, max 2.73, latest -0.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +9.30%; worst month: -9.47%
Positive months: 46%

## Regime Profile
Regime profile: **weak**
- Bull: S=-0.19
- Sideways: S=1.01
- Bear: S=-0.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_esubc, 5))` S=0.70, F=0.53, INFERIOR
Direction gap: +0.45 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_esubc)`: S=0.50, F=0.23, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esubc / close)`: S=0.48, F=0.22, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_esubc, 5))`: S=0.70, F=0.53, T=24.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_esubc)` | TOP200 | 0.23 | 0.13 | 30.7% | 60% | weak |
| `rank(fnd6_esubc / close)` | TOP200 | 0.21 | 0.12 | 31.7% | 60% | weak |
| `rank(ts_delta(fnd6_esubc, 5))` | TOP3000 | 0.10 | 0.02 | 39.5% | 60% | mixed |

## Correlation Notes
Top correlates:
- reporting_currency_code_9: 0.212 (weakly positively correlated)
- anl4_fcf_flag: 0.206 (weakly positively correlated)
- fnd6_newa2v1300_prsho: 0.205 (weakly positively correlated)
- fnd6_incorp: 0.200 (weakly positively correlated)
- anl4_fcfps_flag: 0.190 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
