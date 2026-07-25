---
field: rp_nip_assets
dataset: news18
best_template: rank_neg_delta
best_sharpe: 0.71
best_fitness: 0.21
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 21
regime_profile: all-weather
n_variations_with_pnl: 1
max_drawdown: 0.3306
ann_vol: 0.1325
hit_rate: 0.5255
rolling_sharpe_min: -1.622
rolling_sharpe_max: 2.194
negated_best_sharpe: 0.71
negated_best_template: rank_neg_delta
negated_best_fitness: 0.21
n_negated_sims: 4
direction_gap: 0.22
---
# rp_nip_assets (news18)

*News impact projection of assets news*

## Signal Profile
- `rank(rp_nip_assets)`: S=0.30, F=0.05, T=167.8%, INFERIOR (TOP3000)
- `rank(rp_nip_assets / close)`: S=0.29, F=0.05, T=147.8%, INFERIOR (TOP3000)
- `rank(ts_delta(rp_nip_assets, 5))`: S=-0.23, F=-0.05, T=142.4%, INFERIOR (TOP200)
- `-rank(rp_nip_assets)`: S=0.09, F=0.01, T=159.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_assets, 5))`: S=0.71, F=0.21, T=155.9%, INFERIOR (TOP3000)
- `-ts_zscore(rp_nip_assets, 63)`: S=0.49, F=0.11, T=156.6%, INFERIOR (TOP3000)
- `ts_mean(rp_nip_assets, 10)`: S=0.27, F=0.06, T=33.5%, INFERIOR (TOP3000)
- `rank(ts_rank(rp_nip_assets, 22))`: S=0.13, F=0.01, T=160.9%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_assets)`: S=-0.30, F=-0.05, T=167.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_assets / close)`: S=-0.24, F=-0.04, T=160.4%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 20F/1P
- HIGH_TURNOVER: 20F/1P
- LOW_FITNESS: 21F/0P
- LOW_SHARPE: 21F/0P
- LOW_SUB_UNIVERSE_SHARPE: 10F/9P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.31, Consistency 60% positive years (3/5)
Yearly breakdown:
  - 2019: S=-0.29 (negative), ret=-4.9%
  - 2020: S=-0.84 (negative), ret=-10.2%
  - 2021: S=1.07 (moderate), ret=+12.5%
  - 2022: S=1.60 (strong), ret=+19.4%
  - 2023: S=0.28 (weak), ret=+3.2%

## Risk & Drawdown
- Max drawdown: 33.06% over 1057 days (recovered)
- Annualized: return +4.1%, volatility 13.2% (fraction of booksize)
- Hit rate: 52.5% positive days
- Tail shape: skew -2.45, excess kurtosis +33.75

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.62, max 2.19, latest 0.28

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.55%; worst month: -14.56%
Positive months: 61%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.09
- Sideways: S=-0.44
- Bear: S=0.55

## Negated Direction
Best negated: `rank(-1 * ts_delta(rp_nip_assets, 5))` S=0.71, F=0.21, INFERIOR
Direction gap: +0.22 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * rp_nip_assets)`: S=-0.30, F=-0.05, T=167.8%, INFERIOR (TOP3000)
- `rank(-1 * rp_nip_assets / close)`: S=-0.24, F=-0.04, T=160.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(rp_nip_assets, 5))`: S=0.71, F=0.21, T=155.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(rp_nip_assets)` | TOP3000 | 0.31 | 0.05 | 33.1% | 60% | all-weather |

## Correlation Notes
Top correlates:
- fnd6_loxdr: -0.181 (weakly negatively correlated)
- pv13_revere_term_sector_total: -0.177 (weakly negatively correlated)
- fn_accum_oth_income_loss_net_of_tax_q: 0.177 (weakly positively correlated)
- fnd6_newa1v1300_dv: -0.173 (weakly negatively correlated)
- cashflow_dividends: -0.173 (weakly negatively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
