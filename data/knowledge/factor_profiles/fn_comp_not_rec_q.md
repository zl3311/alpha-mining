---
field: fn_comp_not_rec_q
dataset: fundamental2
best_template: rank_neg_delta
best_sharpe: 0.8
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 5
max_drawdown: 0.1769
ann_vol: 0.0624
hit_rate: 0.5231
rolling_sharpe_min: -2.071
rolling_sharpe_max: 2.547
redundancy_cluster: 17
negated_best_sharpe: 0.8
negated_best_template: rank_neg_delta
negated_best_fitness: 0.58
n_negated_sims: 10
direction_gap: 0.0
---
# fn_comp_not_rec_q (fundamental2)

*Unrecognized cost of unvested share-based compensation awards.*

## Signal Profile
- `rank(fn_comp_not_rec_q)`: S=0.56, F=0.30, T=1.2%, INFERIOR (TOP3000)
- `rank(fn_comp_not_rec_q / close)`: S=0.38, F=0.19, T=1.7%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_comp_not_rec_q, 5))`: S=0.66, F=0.29, T=36.2%, INFERIOR (TOP3000)
- `-rank(fn_comp_not_rec_q)`: S=-0.13, F=-0.04, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_not_rec_q, 5))`: S=0.80, F=0.58, T=34.8%, INFERIOR (TOP3000)
- `-ts_zscore(fn_comp_not_rec_q, 63)`: S=0.80, F=0.49, T=17.6%, INFERIOR (TOP3000)
- `ts_mean(fn_comp_not_rec_q, 10)`: S=-0.04, F=-0.01, T=1.2%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_comp_not_rec_q, 22))`: S=-0.41, F=-0.19, T=16.5%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_not_rec_q)`: S=0.32, F=0.19, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_not_rec_q / close)`: S=0.40, F=0.26, T=2.6%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 13F/19P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 16F/4P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.56, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.98 (moderate), ret=+4.3%
  - 2020: S=-0.46 (negative), ret=-2.8%
  - 2021: S=0.40 (weak), ret=+3.6%
  - 2022: S=1.52 (strong), ret=+7.2%
  - 2023: S=0.93 (moderate), ret=+4.9%

## Risk & Drawdown
- Max drawdown: 17.69% over 888 days (recovered)
- Annualized: return +3.5%, volatility 6.2% (fraction of booksize)
- Hit rate: 52.3% positive days
- Tail shape: skew -0.11, excess kurtosis +2.09

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.07, max 2.55, latest 0.81

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +2.85%; worst month: -4.23%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.69
- Sideways: S=1.48
- Bear: S=-1.34

## Negated Direction
Best negated: `rank(-1 * ts_delta(fn_comp_not_rec_q, 5))` S=0.80, F=0.58, INFERIOR
Direction gap: +0.00 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_comp_not_rec_q)`: S=0.32, F=0.19, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_comp_not_rec_q / close)`: S=0.40, F=0.26, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_comp_not_rec_q, 5))`: S=0.80, F=0.58, T=34.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_comp_not_rec_q)` | TOP3000 | 0.56 | 0.30 | 17.7% | 80% | bull-only |
| `rank(ts_delta(fn_comp_not_rec_q, 5))` | TOP3000 | 0.67 | 0.29 | 18.8% | 80% | mixed |
| `rank(fn_comp_not_rec_q / close)` | TOP3000 | 0.38 | 0.19 | 20.7% | 80% | mixed |
| `rank(fn_comp_not_rec_q / close)` | TOP1000 | 0.37 | 0.17 | 9.4% | 80% | mixed |
| `rank(fn_comp_not_rec_q)` | TOP1000 | 0.13 | 0.04 | 31.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fn_allocated_share_based_compensation_expense_q: 0.876 (strongly positively correlated)
- cash: 0.798 (strongly positively correlated)
- fnd6_newqv1300_xrdq: 0.796 (strongly positively correlated)
- fnd6_fopox: 0.770 (strongly positively correlated)
- fnd6_newa2v1300_wcap: 0.766 (strongly positively correlated)

Redundancy cluster #17: 12 similar fields, mean |rho| 0.768 (representative: fnd6_newqv1300_aol2q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
