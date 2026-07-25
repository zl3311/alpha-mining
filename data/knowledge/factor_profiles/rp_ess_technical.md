---
field: rp_ess_technical
dataset: news18
best_template: rank_level
best_sharpe: 1.05
best_fitness: 0.91
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: all-weather
n_variations_with_pnl: 3
max_drawdown: 0.0686
ann_vol: 0.0863
hit_rate: 0.0413
rolling_sharpe_min: -0.85
rolling_sharpe_max: 1.874
top_merge_partner: anl4_rd_exp_flag
negated_best_sharpe: 0.55
negated_best_template: neg_rank_level
negated_best_fitness: 0.29
n_negated_sims: 4
direction_gap: -0.5
---
# rp_ess_technical (news18)

*Event sentiment score based on technical analysis*

## Signal Profile
- `rank(rp_ess_technical)`: S=1.05, F=0.91, T=8.2%, INFERIOR (TOP500)
- `rank(ts_delta(rp_ess_technical, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `-rank(rp_ess_technical)`: S=-0.33, F=-0.15, T=18.0%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_technical, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_zscore(rp_ess_technical, 22)`: S=0.91, F=0.38, T=5.7%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_technical, 10)`: S=-0.22, F=-0.10, T=40.5%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_technical, 22))`: S=-0.03, F=0.00, T=6.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_technical)`: S=0.55, F=0.29, T=38.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_technical / close)`: S=-1.30, F=-0.86, T=81.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/0P
- HIGH_TURNOVER: 1F/19P
- LOW_FITNESS: 13F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 4F/8P
- LOW_TURNOVER: 7F/13P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.02, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=1.23 (moderate), ret=+8.1%
  - 2020: S=0.17 (weak), ret=+0.6%
  - 2021: S=1.00 (moderate), ret=+10.3%
  - 2022: S=1.59 (strong), ret=+17.1%
  - 2023: S=0.78 (moderate), ret=+7.1%

## Risk & Drawdown
- Max drawdown: 6.86% over 263 days (recovered)
- Annualized: return +8.8%, volatility 8.6% (fraction of booksize)
- Hit rate: 4.1% positive days
- Tail shape: skew +8.76, excess kurtosis +120.71

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.85, max 1.87, latest 0.95

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.37%; worst month: -4.25%
Positive months: 62%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.75
- Sideways: S=0.28
- Bear: S=0.53

## Negated Direction
Best negated: `rank(-1 * rp_ess_technical)` S=0.55, F=0.29, INFERIOR
Direction gap: -0.50 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * rp_ess_technical)`: S=0.55, F=0.29, T=38.7%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_technical / close)`: S=-1.30, F=-0.86, T=81.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_technical, 5))`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_ess_technical)` | TOP500 | 1.02 | 0.91 | 6.9% | 100% | all-weather |
| `rank(rp_ess_technical)` | TOP200 | 0.54 | 0.28 | 3.2% | 80% | bull-only |
| `rank(rp_ess_technical)` | TOP1000 | 0.32 | 0.15 | 25.1% | 60% | mixed |

## Correlation Notes
Top correlates:
- fn_assets_fair_val_l1_q: 0.158 (weakly positively correlated)
- rp_css_technical: 0.149 (weakly positively correlated)
- fnd6_newqv1300_cshopq: 0.125 (weakly positively correlated)
- rank(scl12_buzz * (-1 * returns)): -0.122 (weakly negatively correlated)
- fnd6_newqv1300_lol2q: 0.114 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.03 | 1.46 | +0.44 | -0.97 | yes |
| news_mins_4_chg | news12 | -0.04 | 1.51 | +0.43 | -0.83 | yes |
| implied_volatility_call_10 | option8 | -0.06 | 1.49 | +0.45 | -0.50 | yes |
| sharesout | pv1 | -0.01 | 1.45 | +0.41 | -0.82 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.02 | 1.41 | +0.38 | -0.79 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
