---
field: fnd6_newa2v1300_seqo
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.92
best_fitness: 1.25
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.2689
ann_vol: 0.1569
hit_rate: 0.4955
rolling_sharpe_min: -1.057
rolling_sharpe_max: 1.894
negated_best_sharpe: 0.24
negated_best_template: neg_rank_level
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.68
---
# fnd6_newa2v1300_seqo (fundamental6)

*Other Stockholders' Equity Adjustments*

## Signal Profile
- `rank(fnd6_newa2v1300_seqo)`: S=0.35, F=0.19, T=2.6%, INFERIOR (TOP500)
- `rank(fnd6_newa2v1300_seqo / close)`: S=0.35, F=0.19, T=2.6%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_newa2v1300_seqo, 5))`: S=0.52, F=0.31, T=23.8%, INFERIOR (TOP3000)
- `-rank(fnd6_newa2v1300_seqo)`: S=-0.07, F=-0.02, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_seqo, 5))`: S=-0.56, F=-0.34, T=24.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_seqo, 22)`: S=0.92, F=1.25, T=2.4%, AVERAGE (TOP3000)
- `ts_mean(fnd6_newa2v1300_seqo, 10)`: S=-0.61, F=-0.44, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_seqo, 22))`: S=0.20, F=0.10, T=13.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_seqo)`: S=0.24, F=0.08, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_seqo / close)`: S=0.24, F=0.08, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 15F/17P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.52, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.69 (moderate), ret=+12.3%
  - 2020: S=0.25 (weak), ret=+3.7%
  - 2021: S=-0.13 (negative), ret=-2.2%
  - 2022: S=1.07 (moderate), ret=+16.5%
  - 2023: S=0.88 (moderate), ret=+9.8%

## Risk & Drawdown
- Max drawdown: 26.89% over 943 days (recovered)
- Annualized: return +8.2%, volatility 15.7% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.18, excess kurtosis +5.07

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.06, max 1.89, latest 0.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +10.70%; worst month: -10.45%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.22
- Sideways: S=1.06
- Bear: S=-1.02

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_seqo)` S=0.24, F=0.08, INFERIOR
Direction gap: -0.68 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_seqo)`: S=0.24, F=0.08, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_seqo / close)`: S=0.24, F=0.08, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_seqo, 5))`: S=-0.56, F=-0.34, T=24.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa2v1300_seqo, 5))` | TOP3000 | 0.52 | 0.31 | 26.9% | 80% | bull-only |
| `rank(fnd6_newa2v1300_seqo / close)` | TOP500 | 0.35 | 0.19 | 15.7% | 60% | bear-only |
| `rank(fnd6_newa2v1300_seqo)` | TOP500 | 0.35 | 0.19 | 15.6% | 60% | bear-only |
| `rank(ts_delta(fnd6_newa2v1300_seqo, 5))` | TOP1000 | 0.28 | 0.15 | 38.2% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_seqo, 5))` | TOP500 | 0.18 | 0.08 | 35.1% | 40% | mixed |
| `rank(fnd6_newa2v1300_seqo)` | TOP200 | 0.13 | 0.05 | 31.5% | 40% | bear-only |
| `rank(fnd6_newa2v1300_seqo / close)` | TOP200 | 0.13 | 0.05 | 31.5% | 40% | bear-only |
| `rank(fnd6_newa2v1300_seqo)` | TOP1000 | 0.08 | 0.02 | 11.8% | 40% | mixed |
| `rank(fnd6_newa2v1300_seqo / close)` | TOP1000 | 0.08 | 0.02 | 11.8% | 40% | mixed |

## Correlation Notes
Top correlates:
- pv13_revere_index_value: 0.155 (weakly positively correlated)
- pv13_revere_index_cap: 0.154 (weakly positively correlated)
- rel_num_cust: 0.127 (weakly positively correlated)
- call_breakeven_270: 0.127 (weakly positively correlated)
- call_breakeven_360: 0.127 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
