---
field: est_tot_assets
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.73
best_fitness: 0.48
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0803
ann_vol: 0.0738
hit_rate: 0.4874
rolling_sharpe_min: -0.986
rolling_sharpe_max: 2.519
redundancy_cluster: 1
negated_best_sharpe: 0.35
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.38
---
# est_tot_assets (analyst4)

*Total Assets - mean of estimations*

## Signal Profile
- `rank(est_tot_assets)`: S=0.56, F=0.39, T=0.9%, INFERIOR (TOP3000)
- `rank(est_tot_assets / close)`: S=0.73, F=0.48, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(est_tot_assets, 5))`: S=0.86, F=0.43, T=35.1%, INFERIOR (TOP200)
- `-rank(est_tot_assets)`: S=-0.26, F=-0.13, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_tot_assets, 5))`: S=0.35, F=0.09, T=36.8%, INFERIOR (TOP3000)
- `ts_zscore(est_tot_assets, 22)`: S=0.06, F=0.01, T=34.7%, INFERIOR (TOP3000)
- `ts_mean(est_tot_assets, 10)`: S=0.08, F=0.02, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(est_tot_assets, 22))`: S=-0.47, F=-0.17, T=13.6%, INFERIOR (TOP3000)
- `rank(-1 * est_tot_assets)`: S=-0.14, F=-0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * est_tot_assets / close)`: S=-0.32, F=-0.17, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 1F/31P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 22F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.72, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.03 (weak), ret=+0.2%
  - 2020: S=0.31 (weak), ret=+2.8%
  - 2021: S=1.52 (strong), ret=+13.4%
  - 2022: S=0.98 (moderate), ret=+6.5%
  - 2023: S=0.59 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 8.03% over 490 days (recovered)
- Annualized: return +5.3%, volatility 7.4% (fraction of booksize)
- Hit rate: 48.7% positive days
- Tail shape: skew +0.69, excess kurtosis +3.27

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 2.52, latest 0.69

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +7.51%; worst month: -3.41%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.66
- Sideways: S=0.16
- Bear: S=-1.02

## Negated Direction
Best negated: `rank(-1 * ts_delta(est_tot_assets, 5))` S=0.35, F=0.09, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * est_tot_assets)`: S=-0.14, F=-0.05, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * est_tot_assets / close)`: S=-0.32, F=-0.17, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(est_tot_assets, 5))`: S=0.35, F=0.09, T=36.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(est_tot_assets / close)` | TOP3000 | 0.72 | 0.48 | 8.0% | 100% | bull-only |
| `rank(ts_delta(est_tot_assets, 5))` | TOP200 | 0.87 | 0.43 | 11.8% | 100% | mixed |
| `rank(est_tot_assets)` | TOP3000 | 0.56 | 0.39 | 30.8% | 80% | bull-only |
| `rank(est_tot_assets / close)` | TOP1000 | 0.39 | 0.21 | 14.6% | 60% | bull-only |
| `rank(ts_delta(est_tot_assets, 5))` | TOP3000 | 0.70 | 0.19 | 5.6% | 100% | mixed |
| `rank(est_tot_assets / close)` | TOP500 | 0.32 | 0.17 | 23.1% | 80% | bull-only |
| `rank(est_tot_assets)` | TOP1000 | 0.25 | 0.13 | 32.8% | 60% | bull-only |
| `rank(est_tot_assets)` | TOP500 | 0.13 | 0.05 | 46.8% | 60% | bull-only |
| `rank(ts_delta(est_tot_assets, 5))` | TOP1000 | 0.23 | 0.04 | 14.2% | 60% | mixed |

## Correlation Notes
Top correlates:
- fnd6_mfma1_at: 0.980 (strongly positively correlated)
- fnd6_cptnewqv1300_atq: 0.980 (strongly positively correlated)
- fnd6_newqv1300_lseq: 0.980 (strongly positively correlated)
- assets: 0.980 (strongly positively correlated)
- fnd6_cptmfmq_atq: 0.980 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
