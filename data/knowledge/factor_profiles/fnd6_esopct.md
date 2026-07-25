---
field: fnd6_esopct
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.78
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1897
ann_vol: 0.1313
hit_rate: 0.498
rolling_sharpe_min: -1.304
rolling_sharpe_max: 2.78
negated_best_sharpe: 0.63
negated_best_template: neg_rank_level
negated_best_fitness: 0.49
n_negated_sims: 10
direction_gap: -0.15
---
# fnd6_esopct (fundamental6)

*Common ESOP Obligation - Total*

## Signal Profile
- `rank(fnd6_esopct)`: S=0.24, F=0.12, T=2.0%, INFERIOR (TOP200)
- `rank(fnd6_esopct / close)`: S=0.24, F=0.12, T=2.0%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_esopct, 5))`: S=0.78, F=0.71, T=8.5%, INFERIOR (TOP3000)
- `-rank(fnd6_esopct)`: S=0.59, F=0.46, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_esopct, 5))`: S=0.43, F=0.23, T=5.8%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_esopct, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_esopct, 10)`: S=-0.53, F=-0.45, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_esopct, 22))`: S=-0.27, F=-0.12, T=4.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esopct)`: S=0.63, F=0.49, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esopct / close)`: S=0.63, F=0.49, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 23F/4P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.77, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.64 (strong), ret=+24.6%
  - 2020: S=0.18 (weak), ret=+3.6%
  - 2021: S=0.53 (moderate), ret=+5.1%
  - 2022: S=2.40 (strong), ret=+18.5%
  - 2023: S=-0.53 (negative), ret=-2.2%

## Risk & Drawdown
- Max drawdown: 18.97% over 624 days (recovered)
- Annualized: return +10.1%, volatility 13.1% (fraction of booksize)
- Hit rate: 49.8% positive days
- Tail shape: skew +2.97, excess kurtosis +64.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.30, max 2.78, latest -0.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +15.16%; worst month: -6.46%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.65
- Sideways: S=0.72
- Bear: S=-0.27

## Negated Direction
Best negated: `rank(-1 * fnd6_esopct)` S=0.63, F=0.49, INFERIOR
Direction gap: -0.15 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_esopct)`: S=0.63, F=0.49, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_esopct / close)`: S=0.63, F=0.49, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_esopct, 5))`: S=0.43, F=0.23, T=5.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_esopct, 5))` | TOP3000 | 0.77 | 0.71 | 19.0% | 80% | mixed |
| `rank(fnd6_esopct)` | TOP200 | 0.23 | 0.12 | 19.4% | 60% | mixed |
| `rank(fnd6_esopct / close)` | TOP200 | 0.23 | 0.12 | 19.4% | 60% | mixed |
| `rank(ts_delta(fnd6_esopct, 5))` | TOP500 | 0.18 | 0.06 | 20.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dd5: 0.372 (weakly positively correlated)
- fnd6_txs: 0.370 (weakly positively correlated)
- max_share_buyback_guidance: 0.367 (weakly positively correlated)
- min_adjusted_funds_from_operations_adj_guidance: 0.367 (weakly positively correlated)
- max_total_goodwill_guidance_2: 0.367 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
