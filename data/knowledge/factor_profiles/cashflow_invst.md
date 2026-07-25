---
field: cashflow_invst
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.79
best_fitness: 0.5
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 36
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.2129
ann_vol: 0.1732
hit_rate: 0.5279
rolling_sharpe_min: -0.533
rolling_sharpe_max: 2.28
redundancy_cluster: 59
negated_best_sharpe: 0.57
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.32
n_negated_sims: 10
direction_gap: -0.22
---
# cashflow_invst (fundamental6)

*Investing Activities - Net Cash Flow*

## Signal Profile
- `rank(cashflow_invst)`: S=0.33, F=0.16, T=2.4%, INFERIOR (TOP200)
- `rank(cashflow_invst / close)`: S=0.27, F=0.12, T=2.5%, INFERIOR (TOP200)
- `rank(ts_delta(cashflow_invst, 5))`: S=0.79, F=0.50, T=33.7%, INFERIOR (TOP500)
- `ts_decay_linear(rank(cashflow_invst), 5)`: S=-0.43, F=-0.19, T=1.4%, INFERIOR (TOP3000)
- `-rank(cashflow_invst)`: S=0.20, F=0.07, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_invst, 5))`: S=-0.69, F=-0.41, T=33.9%, INFERIOR (TOP3000)
- `-ts_zscore(cashflow_invst, 63)`: S=-0.09, F=-0.02, T=17.9%, INFERIOR (TOP3000)
- `ts_mean(cashflow_invst, 10)`: S=-0.10, F=-0.02, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_rank(cashflow_invst, 22))`: S=-0.52, F=-0.26, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_invst)`: S=0.27, F=0.11, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_invst / close)`: S=0.57, F=0.32, T=2.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/23P
- LOW_FITNESS: 36F/0P
- LOW_SHARPE: 36F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/18P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.80, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.91 (moderate), ret=+11.7%
  - 2020: S=1.24 (moderate), ret=+21.4%
  - 2021: S=-0.11 (negative), ret=-2.0%
  - 2022: S=1.32 (moderate), ret=+27.9%
  - 2023: S=0.65 (moderate), ret=+8.5%

## Risk & Drawdown
- Max drawdown: 21.29% over 341 days (recovered)
- Annualized: return +13.8%, volatility 17.3% (fraction of booksize)
- Hit rate: 52.8% positive days
- Tail shape: skew +0.30, excess kurtosis +4.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.53, max 2.28, latest 0.67

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2021
Best month: +12.68%; worst month: -7.57%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.18
- Sideways: S=1.62
- Bear: S=0.67

## Negated Direction
Best negated: `rank(-1 * cashflow_invst / close)` S=0.57, F=0.32, INFERIOR
Direction gap: -0.22 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * cashflow_invst)`: S=0.27, F=0.11, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * cashflow_invst / close)`: S=0.57, F=0.32, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(cashflow_invst, 5))`: S=-0.69, F=-0.41, T=33.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(cashflow_invst, 5))` | TOP500 | 0.80 | 0.50 | 21.3% | 80% | mixed |
| `rank(ts_delta(cashflow_invst, 5))` | TOP200 | 0.53 | 0.31 | 34.6% | 60% | weak |
| `rank(ts_delta(cashflow_invst, 5))` | TOP3000 | 0.70 | 0.29 | 14.6% | 80% | mixed |
| `rank(cashflow_invst)` | TOP200 | 0.35 | 0.16 | 26.3% | 80% | bear-only |
| `rank(cashflow_invst / close)` | TOP200 | 0.29 | 0.12 | 19.3% | 20% | bear-only |
| `rank(ts_delta(cashflow_invst, 5))` | TOP1000 | 0.32 | 0.10 | 24.3% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_ivncf: 0.987 (strongly positively correlated)
- fnd6_ivstch: 0.324 (weakly positively correlated)
- fnd6_optca: 0.199 (weakly positively correlated)
- fnd2_dfdfritxexp: 0.174 (weakly positively correlated)
- fnd6_ivst: -0.157 (weakly negatively correlated)

Redundancy cluster #59: 2 similar fields, mean |rho| 0.987 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
