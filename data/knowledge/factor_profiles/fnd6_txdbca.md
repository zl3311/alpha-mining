---
field: fnd6_txdbca
dataset: fundamental6
best_template: neg_rank_level
best_sharpe: 1.06
best_fitness: 1.63
best_universe: TOP3000
grade: GOOD
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 2
max_drawdown: 0.1069
ann_vol: 0.0998
hit_rate: 0.4591
rolling_sharpe_min: -0.567
rolling_sharpe_max: 3.437
top_merge_partner: anl4_rd_exp_flag
negated_best_sharpe: 1.06
negated_best_template: neg_rank_level
negated_best_fitness: 1.63
n_negated_sims: 10
direction_gap: 0.09
---
# fnd6_txdbca (fundamental6)

*Deferred Tax Asset - Current*

## Signal Profile
- `rank(fnd6_txdbca)`: S=-0.04, F=-0.01, T=3.5%, INFERIOR (TOP200)
- `rank(fnd6_txdbca / close)`: S=-0.04, F=-0.01, T=3.5%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_txdbca, 5))`: S=0.97, F=0.86, T=6.2%, INFERIOR (TOP3000)
- `-rank(fnd6_txdbca)`: S=0.65, F=0.83, T=4.1%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdbca, 5))`: S=0.30, F=0.12, T=4.8%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_txdbca, 22)`: S=0.00, F=0.00, T=0.0%, UNKNOWN (TOP3000)
- `ts_mean(fnd6_txdbca, 10)`: S=-0.51, F=-0.60, T=2.3%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_txdbca, 22))`: S=-0.08, F=-0.02, T=4.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_txdbca)`: S=1.06, F=1.63, T=6.1%, GOOD (TOP3000)
- `rank(-1 * fnd6_txdbca / close)`: S=1.06, F=1.63, T=6.1%, GOOD (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 32F/0P
- LOW_FITNESS: 24F/6P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/18P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.95, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.68 (moderate), ret=+10.4%
  - 2020: S=0.22 (weak), ret=+1.7%
  - 2021: S=0.90 (moderate), ret=+10.2%
  - 2022: S=2.31 (strong), ret=+15.5%
  - 2023: S=2.13 (strong), ret=+8.4%

## Risk & Drawdown
- Max drawdown: 10.69% over 193 days (recovered)
- Annualized: return +9.4%, volatility 10.0% (fraction of booksize)
- Hit rate: 45.9% positive days
- Tail shape: skew +6.43, excess kurtosis +101.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.57, max 3.44, latest 1.96

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +15.25%; worst month: -5.95%
Positive months: 56%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.41
- Sideways: S=1.22
- Bear: S=0.10

## Negated Direction
Best negated: `rank(-1 * fnd6_txdbca)` S=1.06, F=1.63, GOOD
Direction gap: +0.09 (negated - positive best Sharpe). Negation slightly better.

Negated template variants:
- `rank(-1 * fnd6_txdbca)`: S=1.06, F=1.63, T=6.1%, GOOD (TOP3000)
- `rank(-1 * fnd6_txdbca / close)`: S=1.06, F=1.63, T=6.1%, GOOD (TOP3000)
- `rank(-1 * ts_delta(fnd6_txdbca, 5))`: S=0.30, F=0.12, T=4.8%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_txdbca, 5))` | TOP3000 | 0.95 | 0.86 | 10.7% | 100% | mixed |
| `rank(ts_delta(fnd6_txdbca, 5))` | TOP500 | 0.37 | 0.19 | 23.2% | 80% | bull-only |

## Correlation Notes
Top correlates:
- anl4_ffo_flag: 0.389 (weakly positively correlated)
- pv13_revere_level: 0.355 (weakly positively correlated)
- pv13_revere_parent: 0.355 (weakly positively correlated)
- max_share_buyback_guidance: 0.348 (weakly positively correlated)
- min_adjusted_funds_from_operations_adj_guidance: 0.348 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_rd_exp_flag | analyst4 | -0.12 | 1.49 | +0.46 | -0.62 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.13 | 1.43 | +0.48 | -0.37 | yes |
| systematic_risk_last_360_days | model51 | -0.09 | 1.45 | +0.44 | -0.74 | yes |
| anl4_afv4_dts_spe | analyst4 | -0.15 | 1.49 | +0.49 | +0.16 | yes |
| sharesout | pv1 | -0.09 | 1.47 | +0.43 | -0.56 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
