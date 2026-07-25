---
field: rank(fnd6_acdo) * rank(volume/adv20)
dataset: unknown
best_template: unknown
best_sharpe: 0.79
best_fitness: 0.25
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 1
regime_profile: bull-only
n_variations_with_pnl: 1
max_drawdown: 0.1091
ann_vol: 0.0496
hit_rate: 0.5198
rolling_sharpe_min: -2.027
rolling_sharpe_max: 3.64
top_merge_partner: news_mins_3_chg
---
# rank(fnd6_acdo) * rank(volume/adv20) (unknown)


## Signal Profile
- No simulation data available

## Check Summary
- LOW_FITNESS: 1F/0P
- LOW_SHARPE: 1F/0P

## Temporal Behavior
Headline (unknown): Overall Sharpe 0.81, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.20 (weak), ret=+0.5%
  - 2020: S=-1.43 (negative), ret=-6.5%
  - 2021: S=2.82 (strong), ret=+16.2%
  - 2022: S=0.34 (weak), ret=+2.3%
  - 2023: S=1.99 (strong), ret=+7.2%

## Risk & Drawdown
- Max drawdown: 10.91% over 722 days (recovered)
- Annualized: return +4.0%, volatility 5.0% (fraction of booksize)
- Hit rate: 52.0% positive days
- Tail shape: skew +0.89, excess kurtosis +8.51

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.03, max 3.64, latest 2.27

## Yearly & Monthly Returns
Best year (by Sharpe): 2021; worst year: 2020
Best month: +4.08%; worst month: -3.14%
Positive months: 63%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.32
- Sideways: S=0.51
- Bear: S=-0.72

## Negated Direction
No negated-direction simulations available for this field.

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_acdo) * rank(volume/adv20)` | TOP3000 | 0.81 | 0.25 | 10.9% | 80% | bull-only |

## Correlation Notes
Top correlates:
- snt_social_volume: 0.515 (moderately positively correlated)
- historical_volatility_20: 0.406 (moderately positively correlated)
- historical_volatility_10: 0.390 (weakly positively correlated)
- parkinson_volatility_20: 0.366 (weakly positively correlated)
- parkinson_volatility_10: 0.358 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| news_mins_3_chg | news12 | -0.12 | 1.17 | +0.35 | -0.87 | yes |
| rp_ess_revenue | news18 | -0.08 | 1.20 | +0.31 | -0.86 | yes |
| news_pct_10min | news12 | -0.03 | 1.17 | +0.30 | -0.94 | yes |
| anl4_ptpr_number | analyst4 | -0.05 | 1.17 | +0.33 | -0.51 | yes |
| fnd6_newqv1300_miiq | fundamental6 | +0.05 | 1.15 | +0.28 | -0.92 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_delta, rank_level, rank_value_norm, trade_when
