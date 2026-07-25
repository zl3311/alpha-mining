---
field: max_net_profit_guidance
dataset: analyst4
best_template: rank_delta
best_sharpe: 0.67
best_fitness: 0.29
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bear-only
n_variations_with_pnl: 4
max_drawdown: 0.1086
ann_vol: 0.0921
hit_rate: 0.5142
rolling_sharpe_min: -0.987
rolling_sharpe_max: 3.145
redundancy_cluster: 40
negated_best_sharpe: 0.12
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 10
direction_gap: -0.55
---
# max_net_profit_guidance (analyst4)

*The maximum guidance value for net profit on an annual basis.*

## Signal Profile
- `rank(max_net_profit_guidance)`: S=0.44, F=0.18, T=1.8%, INFERIOR (TOP1000)
- `rank(max_net_profit_guidance / close)`: S=0.12, F=0.04, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(max_net_profit_guidance, 5))`: S=0.67, F=0.29, T=33.6%, INFERIOR (TOP200)
- `-rank(max_net_profit_guidance)`: S=-0.44, F=-0.18, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_net_profit_guidance, 5))`: S=0.12, F=0.02, T=36.1%, INFERIOR (TOP3000)
- `-ts_zscore(max_net_profit_guidance, 63)`: S=0.35, F=0.11, T=21.2%, INFERIOR (TOP3000)
- `ts_mean(max_net_profit_guidance, 10)`: S=0.47, F=0.20, T=2.0%, INFERIOR (TOP3000)
- `rank(ts_rank(max_net_profit_guidance, 22))`: S=-0.07, F=-0.01, T=12.6%, INFERIOR (TOP3000)
- `rank(-1 * max_net_profit_guidance)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * max_net_profit_guidance / close)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 3F/29P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/15P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.70, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.24 (weak), ret=+1.7%
  - 2020: S=3.14 (strong), ret=+26.0%
  - 2021: S=-0.32 (negative), ret=-3.4%
  - 2022: S=0.16 (weak), ret=+1.5%
  - 2023: S=0.63 (moderate), ret=+5.7%

## Risk & Drawdown
- Max drawdown: 10.86% over 800 days (recovered)
- Annualized: return +6.4%, volatility 9.2% (fraction of booksize)
- Hit rate: 51.4% positive days
- Tail shape: skew +0.55, excess kurtosis +4.25

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 3.15, latest 0.74

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2021
Best month: +5.72%; worst month: -5.36%
Positive months: 54%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.61
- Sideways: S=0.51
- Bear: S=2.48

## Negated Direction
Best negated: `rank(-1 * ts_delta(max_net_profit_guidance, 5))` S=0.12, F=0.02, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * max_net_profit_guidance)`: S=-0.06, F=-0.01, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * max_net_profit_guidance / close)`: S=0.02, F=0.00, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(max_net_profit_guidance, 5))`: S=0.12, F=0.02, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(max_net_profit_guidance, 5))` | TOP200 | 0.70 | 0.29 | 10.9% | 80% | bear-only |
| `rank(max_net_profit_guidance)` | TOP1000 | 0.46 | 0.18 | 6.8% | 80% | weak |
| `rank(max_net_profit_guidance)` | TOP3000 | 0.48 | 0.17 | 4.8% | 60% | mixed |
| `rank(max_net_profit_guidance / close)` | TOP3000 | 0.12 | 0.04 | 42.2% | 60% | bull-only |

## Correlation Notes
Top correlates:
- max_adjusted_net_profit_guidance: 0.982 (strongly positively correlated)
- min_net_profit_guidance: 0.927 (strongly positively correlated)
- net_profit_adjusted_min_guidance: 0.911 (strongly positively correlated)
- cashflow_per_share_max_guidance: 0.910 (strongly positively correlated)
- cashflow_per_share_min_guidance: 0.910 (strongly positively correlated)

Redundancy cluster #40: 20 similar fields, mean |rho| 0.904 (representative: net_profit_adjusted_min_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
