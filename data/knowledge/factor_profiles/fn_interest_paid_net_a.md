---
field: fn_interest_paid_net_a
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.92
best_fitness: 0.67
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.0709
ann_vol: 0.0725
hit_rate: 0.4915
rolling_sharpe_min: -0.995
rolling_sharpe_max: 2.365
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.15
negated_best_template: neg_rank_level
negated_best_fitness: 0.06
n_negated_sims: 10
direction_gap: -0.77
---
# fn_interest_paid_net_a (fundamental2)

*Net interest*

## Signal Profile
- `rank(fn_interest_paid_net_a)`: S=0.65, F=0.44, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_interest_paid_net_a / close)`: S=0.92, F=0.67, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_interest_paid_net_a, 5))`: S=0.58, F=0.27, T=33.6%, INFERIOR (TOP3000)
- `-rank(fn_interest_paid_net_a)`: S=-0.36, F=-0.20, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_interest_paid_net_a, 5))`: S=-0.38, F=-0.19, T=29.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_interest_paid_net_a, 63)`: S=0.38, F=0.23, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(fn_interest_paid_net_a, 10)`: S=0.02, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_interest_paid_net_a, 22))`: S=-0.14, F=-0.04, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_interest_paid_net_a)`: S=0.15, F=0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_interest_paid_net_a / close)`: S=0.12, F=0.04, T=2.0%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/3P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.92, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.73 (moderate), ret=+3.4%
  - 2020: S=0.73 (moderate), ret=+7.3%
  - 2021: S=1.55 (strong), ret=+12.0%
  - 2022: S=1.40 (moderate), ret=+9.1%
  - 2023: S=0.14 (weak), ret=+0.7%

## Risk & Drawdown
- Max drawdown: 7.09% over 576 days (not yet recovered, ongoing at window end)
- Annualized: return +6.6%, volatility 7.2% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.56, excess kurtosis +3.01

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.99, max 2.37, latest 0.21

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2023
Best month: +6.12%; worst month: -3.20%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.58
- Sideways: S=0.55
- Bear: S=-0.48

## Negated Direction
Best negated: `rank(-1 * fn_interest_paid_net_a)` S=0.15, F=0.06, INFERIOR
Direction gap: -0.77 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fn_interest_paid_net_a)`: S=0.15, F=0.06, T=1.7%, INFERIOR (TOP3000)
- `rank(-1 * fn_interest_paid_net_a / close)`: S=0.12, F=0.04, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_interest_paid_net_a, 5))`: S=-0.38, F=-0.19, T=29.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_interest_paid_net_a / close)` | TOP3000 | 0.92 | 0.67 | 7.1% | 100% | mixed |
| `rank(fn_interest_paid_net_a)` | TOP3000 | 0.64 | 0.44 | 17.3% | 80% | bull-only |
| `rank(fn_interest_paid_net_a / close)` | TOP1000 | 0.55 | 0.36 | 9.2% | 60% | bull-only |
| `rank(ts_delta(fn_interest_paid_net_a, 5))` | TOP3000 | 0.57 | 0.27 | 21.8% | 60% | all-weather |
| `rank(fn_interest_paid_net_a)` | TOP1000 | 0.35 | 0.20 | 24.0% | 60% | bull-only |
| `rank(ts_delta(fn_interest_paid_net_a, 5))` | TOP200 | 0.33 | 0.16 | 56.5% | 60% | bull-only |
| `rank(fn_interest_paid_net_a / close)` | TOP500 | 0.16 | 0.06 | 23.7% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_intpn: 0.968 (strongly positively correlated)
- fnd6_newa2v1300_xint: 0.950 (strongly positively correlated)
- fn_interest_paid_net_q: 0.941 (strongly positively correlated)
- fnd6_newqv1300_xintq: 0.937 (strongly positively correlated)
- interest_expense: 0.937 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.39 | 1.88 | +0.70 | -0.82 | yes |
| rp_ess_revenue | news18 | -0.35 | 1.54 | +0.63 | -0.61 | yes |
| anl4_rd_exp_flag | analyst4 | -0.29 | 1.61 | +0.58 | -0.31 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.20 | 1.46 | +0.52 | -0.63 | yes |
| max_gross_income_guidance_2 | analyst4 | -0.33 | 1.43 | +0.51 | -0.57 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
