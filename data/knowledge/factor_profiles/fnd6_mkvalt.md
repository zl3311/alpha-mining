---
field: fnd6_mkvalt
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.64
best_fitness: 0.38
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1107
ann_vol: 0.0686
hit_rate: 0.4915
rolling_sharpe_min: -1.013
rolling_sharpe_max: 2.502
negated_best_sharpe: 0.22
negated_best_template: neg_rank_level
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.42
---
# fnd6_mkvalt (fundamental6)

*Market Value - Total*

## Signal Profile
- `rank(fnd6_mkvalt)`: S=0.38, F=0.21, T=6.6%, INFERIOR (TOP3000)
- `rank(fnd6_mkvalt / close)`: S=0.64, F=0.38, T=6.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_mkvalt, 5))`: S=0.38, F=0.17, T=33.3%, INFERIOR (TOP500)
- `-rank(fnd6_mkvalt)`: S=-0.26, F=-0.12, T=6.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mkvalt, 5))`: S=-0.18, F=-0.07, T=26.6%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_mkvalt, 63)`: S=0.08, F=0.02, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_mkvalt, 10)`: S=0.03, F=0.00, T=5.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_mkvalt, 22))`: S=0.11, F=0.03, T=17.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mkvalt)`: S=0.22, F=0.11, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mkvalt / close)`: S=-0.02, F=0.00, T=5.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.63, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.77 (moderate), ret=+3.3%
  - 2020: S=1.35 (moderate), ret=+10.0%
  - 2021: S=1.27 (moderate), ret=+8.5%
  - 2022: S=-0.59 (negative), ret=-5.2%
  - 2023: S=0.89 (moderate), ret=+4.7%

## Risk & Drawdown
- Max drawdown: 11.07% over 639 days (not yet recovered, ongoing at window end)
- Annualized: return +4.3%, volatility 6.9% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.82, excess kurtosis +4.74

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.01, max 2.50, latest 1.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +3.72%; worst month: -4.14%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.18
- Sideways: S=0.94
- Bear: S=-0.28

## Negated Direction
Best negated: `rank(-1 * fnd6_mkvalt)` S=0.22, F=0.11, INFERIOR
Direction gap: -0.42 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_mkvalt)`: S=0.22, F=0.11, T=5.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_mkvalt / close)`: S=-0.02, F=0.00, T=5.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_mkvalt, 5))`: S=-0.18, F=-0.07, T=26.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_mkvalt / close)` | TOP3000 | 0.63 | 0.38 | 11.1% | 80% | mixed |
| `rank(fnd6_mkvalt / close)` | TOP1000 | 0.56 | 0.33 | 8.2% | 80% | bull-only |
| `rank(fnd6_mkvalt)` | TOP3000 | 0.38 | 0.21 | 23.2% | 80% | bull-only |
| `rank(ts_delta(fnd6_mkvalt, 5))` | TOP500 | 0.38 | 0.17 | 47.5% | 80% | mixed |
| `rank(fnd6_mkvalt)` | TOP1000 | 0.26 | 0.12 | 25.8% | 60% | bull-only |
| `rank(fnd6_mkvalt / close)` | TOP500 | 0.24 | 0.10 | 17.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_mkvalt, 5))` | TOP200 | 0.24 | 0.10 | 41.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_unrgtxbnfinregfcrps: 0.698 (moderately positively correlated)
- fnd6_teq: 0.681 (moderately positively correlated)
- fnd6_newa2v1300_seq: 0.680 (moderately positively correlated)
- fnd6_ceql: 0.679 (moderately positively correlated)
- fnd6_newa1v1300_ceq: 0.676 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
