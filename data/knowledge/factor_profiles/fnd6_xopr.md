---
field: fnd6_xopr
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.96
best_fitness: 0.75
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.0937
ann_vol: 0.0805
hit_rate: 0.4899
rolling_sharpe_min: -1.288
rolling_sharpe_max: 2.58
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.75
negated_best_template: rank_neg_delta
negated_best_fitness: 0.31
n_negated_sims: 10
direction_gap: -0.21
---
# fnd6_xopr (fundamental6)

*Operating Expenses - Total*

## Signal Profile
- `rank(fnd6_xopr)`: S=0.78, F=0.65, T=1.0%, INFERIOR (TOP3000)
- `rank(fnd6_xopr / close)`: S=0.96, F=0.75, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_xopr, 5))`: S=-0.75, F=-0.31, T=36.1%, INFERIOR (TOP3000)
- `-rank(fnd6_xopr)`: S=-0.41, F=-0.27, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xopr, 5))`: S=0.75, F=0.31, T=36.1%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_xopr, 63)`: S=0.35, F=0.16, T=20.5%, INFERIOR (TOP3000)
- `ts_mean(fnd6_xopr, 10)`: S=0.13, F=0.04, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_xopr, 22))`: S=-0.40, F=-0.18, T=14.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xopr)`: S=-0.78, F=-0.65, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xopr / close)`: S=-0.96, F=-0.75, T=1.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 5F/27P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.95, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.14 (negative), ret=-0.7%
  - 2020: S=0.60 (moderate), ret=+5.9%
  - 2021: S=1.65 (strong), ret=+16.0%
  - 2022: S=1.33 (moderate), ret=+9.9%
  - 2023: S=1.09 (moderate), ret=+6.5%

## Risk & Drawdown
- Max drawdown: 9.37% over 237 days (recovered)
- Annualized: return +7.7%, volatility 8.1% (fraction of booksize)
- Hit rate: 49.0% positive days
- Tail shape: skew +0.69, excess kurtosis +3.14

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.29, max 2.58, latest 1.22

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +8.95%; worst month: -4.12%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.79
- Sideways: S=-0.05
- Bear: S=-0.36

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_xopr, 5))` S=0.75, F=0.31, INFERIOR
Direction gap: -0.21 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd6_xopr)`: S=-0.78, F=-0.65, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_xopr / close)`: S=-0.96, F=-0.75, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_xopr, 5))`: S=0.75, F=0.31, T=36.1%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_xopr / close)` | TOP3000 | 0.95 | 0.75 | 9.4% | 80% | mixed |
| `rank(fnd6_xopr)` | TOP3000 | 0.77 | 0.65 | 28.2% | 80% | bull-only |
| `rank(fnd6_xopr / close)` | TOP1000 | 0.63 | 0.46 | 12.5% | 80% | bull-only |
| `rank(fnd6_xopr / close)` | TOP500 | 0.47 | 0.30 | 20.0% | 80% | bull-only |
| `rank(fnd6_xopr)` | TOP1000 | 0.40 | 0.27 | 32.7% | 60% | bull-only |
| `rank(fnd6_xopr)` | TOP500 | 0.18 | 0.08 | 43.3% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa1v1300_at: 0.977 (strongly positively correlated)
- fnd6_newa1v1300_lse: 0.977 (strongly positively correlated)
- fnd6_mfma1_at: 0.977 (strongly positively correlated)
- fnd6_cptnewqv1300_ltq: 0.969 (strongly positively correlated)
- liabilities: 0.969 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.37 | 1.90 | +0.72 | -0.43 | yes |
| rp_ess_revenue | news18 | -0.34 | 1.58 | +0.63 | -0.58 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.27 | 1.43 | +0.47 | -0.96 | yes |
| max_gross_income_guidance | analyst4 | -0.20 | 1.43 | +0.48 | -0.76 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.14 | 1.45 | +0.49 | -0.47 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
