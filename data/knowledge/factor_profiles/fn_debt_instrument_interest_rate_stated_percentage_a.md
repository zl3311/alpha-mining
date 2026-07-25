---
field: fn_debt_instrument_interest_rate_stated_percentage_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.69
best_fitness: 0.42
best_universe: TOP1000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 7
max_drawdown: 0.111
ann_vol: 0.0658
hit_rate: 0.4842
rolling_sharpe_min: -1.823
rolling_sharpe_max: 2.658
redundancy_cluster: 75
negated_best_sharpe: 0.27
negated_best_template: rank_neg_delta
negated_best_fitness: 0.13
n_negated_sims: 10
direction_gap: -0.42
---
# fn_debt_instrument_interest_rate_stated_percentage_a (fundamental2)

*Stated percentage of interest rate on debt*

## Signal Profile
- `rank(fn_debt_instrument_interest_rate_stated_percentage_a)`: S=0.44, F=0.15, T=0.6%, INFERIOR (TOP3000)
- `rank(fn_debt_instrument_interest_rate_stated_percentage_a / close)`: S=0.69, F=0.42, T=1.4%, INFERIOR (TOP1000)
- `rank(ts_delta(fn_debt_instrument_interest_rate_stated_percentage_a, 5))`: S=0.43, F=0.24, T=22.8%, INFERIOR (TOP3000)
- `-rank(fn_debt_instrument_interest_rate_stated_percentage_a)`: S=-0.25, F=-0.07, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_interest_rate_stated_percentage_a, 5))`: S=0.27, F=0.13, T=18.9%, INFERIOR (TOP3000)
- `-ts_zscore(fn_debt_instrument_interest_rate_stated_percentage_a, 63)`: S=0.20, F=0.11, T=14.3%, INFERIOR (TOP3000)
- `ts_mean(fn_debt_instrument_interest_rate_stated_percentage_a, 10)`: S=-0.11, F=-0.03, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_debt_instrument_interest_rate_stated_percentage_a, 22))`: S=0.33, F=0.18, T=10.9%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_interest_rate_stated_percentage_a)`: S=0.16, F=0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_interest_rate_stated_percentage_a / close)`: S=0.11, F=0.03, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 7F/13P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.69, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.14 (moderate), ret=+4.2%
  - 2020: S=0.97 (moderate), ret=+8.3%
  - 2021: S=1.17 (moderate), ret=+9.6%
  - 2022: S=-0.26 (negative), ret=-1.3%
  - 2023: S=0.30 (weak), ret=+1.6%

## Risk & Drawdown
- Max drawdown: 11.10% over 933 days (not yet recovered, ongoing at window end)
- Annualized: return +4.5%, volatility 6.6% (fraction of booksize)
- Hit rate: 48.4% positive days
- Tail shape: skew +0.91, excess kurtosis +4.01

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.82, max 2.66, latest 0.40

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2022
Best month: +7.35%; worst month: -3.18%
Positive months: 52%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=0.97
- Sideways: S=-0.30
- Bear: S=1.24

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_debt_instrument_interest_rate_stated_percentage_a, 5))` S=0.27, F=0.13, INFERIOR
Direction gap: -0.42 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_debt_instrument_interest_rate_stated_percentage_a)`: S=0.16, F=0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_debt_instrument_interest_rate_stated_percentage_a / close)`: S=0.11, F=0.03, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_debt_instrument_interest_rate_stated_percentage_a, 5))`: S=0.27, F=0.13, T=18.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_debt_instrument_interest_rate_stated_percentage_a / close)` | TOP1000 | 0.69 | 0.42 | 11.1% | 80% | all-weather |
| `rank(fn_debt_instrument_interest_rate_stated_percentage_a / close)` | TOP3000 | 0.64 | 0.41 | 18.9% | 80% | mixed |
| `rank(ts_delta(fn_debt_instrument_interest_rate_stated_percentage_a, 5))` | TOP3000 | 0.42 | 0.24 | 31.6% | 80% | weak |
| `rank(fn_debt_instrument_interest_rate_stated_percentage_a)` | TOP3000 | 0.43 | 0.15 | 6.6% | 80% | bull-only |
| `rank(fn_debt_instrument_interest_rate_stated_percentage_a / close)` | TOP500 | 0.27 | 0.11 | 10.1% | 60% | mixed |
| `rank(ts_delta(fn_debt_instrument_interest_rate_stated_percentage_a, 5))` | TOP1000 | 0.20 | 0.08 | 29.0% | 40% | weak |
| `rank(fn_debt_instrument_interest_rate_stated_percentage_a)` | TOP1000 | 0.24 | 0.07 | 9.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_debt_instrument_interest_rate_stated_percentage_q: 0.906 (strongly positively correlated)
- fnd6_beta: 0.809 (strongly positively correlated)
- anl4_qfd1_az_cfps_number: 0.800 (strongly positively correlated)
- anl4_qf_az_cfps_number: 0.800 (strongly positively correlated)
- anl4_afv4_cfps_number: 0.785 (strongly positively correlated)

Redundancy cluster #75: 5 similar fields, mean |rho| 0.829 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
