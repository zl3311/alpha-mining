---
field: anl4_rd_exp_flag
dataset: analyst4
best_template: rank_level
best_sharpe: 1.02
best_fitness: 0.93
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 32
regime_profile: mixed
n_variations_with_pnl: 6
max_drawdown: 0.1585
ann_vol: 0.1034
hit_rate: 0.532
rolling_sharpe_min: -0.931
rolling_sharpe_max: 3.421
top_merge_partner: fnd6_txs
negated_best_sharpe: 0.66
negated_best_template: rank_neg_delta
negated_best_fitness: 0.69
n_negated_sims: 10
direction_gap: -0.36
---
# anl4_rd_exp_flag (analyst4)

*Research and Development Expense - forecast type (revision/new/...)*

## Signal Profile
- `rank(anl4_rd_exp_flag)`: S=1.02, F=0.93, T=2.6%, INFERIOR (TOP500)
- `rank(anl4_rd_exp_flag / close)`: S=0.21, F=0.09, T=2.6%, INFERIOR (TOP200)
- `rank(ts_delta(anl4_rd_exp_flag, 5))`: S=-0.01, F=0.00, T=16.6%, INFERIOR (TOP200)
- `-rank(anl4_rd_exp_flag)`: S=-0.35, F=-0.17, T=2.3%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_rd_exp_flag, 5))`: S=0.66, F=0.69, T=21.6%, INFERIOR (TOP3000)
- `-ts_zscore(anl4_rd_exp_flag, 63)`: S=-0.07, F=-0.04, T=10.5%, INFERIOR (TOP3000)
- `ts_mean(anl4_rd_exp_flag, 10)`: S=0.35, F=0.17, T=2.2%, INFERIOR (TOP3000)
- `rank(ts_rank(anl4_rd_exp_flag, 22))`: S=0.53, F=0.57, T=17.2%, INFERIOR (TOP3000)
- `rank(-1 * anl4_rd_exp_flag)`: S=-1.02, F=-0.93, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_rd_exp_flag / close)`: S=-0.14, F=-0.05, T=2.5%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 12F/20P
- LOW_FITNESS: 32F/0P
- LOW_SHARPE: 32F/0P
- LOW_SUB_UNIVERSE_SHARPE: 12F/17P

## Temporal Behavior
Headline (rank_level): Overall Sharpe 1.02, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=0.31 (weak), ret=+1.9%
  - 2020: S=3.06 (strong), ret=+30.2%
  - 2021: S=0.95 (moderate), ret=+11.3%
  - 2022: S=-0.07 (negative), ret=-0.9%
  - 2023: S=1.09 (moderate), ret=+9.5%

## Risk & Drawdown
- Max drawdown: 15.85% over 566 days (recovered)
- Annualized: return +10.6%, volatility 10.3% (fraction of booksize)
- Hit rate: 53.2% positive days
- Tail shape: skew +0.40, excess kurtosis +4.58

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -0.93, max 3.42, latest 1.10

## Yearly & Monthly Returns
Best year (by Sharpe): 2020; worst year: 2022
Best month: +8.16%; worst month: -6.75%
Positive months: 64%

## Regime Profile
Regime profile: **mixed**
- Bull: S=0.04
- Sideways: S=0.68
- Bear: S=2.81

## Negated Direction
Best negated: `rank(-1 * ts_delta(anl4_rd_exp_flag, 5))` S=0.66, F=0.69, INFERIOR
Direction gap: -0.36 (negated - positive best Sharpe). Positive direction slightly better.

Negated template variants:
- `rank(-1 * anl4_rd_exp_flag)`: S=-1.02, F=-0.93, T=2.6%, INFERIOR (TOP3000)
- `rank(-1 * anl4_rd_exp_flag / close)`: S=-0.14, F=-0.05, T=2.5%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(anl4_rd_exp_flag, 5))`: S=0.66, F=0.69, T=21.6%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(anl4_rd_exp_flag)` | TOP500 | 1.02 | 0.93 | 15.8% | 80% | mixed |
| `rank(anl4_rd_exp_flag)` | TOP1000 | 0.36 | 0.17 | 16.2% | 60% | bear-only |
| `rank(anl4_rd_exp_flag)` | TOP200 | 0.22 | 0.10 | 46.1% | 40% | bear-only |
| `rank(anl4_rd_exp_flag / close)` | TOP200 | 0.22 | 0.09 | 24.5% | 60% | bear-only |
| `rank(anl4_rd_exp_flag / close)` | TOP500 | 0.14 | 0.05 | 33.5% | 80% | bear-only |
| `rank(anl4_rd_exp_flag / close)` | TOP1000 | 0.09 | 0.03 | 39.9% | 40% | bear-only |

## Correlation Notes
Top correlates:
- cash_flow_from_financing: 0.577 (moderately positively correlated)
- est_cashflow_fin: 0.574 (moderately positively correlated)
- anl4_af_div_value: -0.568 (moderately negatively correlated)
- fnd2_a_sbcpnargmtwfsptepddvdrt: -0.558 (moderately negatively correlated)
- fnd6_newqv1300_cstkq: -0.555 (moderately negatively correlated)

## Merge Candidates
Top blend partners (equal-weight screening estimate; verify with a sim + self-corr check):

| Partner | Family | rho | S_comb | div+ | temporal_rho | cross-family |
|---|---|---|---|---|---|---|
| fnd6_txs | fundamental6 | -0.52 | 1.90 | +0.87 | -0.73 | yes |
| fnd6_dn | fundamental6 | -0.51 | 1.88 | +0.86 | -0.82 | yes |
| implied_volatility_mean_skew_180 | option8 | -0.42 | 1.90 | +0.83 | -0.98 | yes |
| fnd2_currstatelocaltxexp | fundamental2 | -0.52 | 1.86 | +0.84 | -0.92 | yes |
| fnd6_newa1v1300_dpact | fundamental6 | -0.41 | 1.89 | +0.86 | -0.58 | yes |

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
