---
field: fn_repayments_of_debt_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 1.2
best_fitness: 0.8
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 9
max_drawdown: 0.0467
ann_vol: 0.0464
hit_rate: 0.5134
rolling_sharpe_min: -1.124
rolling_sharpe_max: 2.767
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.72
negated_best_template: rank_neg_delta
negated_best_fitness: 0.5
n_negated_sims: 10
direction_gap: -0.48
---
# fn_repayments_of_debt_a (fundamental2)

*The cash outflow during the period from the repayment of aggregate short-term and long-term debt. Excludes payment of capital lease obligations.*

## Signal Profile
- `rank(fn_repayments_of_debt_a)`: S=0.79, F=0.47, T=1.0%, INFERIOR (TOP3000)
- `rank(fn_repayments_of_debt_a / close)`: S=1.20, F=0.80, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_repayments_of_debt_a, 5))`: S=0.43, F=0.18, T=34.3%, INFERIOR (TOP1000)
- `-rank(fn_repayments_of_debt_a)`: S=-0.59, F=-0.32, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_debt_a, 5))`: S=0.72, F=0.50, T=28.6%, INFERIOR (TOP3000)
- `-ts_zscore(fn_repayments_of_debt_a, 63)`: S=-0.08, F=-0.02, T=15.8%, INFERIOR (TOP3000)
- `ts_mean(fn_repayments_of_debt_a, 10)`: S=0.00, F=0.00, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_repayments_of_debt_a, 22))`: S=0.43, F=0.22, T=14.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_debt_a)`: S=0.01, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_debt_a / close)`: S=-0.07, F=-0.02, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P
- LOW_TURNOVER: 1F/31P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.19, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.36 (weak), ret=+1.1%
  - 2020: S=0.74 (moderate), ret=+4.6%
  - 2021: S=1.84 (strong), ret=+9.4%
  - 2022: S=1.94 (strong), ret=+8.6%
  - 2023: S=1.15 (moderate), ret=+3.3%

## Risk & Drawdown
- Max drawdown: 4.67% over 212 days (recovered)
- Annualized: return +5.5%, volatility 4.6% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.57, excess kurtosis +3.04

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.12, max 2.77, latest 1.19

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2019
Best month: +4.00%; worst month: -3.06%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.87
- Sideways: S=0.62
- Bear: S=-0.07

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_repayments_of_debt_a, 5))` S=0.72, F=0.50, INFERIOR
Direction gap: -0.48 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_repayments_of_debt_a)`: S=0.01, F=0.00, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_repayments_of_debt_a / close)`: S=-0.07, F=-0.02, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_repayments_of_debt_a, 5))`: S=0.72, F=0.50, T=28.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_repayments_of_debt_a / close)` | TOP3000 | 1.19 | 0.80 | 4.7% | 100% | mixed |
| `rank(fn_repayments_of_debt_a / close)` | TOP1000 | 0.96 | 0.65 | 6.0% | 100% | mixed |
| `rank(fn_repayments_of_debt_a)` | TOP3000 | 0.78 | 0.47 | 11.5% | 80% | bull-only |
| `rank(fn_repayments_of_debt_a)` | TOP1000 | 0.59 | 0.32 | 12.1% | 60% | bull-only |
| `rank(fn_repayments_of_debt_a / close)` | TOP500 | 0.43 | 0.22 | 14.6% | 60% | bull-only |
| `rank(ts_delta(fn_repayments_of_debt_a, 5))` | TOP1000 | 0.41 | 0.18 | 28.9% | 80% | bull-only |
| `rank(ts_delta(fn_repayments_of_debt_a, 5))` | TOP500 | 0.09 | 0.03 | 55.9% | 60% | bull-only |
| `rank(fn_repayments_of_debt_a)` | TOP500 | 0.11 | 0.03 | 23.7% | 40% | bull-only |
| `rank(fn_repayments_of_debt_a / close)` | TOP200 | 0.07 | 0.02 | 24.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_interest_paid_net_a: 0.906 (strongly positively correlated)
- fnd6_intpn: 0.895 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.886 (strongly positively correlated)
- fnd6_newa2v1300_xint: 0.885 (strongly positively correlated)
- fnd6_newa1v1300_cogs: 0.884 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.37 | 1.85 | +0.67 | -0.52 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.25 | 1.89 | +0.70 | +0.30 | yes |
| anl4_cfo_flag | analyst4 | -0.10 | 1.68 | +0.49 | -0.99 | yes |
| anl4_totassets_number | analyst4 | -0.07 | 1.72 | +0.53 | -0.33 | yes |
| anl4_qfd1_az_wol_spfc | analyst4 | -0.02 | 1.89 | +0.44 | -0.79 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
