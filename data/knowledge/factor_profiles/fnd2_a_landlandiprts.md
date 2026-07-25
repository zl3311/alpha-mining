---
field: fnd2_a_landlandiprts
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.95
best_fitness: 0.58
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: bull-only
n_variations_with_pnl: 7
max_drawdown: 0.0728
ann_vol: 0.049
hit_rate: 0.4947
rolling_sharpe_min: -0.566
rolling_sharpe_max: 2.819
top_merge_partner: anl4_epsr_flag
redundancy_cluster: 1
negated_best_sharpe: 0.51
negated_best_template: rank_neg_delta
negated_best_fitness: 0.29
n_negated_sims: 10
direction_gap: -0.44
---
# fnd2_a_landlandiprts (fundamental2)

*Amount before accumulated depreciation and depletion of real estate held for productive use and additions or improvements to real estate held for productive use, examples include, but are not limited to, walkways, driveways, fences, and parking lots. Excludes land held for sale*

## Signal Profile
- `rank(fnd2_a_landlandiprts)`: S=0.36, F=0.16, T=0.7%, INFERIOR (TOP3000)
- `rank(fnd2_a_landlandiprts / close)`: S=0.95, F=0.58, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_delta(fnd2_a_landlandiprts, 5))`: S=0.35, F=0.14, T=34.7%, INFERIOR (TOP1000)
- `-rank(fnd2_a_landlandiprts)`: S=-0.26, F=-0.10, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_landlandiprts, 5))`: S=0.51, F=0.29, T=27.4%, INFERIOR (TOP3000)
- `-ts_zscore(fnd2_a_landlandiprts, 63)`: S=0.62, F=0.58, T=16.0%, INFERIOR (TOP3000)
- `ts_mean(fnd2_a_landlandiprts, 10)`: S=0.32, F=0.16, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_a_landlandiprts, 22))`: S=-0.32, F=-0.14, T=15.2%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_landlandiprts)`: S=-0.22, F=-0.09, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_landlandiprts / close)`: S=-0.06, F=-0.01, T=1.9%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/8P
- LOW_TURNOVER: 3F/29P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.93, Consistency 100% positive years (5/5)
Yearly breakdown:
  - 2019: S=0.75 (moderate), ret=+2.8%
  - 2020: S=0.28 (weak), ret=+1.7%
  - 2021: S=1.25 (moderate), ret=+6.8%
  - 2022: S=2.31 (strong), ret=+11.0%
  - 2023: S=0.06 (weak), ret=+0.2%

## Risk & Drawdown
- Max drawdown: 7.28% over 294 days (recovered)
- Annualized: return +4.6%, volatility 4.9% (fraction of booksize)
- Hit rate: 49.5% positive days
- Tail shape: skew +0.45, excess kurtosis +1.83

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.57, max 2.82, latest 0.06

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2023
Best month: +4.93%; worst month: -2.30%
Positive months: 56%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=2.62
- Sideways: S=0.91
- Bear: S=-0.98

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_a_landlandiprts, 5))` S=0.51, F=0.29, INFERIOR
Direction gap: -0.44 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fnd2_a_landlandiprts)`: S=-0.22, F=-0.09, T=1.6%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_a_landlandiprts / close)`: S=-0.06, F=-0.01, T=1.9%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_a_landlandiprts, 5))`: S=0.51, F=0.29, T=27.4%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_a_landlandiprts / close)` | TOP3000 | 0.93 | 0.58 | 7.3% | 100% | bull-only |
| `rank(fnd2_a_landlandiprts / close)` | TOP1000 | 0.40 | 0.19 | 10.1% | 40% | bull-only |
| `rank(fnd2_a_landlandiprts)` | TOP3000 | 0.35 | 0.16 | 26.2% | 80% | bull-only |
| `rank(ts_delta(fnd2_a_landlandiprts, 5))` | TOP1000 | 0.34 | 0.14 | 18.8% | 60% | mixed |
| `rank(fnd2_a_landlandiprts)` | TOP1000 | 0.26 | 0.10 | 21.3% | 60% | bull-only |
| `rank(fnd2_a_landlandiprts)` | TOP200 | 0.22 | 0.09 | 22.2% | 60% | bull-only |
| `rank(ts_delta(fnd2_a_landlandiprts, 5))` | TOP500 | 0.07 | 0.02 | 29.4% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_a_blgandiprtsg: 0.890 (strongly positively correlated)
- fnd6_intpn: 0.833 (strongly positively correlated)
- fnd2_dfctrbplancstrg: 0.833 (strongly positively correlated)
- fn_debt_instrument_carrying_amount_a: 0.831 (strongly positively correlated)
- fnd6_newa1v1300_lt: 0.825 (strongly positively correlated)

Redundancy cluster #1: 232 similar fields, mean |rho| 0.81 (representative: min_adjusted_net_income_guidance). Members are largely interchangeable -- self-correlation risk, not blend partners.

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_epsr_flag | analyst4 | -0.31 | 1.70 | +0.52 | -0.54 | yes |
| anl4_rd_exp_flag | analyst4 | -0.28 | 1.50 | +0.47 | -0.64 | yes |
| net_profit_adjusted_min_guidance | analyst4 | -0.20 | 1.42 | +0.47 | -0.64 | yes |
| rp_ess_revenue | news18 | -0.31 | 1.39 | +0.46 | -0.48 | yes |
| pv13_ompetitorgraphrank_hub_rank | pv13 | -0.22 | 1.61 | +0.46 | -0.34 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
