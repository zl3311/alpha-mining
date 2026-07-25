---
field: fn_liab_fair_val_l2_a
dataset: fundamental2
best_template: ts_zscore
best_sharpe: 0.82
best_fitness: 0.77
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.0696
ann_vol: 0.0329
hit_rate: 0.5304
rolling_sharpe_min: -1.501
rolling_sharpe_max: 3.564
top_merge_partner: pv13_ompetitorgraphrank_hub_rank
redundancy_cluster: 10
negated_best_sharpe: 0.44
negated_best_template: neg_rank_level
negated_best_fitness: 0.23
n_negated_sims: 10
direction_gap: -0.38
---
# fn_liab_fair_val_l2_a (fundamental2)

*Liabilities Fair Value, Recurring, Level 2*

## Signal Profile
- `rank(fn_liab_fair_val_l2_a)`: S=0.79, F=0.40, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_liab_fair_val_l2_a / close)`: S=1.19, F=0.66, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_liab_fair_val_l2_a, 5))`: S=0.82, F=0.53, T=32.9%, INFERIOR (TOP1000)
- `-rank(fn_liab_fair_val_l2_a)`: S=0.15, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_l2_a, 5))`: S=-0.12, F=-0.03, T=25.8%, INFERIOR (TOP3000)
- `ts_zscore(fn_liab_fair_val_l2_a, 22)`: S=0.82, F=0.77, T=15.9%, INFERIOR (TOP3000)
- `ts_mean(fn_liab_fair_val_l2_a, 10)`: S=0.16, F=0.05, T=0.7%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_liab_fair_val_l2_a, 22))`: S=0.52, F=0.33, T=15.3%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l2_a)`: S=0.44, F=0.23, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l2_a / close)`: S=0.35, F=0.17, T=2.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 1.18, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.10 (strong), ret=+5.0%
  - 2020: S=0.88 (moderate), ret=+3.0%
  - 2021: S=-0.17 (negative), ret=-0.7%
  - 2022: S=1.86 (strong), ret=+5.9%
  - 2023: S=1.88 (strong), ret=+5.7%

## Risk & Drawdown
- Max drawdown: 6.96% over 866 days (recovered)
- Annualized: return +3.9%, volatility 3.3% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.29, excess kurtosis +2.12

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.50, max 3.56, latest 1.89

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2021
Best month: +2.33%; worst month: -1.70%
Positive months: 59%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.12
- Sideways: S=1.48
- Bear: S=0.06

## Negated Direction
Best negated: `rank(-1 * fn_liab_fair_val_l2_a)` S=0.44, F=0.23, INFERIOR
Direction gap: -0.38 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_liab_fair_val_l2_a)`: S=0.44, F=0.23, T=2.1%, INFERIOR (TOP3000)
- `rank(-1 * fn_liab_fair_val_l2_a / close)`: S=0.35, F=0.17, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_liab_fair_val_l2_a, 5))`: S=-0.12, F=-0.03, T=25.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fn_liab_fair_val_l2_a / close)` | TOP3000 | 1.18 | 0.66 | 7.0% | 80% | mixed |
| `rank(ts_delta(fn_liab_fair_val_l2_a, 5))` | TOP1000 | 0.83 | 0.53 | 22.7% | 100% | mixed |
| `rank(fn_liab_fair_val_l2_a)` | TOP3000 | 0.78 | 0.40 | 12.8% | 60% | bull-only |
| `rank(ts_delta(fn_liab_fair_val_l2_a, 5))` | TOP200 | 0.27 | 0.11 | 45.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fn_liab_fair_val_l2_q: 0.738 (strongly positively correlated)
- fn_assets_fair_val_l2_a: 0.563 (moderately positively correlated)
- fnd6_newa1v1300_aol2: 0.501 (moderately positively correlated)
- fn_assets_fair_val_l2_q: 0.477 (moderately positively correlated)
- fnd6_newqv1300_aol2q: 0.468 (moderately positively correlated)

Redundancy cluster #10: 2 similar fields, mean |rho| 0.738 (representative: fn_liab_fair_val_l2_q). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.08 | 1.72 | +0.54 | -0.76 | yes |
| fnd6_rank | fundamental6 | -0.06 | 1.70 | +0.53 | -0.15 | yes |
| anl4_totassets_number | analyst4 | -0.01 | 1.66 | +0.49 | -0.23 | yes |
| sales_max_guidance_quarterly | analyst4 | -0.00 | 1.58 | +0.40 | -0.98 | yes |
| rank(scl12_sentiment * (-1 * returns)) | socialmedia12 | -0.04 | 1.67 | +0.49 | +0.20 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
