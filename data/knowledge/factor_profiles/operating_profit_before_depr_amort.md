---
field: operating_profit_before_depr_amort
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.56
best_fitness: 0.4
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.2314
ann_vol: 0.1143
hit_rate: 0.5101
rolling_sharpe_min: -2.18
rolling_sharpe_max: 2.645
redundancy_cluster: 13
negated_best_sharpe: 0.44
negated_best_template: rank_neg_delta
negated_best_fitness: 0.11
n_negated_sims: 10
direction_gap: -0.12
---
# operating_profit_before_depr_amort (analyst4)

*EBITDA value - Annual*

## Signal Profile
- `rank(operating_profit_before_depr_amort)`: S=0.26, F=0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(operating_profit_before_depr_amort / close)`: S=0.56, F=0.40, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(operating_profit_before_depr_amort, 5))`: S=-0.09, F=-0.01, T=36.8%, INFERIOR (TOP500)
- `-rank(operating_profit_before_depr_amort)`: S=-0.08, F=-0.02, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_profit_before_depr_amort, 5))`: S=0.44, F=0.11, T=35.1%, INFERIOR (TOP3000)
- `-ts_zscore(operating_profit_before_depr_amort, 63)`: S=0.10, F=0.02, T=21.2%, INFERIOR (TOP3000)
- `ts_mean(operating_profit_before_depr_amort, 10)`: S=-0.06, F=-0.01, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(operating_profit_before_depr_amort, 22))`: S=0.12, F=0.02, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_depr_amort)`: S=-0.26, F=-0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_depr_amort / close)`: S=-0.56, F=-0.40, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.55, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.18 (negative), ret=-0.9%
  - 2020: S=-1.40 (negative), ret=-12.2%
  - 2021: S=1.36 (moderate), ret=+19.2%
  - 2022: S=1.51 (strong), ret=+24.0%
  - 2023: S=0.11 (weak), ret=+1.0%

## Risk & Drawdown
- Max drawdown: 23.14% over 770 days (recovered)
- Annualized: return +6.3%, volatility 11.4% (fraction of booksize)
- Hit rate: 51.0% positive days
- Tail shape: skew +0.08, excess kurtosis +1.76

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.18, max 2.65, latest -0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +10.65%; worst month: -5.04%
Positive months: 46%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.31
- Sideways: S=0.44
- Bear: S=-3.06

## Negated Direction
Best negated: `rank(-1 * ts_delta(operating_profit_before_depr_amort, 5))` S=0.44, F=0.11, INFERIOR
Direction gap: -0.12 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * operating_profit_before_depr_amort)`: S=-0.26, F=-0.14, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * operating_profit_before_depr_amort / close)`: S=-0.56, F=-0.40, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(operating_profit_before_depr_amort, 5))`: S=0.44, F=0.11, T=35.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(operating_profit_before_depr_amort / close)` | TOP3000 | 0.55 | 0.40 | 23.1% | 60% | bull-only |
| `rank(operating_profit_before_depr_amort / close)` | TOP1000 | 0.29 | 0.16 | 26.4% | 60% | bull-only |
| `rank(operating_profit_before_depr_amort)` | TOP3000 | 0.25 | 0.14 | 44.5% | 60% | bull-only |
| `rank(operating_profit_before_depr_amort / close)` | TOP500 | 0.04 | 0.02 | 48.5% | 60% | bull-only |

## Correlation Notes
Top correlates:
- ebitda: 0.986 (strongly positively correlated)
- fnd6_newa2v1300_oibdp: 0.986 (strongly positively correlated)
- fnd6_newa1v1300_ebitda: 0.986 (strongly positively correlated)
- fnd6_mfma2_oancf: 0.977 (strongly positively correlated)
- cashflow_op: 0.976 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
