---
field: rp_ess_mna
dataset: news18
best_template: rank_delta
best_sharpe: 0.85
best_fitness: 0.21
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 20
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1712
ann_vol: 0.1016
hit_rate: 0.5296
rolling_sharpe_min: -1.086
rolling_sharpe_max: 3.299
top_merge_partner: fn_finite_lived_intangible_assets_net_q
negated_best_sharpe: 0.66
negated_best_template: neg_rank_level
negated_best_fitness: 0.11
n_negated_sims: 4
direction_gap: -0.19
---
# rp_ess_mna (news18)

*Event sentiment score of mergers and acquisitions-related news*

## Signal Profile
- `rank(rp_ess_mna)`: S=0.09, F=0.01, T=127.0%, INFERIOR (TOP200)
- `rank(ts_delta(rp_ess_mna, 5))`: S=0.85, F=0.21, T=141.2%, INFERIOR (TOP200)
- `-rank(rp_ess_mna)`: S=-0.11, F=-0.01, T=144.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_mna, 5))`: S=-0.34, F=-0.04, T=161.5%, INFERIOR (TOP3000)
- `ts_zscore(rp_ess_mna, 22)`: S=-0.07, F=0.00, T=144.4%, INFERIOR (TOP3000)
- `ts_mean(rp_ess_mna, 10)`: S=-0.41, F=-0.14, T=19.1%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_ess_mna, 22))`: S=0.23, F=0.02, T=147.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_mna)`: S=0.66, F=0.11, T=153.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_mna / close)`: S=0.21, F=0.03, T=142.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 6F/14P
- HIGH_TURNOVER: 19F/1P
- LOW_FITNESS: 20F/0P
- LOW_SHARPE: 20F/0P
- LOW_SUB_UNIVERSE_SHARPE: 8F/10P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.83, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=1.62 (strong), ret=+13.1%
  - 2020: S=-0.95 (negative), ret=-11.3%
  - 2021: S=1.25 (moderate), ret=+13.5%
  - 2022: S=2.59 (strong), ret=+27.3%
  - 2023: S=-0.15 (negative), ret=-1.1%

## Risk & Drawdown
- Max drawdown: 17.12% over 525 days (recovered)
- Annualized: return +8.5%, volatility 10.2% (fraction of booksize)
- Hit rate: 53.0% positive days
- Tail shape: skew -0.19, excess kurtosis +3.41

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.09, max 3.30, latest -0.20

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +9.47%; worst month: -7.45%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=2.10
- Sideways: S=0.23
- Bear: S=0.09

## Negated Direction
Best negated: `rank(-1 * rp_ess_mna)` S=0.66, F=0.11, INFERIOR
Direction gap: -0.19 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * rp_ess_mna)`: S=0.66, F=0.11, T=153.0%, INFERIOR (TOP3000)
- `rank(-1 * rp_ess_mna / close)`: S=0.21, F=0.03, T=142.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_ess_mna, 5))`: S=-0.34, F=-0.04, T=161.5%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(rp_ess_mna, 5))` | TOP200 | 0.83 | 0.21 | 17.1% | 60% | mixed |
| `rank(ts_delta(rp_ess_mna, 5))` | TOP500 | 0.72 | 0.14 | 15.5% | 60% | mixed |
| `rank(ts_delta(rp_ess_mna, 5))` | TOP1000 | 0.66 | 0.12 | 9.5% | 80% | mixed |
| `rank(ts_delta(rp_ess_mna, 5))` | TOP3000 | 0.33 | 0.04 | 14.2% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_invoq: -0.138 (weakly negatively correlated)
- scl12_buzz: 0.131 (weakly positively correlated)
- snt_buzz: -0.129 (weakly negatively correlated)
- fnd6_cibegni: -0.122 (weakly negatively correlated)
- rp_nip_earnings: 0.108 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_finite_lived_intangible_assets_net_q | fundamental2 | -0.04 | 1.20 | +0.36 | -0.88 | yes |
| news_mins_5_chg | news12 | -0.03 | 1.17 | +0.33 | -0.75 | yes |
| fnd6_newa1v1300_acominc | fundamental6 | -0.05 | 1.31 | +0.33 | -0.78 | yes |
| fn_income_taxes_paid_q | fundamental2 | -0.02 | 1.24 | +0.32 | -0.81 | yes |
| sharesout | pv1 | -0.04 | 1.35 | +0.32 | -0.86 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
