---
field: min_net_profit_guidance
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.7
best_fitness: 0.3
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 6
max_drawdown: 0.1433
ann_vol: 0.0861
hit_rate: 0.5223
rolling_sharpe_min: -1.453
rolling_sharpe_max: 3.001
redundancy_cluster: 40
negated_best_sharpe: 0.16
negated_best_template: rank_neg_delta
negated_best_fitness: 0.03
n_negated_sims: 10
direction_gap: -0.54
---
# min_net_profit_guidance (analyst4)

*Minimum guidance value for Net Profit on an annual basis*

## Signal Profile
- `rank(min_net_profit_guidance)`: S=0.44, F=0.18, T=1.8%, INFERIOR (TOP1000)
- `rank(min_net_profit_guidance / close)`: S=0.12, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(min_net_profit_guidance, 5))`: S=0.70, F=0.30, T=33.7%, INFERIOR (TOP200)
- `-rank(min_net_profit_guidance)`: S=-0.44, F=-0.18, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_net_profit_guidance, 5))`: S=0.16, F=0.03, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(min_net_profit_guidance, 22)`: S=0.42, F=0.13, T=40.6%, INFERIOR (TOP3000)
- `ts_mean(min_net_profit_guidance, 10)`: S=0.46, F=0.19, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(min_net_profit_guidance, 22))`: S=0.03, F=0.00, T=12.7%, INFERIOR (TOP3000)
- `rank(-1 * min_net_profit_guidance)`: S=-0.05, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * min_net_profit_guidance / close)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 11F/18P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.73, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.38 (weak), ret=+2.7%
  - 2020: S=2.97 (strong), ret=+23.4%
  - 2021: S=-0.71 (negative), ret=-7.1%
  - 2022: S=0.17 (weak), ret=+1.5%
  - 2023: S=1.26 (moderate), ret=+10.3%

## Risk & Drawdown
- Max drawdown: 14.33% over 918 days (recovered)
- Annualized: return +6.3%, volatility 8.6% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.43, excess kurtosis +3.90

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.45, max 3.00, latest 1.38

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.84%; worst month: -5.47%
Positive months: 58%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.58
- Sideways: S=0.27
- Bear: S=2.83

## Negated Direction
Best negated: `rank(-1 * ts_delta(min_net_profit_guidance, 5))` S=0.16, F=0.03, INFERIOR
Direction gap: -0.54 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * min_net_profit_guidance)`: S=-0.05, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * min_net_profit_guidance / close)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(min_net_profit_guidance, 5))`: S=0.16, F=0.03, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(min_net_profit_guidance, 5))` | TOP200 | 0.73 | 0.30 | 14.3% | 80% | bear-only |
| `rank(min_net_profit_guidance)` | TOP1000 | 0.45 | 0.18 | 6.5% | 80% | weak |
| `rank(min_net_profit_guidance)` | TOP3000 | 0.47 | 0.17 | 4.7% | 60% | mixed |
| `rank(min_net_profit_guidance / close)` | TOP3000 | 0.12 | 0.04 | 41.4% | 60% | bull-only |
| `rank(min_net_profit_guidance / close)` | TOP1000 | 0.10 | 0.03 | 31.5% | 60% | bull-only |
| `rank(ts_delta(min_net_profit_guidance, 5))` | TOP3000 | 0.17 | 0.02 | 14.6% | 40% | bear-only |

## Correlation Notes
Top correlates:
- net_profit_adjusted_min_guidance: 0.969 (strongly positively correlated)
- max_net_profit_guidance: 0.927 (strongly positively correlated)
- max_adjusted_net_profit_guidance: 0.913 (strongly positively correlated)
- cashflow_per_share_min_guidance: 0.811 (strongly positively correlated)
- cashflow_per_share_max_guidance: 0.811 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
