---
field: fnd6_optosey
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.8
best_fitness: 0.52
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.1738
ann_vol: 0.0674
hit_rate: 0.5117
rolling_sharpe_min: -2.111
rolling_sharpe_max: 3.563
redundancy_cluster: 57
negated_best_sharpe: 0.34
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.46
---
# fnd6_optosey (fundamental6)

*Options Outstanding - End of Year*

## Signal Profile
- `rank(fnd6_optosey)`: S=0.84, F=0.50, T=2.8%, INFERIOR (TOP500)
- `rank(fnd6_optosey / close)`: S=0.80, F=0.52, T=3.0%, INFERIOR (TOP500)
- `rank(ts_delta(fnd6_optosey, 5))`: S=0.35, F=0.14, T=37.3%, INFERIOR (TOP1000)
- `-rank(fnd6_optosey)`: S=-0.49, F=-0.20, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optosey, 5))`: S=0.34, F=0.20, T=22.1%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_optosey, 22)`: S=-0.10, F=-0.03, T=22.4%, INFERIOR (TOP3000)
- `ts_mean(fnd6_optosey, 10)`: S=0.74, F=0.51, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_optosey, 22))`: S=0.44, F=0.23, T=20.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optosey)`: S=-0.62, F=-0.41, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optosey / close)`: S=-0.68, F=-0.49, T=3.7%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/12P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.80, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.65 (strong), ret=+6.7%
  - 2020: S=2.85 (strong), ret=+18.9%
  - 2021: S=-1.18 (negative), ret=-8.4%
  - 2022: S=0.66 (moderate), ret=+5.5%
  - 2023: S=0.61 (moderate), ret=+3.7%

## Risk & Drawdown
- Max drawdown: 17.38% over 1054 days (not yet recovered, ongoing at window end)
- Annualized: return +5.4%, volatility 6.7% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.36, excess kurtosis +1.43

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.11, max 3.56, latest 0.70

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +8.55%; worst month: -3.32%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.29
- Sideways: S=0.28
- Bear: S=1.86

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_optosey, 5))` S=0.34, F=0.20, INFERIOR
Direction gap: -0.46 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_optosey)`: S=-0.62, F=-0.41, T=3.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_optosey / close)`: S=-0.68, F=-0.49, T=3.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_optosey, 5))`: S=0.34, F=0.20, T=22.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_optosey / close)` | TOP500 | 0.80 | 0.52 | 17.4% | 80% | mixed |
| `rank(fnd6_optosey)` | TOP500 | 0.83 | 0.50 | 12.3% | 80% | all-weather |
| `rank(fnd6_optosey / close)` | TOP200 | 0.69 | 0.49 | 14.1% | 60% | mixed |
| `rank(fnd6_optosey)` | TOP200 | 0.63 | 0.41 | 14.6% | 60% | all-weather |
| `rank(fnd6_optosey / close)` | TOP1000 | 0.44 | 0.21 | 16.8% | 60% | bear-only |
| `rank(fnd6_optosey)` | TOP1000 | 0.50 | 0.20 | 9.9% | 60% | mixed |
| `rank(ts_delta(fnd6_optosey, 5))` | TOP1000 | 0.35 | 0.14 | 33.3% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_comp_options_out_number_a: 0.846 (strongly positively correlated)
- fnd6_optgr: 0.742 (strongly positively correlated)
- anl4_fcf_number: 0.656 (moderately positively correlated)
- fnd6_sstk: 0.648 (moderately positively correlated)
- fnd2_dfdtxasoprlcarryfwd: 0.623 (moderately positively correlated)

Redundancy cluster #57: 2 similar fields, mean |rho| 0.846 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
