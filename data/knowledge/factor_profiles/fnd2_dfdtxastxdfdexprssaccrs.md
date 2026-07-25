---
field: fnd2_dfdtxastxdfdexprssaccrs
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.8
best_fitness: 0.73
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0634
ann_vol: 0.0618
hit_rate: 0.4931
rolling_sharpe_min: -1.304
rolling_sharpe_max: 2.532
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.71
negated_best_template: rank_neg_delta
negated_best_fitness: 0.5
n_negated_sims: 10
direction_gap: -0.09
---
# fnd2_dfdtxastxdfdexprssaccrs (fundamental2)

*Amount before allocation of valuation allowances of deferred tax asset attributable to deductible temporary differences from reserves and accruals.*

## Signal Profile
- `rank(fnd2_dfdtxastxdfdexprssaccrs)`: S=0.72, F=0.49, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_dfdtxastxdfdexprssaccrs / close)`: S=0.88, F=0.58, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_dfdtxastxdfdexprssaccrs, 5))`: S=0.18, F=0.05, T=34.3%, INFERIOR (TOP3000)
- `-rank(fnd2_dfdtxastxdfdexprssaccrs)`: S=-0.38, F=-0.21, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxastxdfdexprssaccrs, 5))`: S=0.71, F=0.50, T=29.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_dfdtxastxdfdexprssaccrs, 63)`: S=0.80, F=0.73, T=16.0%, INFERIOR (TOP3000)
- `ts_mean(fnd2_dfdtxastxdfdexprssaccrs, 10)`: S=0.36, F=0.17, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_dfdtxastxdfdexprssaccrs, 22))`: S=-0.21, F=-0.08, T=15.1%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxastxdfdexprssaccrs)`: S=0.35, F=0.21, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxastxdfdexprssaccrs / close)`: S=0.22, F=0.09, T=2.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.87, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-0.06 (negative), ret=-0.2%
  - 2020: S=0.98 (moderate), ret=+8.1%
  - 2021: S=1.59 (strong), ret=+10.6%
  - 2022: S=1.38 (moderate), ret=+7.4%
  - 2023: S=0.12 (weak), ret=+0.6%

## Risk & Drawdown
- Max drawdown: 6.34% over 456 days (recovered)
- Annualized: return +5.4%, volatility 6.2% (fraction of booksize)
- Hit rate: 49.3% positive days
- Tail shape: skew +0.68, excess kurtosis +4.40

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.30, max 2.53, latest 0.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2019
Best month: +6.05%; worst month: -3.14%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.42
- Sideways: S=-0.05
- Bear: S=-0.02

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_dfdtxastxdfdexprssaccrs, 5))` S=0.71, F=0.50, INFERIOR
Direction gap: -0.09 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_dfdtxastxdfdexprssaccrs)`: S=0.35, F=0.21, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxastxdfdexprssaccrs / close)`: S=0.22, F=0.09, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxastxdfdexprssaccrs, 5))`: S=0.71, F=0.50, T=29.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_dfdtxastxdfdexprssaccrs / close)` | TOP3000 | 0.87 | 0.58 | 6.3% | 80% | mixed |
| `rank(fnd2_dfdtxastxdfdexprssaccrs)` | TOP3000 | 0.72 | 0.49 | 17.8% | 80% | bull-only |
| `rank(fnd2_dfdtxastxdfdexprssaccrs / close)` | TOP1000 | 0.52 | 0.31 | 9.4% | 40% | bull-only |
| `rank(fnd2_dfdtxastxdfdexprssaccrs)` | TOP1000 | 0.37 | 0.21 | 23.3% | 40% | bull-only |
| `rank(fnd2_dfdtxastxdfdexprssaccrs / close)` | TOP500 | 0.27 | 0.12 | 20.5% | 60% | bull-only |
| `rank(ts_delta(fnd2_dfdtxastxdfdexprssaccrs, 5))` | TOP3000 | 0.17 | 0.05 | 23.7% | 40% | bear-only |
| `rank(fnd2_dfdtxastxdfdexprssaccrs)` | TOP500 | 0.12 | 0.04 | 30.0% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_xopr: 0.919 (strongly positively correlated)
- fn_op_lease_rent_exp_a: 0.917 (strongly positively correlated)
- fn_employee_related_liab_a: 0.909 (strongly positively correlated)
- fnd6_newa1v1300_at: 0.903 (strongly positively correlated)
- fnd6_newa1v1300_lse: 0.903 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.37 | 1.79 | +0.61 | -0.57 | yes |
| rp_ess_revenue | news18 | -0.32 | 1.44 | +0.55 | -0.40 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.28 | 1.31 | +0.44 | -0.86 | yes |
| min_gross_income_guidance | analyst4 | -0.23 | 1.33 | +0.46 | -0.58 | yes |
| max_gross_income_guidance | analyst4 | -0.23 | 1.34 | +0.46 | -0.57 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
