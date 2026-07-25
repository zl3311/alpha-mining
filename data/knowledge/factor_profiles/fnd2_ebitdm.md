---
field: fnd2_ebitdm
dataset: fundamental2
best_template: neg_rank_level
best_sharpe: 0.83
best_fitness: 0.71
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.4528
ann_vol: 0.1739
hit_rate: 0.4858
rolling_sharpe_min: -2.018
rolling_sharpe_max: 3.369
negated_best_sharpe: 0.83
negated_best_template: neg_rank_level
negated_best_fitness: 0.71
n_negated_sims: 10
direction_gap: 0.61
---
# fnd2_ebitdm (fundamental2)

*EBIT, Domestic*

## Signal Profile
- `rank(fnd2_ebitdm)`: S=-0.11, F=-0.03, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_ebitdm / close)`: S=0.04, F=0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_ebitdm, 5))`: S=0.22, F=0.08, T=29.3%, INFERIOR (TOP200)
- `-rank(fnd2_ebitdm)`: S=0.14, F=0.04, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_ebitdm, 5))`: S=-0.38, F=-0.18, T=29.5%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_ebitdm, 22)`: S=-0.22, F=-0.10, T=22.3%, INFERIOR (TOP3000)
- `ts_mean(fnd2_ebitdm, 10)`: S=-0.08, F=-0.02, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_ebitdm, 22))`: S=0.03, F=0.00, T=14.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_ebitdm)`: S=0.83, F=0.71, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_ebitdm / close)`: S=0.76, F=0.62, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 18F/2P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.23, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=0.05 (weak), ret=+0.7%
  - 2020: S=-0.78 (negative), ret=-12.2%
  - 2021: S=0.70 (moderate), ret=+15.8%
  - 2022: S=1.24 (moderate), ret=+22.6%
  - 2023: S=-0.55 (negative), ret=-7.7%

## Risk & Drawdown
- Max drawdown: 45.28% over 822 days (recovered)
- Annualized: return +3.9%, volatility 17.4% (fraction of booksize)
- Hit rate: 48.6% positive days
- Tail shape: skew -0.45, excess kurtosis +6.00

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.02, max 3.37, latest -0.58

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +15.97%; worst month: -12.70%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.52
- Sideways: S=-0.09
- Bear: S=-0.85

## Negated Direction
Best negated: `rank(-1 * fnd2_ebitdm)` S=0.83, F=0.71, INFERIOR
Direction gap: +0.61 (negated - positive best Sharpe). NEGATION DOMINANT — field is significantly stronger when reversed.

Negated template variants:
- `rank(-1 * fnd2_ebitdm)`: S=0.83, F=0.71, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_ebitdm / close)`: S=0.76, F=0.62, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_ebitdm, 5))`: S=-0.38, F=-0.18, T=29.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_ebitdm, 5))` | TOP200 | 0.23 | 0.08 | 45.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_itxreclstatelocalitxes: 0.281 (weakly positively correlated)
- fnd2_ebitfr: 0.278 (weakly positively correlated)
- fnd6_newa1v1300_ibc: 0.255 (weakly positively correlated)
- fnd6_newa1v1300_epsfx: 0.242 (weakly positively correlated)
- fnd6_newa1v1300_epsfi: 0.240 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
