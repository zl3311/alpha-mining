---
field: fnd6_cidergl
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.57
best_fitness: 0.29
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.3414
ann_vol: 0.151
hit_rate: 0.4753
rolling_sharpe_min: -1.076
rolling_sharpe_max: 1.984
negated_best_sharpe: 0.21
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 10
direction_gap: -0.36
---
# fnd6_cidergl (fundamental6)

*Comp Inc - Derivative Gains/Losses*

## Signal Profile
- `rank(fnd6_cidergl)`: S=0.37, F=0.17, T=3.4%, INFERIOR (TOP200)
- `rank(fnd6_cidergl / close)`: S=0.29, F=0.12, T=3.4%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_cidergl, 5))`: S=0.57, F=0.29, T=32.3%, INFERIOR (TOP500)
- `-rank(fnd6_cidergl)`: S=-0.13, F=-0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cidergl, 5))`: S=0.21, F=0.07, T=26.7%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cidergl, 22)`: S=-0.90, F=-0.82, T=19.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cidergl, 10)`: S=0.12, F=0.03, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cidergl, 22))`: S=0.30, F=0.12, T=19.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cidergl)`: S=-0.37, F=-0.17, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cidergl / close)`: S=-0.29, F=-0.12, T=3.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.57, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-1.04 (negative), ret=-12.3%
  - 2020: S=0.83 (moderate), ret=+15.1%
  - 2021: S=0.83 (moderate), ret=+13.5%
  - 2022: S=0.05 (weak), ret=+0.6%
  - 2023: S=1.90 (strong), ret=+25.7%

## Risk & Drawdown
- Max drawdown: 34.14% over 363 days (recovered)
- Annualized: return +8.7%, volatility 15.1% (fraction of booksize)
- Hit rate: 47.5% positive days
- Tail shape: skew +0.90, excess kurtosis +9.26

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.08, max 1.98, latest 1.90

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +15.05%; worst month: -15.39%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.36
- Sideways: S=-0.14
- Bear: S=0.45

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_cidergl, 5))` S=0.21, F=0.07, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_cidergl)`: S=-0.37, F=-0.17, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cidergl / close)`: S=-0.29, F=-0.12, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cidergl, 5))`: S=0.21, F=0.07, T=26.7%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_cidergl, 5))` | TOP500 | 0.57 | 0.29 | 34.1% | 80% | mixed |
| `rank(fnd6_cidergl)` | TOP200 | 0.38 | 0.17 | 19.6% | 80% | mixed |
| `rank(fnd6_cidergl / close)` | TOP200 | 0.30 | 0.12 | 20.2% | 80% | bear-only |
| `rank(ts_delta(fnd6_cidergl, 5))` | TOP1000 | 0.30 | 0.11 | 30.4% | 40% | mixed |
| `rank(fnd6_cidergl)` | TOP500 | 0.23 | 0.07 | 13.5% | 60% | mixed |
| `rank(fnd6_cidergl / close)` | TOP500 | 0.15 | 0.04 | 14.0% | 60% | mixed |
| `rank(fnd6_cidergl)` | TOP3000 | 0.14 | 0.03 | 7.5% | 40% | weak |
| `rank(fnd6_cidergl)` | TOP1000 | 0.13 | 0.03 | 10.4% | 60% | mixed |
| `rank(ts_delta(fnd6_cidergl, 5))` | TOP3000 | 0.11 | 0.02 | 25.6% | 60% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_reajo: 0.315 (weakly positively correlated)
- fnd6_txdfed: 0.211 (weakly positively correlated)
- fnd6_optca: 0.193 (weakly positively correlated)
- fn_repurchased_shares_value_a: 0.191 (weakly positively correlated)
- fnd2_a_ltrmdmrepoplinnext12m: 0.168 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
