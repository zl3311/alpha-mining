---
field: fn_finite_lived_intangible_assets_net_q
dataset: fundamental2
best_template: neg_rank_value_norm
best_sharpe: 0.69
best_fitness: 0.61
best_universe: TOP3000
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 4
max_drawdown: 0.1611
ann_vol: 0.1017
hit_rate: 0.5093
rolling_sharpe_min: -1.659
rolling_sharpe_max: 2.818
top_merge_partner: anl4_fcf_low
negated_best_sharpe: 0.69
negated_best_template: neg_rank_value_norm
negated_best_fitness: 0.61
n_negated_sims: 10
direction_gap: -0.16
---
# fn_finite_lived_intangible_assets_net_q (fundamental2)

*Finite Lived Intangible Assets, Net*

## Signal Profile
- `rank(fn_finite_lived_intangible_assets_net_q)`: S=0.12, F=0.03, T=0.8%, INFERIOR (TOP3000)
- `rank(fn_finite_lived_intangible_assets_net_q / close)`: S=0.10, F=0.02, T=1.1%, INFERIOR (TOP3000)
- `rank(ts_delta(fn_finite_lived_intangible_assets_net_q, 5))`: S=0.85, F=0.42, T=35.4%, INFERIOR (TOP3000)
- `-rank(fn_finite_lived_intangible_assets_net_q)`: S=0.02, F=0.00, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_finite_lived_intangible_assets_net_q, 5))`: S=0.58, F=0.32, T=37.2%, INFERIOR (TOP3000)
- `-ts_zscore(fn_finite_lived_intangible_assets_net_q, 63)`: S=0.66, F=0.35, T=18.6%, INFERIOR (TOP3000)
- `ts_mean(fn_finite_lived_intangible_assets_net_q, 10)`: S=-0.11, F=-0.03, T=1.0%, INFERIOR (TOP3000)
- `rank(ts_rank(fn_finite_lived_intangible_assets_net_q, 22))`: S=0.21, F=0.06, T=16.8%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_net_q)`: S=0.54, F=0.44, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_net_q / close)`: S=0.69, F=0.61, T=2.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 15F/5P
- LOW_TURNOVER: 2F/30P

## Temporal Behavior
Headline (rank_delta): Overall Sharpe 0.83, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.50 (moderate), ret=+4.3%
  - 2020: S=1.50 (strong), ret=+16.3%
  - 2021: S=0.43 (weak), ret=+3.8%
  - 2022: S=-0.53 (negative), ret=-6.0%
  - 2023: S=2.38 (strong), ret=+22.9%

## Risk & Drawdown
- Max drawdown: 16.11% over 383 days (recovered)
- Annualized: return +8.4%, volatility 10.2% (fraction of booksize)
- Hit rate: 50.9% positive days
- Tail shape: skew +0.24, excess kurtosis +3.93

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.66, max 2.82, latest 2.47

## Yearly & Monthly Returns
Best year (by Sharpe): 2023; worst year: 2022
Best month: +7.27%; worst month: -6.83%
Positive months: 61%

## Regime Profile
Regime profile: **mixed**
- Bull: S=-0.29
- Sideways: S=0.56
- Bear: S=2.10

## Negated Direction
Best negated: `rank(-1 * fn_finite_lived_intangible_assets_net_q / close)` S=0.69, F=0.61, INFERIOR
Direction gap: -0.16 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * fn_finite_lived_intangible_assets_net_q)`: S=0.54, F=0.44, T=2.0%, INFERIOR (TOP3000)
- `rank(-1 * fn_finite_lived_intangible_assets_net_q / close)`: S=0.69, F=0.61, T=2.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fn_finite_lived_intangible_assets_net_q, 5))`: S=0.58, F=0.32, T=37.2%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(ts_delta(fn_finite_lived_intangible_assets_net_q, 5))` | TOP3000 | 0.83 | 0.42 | 16.1% | 80% | mixed |
| `rank(ts_delta(fn_finite_lived_intangible_assets_net_q, 5))` | TOP1000 | 0.31 | 0.10 | 24.7% | 40% | bear-only |
| `rank(fn_finite_lived_intangible_assets_net_q)` | TOP3000 | 0.11 | 0.03 | 23.4% | 60% | bull-only |
| `rank(fn_finite_lived_intangible_assets_net_q / close)` | TOP3000 | 0.10 | 0.02 | 10.9% | 60% | bull-only |

## Correlation Notes
Top correlates:
- fnd2_q_flintasamt1expythree: 0.161 (weakly positively correlated)
- parkinson_volatility_90: 0.160 (weakly positively correlated)
- fnd6_newqv1300_intanoq: 0.143 (weakly positively correlated)
- implied_volatility_call_30 - implied_volatility_call_270: 0.143 (weakly positively correlated)
- fnd2_q_flintasamt1expyfour: 0.143 (weakly positively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| anl4_fcf_low | analyst4 | -0.11 | 1.24 | +0.40 | -0.62 | yes |
| rp_ess_mna | news18 | -0.04 | 1.20 | +0.36 | -0.88 | yes |
| fnd6_newqv1300_xoprq | fundamental6 | -0.10 | 1.24 | +0.40 | -0.48 | yes |
| operating_expense | fundamental6 | -0.10 | 1.24 | +0.40 | -0.48 | yes |
| fnd6_newqv1300_xsgaq | fundamental6 | -0.09 | 1.22 | +0.39 | -0.54 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
