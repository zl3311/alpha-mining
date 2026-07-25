---
field: fnd6_tfvl
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.81
best_fitness: 0.81
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.3233
ann_vol: 0.1862
hit_rate: 0.4559
rolling_sharpe_min: -1.224
rolling_sharpe_max: 2.636
negated_best_sharpe: 0.6
negated_best_template: neg_rank_level
negated_best_fitness: 0.42
n_negated_sims: 10
direction_gap: -0.21
---
# fnd6_tfvl (fundamental6)

*Total Fair Value Liabilities*

## Signal Profile
- `rank(fnd6_tfvl)`: S=0.25, F=0.08, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_tfvl / close)`: S=0.21, F=0.06, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_tfvl, 5))`: S=0.45, F=0.25, T=26.5%, INFERIOR (TOP200)
- `-rank(fnd6_tfvl)`: S=-0.03, F=0.00, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_tfvl, 5))`: S=0.01, F=0.00, T=26.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_tfvl, 22)`: S=0.81, F=0.81, T=20.9%, INFERIOR (TOP3000)
- `ts_mean(fnd6_tfvl, 10)`: S=0.44, F=0.28, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_tfvl, 22))`: S=-0.26, F=-0.11, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tfvl)`: S=0.60, F=0.42, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tfvl / close)`: S=0.56, F=0.38, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.44, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.68 (strong), ret=+22.4%
  - 2020: S=1.22 (moderate), ret=+19.2%
  - 2021: S=0.51 (moderate), ret=+10.6%
  - 2022: S=0.16 (weak), ret=+4.0%
  - 2023: S=-1.16 (negative), ret=-16.2%

## Risk & Drawdown
- Max drawdown: 32.33% over 680 days (not yet recovered, ongoing at window end)
- Annualized: return +8.2%, volatility 18.6% (fraction of booksize)
- Hit rate: 45.6% positive days
- Tail shape: skew +1.27, excess kurtosis +34.22

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.22, max 2.64, latest -1.13

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2023
Best month: +9.88%; worst month: -11.82%
Positive months: 53%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.37
- Sideways: S=0.43
- Bear: S=-0.92

## Negated Direction
Best negated: `rank(-1 * fnd6_tfvl)` S=0.60, F=0.42, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_tfvl)`: S=0.60, F=0.42, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_tfvl / close)`: S=0.56, F=0.38, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_tfvl, 5))`: S=0.01, F=0.00, T=26.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_tfvl, 5))` | TOP200 | 0.44 | 0.25 | 32.3% | 80% | bull-only |
| `rank(ts_delta(fnd6_tfvl, 5))` | TOP3000 | 0.29 | 0.10 | 28.0% | 60% | mixed |
| `rank(fnd6_tfvl)` | TOP3000 | 0.24 | 0.08 | 14.9% | 60% | bull-only |
| `rank(fnd6_tfvl / close)` | TOP3000 | 0.20 | 0.06 | 13.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_lol2: 0.647 (moderately positively correlated)
- fnd6_newa1v1300_fca: 0.439 (moderately positively correlated)
- fnd6_txr: 0.332 (weakly positively correlated)
- fnd6_newa1v1300_ibc: -0.314 (weakly negatively correlated)
- fnd6_txndb: -0.311 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
