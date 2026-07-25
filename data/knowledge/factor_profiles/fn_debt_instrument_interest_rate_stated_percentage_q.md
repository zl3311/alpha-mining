---
field: fn_debt_instrument_interest_rate_stated_percentage_q
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.66
best_fitness: 0.38
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 5
max_drawdown: 0.0944
ann_vol: 0.0644
hit_rate: 0.4713
rolling_sharpe_min: -1.657
rolling_sharpe_max: 2.572
redundancy_cluster: 75
negated_best_sharpe: 0.32
negated_best_template: neg_rank_level
negated_best_fitness: 0.12
n_negated_sims: 10
direction_gap: -0.34
---
# fn_debt_instrument_interest_rate_stated_percentage_q (fundamental2)

*Stated percentage of interest rate on debt*

## Signal Profile
- `rank(fn_debt_instrument_interest_rate_stated_percentage_q)`: S=0.42, F=0.14, T=0.7%, INFERIOR (TOP3000)
- `rank(fn_debt_instrument_interest_rate_stated_percentage_q / close)`: S=0.66, F=0.38, T=1.5%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_debt_instrument_interest_rate_stated_percentage_q, 5))`: S=0.11, F=0.03, T=23.4%, INFERIOR (TOP1000)
- `-rank(fn_debt_instrument_interest_rate_stated_percentage_q)`: S=-0.22, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_interest_rate_stated_percentage_q, 5))`: S=0.07, F=0.01, T=24.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_debt_instrument_interest_rate_stated_percentage_q, 63)`: S=0.19, F=0.08, T=13.9%, INFERIOR (TOP3000)
- `ts_mean(fn_debt_instrument_interest_rate_stated_percentage_q, 10)`: S=-0.20, F=-0.07, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_debt_instrument_interest_rate_stated_percentage_q, 22))`: S=0.13, F=0.04, T=11.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_interest_rate_stated_percentage_q)`: S=0.32, F=0.12, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_interest_rate_stated_percentage_q / close)`: S=-0.04, F=-0.01, T=1.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/16P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.66, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.15 (negative), ret=-0.7%
  - 2020: S=0.82 (moderate), ret=+7.0%
  - 2021: S=1.10 (moderate), ret=+8.9%
  - 2022: S=-0.29 (negative), ret=-1.3%
  - 2023: S=1.66 (strong), ret=+7.1%

## Risk & Drawdown
- Max drawdown: 9.44% over 493 days (recovered)
- Annualized: return +4.3%, volatility 6.4% (fraction of booksize)
- Hit rate: 47.1% positive days
- Tail shape: skew +1.14, excess kurtosis +5.95

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.66, max 2.57, latest 1.76

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +8.87%; worst month: -3.20%
Positive months: 51%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.31
- Sideways: S=-0.37
- Bear: S=1.81

## Negated Direction
Best negated: `rank(-1 * fn_debt_instrument_interest_rate_stated_percentage_q)` S=0.32, F=0.12, INFERIOR
Direction gap: -0.34 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_debt_instrument_interest_rate_stated_percentage_q)`: S=0.32, F=0.12, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_interest_rate_stated_percentage_q / close)`: S=-0.04, F=-0.01, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_interest_rate_stated_percentage_q, 5))`: S=0.07, F=0.01, T=24.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_debt_instrument_interest_rate_stated_percentage_q / close)` | TOP1000 | 0.66 | 0.38 | 9.4% | 60% | mixed |
| `rank(fn_debt_instrument_interest_rate_stated_percentage_q / close)` | TOP3000 | 0.44 | 0.24 | 25.2% | 80% | bear-only |
| `rank(fn_debt_instrument_interest_rate_stated_percentage_q)` | TOP3000 | 0.41 | 0.14 | 4.0% | 80% | bull-only |
| `rank(fn_debt_instrument_interest_rate_stated_percentage_q)` | TOP1000 | 0.21 | 0.06 | 10.3% | 80% | bull-only |
| `rank(ts_delta(fn_debt_instrument_interest_rate_stated_percentage_q, 5))` | TOP1000 | 0.10 | 0.03 | 26.3% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fn_debt_instrument_interest_rate_stated_percentage_a: 0.906 (strongly positively correlated)
- fnd6_beta: 0.824 (strongly positively correlated)
- anl4_qfd1_az_cfps_number: 0.808 (strongly positively correlated)
- anl4_qf_az_cfps_number: 0.808 (strongly positively correlated)
- anl4_afv4_cfps_number: 0.774 (strongly positively correlated)

Redundancy cluster #75: 5 similar fields, mean |rho| 0.829 (representative: fn_debt_instrument_interest_rate_stated_percentage_a). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
