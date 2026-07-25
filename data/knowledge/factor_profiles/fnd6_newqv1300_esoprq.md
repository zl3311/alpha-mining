---
field: fnd6_newqv1300_esoprq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.56
best_fitness: 0.69
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.7501
ann_vol: 0.3411
hit_rate: 0.5109
rolling_sharpe_min: -2.431
rolling_sharpe_max: 3.55
redundancy_cluster: 96
negated_best_sharpe: 0.15
negated_best_template: neg_rank
negated_best_fitness: 0.05
n_negated_sims: 10
direction_gap: -0.41
---
# fnd6_newqv1300_esoprq (fundamental6)

*Preferred ESOP Obligation - Redeemable*

## Signal Profile
- `rank(fnd6_newqv1300_esoprq)`: S=0.56, F=0.69, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_newqv1300_esoprq / close)`: S=0.56, F=0.69, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newqv1300_esoprq, 5))`: S=0.39, F=0.20, T=3.5%, INFERIOR (TOP500)
- `-rank(fnd6_newqv1300_esoprq)`: S=0.15, F=0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_esoprq, 5))`: S=-0.10, F=-0.03, T=3.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_newqv1300_esoprq, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_newqv1300_esoprq, 10)`: S=0.21, F=0.20, T=0.5%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_esoprq, 22))`: S=-0.15, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_esoprq)`: S=-0.16, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_esoprq / close)`: S=-0.16, F=-0.05, T=3.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 25F/1P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.23 (moderate), ret=+41.0%
  - 2020: S=2.39 (strong), ret=+97.1%
  - 2021: S=0.20 (weak), ret=+9.1%
  - 2022: S=-2.27 (negative), ret=-58.1%
  - 2023: S=1.00 (moderate), ret=+5.2%

## Risk & Drawdown
- Max drawdown: 75.01% over 1170 days (not yet recovered, ongoing at window end)
- Annualized: return +19.2%, volatility 34.1% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.46, excess kurtosis +10.83

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.43, max 3.55, latest 1.24

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +26.37%; worst month: -20.70%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.40
- Sideways: S=0.26
- Bear: S=1.76

## Negated Direction
Best negated: `-rank(fnd6_newqv1300_esoprq)` S=0.15, F=0.05, INFERIOR
Direction gap: -0.41 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_esoprq)`: S=-0.16, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_esoprq / close)`: S=-0.16, F=-0.05, T=3.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_esoprq, 5))`: S=-0.10, F=-0.03, T=3.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_esoprq)` | TOP3000 | 0.56 | 0.69 | 75.0% | 80% | mixed |
| `rank(fnd6_newqv1300_esoprq / close)` | TOP3000 | 0.56 | 0.69 | 75.0% | 80% | mixed |
| `rank(ts_delta(fnd6_newqv1300_esoprq, 5))` | TOP500 | 0.37 | 0.20 | 27.5% | 80% | bull-only |
| `rank(fnd6_newqv1300_esoprq)` | TOP500 | 0.30 | 0.15 | 27.4% | 80% | bull-only |
| `rank(fnd6_newqv1300_esoprq / close)` | TOP500 | 0.30 | 0.15 | 27.4% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_esopr: 0.996 (strongly positively correlated)
- anl4_afv4_cfps_high: -0.287 (weakly negatively correlated)
- anl4_afv4_cfps_mean: -0.282 (weakly negatively correlated)
- anl4_afv4_cfps_median: -0.282 (weakly negatively correlated)
- fnd6_cshpri: -0.278 (weakly negatively correlated)

Redundancy cluster #96: 2 similar fields, mean |rho| 0.996 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
