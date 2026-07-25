---
field: sharesout
dataset: pv1
best_template: rank_delta
best_sharpe: 1.05
best_fitness: 0.62
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 30
regime_profile: bear-only
n_variations_with_pnl: 3
max_drawdown: 0.1878
ann_vol: 0.1141
hit_rate: 0.5109
rolling_sharpe_min: -0.948
rolling_sharpe_max: 3.201
top_merge_partner: implied_volatility_mean_skew_180
negated_best_sharpe: 0.65
negated_best_template: rank_neg_delta
negated_best_fitness: 0.2
n_negated_sims: 10
direction_gap: -0.4
---
# sharesout (pv1)

*Daily outstanding shares (in millions)*

## Signal Profile
- `rank(sharesout)`: S=0.24, F=0.08, T=1.4%, INFERIOR (TOP1000)
- `rank(sharesout / close)`: S=-0.08, F=-0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(ts_delta(sharesout, 5))`: S=1.05, F=0.62, T=34.1%, INFERIOR (TOP200)
- `ts_decay_linear(rank(sharesout), 5)`: S=0.03, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `-rank(sharesout)`: S=-0.24, F=-0.08, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sharesout, 5))`: S=0.65, F=0.20, T=33.2%, INFERIOR (TOP3000)
- `-ts_zscore(sharesout, 63)`: S=0.39, F=0.20, T=20.2%, INFERIOR (TOP3000)
- `ts_mean(sharesout, 10)`: S=-0.03, F=0.00, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(sharesout, 22))`: S=-0.75, F=-0.40, T=13.5%, INFERIOR (TOP3000)
- `rank(-1 * sharesout)`: S=-0.03, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * sharesout / close)`: S=0.08, F=0.02, T=1.3%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 2F/28P
- LOW_FITNESS: 30F/0P
- LOW_SHARPE: 30F/0P
- LOW_SUB_UNIVERSE_SHARPE: 14F/14P
- LOW_TURNOVER: 6F/24P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 1.03, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.31 (moderate), ret=+10.2%
  - 2020: S=1.73 (strong), ret=+16.0%
  - 2021: S=1.09 (moderate), ret=+16.1%
  - 2022: S=-0.21 (negative), ret=-2.6%
  - 2023: S=1.70 (strong), ret=+18.0%

## Risk & Drawdown
- Max drawdown: 18.78% over 742 days (recovered)
- Annualized: return +11.8%, volatility 11.4% (fraction of booksize)
- Hit rate: 51.1% positive days
- Tail shape: skew +0.48, excess kurtosis +5.46

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.95, max 3.20, latest 1.69

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +20.58%; worst month: -7.76%
Positive months: 59%

## Regime Profile
Regime profile: **bear-only**
- Bull: S=-0.98
- Sideways: S=1.85
- Bear: S=2.45

## Negated Direction
Best negated: `rank(-1 * ts_delta(sharesout, 5))` S=0.65, F=0.20, INFERIOR
Direction gap: -0.40 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * sharesout)`: S=-0.03, F=0.00, T=0.9%, INFERIOR (TOP3000)
- `rank(-1 * sharesout / close)`: S=0.08, F=0.02, T=1.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(sharesout, 5))`: S=0.65, F=0.20, T=33.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(sharesout, 5))` | TOP200 | 1.03 | 0.62 | 18.8% | 80% | bear-only |
| `rank(sharesout)` | TOP1000 | 0.24 | 0.08 | 11.2% | 60% | bull-only |
| `rank(sharesout)` | TOP500 | 0.16 | 0.06 | 25.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- unsystematic_risk_last_30_days: 0.296 (weakly positively correlated)
- anl4_cff_low: 0.281 (weakly positively correlated)
- anl4_cff_median: 0.281 (weakly positively correlated)
- implied_volatility_mean_skew_90: -0.281 (weakly negatively correlated)
- implied_volatility_mean_skew_120: -0.280 (weakly negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| implied_volatility_mean_skew_180 | option8 | -0.25 | 1.66 | +0.60 | -0.69 | yes |
| anl4_fcf_high | analyst4 | -0.23 | 1.62 | +0.59 | -0.62 | yes |
| implied_volatility_mean_skew_270 | option8 | -0.27 | 1.62 | +0.59 | -0.51 | yes |
| fnd6_dpvieb | fundamental6 | -0.16 | 1.59 | +0.55 | -0.78 | yes |
| anl4_tot_gw_ft | analyst4 | -0.20 | 1.60 | +0.57 | -0.60 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: trade_when
