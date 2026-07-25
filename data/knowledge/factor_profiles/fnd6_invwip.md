---
field: fnd6_invwip
dataset: fundamental6
best_template: neg_rank_value_norm
best_sharpe: 1.01
best_fitness: 1.04
best_universe: TOP3000
grade: AVERAGE
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1744
ann_vol: 0.1081
hit_rate: 0.5223
rolling_sharpe_min: -1.693
rolling_sharpe_max: 1.728
negated_best_sharpe: 1.01
negated_best_template: neg_rank_value_norm
negated_best_fitness: 1.04
n_negated_sims: 10
direction_gap: 0.65
---
# fnd6_invwip (fundamental6)

*Inventories - Work In Process*

## Signal Profile
- `rank(fnd6_invwip)`: S=0.30, F=0.16, T=3.7%, INFERIOR (TOP500)
- `rank(fnd6_invwip / close)`: S=0.31, F=0.16, T=3.8%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_invwip, 5))`: S=0.07, F=0.01, T=30.6%, INFERIOR (TOP1000)
- `-rank(fnd6_invwip)`: S=-0.18, F=-0.07, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_invwip, 5))`: S=0.63, F=0.44, T=20.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_invwip, 22)`: S=0.36, F=0.28, T=15.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_invwip, 10)`: S=0.03, F=0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_invwip, 22))`: S=0.05, F=0.01, T=20.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_invwip)`: S=0.90, F=0.93, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_invwip / close)`: S=1.01, F=1.04, T=3.5%, AVERAGE (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 29F/3P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.29, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.01 (weak), ret=+0.1%
  - 2020: S=-0.57 (negative), ret=-6.2%
  - 2021: S=1.11 (moderate), ret=+16.7%
  - 2022: S=0.99 (moderate), ret=+10.0%
  - 2023: S=-0.65 (negative), ret=-5.1%

## Risk & Drawdown
- Max drawdown: 17.44% over 599 days (recovered)
- Annualized: return +3.2%, volatility 10.8% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew -0.07, excess kurtosis +1.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.69, max 1.73, latest -0.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +9.70%; worst month: -7.04%
Positive months: 54%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.34
- Sideways: S=0.18
- Bear: S=-1.87

## Negated Direction
Best negated: `rank(-1 * fnd6_invwip / close)` S=1.01, F=1.04, AVERAGE
Direction gap: +0.65 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd6_invwip)`: S=0.90, F=0.93, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_invwip / close)`: S=1.01, F=1.04, T=3.5%, AVERAGE (TOP3000)
- `rank(-1 * ts_delta(fnd6_invwip, 5))`: S=0.63, F=0.44, T=20.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_invwip)` | TOP500 | 0.29 | 0.16 | 23.8% | 40% | bull-only |
| `rank(fnd6_invwip / close)` | TOP500 | 0.29 | 0.16 | 17.4% | 60% | bull-only |
| `rank(fnd6_invwip / close)` | TOP3000 | 0.28 | 0.13 | 20.4% | 60% | bull-only |
| `rank(fnd6_invwip)` | TOP3000 | 0.19 | 0.08 | 28.5% | 60% | bull-only |
| `rank(fnd6_invwip)` | TOP1000 | 0.17 | 0.07 | 20.5% | 40% | bull-only |
| `rank(fnd6_invwip / close)` | TOP1000 | 0.12 | 0.05 | 18.6% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_invrmq: 0.765 (strongly positively correlated)
- fnd6_newqv1300_invfgq: 0.703 (strongly positively correlated)
- fnd6_loxdr: 0.522 (moderately positively correlated)
- fnd6_ch: 0.516 (moderately positively correlated)
- pv13_revere_term_sector_total: 0.512 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
