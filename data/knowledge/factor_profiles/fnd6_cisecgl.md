---
field: fnd6_cisecgl
dataset: fundamental6
best_template: rank_ts_rank
best_sharpe: 0.98
best_fitness: 0.79
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: all-weather
n_variations_with_pnl: 9
max_drawdown: 0.3549
ann_vol: 0.1778
hit_rate: 0.5117
rolling_sharpe_min: -2.086
rolling_sharpe_max: 2.555
top_merge_partner: pv13_revere_company_total
negated_best_sharpe: 0.03
negated_best_template: neg_rank_level
negated_best_fitness: 0.0
n_negated_sims: 10
direction_gap: -0.95
---
# fnd6_cisecgl (fundamental6)

*Comp Inc - Securities Gains/Losses*

## Signal Profile
- `rank(fnd6_cisecgl)`: S=0.14, F=0.04, T=3.0%, INFERIOR (TOP500)
- `rank(fnd6_cisecgl / close)`: S=0.20, F=0.05, T=2.7%, INFERIOR (TOP1000)
- `rank(ts_delta(fnd6_cisecgl, 5))`: S=0.99, F=0.72, T=33.0%, INFERIOR (TOP1000)
- `-rank(fnd6_cisecgl)`: S=-0.15, F=-0.04, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cisecgl, 5))`: S=-0.88, F=-0.59, T=34.4%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_cisecgl, 22)`: S=-0.11, F=-0.04, T=16.2%, INFERIOR (TOP3000)
- `ts_mean(fnd6_cisecgl, 10)`: S=-0.10, F=-0.02, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_cisecgl, 22))`: S=0.98, F=0.79, T=20.0%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cisecgl)`: S=0.03, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cisecgl / close)`: S=-0.11, F=-0.02, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/14P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.99, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=2.48 (strong), ret=+36.1%
  - 2020: S=-1.57 (negative), ret=-23.4%
  - 2021: S=0.79 (moderate), ret=+15.1%
  - 2022: S=1.53 (strong), ret=+34.9%
  - 2023: S=1.71 (strong), ret=+23.9%

## Risk & Drawdown
- Max drawdown: 35.49% over 798 days (recovered)
- Annualized: return +17.7%, volatility 17.8% (fraction of booksize)
- Hit rate: 51.2% positive days
- Tail shape: skew +1.30, excess kurtosis +20.29

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -2.09, max 2.56, latest 1.75

## Yearly & Monthly Returns
Best year (by Sharpe): 2019; worst year: 2020
Best month: +15.76%; worst month: -10.06%
Positive months: 64%

## Regime Profile
Regime profile: **all-weather**
- Bull: S=1.14
- Sideways: S=1.21
- Bear: S=0.67

## Negated Direction
Best negated: `rank(-1 * fnd6_cisecgl)` S=0.03, F=0.00, INFERIOR
Direction gap: -0.95 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_cisecgl)`: S=0.03, F=0.00, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_cisecgl / close)`: S=-0.11, F=-0.02, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_cisecgl, 5))`: S=-0.88, F=-0.59, T=34.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fnd6_cisecgl, 5))` | TOP1000 | 0.99 | 0.72 | 35.5% | 80% | all-weather |
| `rank(ts_delta(fnd6_cisecgl, 5))` | TOP3000 | 1.00 | 0.71 | 16.6% | 100% | all-weather |
| `rank(ts_delta(fnd6_cisecgl, 5))` | TOP500 | 0.46 | 0.26 | 62.4% | 80% | mixed |
| `rank(ts_delta(fnd6_cisecgl, 5))` | TOP200 | 0.38 | 0.20 | 32.6% | 80% | mixed |
| `rank(fnd6_cisecgl / close)` | TOP1000 | 0.21 | 0.05 | 12.0% | 60% | bull-only |
| `rank(fnd6_cisecgl)` | TOP500 | 0.16 | 0.04 | 19.1% | 40% | bull-only |
| `rank(fnd6_cisecgl / close)` | TOP500 | 0.17 | 0.04 | 17.6% | 40% | bull-only |
| `rank(fnd6_cisecgl)` | TOP1000 | 0.17 | 0.04 | 13.0% | 40% | bull-only |
| `rank(fnd6_cisecgl / close)` | TOP3000 | 0.12 | 0.02 | 8.6% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_msa: 0.413 (moderately positively correlated)
- fnd6_txpd: 0.189 (weakly positively correlated)
- fnd6_mrcta: 0.186 (weakly positively correlated)
- fnd6_tfvl: 0.179 (weakly positively correlated)
- fnd6_ivst: 0.176 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| pv13_revere_company_total | pv13 | -0.06 | 1.49 | +0.43 | -0.51 | yes |
| rp_css_ptg | news18 | -0.07 | 1.40 | +0.40 | -0.78 | yes |
| max_net_debt_guidance | company_guidance | -0.08 | 1.49 | +0.46 | +0.26 | yes |
| min_net_debt_guidance | company_guidance | -0.08 | 1.49 | +0.46 | +0.26 | yes |
| fn_assets_fair_val_l3_a | fundamental2 | -0.04 | 1.45 | +0.43 | -0.23 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
