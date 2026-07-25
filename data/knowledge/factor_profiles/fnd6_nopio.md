---
field: fnd6_nopio
dataset: fundamental6
best_template: rank_delta
best_sharpe: 1.27
best_fitness: 1.03
best_universe: TOP200
grade: AVERAGE
submittability: blocked_CONCENTRATED_WEIGHT
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.4107
ann_vol: 0.1874
hit_rate: 0.532
rolling_sharpe_min: -1.061
rolling_sharpe_max: 2.365
top_merge_partner: fn_effect_of_exchange_rate_on_cash_and_equiv_a
redundancy_cluster: 16
negated_best_sharpe: 0.43
negated_best_template: neg_rank_level
negated_best_fitness: 0.24
n_negated_sims: 10
direction_gap: -0.84
---
# fnd6_nopio (fundamental6)

*Nonoperating Income (Expense) - Other*

## Signal Profile
- `rank(fnd6_nopio)`: S=0.14, F=0.03, T=1.2%, INFERIOR (TOP3000)
- `rank(fnd6_nopio / close)`: S=0.23, F=0.06, T=1.4%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_nopio, 5))`: S=1.27, F=1.03, T=35.7%, AVERAGE (TOP200)
- `-rank(fnd6_nopio)`: S=0.20, F=0.06, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_nopio, 5))`: S=-1.31, F=-1.09, T=35.6%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_nopio, 22)`: S=-0.16, F=-0.05, T=30.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_nopio, 10)`: S=-0.33, F=-0.15, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_nopio, 22))`: S=0.61, F=0.33, T=14.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_nopio)`: S=0.43, F=0.24, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_nopio / close)`: S=0.41, F=0.22, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 11F/21P
- LOW_FITNESS: 31F/1P
- LOW_SHARPE: 31F/1P
- LOW_SUB_UNIVERSE_SHARPE: 13F/7P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.28, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.37 (weak), ret=+5.0%
  - 2020: S=2.14 (strong), ret=+36.8%
  - 2021: S=1.55 (strong), ret=+33.2%
  - 2022: S=0.34 (weak), ret=+7.9%
  - 2023: S=2.30 (strong), ret=+34.5%

## Risk & Drawdown
- Max drawdown: 41.07% over 497 days (recovered)
- Annualized: return +24.0%, volatility 18.7% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew +0.67, excess kurtosis +6.37

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.06, max 2.37, latest 2.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +17.79%; worst month: -13.16%
Positive months: 68%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.46
- Sideways: S=1.08
- Bear: S=2.43

## Negated Direction
Best negated: `rank(-1 * fnd6_nopio)` S=0.43, F=0.24, INFERIOR
Direction gap: -0.84 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_nopio)`: S=0.43, F=0.24, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_nopio / close)`: S=0.41, F=0.22, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_nopio, 5))`: S=-1.31, F=-1.09, T=35.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_nopio, 5))` | TOP200 | 1.28 | 1.03 | 41.1% | 100% | mixed |
| `rank(ts_delta(fnd6_nopio, 5))` | TOP500 | 0.64 | 0.33 | 21.4% | 80% | mixed |
| `rank(ts_delta(fnd6_nopio, 5))` | TOP1000 | 0.60 | 0.25 | 15.0% | 60% | all-weather |
| `rank(fnd6_nopio / close)` | TOP3000 | 0.24 | 0.06 | 9.0% | 60% | bull-only |
| `rank(ts_delta(fnd6_nopio, 5))` | TOP3000 | 0.22 | 0.05 | 14.7% | 60% | weak |
| `rank(fnd6_nopio)` | TOP3000 | 0.14 | 0.03 | 13.8% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_nopi: 0.732 (strongly positively correlated)
- fnd6_txpd: 0.177 (weakly positively correlated)
- fnd6_lcoxdr: 0.163 (weakly positively correlated)
- fnd6_recco: 0.162 (weakly positively correlated)
- fnd6_lqpl1: 0.161 (weakly positively correlated)

Redundancy cluster #16: 2 similar fields, mean |rho| 0.732 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_effect_of_exchange_rate_on_cash_and_equiv_a | fundamental2 | -0.06 | 1.88 | +0.59 | -0.32 | yes |
| news_mins_4_pct_dn | news12 | -0.03 | 1.85 | +0.55 | +0.14 | yes |
| fn_line_of_credit_facility_amount_out_a | fundamental2 | -0.01 | 1.82 | +0.54 | -0.11 | yes |
| implied_volatility_put_10 | option8 | -0.07 | 1.81 | +0.52 | -0.11 | yes |
| fn_assets_fair_val_a | fundamental2 | -0.03 | 1.92 | +0.53 | +0.11 | yes |

## Actionability
Blocked by CONCENTRATED_WEIGHT. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
