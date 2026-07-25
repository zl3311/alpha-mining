---
field: pv13_revere_key_sector_total
dataset: pv13
best_template: rank_level
best_sharpe: 0.85
best_fitness: 0.94
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 24
regime_profile: all-weather
n_variations_with_pnl: 5
max_drawdown: 0.4196
ann_vol: 0.1814
hit_rate: 0.4996
rolling_sharpe_min: -2.596
rolling_sharpe_max: 3.537
top_merge_partner: fnd6_newa2v1300_recch
negated_best_sharpe: 0.66
negated_best_template: rank_neg_delta
negated_best_fitness: 0.56
n_negated_sims: 10
direction_gap: -0.19
---
# pv13_revere_key_sector_total (pv13)

*Number of key focus sectors for the company*

## Signal Profile
- `rank(pv13_revere_key_sector_total)`: S=0.85, F=0.94, T=1.6%, INFERIOR (TOP3000)
- `rank(ts_delta(pv13_revere_key_sector_total, 5))`: S=0.65, F=0.48, T=5.2%, INFERIOR (TOP500)
- `-rank(pv13_revere_key_sector_total)`: S=-0.04, F=-0.01, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_key_sector_total, 5))`: S=0.66, F=0.56, T=8.6%, INFERIOR (TOP3000)
- `-ts_zscore(pv13_revere_key_sector_total, 63)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(pv13_revere_key_sector_total, 10)`: S=0.18, F=0.10, T=2.6%, INFERIOR (TOP3000)
- `rank(ts_rank(pv13_revere_key_sector_total, 22))`: S=0.44, F=0.34, T=5.4%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_key_sector_total)`: S=-0.96, F=-1.14, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_key_sector_total / close)`: S=-0.37, F=-0.21, T=1.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 21F/3P
- LOW_FITNESS: 22F/0P
- LOW_SHARPE: 24F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/10P
- LOW_TURNOVER: 2F/22P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.85, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.61 (strong), ret=+42.8%
  - 2020: S=0.84 (moderate), ret=+13.7%
  - 2021: S=1.52 (strong), ret=+20.4%
  - 2022: S=1.85 (strong), ret=+29.6%
  - 2023: S=-2.41 (negative), ret=-30.9%

## Risk & Drawdown
- Max drawdown: 41.96% over 431 days (not yet recovered, ongoing at window end)
- Annualized: return +15.4%, volatility 18.1% (fraction of booksize)
- Hit rate: 50.0% positive days
- Tail shape: skew +0.87, excess kurtosis +11.02

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.60, max 3.54, latest -2.44

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +26.14%; worst month: -12.30%
Positive months: 55%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.23
- Sideways: S=0.77
- Bear: S=0.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(pv13_revere_key_sector_total, 5))` S=0.66, F=0.56, INFERIOR
Direction gap: -0.19 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * pv13_revere_key_sector_total)`: S=-0.96, F=-1.14, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * pv13_revere_key_sector_total / close)`: S=-0.37, F=-0.21, T=1.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(pv13_revere_key_sector_total, 5))`: S=0.66, F=0.56, T=8.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(pv13_revere_key_sector_total)` | TOP3000 | 0.85 | 0.94 | 42.0% | 80% | all-weather |
| `rank(ts_delta(pv13_revere_key_sector_total, 5))` | TOP500 | 0.62 | 0.48 | 32.9% | 80% | bull-only |
| `rank(pv13_revere_key_sector_total)` | TOP500 | 0.26 | 0.26 | 36.5% | 80% | mixed |
| `rank(ts_delta(pv13_revere_key_sector_total, 5))` | TOP200 | 0.37 | 0.25 | 30.1% | 60% | bull-only |
| `rank(pv13_revere_key_sector_total)` | TOP200 | 0.23 | 0.25 | 45.6% | 60% | weak |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_tstkn: 0.286 (weakly positively correlated)
- fnd6_newqv1300_tstknq: 0.284 (weakly positively correlated)
- fn_income_tax_expense_a: 0.283 (weakly positively correlated)
- fnd6_newqv1300_tstkq: 0.282 (weakly positively correlated)
- fnd6_tstkc: 0.282 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_newa2v1300_recch | fundamental6 | -0.03 | 1.26 | +0.33 | -0.95 | yes |
| fnd6_newqv1300_cipenq | fundamental6 | -0.02 | 1.27 | +0.35 | -0.74 | yes |
| fnd6_lcoxdr | fundamental6 | -0.08 | 1.28 | +0.36 | -0.55 | yes |
| fnd6_newqv1300_stkcpaq | fundamental6 | -0.03 | 1.23 | +0.35 | -0.57 | yes |
| fn_finite_lived_intangible_assets_net_q | fundamental2 | -0.05 | 1.17 | +0.32 | -0.88 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, rank_value_norm, trade_when
