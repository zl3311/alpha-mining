---
field: fnd6_newqv1300_miiq
dataset: fundamental6
best_template: rank_level
best_sharpe: 0.87
best_fitness: 0.61
best_universe: TOP200
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 10
max_drawdown: 0.1143
ann_vol: 0.0697
hit_rate: 0.5393
rolling_sharpe_min: -0.657
rolling_sharpe_max: 3.298
top_merge_partner: anl4_afv4_dts_spe
redundancy_cluster: 51
negated_best_sharpe: 0.29
negated_best_template: rank_neg_delta
negated_best_fitness: 0.09
n_negated_sims: 10
direction_gap: -0.58
---
# fnd6_newqv1300_miiq (fundamental6)

*Noncontrolling Interest - Income Account*

## Signal Profile
- `rank(fnd6_newqv1300_miiq)`: S=0.87, F=0.61, T=3.3%, INFERIOR (TOP200)
- `rank(fnd6_newqv1300_miiq / close)`: S=0.83, F=0.57, T=3.3%, INFERIOR (TOP200)
- `rank(ts_delta(fnd6_newqv1300_miiq, 5))`: S=0.36, F=0.15, T=36.8%, INFERIOR (TOP200)
- `-rank(fnd6_newqv1300_miiq)`: S=-0.24, F=-0.07, T=2.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_miiq, 5))`: S=0.29, F=0.09, T=36.3%, INFERIOR (TOP3000)
- `ts_zscore(fnd6_newqv1300_miiq, 22)`: S=0.16, F=0.04, T=35.7%, INFERIOR (TOP3000)
- `ts_mean(fnd6_newqv1300_miiq, 10)`: S=-0.33, F=-0.14, T=2.4%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd6_newqv1300_miiq, 22))`: S=-0.02, F=0.00, T=16.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_miiq)`: S=-0.21, F=-0.06, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_miiq / close)`: S=-0.20, F=-0.06, T=2.8%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/22P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 17F/12P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 0.87, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.67 (strong), ret=+7.3%
  - 2020: S=1.93 (strong), ret=+13.1%
  - 2021: S=0.01 (weak), ret=+0.1%
  - 2022: S=1.40 (moderate), ret=+10.8%
  - 2023: S=-0.29 (negative), ret=-1.5%

## Risk & Drawdown
- Max drawdown: 11.43% over 362 days (recovered)
- Annualized: return +6.1%, volatility 7.0% (fraction of booksize)
- Hit rate: 53.9% positive days
- Tail shape: skew -0.25, excess kurtosis +1.94

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.66, max 3.30, latest -0.32

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2023
Best month: +6.22%; worst month: -4.84%
Positive months: 58%

## Regime Profile
Regime profile: **mixed**
- Bull: S=1.31
- Sideways: S=1.29
- Bear: S=0.06

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd6_newqv1300_miiq, 5))` S=0.29, F=0.09, INFERIOR
Direction gap: -0.58 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd6_newqv1300_miiq)`: S=-0.21, F=-0.06, T=2.7%, INFERIOR (TOP3000)
- `rank(-1 * fnd6_newqv1300_miiq / close)`: S=-0.20, F=-0.06, T=2.8%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd6_newqv1300_miiq, 5))`: S=0.29, F=0.09, T=36.3%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd6_newqv1300_miiq)` | TOP200 | 0.87 | 0.61 | 11.4% | 80% | mixed |
| `rank(fnd6_newqv1300_miiq / close)` | TOP200 | 0.83 | 0.57 | 11.4% | 60% | mixed |
| `rank(fnd6_newqv1300_miiq / close)` | TOP3000 | 0.48 | 0.21 | 13.9% | 80% | bull-only |
| `rank(fnd6_newqv1300_miiq)` | TOP3000 | 0.43 | 0.18 | 14.8% | 80% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_miiq, 5))` | TOP200 | 0.35 | 0.15 | 20.2% | 100% | mixed |
| `rank(fnd6_newqv1300_miiq / close)` | TOP1000 | 0.30 | 0.10 | 11.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_miiq)` | TOP1000 | 0.24 | 0.07 | 12.0% | 60% | bull-only |
| `rank(fnd6_newqv1300_miiq / close)` | TOP500 | 0.18 | 0.06 | 12.5% | 60% | bull-only |
| `rank(fnd6_newqv1300_miiq)` | TOP500 | 0.20 | 0.06 | 12.4% | 60% | bull-only |
| `rank(ts_delta(fnd6_newqv1300_miiq, 5))` | TOP1000 | 0.20 | 0.04 | 25.1% | 40% | mixed |

## Correlation Notes
Top correlates:
- fnd6_newqv1300_cimiiq: 0.802 (strongly positively correlated)
- fnd6_newa2v1300_mii: 0.629 (moderately positively correlated)
- fnd6_newa1v1300_fincf: -0.366 (weakly negatively correlated)
- cashflow_fin: -0.365 (weakly negatively correlated)
- fn_antidilutive_securities_excl_from_eps_a: -0.364 (weakly negatively correlated)

Redundancy cluster #51: 2 similar fields, mean |rho| 0.802 (representative). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_afv4_dts_spe | analyst4 | -0.29 | 1.56 | +0.56 | +0.21 | yes |
| parkinson_volatility_120 | option8 | -0.25 | 1.43 | +0.54 | +0.16 | yes |
| fn_def_tax_assets_liab_net_a | fundamental2 | -0.27 | 1.33 | +0.42 | -0.75 | yes |
| news_open_vol | news12 | -0.20 | 1.42 | +0.49 | +0.60 | yes |
| parkinson_volatility_90 | option8 | -0.17 | 1.37 | +0.48 | -0.14 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
