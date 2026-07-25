---
field: fnd6_aqs
dataset: fundamental6
best_template: ts_zscore
best_sharpe: 0.66
best_fitness: 0.36
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.3824
ann_vol: 0.2111
hit_rate: 0.4931
rolling_sharpe_min: -1.963
rolling_sharpe_max: 1.895
negated_best_sharpe: 0.04
negated_best_template: neg_rank
negated_best_fitness: 0.01
n_negated_sims: 10
direction_gap: -0.62
---
# fnd6_aqs (fundamental6)

*Acquisitions - Sales Contribution*

## Signal Profile
- `rank(fnd6_aqs)`: S=0.26, F=0.17, T=4.1%, INFERIOR (TOP200)
- `rank(fnd6_aqs / close)`: S=0.23, F=0.11, T=4.3%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_aqs, 5))`: S=-0.09, F=-0.03, T=2.8%, INFERIOR (TOP200)
- `-rank(fnd6_aqs)`: S=0.04, F=0.01, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aqs, 5))`: S=-0.71, F=-0.81, T=14.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_aqs, 22)`: S=0.66, F=0.36, T=2.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_aqs, 10)`: S=-0.53, F=-0.38, T=3.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_aqs, 22))`: S=-0.80, F=-0.96, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aqs)`: S=0.04, F=0.01, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aqs / close)`: S=-0.23, F=-0.11, T=4.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 17F/15P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.25, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-1.16 (negative), ret=-17.3%
  - 2020: S=-0.47 (negative), ret=-9.3%
  - 2021: S=0.93 (moderate), ret=+17.6%
  - 2022: S=0.53 (moderate), ret=+7.1%
  - 2023: S=0.88 (moderate), ret=+27.7%

## Risk & Drawdown
- Max drawdown: 38.24% over 1211 days (recovered)
- Annualized: return +5.2%, volatility 21.1% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.97, excess kurtosis +12.28

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.96, max 1.90, latest 0.88

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +17.00%; worst month: -14.17%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.29
- Sideways: S=0.43
- Bear: S=-0.81

## Negated Direction
Best negated: `-rank(fnd6_aqs)` S=0.04, F=0.01, INFERIOR
Direction gap: -0.62 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_aqs)`: S=0.04, F=0.01, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_aqs / close)`: S=-0.23, F=-0.11, T=4.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_aqs, 5))`: S=-0.71, F=-0.81, T=14.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_aqs)` | TOP200 | 0.25 | 0.17 | 38.2% | 60% | bull-only |
| `rank(fnd6_aqs / close)` | TOP1000 | 0.25 | 0.11 | 31.7% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_acqintan: 0.217 (weakly positively correlated)
- fnd6_acqgdwl: 0.166 (weakly positively correlated)
- correlation_last_360_days_spy: 0.160 (weakly positively correlated)
- max_ebitda_guidance: -0.157 (weakly negatively correlated)
- min_ebitda_guidance: -0.156 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
