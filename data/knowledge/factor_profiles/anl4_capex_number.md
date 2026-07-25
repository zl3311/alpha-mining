---
field: anl4_capex_number
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.54
best_fitness: 0.34
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.1981
ann_vol: 0.0935
hit_rate: 0.5117
rolling_sharpe_min: -1.797
rolling_sharpe_max: 2.044
redundancy_cluster: 72
negated_best_sharpe: 0.01
negated_best_template: rank_neg_delta
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.53
---
# anl4_capex_number (analyst4)

*Capital Expenditures - number of estimations*

## Signal Profile
- `rank(anl4_capex_number)`: S=0.32, F=0.15, T=4.5%, INFERIOR (TOP200)
- `rank(anl4_capex_number / close)`: S=0.54, F=0.34, T=3.7%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_capex_number, 5))`: S=0.79, F=0.29, T=36.6%, INFERIOR (TOP3000)
- `-rank(anl4_capex_number)`: S=-0.22, F=-0.06, T=3.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_number, 5))`: S=0.01, F=0.00, T=35.4%, INFERIOR (TOP3000)
- `ts_zscore(anl4_capex_number, 22)`: S=0.22, F=0.06, T=35.4%, INFERIOR (TOP3000)
- `ts_mean(anl4_capex_number, 10)`: S=0.46, F=0.19, T=3.3%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_capex_number, 22))`: S=0.54, F=0.25, T=13.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_number)`: S=-0.15, F=-0.04, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_number / close)`: S=-0.21, F=-0.08, T=3.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/26P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.46 (moderate), ret=+9.5%
  - 2020: S=0.30 (weak), ret=+3.2%
  - 2021: S=0.01 (weak), ret=+0.1%
  - 2022: S=0.65 (moderate), ret=+6.0%
  - 2023: S=0.76 (moderate), ret=+6.7%

## Risk & Drawdown
- Max drawdown: 19.81% over 369 days (recovered)
- Annualized: return +5.2%, volatility 9.3% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +0.23, excess kurtosis +1.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.80, max 2.04, latest 0.78

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +10.68%; worst month: -5.62%
Positive months: 54%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.01
- Sideways: S=0.34
- Bear: S=1.30

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_capex_number, 5))` S=0.01, F=0.00, INFERIOR
Direction gap: -0.53 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * anl4_capex_number)`: S=-0.15, F=-0.04, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * anl4_capex_number / close)`: S=-0.21, F=-0.08, T=3.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_capex_number, 5))`: S=0.01, F=0.00, T=35.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_capex_number / close)` | TOP200 | 0.56 | 0.34 | 19.8% | 100% | mixed |
| `rank(ts_delta(anl4_capex_number, 5))` | TOP3000 | 0.83 | 0.29 | 7.8% | 60% | mixed |
| `rank(ts_delta(anl4_capex_number, 5))` | TOP200 | 0.50 | 0.22 | 16.2% | 80% | weak |
| `rank(anl4_capex_number)` | TOP200 | 0.32 | 0.15 | 12.1% | 60% | bull-only |
| `rank(anl4_capex_number / close)` | TOP1000 | 0.26 | 0.12 | 28.4% | 40% | bear-only |
| `rank(anl4_capex_number / close)` | TOP500 | 0.21 | 0.08 | 24.6% | 60% | bear-only |
| `rank(ts_delta(anl4_capex_number, 5))` | TOP1000 | 0.28 | 0.06 | 10.1% | 80% | mixed |
| `rank(anl4_capex_number)` | TOP1000 | 0.23 | 0.06 | 8.7% | 40% | weak |
| `rank(anl4_capex_number)` | TOP500 | 0.17 | 0.04 | 11.8% | 80% | mixed |
| `rank(anl4_capex_number / close)` | TOP3000 | 0.09 | 0.02 | 46.0% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_cshtrq: 0.772 (strongly positively correlated)
- anl4_afv4_eps_number: 0.766 (strongly positively correlated)
- anl4_epsa_flag: 0.759 (strongly positively correlated)
- anl4_fcf_number: 0.706 (strongly positively correlated)
- anl4_afv4_cfps_number: 0.637 (moderately positively correlated)

Redundancy cluster #72: 3 similar fields, mean |rho| 0.779 (representative: anl4_afv4_eps_number). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
