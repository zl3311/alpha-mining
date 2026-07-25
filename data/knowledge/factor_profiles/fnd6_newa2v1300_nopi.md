---
field: fnd6_newa2v1300_nopi
dataset: fundamental6
best_template: rank_delta
best_sharpe: 0.56
best_fitness: 0.3
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.3895
ann_vol: 0.1868
hit_rate: 0.5231
rolling_sharpe_min: -1.124
rolling_sharpe_max: 2.141
redundancy_cluster: 16
negated_best_sharpe: 0.45
negated_best_template: neg_rank_level
negated_best_fitness: 0.27
n_negated_sims: 10
direction_gap: -0.11
---
# fnd6_newa2v1300_nopi (fundamental6)

*Nonoperating Income (Expense)*

## Signal Profile
- `rank(fnd6_newa2v1300_nopi)`: S=0.13, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_newa2v1300_nopi / close)`: S=0.31, F=0.09, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_newa2v1300_nopi, 5))`: S=0.56, F=0.30, T=35.5%, INFERIOR (TOP200)
- `-rank(fnd6_newa2v1300_nopi)`: S=0.20, F=0.06, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_nopi, 5))`: S=-0.67, F=-0.40, T=35.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newa2v1300_nopi, 22)`: S=0.04, F=0.01, T=30.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newa2v1300_nopi, 10)`: S=-0.16, F=-0.05, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newa2v1300_nopi, 22))`: S=0.12, F=0.03, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_nopi)`: S=0.45, F=0.27, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_nopi / close)`: S=0.25, F=0.11, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.13 (weak), ret=+1.7%
  - 2020: S=-0.40 (negative), ret=-6.6%
  - 2021: S=1.63 (strong), ret=+37.3%
  - 2022: S=0.05 (weak), ret=+1.1%
  - 2023: S=1.16 (moderate), ret=+18.0%

## Risk & Drawdown
- Max drawdown: 38.95% over 494 days (not yet recovered, ongoing at window end)
- Annualized: return +10.5%, volatility 18.7% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew +0.08, excess kurtosis +4.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 2.14, latest 1.14

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +17.47%; worst month: -13.17%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.21
- Sideways: S=0.52
- Bear: S=0.99

## Negated Direction
Best negated: `rank(-1 * fnd6_newa2v1300_nopi)` S=0.45, F=0.27, INFERIOR
Direction gap: -0.11 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_newa2v1300_nopi)`: S=0.45, F=0.27, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newa2v1300_nopi / close)`: S=0.25, F=0.11, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newa2v1300_nopi, 5))`: S=-0.67, F=-0.40, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_newa2v1300_nopi, 5))` | TOP200 | 0.56 | 0.30 | 39.0% | 80% | mixed |
| `rank(fnd6_newa2v1300_nopi / close)` | TOP3000 | 0.31 | 0.09 | 7.2% | 40% | bull-only |
| `rank(fnd6_newa2v1300_nopi)` | TOP3000 | 0.14 | 0.03 | 17.5% | 60% | bull-only |
| `rank(ts_delta(fnd6_newa2v1300_nopi, 5))` | TOP3000 | 0.09 | 0.02 | 12.4% | 40% | weak |

## Correlation Notes
Top correlates:
- fnd6_nopio: 0.732 (strongly positively correlated)
- fnd6_ibmii: 0.186 (weakly positively correlated)
- fnd6_newa2v1300_pi: 0.164 (weakly positively correlated)
- fnd6_ivao: 0.153 (weakly positively correlated)
- fnd6_newa1v1300_ibcom: 0.149 (weakly positively correlated)

Redundancy cluster #16: 2 similar fields, mean |rho| 0.732 (representative: fnd6_nopio). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
