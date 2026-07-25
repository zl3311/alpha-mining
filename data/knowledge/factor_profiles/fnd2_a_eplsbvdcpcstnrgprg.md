---
field: fnd2_a_eplsbvdcpcstnrgprg
dataset: fundamental2
best_template: rank_delta
best_sharpe: 0.59
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.2717
ann_vol: 0.1804
hit_rate: 0.5077
rolling_sharpe_min: -0.608
rolling_sharpe_max: 2.099
negated_best_sharpe: 0.1
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.49
---
# fnd2_a_eplsbvdcpcstnrgprg (fundamental2)

*The weighted average period over which unrecognized compensation is expected to be recognized for equity-based compensation plans, using a decimal to express in number of years.*

## Signal Profile
- `rank(fnd2_a_eplsbvdcpcstnrgprg)`: S=0.77, F=0.33, T=0.9%, INFERIOR (TOP3000)
- `rank(fnd2_a_eplsbvdcpcstnrgprg / close)`: S=0.25, F=0.12, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_eplsbvdcpcstnrgprg, 5))`: S=0.59, F=0.35, T=30.8%, INFERIOR (TOP3000)
- `-rank(fnd2_a_eplsbvdcpcstnrgprg)`: S=-0.50, F=-0.19, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_eplsbvdcpcstnrgprg, 5))`: S=-0.02, F=0.00, T=20.3%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_eplsbvdcpcstnrgprg, 63)`: S=0.07, F=0.02, T=11.8%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_eplsbvdcpcstnrgprg, 10)`: S=-0.16, F=-0.08, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_eplsbvdcpcstnrgprg, 22))`: S=-0.30, F=-0.19, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_eplsbvdcpcstnrgprg)`: S=-0.50, F=-0.27, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_eplsbvdcpcstnrgprg / close)`: S=0.10, F=0.03, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 5F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.59, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.56 (negative), ret=-11.1%
  - 2020: S=0.98 (moderate), ret=+23.4%
  - 2021: S=1.34 (moderate), ret=+25.0%
  - 2022: S=0.75 (moderate), ret=+9.0%
  - 2023: S=0.61 (moderate), ret=+6.0%

## Risk & Drawdown
- Max drawdown: 27.17% over 365 days (recovered)
- Annualized: return +10.7%, volatility 18.0% (fraction of booksize)
- Hit rate: 50.8% positive days
- Tail shape: skew +0.90, excess kurtosis +28.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.61, max 2.10, latest 0.71

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +22.18%; worst month: -14.25%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.05
- Sideways: S=0.60
- Bear: S=1.17

## Negated Direction
Best negated: `rank(-1 * fnd2_a_eplsbvdcpcstnrgprg / close)` S=0.10, F=0.03, INFERIOR
Direction gap: -0.49 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_eplsbvdcpcstnrgprg)`: S=-0.50, F=-0.27, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_eplsbvdcpcstnrgprg / close)`: S=0.10, F=0.03, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_eplsbvdcpcstnrgprg, 5))`: S=-0.02, F=0.00, T=20.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd2_a_eplsbvdcpcstnrgprg, 5))` | TOP3000 | 0.59 | 0.35 | 27.2% | 80% | mixed |
| `rank(fnd2_a_eplsbvdcpcstnrgprg)` | TOP3000 | 0.80 | 0.33 | 9.0% | 80% | mixed |
| `rank(ts_delta(fnd2_a_eplsbvdcpcstnrgprg, 5))` | TOP500 | 0.52 | 0.31 | 35.4% | 80% | mixed |
| `rank(fnd2_a_eplsbvdcpcstnrgprg)` | TOP200 | 0.51 | 0.27 | 11.3% | 60% | mixed |
| `rank(fnd2_a_eplsbvdcpcstnrgprg)` | TOP500 | 0.52 | 0.21 | 12.3% | 80% | mixed |
| `rank(fnd2_a_eplsbvdcpcstnrgprg)` | TOP1000 | 0.53 | 0.19 | 9.3% | 80% | mixed |
| `rank(ts_delta(fnd2_a_eplsbvdcpcstnrgprg, 5))` | TOP1000 | 0.38 | 0.17 | 27.3% | 60% | mixed |
| `rank(fnd2_a_eplsbvdcpcstnrgprg / close)` | TOP3000 | 0.26 | 0.12 | 34.0% | 60% | bear-only |
| `rank(fnd2_a_eplsbvdcpcstnrgprg / close)` | TOP1000 | 0.21 | 0.08 | 23.3% | 40% | bear-only |

## Correlation Notes
Top correlates:
- rp_ess_credit: -0.163 (weakly negatively correlated)
- fnd6_cimii: -0.117 (weakly negatively correlated)
- fnd6_mfma1_aoloch: 0.116 (weakly positively correlated)
- fnd6_newa1v1300_aoloch: 0.115 (weakly positively correlated)
- fn_comprehensive_income_net_of_tax_a: 0.106 (weakly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
