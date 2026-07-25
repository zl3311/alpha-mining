---
field: fnd6_beta
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.66
best_fitness: 0.47
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.1372
ann_vol: 0.0974
hit_rate: 0.4777
rolling_sharpe_min: -1.889
rolling_sharpe_max: 3.04
redundancy_cluster: 75
negated_best_sharpe: -0.7
negated_best_template: neg_rank
negated_best_fitness: -0.43
n_negated_sims: 10
direction_gap: -1.36
---
# fnd6_beta (fundamental6)

*beta*

## Signal Profile
- `rank(fnd6_beta)`: S=0.70, F=0.43, T=1.2%, INFERIOR (TOP1000)
- `rank(fnd6_beta / close)`: S=0.66, F=0.47, T=1.6%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_beta, 5))`: S=0.48, F=0.31, T=3.9%, INFERIOR (TOP200)
- `-rank(fnd6_beta)`: S=-0.70, F=-0.43, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_beta, 5))`: S=-0.69, F=-0.53, T=3.0%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_beta, 22)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_beta, 10)`: S=0.60, F=0.36, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_beta, 22))`: S=-0.69, F=-0.53, T=3.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_beta)`: S=-0.70, F=-0.43, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_beta / close)`: S=-0.66, F=-0.47, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/12P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.66, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.37 (negative), ret=-2.5%
  - 2020: S=1.41 (moderate), ret=+18.1%
  - 2021: S=1.13 (moderate), ret=+12.2%
  - 2022: S=0.08 (weak), ret=+0.6%
  - 2023: S=0.41 (weak), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 13.72% over 464 days (recovered)
- Annualized: return +6.5%, volatility 9.7% (fraction of booksize)
- Hit rate: 47.8% positive days
- Tail shape: skew +0.55, excess kurtosis +1.81

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.89, max 3.04, latest 0.50

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +10.54%; worst month: -5.41%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.12
- Sideways: S=-0.77
- Bear: S=2.50

## Negated Direction
Best negated: `-rank(fnd6_beta)` S=-0.70, F=-0.43, INFERIOR
Direction gap: -1.36 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_beta)`: S=-0.70, F=-0.43, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_beta / close)`: S=-0.66, F=-0.47, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_beta, 5))`: S=-0.69, F=-0.53, T=3.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_beta / close)` | TOP1000 | 0.66 | 0.47 | 13.7% | 80% | mixed |
| `rank(fnd6_beta)` | TOP1000 | 0.70 | 0.43 | 12.0% | 80% | mixed |
| `rank(fnd6_beta / close)` | TOP3000 | 0.52 | 0.35 | 22.1% | 40% | bear-only |
| `rank(ts_delta(fnd6_beta, 5))` | TOP200 | 0.46 | 0.31 | 17.1% | 60% | bull-only |
| `rank(fnd6_beta)` | TOP3000 | 0.55 | 0.29 | 9.9% | 40% | mixed |
| `rank(fnd6_beta / close)` | TOP500 | 0.27 | 0.12 | 20.9% | 40% | mixed |
| `rank(fnd6_beta)` | TOP500 | 0.23 | 0.08 | 18.1% | 60% | bear-only |
| `rank(ts_delta(fnd6_beta, 5))` | TOP500 | 0.15 | 0.05 | 22.0% | 60% | bull-only |
| `rank(fnd6_beta)` | TOP200 | 0.09 | 0.02 | 37.6% | 60% | bear-only |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_cfps_number: 0.900 (strongly positively correlated)
- anl4_qf_az_cfps_number: 0.900 (strongly positively correlated)
- anl4_qf_az_div_number: 0.869 (strongly positively correlated)
- anl4_qfd1_az_div_number: 0.869 (strongly positively correlated)
- anl4_afv4_cfps_number: 0.866 (strongly positively correlated)

Redundancy cluster #75: 5 similar fields, mean |rho| 0.829 (representative: fn_debt_instrument_interest_rate_stated_percentage_a). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
