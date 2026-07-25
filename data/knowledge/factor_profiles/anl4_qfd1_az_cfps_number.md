---
field: anl4_qfd1_az_cfps_number
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.48
best_fitness: 0.29
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 3
max_drawdown: 0.175
ann_vol: 0.0968
hit_rate: 0.481
rolling_sharpe_min: -2.35
rolling_sharpe_max: 2.734
negated_best_sharpe: 0.53
negated_best_template: rank_neg_delta
negated_best_fitness: 0.26
n_negated_sims: 10
direction_gap: 0.05
---
# anl4_qfd1_az_cfps_number (analyst4)

*Cash Flow Per Share - number of estimations*

## Signal Profile
- `rank(anl4_qfd1_az_cfps_number)`: S=-0.01, F=0.00, T=1.6%, INFERIOR (TOP3000)
- `rank(anl4_qfd1_az_cfps_number / close)`: S=0.48, F=0.29, T=1.9%, INFERIOR (TOP1000)
- `rank(ts_delta(anl4_qfd1_az_cfps_number, 5))`: S=-0.27, F=-0.12, T=31.8%, INFERIOR (TOP200)
- `-rank(anl4_qfd1_az_cfps_number)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_cfps_number, 5))`: S=0.53, F=0.26, T=32.1%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qfd1_az_cfps_number, 22)`: S=-0.12, F=-0.04, T=29.2%, INFERIOR (TOP3000)
- `ts_mean(anl4_qfd1_az_cfps_number, 10)`: S=0.40, F=0.18, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qfd1_az_cfps_number, 22))`: S=0.13, F=0.04, T=13.8%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_cfps_number)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_cfps_number / close)`: S=-0.48, F=-0.29, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.48, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-1.14 (negative), ret=-7.1%
  - 2020: S=1.33 (moderate), ret=+16.4%
  - 2021: S=0.45 (weak), ret=+4.7%
  - 2022: S=0.27 (weak), ret=+2.4%
  - 2023: S=0.78 (moderate), ret=+6.3%

## Risk & Drawdown
- Max drawdown: 17.50% over 495 days (recovered)
- Annualized: return +4.6%, volatility 9.7% (fraction of booksize)
- Hit rate: 48.1% positive days
- Tail shape: skew +0.57, excess kurtosis +1.76

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.35, max 2.73, latest 0.88

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +10.64%; worst month: -6.07%
Positive months: 52%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.49
- Sideways: S=-0.63
- Bear: S=2.18

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_qfd1_az_cfps_number, 5))` S=0.53, F=0.26, INFERIOR
Direction gap: +0.05 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * anl4_qfd1_az_cfps_number)`: S=0.01, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qfd1_az_cfps_number / close)`: S=-0.48, F=-0.29, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qfd1_az_cfps_number, 5))`: S=0.53, F=0.26, T=32.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qfd1_az_cfps_number / close)` | TOP1000 | 0.48 | 0.29 | 17.5% | 80% | mixed |
| `rank(anl4_qfd1_az_cfps_number / close)` | TOP3000 | 0.15 | 0.06 | 35.6% | 20% | bear-only |
| `rank(anl4_qfd1_az_cfps_number / close)` | TOP500 | 0.12 | 0.03 | 19.6% | 40% | mixed |

## Correlation Notes
Top correlates:
- anl4_qf_az_cfps_number: 1.000 (strongly positively correlated)
- anl4_afv4_cfps_number: 0.922 (strongly positively correlated)
- fnd6_beta: 0.900 (strongly positively correlated)
- anl4_qf_az_div_number: 0.870 (strongly positively correlated)
- anl4_qfd1_az_div_number: 0.870 (strongly positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
