---
field: rank(scl12_sentiment * (-1 * returns))
dataset: socialmedia12
best_template: unknown
best_sharpe: 1.16
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 1
regime_profile: mixed
n_variations_with_pnl: 1
max_drawdown: 0.0665
ann_vol: 0.0358
hit_rate: 0.5109
rolling_sharpe_min: -1.415
rolling_sharpe_max: 3.314
top_merge_partner: fn_taxes_payable_q
---
# rank(scl12_sentiment * (-1 * returns)) (socialmedia12)


## Signal Profile
- No simulation data available

## Check Summary
- HIGH_TURNOVER: 1F/0P
- LOW_FITNESS: 1F/0P
- LOW_SHARPE: 1F/0P

## Temporal Behavior
Headline (unknown): Overall Sharpe 1.14, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.15 (weak), ret=+0.4%
  - 2020: S=2.06 (strong), ret=+7.3%
  - 2021: S=0.23 (weak), ret=+1.0%
  - 2022: S=0.82 (moderate), ret=+2.7%
  - 2023: S=2.57 (strong), ret=+8.6%

## Risk & Drawdown
- Max drawdown: 6.65% over 680 days (recovered)
- Annualized: return +4.1%, volatility 3.6% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.49, excess kurtosis +3.59

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.42, max 3.31, latest 2.52

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2019
Best month: +4.29%; worst month: -1.57%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.87
- Sideways: S=1.17
- Bear: S=0.40

## Negated Direction
No negated-direction simulations available for this field.

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(scl12_sentiment * (-1 * returns))` | TOP3000 | 1.14 | 0.25 | 6.7% | 100% | mixed |

## Correlation Notes
Top correlates:
- rank(scl12_buzz * (-1 * returns)): 0.577 (moderately positively correlated)
- rank(fnd6_acdo) * rank(-1 * returns): 0.491 (moderately positively correlated)
- rank(fnd6_acdo) + rank(open/close - 1): 0.460 (moderately positively correlated)
- sales_estimate_count: 0.241 (weakly positively correlated)
- news_pct_120min: -0.196 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_taxes_payable_q | fundamental2 | -0.06 | 1.64 | +0.50 | -0.93 | yes |
| anl4_ptpr_flag | analyst_revision | -0.09 | 1.75 | +0.47 | -0.76 | yes |
| fnd6_cld2 | fundamental6 | -0.05 | 1.75 | +0.46 | -0.79 | yes |
| fnd6_dxd5 | fundamental6 | -0.04 | 1.66 | +0.47 | -0.65 | yes |
| unsystematic_risk_last_90_days | model51 | -0.14 | 1.84 | +0.52 | -0.15 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_delta, rank_level, rank_value_norm, trade_when
