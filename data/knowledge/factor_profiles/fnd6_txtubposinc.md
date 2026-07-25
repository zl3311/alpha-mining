---
field: fnd6_txtubposinc
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.68
best_fitness: 0.37
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 6
max_drawdown: 0.1022
ann_vol: 0.0542
hit_rate: 0.5053
rolling_sharpe_min: -1.692
rolling_sharpe_max: 2.593
redundancy_cluster: 17
negated_best_sharpe: 0.68
negated_best_template: rank_neg_delta
negated_best_fitness: 0.35
n_negated_sims: 10
direction_gap: 0.0
---
# fnd6_txtubposinc (fundamental6)

*Increase - Current Tax Positions*

## Signal Profile
- `rank(fnd6_txtubposinc)`: S=0.51, F=0.27, T=1.9%, INFERIOR (TOP3000)
- `rank(fnd6_txtubposinc / close)`: S=0.68, F=0.37, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_txtubposinc, 5))`: S=0.16, F=0.04, T=41.9%, INFERIOR (TOP3000)
- `-rank(fnd6_txtubposinc)`: S=-0.19, F=-0.07, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubposinc, 5))`: S=0.68, F=0.35, T=38.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txtubposinc, 22)`: S=0.44, F=0.28, T=20.3%, INFERIOR (TOP3000)
- `ts_mean(fnd6_txtubposinc, 10)`: S=0.31, F=0.16, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txtubposinc, 22))`: S=0.31, F=0.13, T=21.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubposinc)`: S=-0.19, F=-0.07, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubposinc / close)`: S=-0.23, F=-0.09, T=2.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.68, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.16 (moderate), ret=+4.2%
  - 2020: S=-0.55 (negative), ret=-2.3%
  - 2021: S=1.48 (moderate), ret=+11.8%
  - 2022: S=0.28 (weak), ret=+1.7%
  - 2023: S=0.69 (moderate), ret=+2.6%

## Risk & Drawdown
- Max drawdown: 10.22% over 398 days (recovered)
- Annualized: return +3.7%, volatility 5.4% (fraction of booksize)
- Hit rate: 50.5% positive days
- Tail shape: skew +0.16, excess kurtosis +2.85

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.69, max 2.59, latest 0.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.83%; worst month: -2.71%
Positive months: 59%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.38
- Sideways: S=1.16
- Bear: S=-1.95

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_txtubposinc, 5))` S=0.68, F=0.35, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_txtubposinc)`: S=-0.19, F=-0.07, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txtubposinc / close)`: S=-0.23, F=-0.09, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txtubposinc, 5))`: S=0.68, F=0.35, T=38.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_txtubposinc / close)` | TOP3000 | 0.68 | 0.37 | 10.2% | 80% | bull-only |
| `rank(fnd6_txtubposinc)` | TOP3000 | 0.50 | 0.27 | 21.2% | 80% | bull-only |
| `rank(fnd6_txtubposinc / close)` | TOP1000 | 0.22 | 0.09 | 12.3% | 40% | bull-only |
| `rank(fnd6_txtubposinc)` | TOP1000 | 0.18 | 0.07 | 22.6% | 40% | bull-only |
| `rank(fnd6_txtubposinc / close)` | TOP500 | 0.16 | 0.06 | 18.7% | 60% | bull-only |
| `rank(ts_delta(fnd6_txtubposinc, 5))` | TOP3000 | 0.16 | 0.04 | 28.8% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd6_txtubend: 0.888 (strongly positively correlated)
- fnd6_txtubbegin: 0.864 (strongly positively correlated)
- fnd6_txtubpospinc: 0.836 (strongly positively correlated)
- fn_unrecognized_tax_benefits_a: 0.823 (strongly positively correlated)
- fnd6_newa2v1300_xsga: 0.820 (strongly positively correlated)

Redundancy cluster #17: 12 similar fields, mean |rho| 0.768 (representative: fnd6_newqv1300_aol2q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
