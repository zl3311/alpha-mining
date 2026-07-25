---
field: total_assets_amount
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.58
best_fitness: 0.35
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 4
max_drawdown: 0.1116
ann_vol: 0.0804
hit_rate: 0.4883
rolling_sharpe_min: -0.729
rolling_sharpe_max: 1.931
redundancy_cluster: 1
negated_best_sharpe: 0.59
negated_best_template: rank_neg_delta
negated_best_fitness: 0.22
n_negated_sims: 10
direction_gap: 0.01
---
# total_assets_amount (analyst4)

*Total Assets - actual value*

## Signal Profile
- `rank(total_assets_amount)`: S=0.47, F=0.30, T=1.1%, INFERIOR (TOP3000)
- `rank(total_assets_amount / close)`: S=0.58, F=0.35, T=1.5%, INFERIOR (TOP3000)
- `rank(ts_delta(total_assets_amount, 5))`: S=-0.07, F=-0.01, T=36.3%, INFERIOR (TOP1000)
- `-rank(total_assets_amount)`: S=-0.14, F=-0.05, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(total_assets_amount, 5))`: S=0.59, F=0.22, T=34.3%, INFERIOR (TOP3000)
- `-ts_zscore(total_assets_amount, 63)`: S=0.12, F=0.02, T=22.1%, INFERIOR (TOP3000)
- `ts_mean(total_assets_amount, 10)`: S=-0.12, F=-0.04, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(total_assets_amount, 22))`: S=-0.07, F=-0.01, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * total_assets_amount)`: S=0.20, F=0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * total_assets_amount / close)`: S=0.09, F=0.03, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 5F/27P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.58, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.01 (negative), ret=-0.0%
  - 2020: S=0.10 (weak), ret=+1.0%
  - 2021: S=0.86 (moderate), ret=+7.9%
  - 2022: S=1.18 (moderate), ret=+9.8%
  - 2023: S=0.72 (moderate), ret=+4.2%

## Risk & Drawdown
- Max drawdown: 11.16% over 245 days (recovered)
- Annualized: return +4.6%, volatility 8.0% (fraction of booksize)
- Hit rate: 48.8% positive days
- Tail shape: skew +0.68, excess kurtosis +3.42

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.73, max 1.93, latest 0.79

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +8.13%; worst month: -3.60%
Positive months: 51%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.63
- Sideways: S=0.10
- Bear: S=-1.44

## Negated Direction
Best negated: `rank(-1 * ts_delta(total_assets_amount, 5))` S=0.59, F=0.22, INFERIOR
Direction gap: +0.01 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * total_assets_amount)`: S=0.20, F=0.10, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * total_assets_amount / close)`: S=0.09, F=0.03, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(total_assets_amount, 5))`: S=0.59, F=0.22, T=34.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(total_assets_amount / close)` | TOP3000 | 0.58 | 0.35 | 11.2% | 80% | bull-only |
| `rank(total_assets_amount)` | TOP3000 | 0.46 | 0.30 | 30.7% | 80% | bull-only |
| `rank(total_assets_amount / close)` | TOP1000 | 0.27 | 0.12 | 16.6% | 60% | bull-only |
| `rank(total_assets_amount)` | TOP1000 | 0.13 | 0.05 | 36.6% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_cptnewqv1300_atq: 0.954 (strongly positively correlated)
- fnd6_newqv1300_lseq: 0.954 (strongly positively correlated)
- assets: 0.954 (strongly positively correlated)
- capital_expenditure_amount: 0.954 (strongly positively correlated)
- fnd6_cptmfmq_atq: 0.954 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
