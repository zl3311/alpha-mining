---
field: pv13_ompetitorgraphrank_hub_rank
dataset: pv13
best_template: ts_mean
best_sharpe: 0.82
best_fitness: 0.78
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 18
regime_profile: mixed
n_variations_with_pnl: 8
max_drawdown: 0.043
ann_vol: 0.0356
hit_rate: 0.5287
rolling_sharpe_min: -1.153
rolling_sharpe_max: 3.241
top_merge_partner: fn_repayments_of_debt_a
negated_best_sharpe: 0.09
negated_best_template: rank_neg_delta
negated_best_fitness: 0.02
n_negated_sims: 4
direction_gap: -0.73
---
# pv13_ompetitorgraphrank_hub_rank (pv13)

*the HITS hub score of competitors*

## Signal Profile
- `rank(pv13_ompetitorgraphrank_hub_rank)`: S=1.15, F=0.65, T=1.4%, INFERIOR (TOP1000)
- `rank(ts_delta(pv13_ompetitorgraphrank_hub_rank, 5))`: S=0.61, F=0.38, T=15.9%, INFERIOR (TOP200)
- `-rank(pv13_ompetitorgraphrank_hub_rank)`: S=-1.15, F=-0.65, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_ompetitorgraphrank_hub_rank, 5))`: S=0.09, F=0.02, T=14.4%, INFERIOR (TOP3000)
- `ts_zscore(pv13_ompetitorgraphrank_hub_rank, 22)`: S=0.21, F=0.06, T=18.9%, INFERIOR (TOP3000)
- `ts_mean(pv13_ompetitorgraphrank_hub_rank, 10)`: S=0.82, F=0.78, T=1.9%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_ompetitorgraphrank_hub_rank, 22))`: S=0.20, F=0.04, T=7.1%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ompetitorgraphrank_hub_rank)`: S=-0.16, F=-0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ompetitorgraphrank_hub_rank / close)`: S=-0.22, F=-0.06, T=1.1%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 7F/11P
- LOW_FITNESS: 18F/0P
- LOW_SHARPE: 18F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/7P
- LOW_TURNOVER: 2F/16P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.16, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=-1.07 (negative), ret=-2.5%
  - 2020: S=2.49 (strong), ret=+8.6%
  - 2021: S=2.37 (strong), ret=+9.3%
  - 2022: S=0.11 (weak), ret=+0.5%
  - 2023: S=1.56 (strong), ret=+4.4%

## Risk & Drawdown
- Max drawdown: 4.30% over 144 days (recovered)
- Annualized: return +4.1%, volatility 3.6% (fraction of booksize)
- Hit rate: 52.9% positive days
- Tail shape: skew -0.08, excess kurtosis +1.21

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.15, max 3.24, latest 1.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2019
Best month: +2.84%; worst month: -1.61%
Positive months: 63%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.19
- Sideways: S=1.33
- Bear: S=2.01

## Negated Direction
Best negated: `rank(-1 * ts_delta(pv13_ompetitorgraphrank_hub_rank, 5))` S=0.09, F=0.02, INFERIOR
Direction gap: -0.73 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * pv13_ompetitorgraphrank_hub_rank)`: S=-0.16, F=-0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(-1 * pv13_ompetitorgraphrank_hub_rank / close)`: S=-0.22, F=-0.06, T=1.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_ompetitorgraphrank_hub_rank, 5))`: S=0.09, F=0.02, T=14.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pv13_ompetitorgraphrank_hub_rank)` | TOP1000 | 1.16 | 0.65 | 4.3% | 80% | mixed |
| `rank(ts_delta(pv13_ompetitorgraphrank_hub_rank, 5))` | TOP200 | 0.60 | 0.38 | 12.1% | 100% | mixed |
| `rank(pv13_ompetitorgraphrank_hub_rank)` | TOP500 | 0.64 | 0.28 | 5.6% | 60% | mixed |
| `rank(pv13_ompetitorgraphrank_hub_rank)` | TOP200 | 0.52 | 0.25 | 12.6% | 40% | mixed |
| `rank(ts_delta(pv13_ompetitorgraphrank_hub_rank, 5))` | TOP3000 | 0.32 | 0.13 | 21.1% | 60% | bull-only |
| `rank(ts_delta(pv13_ompetitorgraphrank_hub_rank, 5))` | TOP500 | 0.28 | 0.11 | 20.3% | 80% | bull-only |
| `rank(ts_delta(pv13_ompetitorgraphrank_hub_rank, 5))` | TOP1000 | 0.20 | 0.07 | 21.5% | 80% | bull-only |
| `rank(pv13_ompetitorgraphrank_hub_rank)` | TOP3000 | 0.14 | 0.03 | 4.5% | 40% | bear-only |

## Correlation Notes
Top correlates:
- fnd6_np: -0.373 (weakly negatively correlated)
- anl4_af_cfps_value: -0.347 (weakly negatively correlated)
- anl4_afv4_eps_mean: -0.330 (weakly negatively correlated)
- fnd2_a_curritxexp: -0.327 (weakly negatively correlated)
- anl4_afv4_median_eps: -0.326 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_repayments_of_debt_a | fundamental2 | -0.25 | 1.89 | +0.70 | +0.30 | yes |
| fnd6_dxd5 | fundamental6 | -0.17 | 1.77 | +0.59 | -0.52 | yes |
| fn_taxes_payable_q | fundamental2 | -0.20 | 1.78 | +0.62 | -0.19 | yes |
| fn_repayments_of_debt_q | fundamental2 | -0.25 | 1.78 | +0.62 | -0.16 | yes |
| fn_repayments_of_lt_debt_q | fundamental2 | -0.21 | 1.79 | +0.63 | +0.43 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
