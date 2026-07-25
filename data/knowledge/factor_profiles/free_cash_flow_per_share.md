---
field: free_cash_flow_per_share
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.58
best_fitness: 0.39
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 2
max_drawdown: 0.1638
ann_vol: 0.0999
hit_rate: 0.4923
rolling_sharpe_min: -1.592
rolling_sharpe_max: 2.59
redundancy_cluster: 13
negated_best_sharpe: 0.58
negated_best_template: rank_neg_delta
negated_best_fitness: 0.17
n_negated_sims: 10
direction_gap: 0.0
---
# free_cash_flow_per_share (analyst4)

*Free cash flow per share - actual financial value for the annual period*

## Signal Profile
- `rank(free_cash_flow_per_share)`: S=0.05, F=0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(free_cash_flow_per_share / close)`: S=0.58, F=0.39, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_delta(free_cash_flow_per_share, 5))`: S=-0.16, F=-0.03, T=34.0%, INFERIOR (TOP200)
- `-rank(free_cash_flow_per_share)`: S=0.05, F=0.01, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(free_cash_flow_per_share, 5))`: S=0.58, F=0.17, T=36.9%, INFERIOR (TOP3000)
- `ts_zscore(free_cash_flow_per_share, 22)`: S=0.09, F=0.02, T=39.1%, INFERIOR (TOP3000)
- `ts_mean(free_cash_flow_per_share, 10)`: S=-0.14, F=-0.05, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_rank(free_cash_flow_per_share, 22))`: S=-0.42, F=-0.16, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_per_share)`: S=-0.05, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_per_share / close)`: S=-0.58, F=-0.39, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 19F/10P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.10 (weak), ret=+0.5%
  - 2020: S=-1.17 (negative), ret=-10.3%
  - 2021: S=1.34 (moderate), ret=+12.5%
  - 2022: S=1.75 (strong), ret=+24.1%
  - 2023: S=0.06 (weak), ret=+0.6%

## Risk & Drawdown
- Max drawdown: 16.38% over 764 days (recovered)
- Annualized: return +5.6%, volatility 10.0% (fraction of booksize)
- Hit rate: 49.2% positive days
- Tail shape: skew +0.18, excess kurtosis +1.57

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.59, max 2.59, latest -0.07

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +7.36%; worst month: -3.88%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=3.22
- Sideways: S=0.19
- Bear: S=-2.40

## Negated Direction
Best negated: `rank(-1 * ts_delta(free_cash_flow_per_share, 5))` S=0.58, F=0.17, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * free_cash_flow_per_share)`: S=-0.05, F=-0.01, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * free_cash_flow_per_share / close)`: S=-0.58, F=-0.39, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(free_cash_flow_per_share, 5))`: S=0.58, F=0.17, T=36.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(free_cash_flow_per_share / close)` | TOP3000 | 0.56 | 0.39 | 16.4% | 80% | bull-only |
| `rank(free_cash_flow_per_share / close)` | TOP1000 | 0.31 | 0.17 | 20.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- anl4_af_cfps_value: 0.905 (strongly positively correlated)
- anl4_af_eps_value: 0.903 (strongly positively correlated)
- fnd6_oprepsx: 0.894 (strongly positively correlated)
- fnd6_newa2v1300_opeps: 0.892 (strongly positively correlated)
- fnd6_mfma2_opeps: 0.892 (strongly positively correlated)

Redundancy cluster #13: 127 similar fields, mean |rho| 0.82 (representative: anl4_bvps_flag). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
