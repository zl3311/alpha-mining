---
field: net_debt_amount
dataset: analyst4
best_template: rank_value_norm
best_sharpe: 0.9
best_fitness: 0.68
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.1074
ann_vol: 0.0801
hit_rate: 0.5166
rolling_sharpe_min: -0.527
rolling_sharpe_max: 3.272
top_merge_partner: anl4_rd_exp_flag
redundancy_cluster: 1
negated_best_sharpe: 0.38
negated_best_template: rank_neg_delta
negated_best_fitness: 0.08
n_negated_sims: 10
direction_gap: -0.52
---
# net_debt_amount (analyst4)

*Net debt - actual value for the annual period*

## Signal Profile
- `rank(net_debt_amount)`: S=0.43, F=0.23, T=0.9%, INFERIOR (TOP3000)
- `rank(net_debt_amount / close)`: S=0.90, F=0.68, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(net_debt_amount, 5))`: S=0.13, F=0.02, T=36.9%, INFERIOR (TOP500)
- `-rank(net_debt_amount)`: S=-0.36, F=-0.18, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_debt_amount, 5))`: S=0.38, F=0.08, T=36.4%, INFERIOR (TOP3000)
- `ts_zscore(net_debt_amount, 22)`: S=0.49, F=0.17, T=39.6%, INFERIOR (TOP3000)
- `ts_mean(net_debt_amount, 10)`: S=0.29, F=0.12, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_rank(net_debt_amount, 22))`: S=0.18, F=0.04, T=13.4%, INFERIOR (TOP3000)
- `rank(-1 * net_debt_amount)`: S=-0.43, F=-0.23, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * net_debt_amount / close)`: S=-0.90, F=-0.68, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/30P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/13P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.89, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.68 (moderate), ret=+2.6%
  - 2020: S=0.24 (weak), ret=+1.9%
  - 2021: S=2.01 (strong), ret=+16.0%
  - 2022: S=1.06 (moderate), ret=+12.5%
  - 2023: S=0.40 (weak), ret=+2.1%

## Risk & Drawdown
- Max drawdown: 10.74% over 597 days (not yet recovered, ongoing at window end)
- Annualized: return +7.2%, volatility 8.0% (fraction of booksize)
- Hit rate: 51.7% positive days
- Tail shape: skew +0.02, excess kurtosis +2.20

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.53, max 3.27, latest 0.22

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +5.96%; worst month: -3.56%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.95
- Sideways: S=0.87
- Bear: S=-1.60

## Negated Direction
Best negated: `rank(-1 * ts_delta(net_debt_amount, 5))` S=0.38, F=0.08, INFERIOR
Direction gap: -0.52 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * net_debt_amount)`: S=-0.43, F=-0.23, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * net_debt_amount / close)`: S=-0.90, F=-0.68, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(net_debt_amount, 5))`: S=0.38, F=0.08, T=36.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(net_debt_amount / close)` | TOP3000 | 0.89 | 0.68 | 10.7% | 100% | bull-only |
| `rank(net_debt_amount / close)` | TOP1000 | 0.69 | 0.46 | 8.6% | 80% | bull-only |
| `rank(net_debt_amount / close)` | TOP500 | 0.57 | 0.34 | 9.7% | 40% | bull-only |
| `rank(net_debt_amount)` | TOP3000 | 0.42 | 0.23 | 14.5% | 60% | bull-only |
| `rank(net_debt_amount)` | TOP1000 | 0.35 | 0.18 | 12.0% | 60% | bull-only |
| `rank(net_debt_amount / close)` | TOP200 | 0.32 | 0.16 | 9.9% | 40% | bull-only |
| `rank(net_debt_amount)` | TOP500 | 0.24 | 0.10 | 17.5% | 60% | bull-only |
| `rank(net_debt_amount)` | TOP200 | 0.23 | 0.10 | 11.3% | 40% | bull-only |
| `rank(ts_delta(net_debt_amount, 5))` | TOP500 | 0.12 | 0.02 | 10.9% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dxd2: 0.893 (strongly positively correlated)
- fnd6_dd2: 0.891 (strongly positively correlated)
- fnd6_dd3: 0.879 (strongly positively correlated)
- fnd6_dxd3: 0.876 (strongly positively correlated)
- fnd6_dn: 0.875 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.50 | 1.89 | +0.87 | -0.43 | no |
| rp_ess_revenue | news18 | -0.31 | 1.50 | +0.60 | -0.94 | yes |
| news_open_vol | news12 | -0.31 | 1.55 | +0.62 | -0.77 | yes |
| fnd6_txtubadjust | fundamental6 | -0.34 | 1.52 | +0.63 | -0.28 | yes |
| systematic_risk_last_60_days | model51 | -0.20 | 1.37 | +0.47 | -0.82 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
