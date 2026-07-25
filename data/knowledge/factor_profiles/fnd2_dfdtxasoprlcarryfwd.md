---
field: fnd2_dfdtxasoprlcarryfwd
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.5
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 7
max_drawdown: 0.103
ann_vol: 0.0685
hit_rate: 0.4915
rolling_sharpe_min: -0.883
rolling_sharpe_max: 2.538
redundancy_cluster: 60
negated_best_sharpe: 0.81
negated_best_template: rank_neg_delta
negated_best_fitness: 0.46
n_negated_sims: 10
direction_gap: 0.04
---
# fnd2_dfdtxasoprlcarryfwd (fundamental2)

*Amount before allocation of valuation allowances of deferred tax asset attributable to deductible operating loss carryforwards.*

## Signal Profile
- `rank(fnd2_dfdtxasoprlcarryfwd)`: S=0.83, F=0.44, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_dfdtxasoprlcarryfwd / close)`: S=0.77, F=0.50, T=1.7%, INFERIOR (TOP500)
- `rank(ts_delta(fnd2_dfdtxasoprlcarryfwd, 5))`: S=-0.22, F=-0.07, T=33.9%, INFERIOR (TOP500)
- `-rank(fnd2_dfdtxasoprlcarryfwd)`: S=-0.71, F=-0.37, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxasoprlcarryfwd, 5))`: S=0.81, F=0.46, T=34.5%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_dfdtxasoprlcarryfwd, 63)`: S=0.13, F=0.04, T=16.9%, INFERIOR (TOP3000)
- `ts_mean(fnd2_dfdtxasoprlcarryfwd, 10)`: S=0.72, F=0.46, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_dfdtxasoprlcarryfwd, 22))`: S=-0.66, F=-0.43, T=15.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxasoprlcarryfwd)`: S=-0.83, F=-0.44, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxasoprlcarryfwd / close)`: S=-0.40, F=-0.20, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P
- LOW_TURNOVER: 4F/28P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.79, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.95 (strong), ret=+8.0%
  - 2020: S=1.59 (strong), ret=+10.6%
  - 2021: S=-0.19 (negative), ret=-1.3%
  - 2022: S=0.08 (weak), ret=+0.7%
  - 2023: S=1.24 (moderate), ret=+8.5%

## Risk & Drawdown
- Max drawdown: 10.30% over 935 days (not yet recovered, ongoing at window end)
- Annualized: return +5.4%, volatility 6.9% (fraction of booksize)
- Hit rate: 49.1% positive days
- Tail shape: skew +0.29, excess kurtosis +1.19

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.88, max 2.54, latest 1.37

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +4.61%; worst month: -3.67%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.38
- Sideways: S=0.03
- Bear: S=2.03

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_dfdtxasoprlcarryfwd, 5))` S=0.81, F=0.46, INFERIOR
Direction gap: +0.04 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd2_dfdtxasoprlcarryfwd)`: S=-0.83, F=-0.44, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxasoprlcarryfwd / close)`: S=-0.40, F=-0.20, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxasoprlcarryfwd, 5))`: S=0.81, F=0.46, T=34.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_dfdtxasoprlcarryfwd / close)` | TOP500 | 0.79 | 0.50 | 10.3% | 80% | mixed |
| `rank(fnd2_dfdtxasoprlcarryfwd)` | TOP3000 | 0.83 | 0.44 | 5.3% | 100% | mixed |
| `rank(fnd2_dfdtxasoprlcarryfwd)` | TOP500 | 0.79 | 0.44 | 7.6% | 80% | mixed |
| `rank(fnd2_dfdtxasoprlcarryfwd)` | TOP1000 | 0.72 | 0.37 | 8.8% | 80% | mixed |
| `rank(fnd2_dfdtxasoprlcarryfwd / close)` | TOP1000 | 0.50 | 0.25 | 12.9% | 80% | mixed |
| `rank(fnd2_dfdtxasoprlcarryfwd / close)` | TOP3000 | 0.40 | 0.20 | 20.0% | 80% | bear-only |
| `rank(fnd2_dfdtxasoprlcarryfwd / close)` | TOP200 | 0.23 | 0.08 | 25.4% | 60% | mixed |

## Correlation Notes
Top correlates:
- anl4_fcf_number: 0.738 (strongly positively correlated)
- fn_entity_common_stock_shares_out_q: 0.729 (strongly positively correlated)
- anl4_afv4_cfps_number: 0.712 (strongly positively correlated)
- fnd6_newqv1300_cshoq: 0.710 (strongly positively correlated)
- fnd6_mfmq_cshprq: 0.710 (strongly positively correlated)

Redundancy cluster #60: 3 similar fields, mean |rho| 0.722 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
