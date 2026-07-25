---
field: fnd6_dclo
dataset: fundamental6
best_template: rank_value_norm
best_sharpe: 0.95
best_fitness: 0.5
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 10
max_drawdown: 0.0353
ann_vol: 0.0367
hit_rate: 0.5223
rolling_sharpe_min: -0.651
rolling_sharpe_max: 2.384
top_merge_partner: fn_def_tax_assets_liab_net_a
negated_best_sharpe: 0.26
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.69
---
# fnd6_dclo (fundamental6)

*Debt - Capitalized Lease Obligations*

## Signal Profile
- `rank(fnd6_dclo)`: S=0.83, F=0.43, T=1.8%, INFERIOR (TOP3000)
- `rank(fnd6_dclo / close)`: S=0.95, F=0.50, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd6_dclo, 5))`: S=0.36, F=0.15, T=36.9%, INFERIOR (TOP1000)
- `-rank(fnd6_dclo)`: S=-0.22, F=-0.06, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dclo, 5))`: S=0.26, F=0.09, T=40.0%, INFERIOR (TOP3000)
- `-ts_zscore(fnd6_dclo, 63)`: S=-0.17, F=-0.08, T=16.8%, INFERIOR (TOP3000)
- `ts_mean(fnd6_dclo, 10)`: S=0.39, F=0.23, T=1.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_dclo, 22))`: S=0.23, F=0.09, T=19.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dclo)`: S=-0.83, F=-0.43, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dclo / close)`: S=-0.95, F=-0.50, T=1.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/20P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.95, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.81 (moderate), ret=+1.8%
  - 2020: S=0.90 (moderate), ret=+3.2%
  - 2021: S=1.11 (moderate), ret=+4.8%
  - 2022: S=1.36 (moderate), ret=+6.0%
  - 2023: S=0.43 (weak), ret=+1.4%

## Risk & Drawdown
- Max drawdown: 3.53% over 213 days (recovered)
- Annualized: return +3.5%, volatility 3.7% (fraction of booksize)
- Hit rate: 52.2% positive days
- Tail shape: skew +0.03, excess kurtosis +1.88

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.65, max 2.38, latest 0.26

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.03%; worst month: -1.83%
Positive months: 61%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.89
- Sideways: S=1.06
- Bear: S=-1.34

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_dclo, 5))` S=0.26, F=0.09, INFERIOR
Direction gap: -0.69 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_dclo)`: S=-0.83, F=-0.43, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_dclo / close)`: S=-0.95, F=-0.50, T=1.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_dclo, 5))`: S=0.26, F=0.09, T=40.0%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_dclo / close)` | TOP3000 | 0.95 | 0.50 | 3.5% | 100% | bull-only |
| `rank(fnd6_dclo)` | TOP3000 | 0.83 | 0.43 | 4.1% | 100% | bull-only |
| `rank(ts_delta(fnd6_dclo, 5))` | TOP1000 | 0.36 | 0.15 | 37.9% | 60% | mixed |
| `rank(fnd6_dclo)` | TOP200 | 0.25 | 0.11 | 14.0% | 40% | mixed |
| `rank(fnd6_dclo)` | TOP500 | 0.21 | 0.07 | 9.7% | 60% | bull-only |
| `rank(fnd6_dclo)` | TOP1000 | 0.20 | 0.06 | 11.3% | 40% | bull-only |
| `rank(fnd6_dclo / close)` | TOP500 | 0.17 | 0.05 | 9.9% | 60% | bull-only |
| `rank(fnd6_dclo / close)` | TOP200 | 0.15 | 0.05 | 14.0% | 40% | mixed |
| `rank(ts_delta(fnd6_dclo, 5))` | TOP200 | 0.12 | 0.04 | 39.1% | 60% | weak |
| `rank(fnd6_dclo / close)` | TOP1000 | 0.11 | 0.02 | 9.1% | 40% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_dd2: 0.767 (strongly positively correlated)
- fnd6_dd4: 0.764 (strongly positively correlated)
- fnd6_dd3: 0.763 (strongly positively correlated)
- fnd6_dd5: 0.756 (strongly positively correlated)
- fnd6_newa1v1300_intano: 0.752 (strongly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.29 | 1.56 | +0.61 | -0.59 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.22 | 1.35 | +0.40 | -0.43 | yes |
| rp_nip_credit_ratings | news18 | -0.01 | 1.33 | +0.37 | -0.71 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.12 | 1.58 | +0.43 | -0.10 | yes |
| rank(scl12_buzz * (-1 * returns)) | socialmedia12 | -0.19 | 2.00 | +0.38 | -0.58 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
