---
field: anl4_qf_az_div_number
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.62
best_fitness: 0.42
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.1389
ann_vol: 0.0942
hit_rate: 0.4785
rolling_sharpe_min: -1.893
rolling_sharpe_max: 2.955
redundancy_cluster: 75
negated_best_sharpe: 0.37
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.25
---
# anl4_qf_az_div_number (analyst4)

*Dividend per share - number of estimations*

## Signal Profile
- `rank(anl4_qf_az_div_number)`: S=0.19, F=0.06, T=3.7%, INFERIOR (TOP200)
- `rank(anl4_qf_az_div_number / close)`: S=0.62, F=0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(anl4_qf_az_div_number, 5))`: S=0.19, F=0.05, T=34.5%, INFERIOR (TOP200)
- `-rank(anl4_qf_az_div_number)`: S=-0.25, F=-0.06, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_div_number, 5))`: S=0.37, F=0.08, T=35.9%, INFERIOR (TOP3000)
- `ts_zscore(anl4_qf_az_div_number, 22)`: S=0.35, F=0.12, T=33.9%, INFERIOR (TOP3000)
- `ts_mean(anl4_qf_az_div_number, 10)`: S=0.30, F=0.09, T=2.7%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_qf_az_div_number, 22))`: S=0.36, F=0.12, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_div_number)`: S=-0.21, F=-0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_div_number / close)`: S=-0.62, F=-0.42, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.62, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.33 (negative), ret=-2.1%
  - 2020: S=1.58 (strong), ret=+19.9%
  - 2021: S=0.96 (moderate), ret=+8.0%
  - 2022: S=-0.21 (negative), ret=-1.8%
  - 2023: S=0.53 (moderate), ret=+4.9%

## Risk & Drawdown
- Max drawdown: 13.89% over 469 days (recovered)
- Annualized: return +5.9%, volatility 9.4% (fraction of booksize)
- Hit rate: 47.9% positive days
- Tail shape: skew +0.70, excess kurtosis +2.76

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.89, max 2.96, latest 0.69

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +9.31%; worst month: -3.91%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.18
- Sideways: S=-0.43
- Bear: S=2.32

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_qf_az_div_number, 5))` S=0.37, F=0.08, INFERIOR
Direction gap: -0.25 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_qf_az_div_number)`: S=-0.21, F=-0.04, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_qf_az_div_number / close)`: S=-0.62, F=-0.42, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_qf_az_div_number, 5))`: S=0.37, F=0.08, T=35.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_qf_az_div_number / close)` | TOP3000 | 0.62 | 0.42 | 13.9% | 60% | mixed |
| `rank(anl4_qf_az_div_number / close)` | TOP1000 | 0.52 | 0.31 | 15.1% | 60% | mixed |
| `rank(anl4_qf_az_div_number / close)` | TOP500 | 0.52 | 0.29 | 10.7% | 60% | all-weather |
| `rank(anl4_qf_az_div_number)` | TOP1000 | 0.23 | 0.06 | 5.6% | 40% | bull-only |
| `rank(anl4_qf_az_div_number)` | TOP200 | 0.17 | 0.06 | 12.8% | 60% | bull-only |
| `rank(ts_delta(anl4_qf_az_div_number, 5))` | TOP200 | 0.21 | 0.05 | 43.5% | 60% | mixed |
| `rank(anl4_qf_az_div_number / close)` | TOP200 | 0.16 | 0.05 | 19.9% | 40% | weak |
| `rank(anl4_qf_az_div_number)` | TOP3000 | 0.18 | 0.04 | 7.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_qfd1_az_div_number: 1.000 (strongly positively correlated)
- anl4_afv4_div_number: 0.936 (strongly positively correlated)
- fnd2_propplteqmuflmblgland: 0.931 (strongly positively correlated)
- option_breakeven_1080: -0.903 (strongly negatively correlated)
- option_breakeven_720: -0.902 (strongly negatively correlated)

Redundancy cluster #75: 5 similar fields, mean |rho| 0.829 (representative: fn_debt_instrument_interest_rate_stated_percentage_a). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
