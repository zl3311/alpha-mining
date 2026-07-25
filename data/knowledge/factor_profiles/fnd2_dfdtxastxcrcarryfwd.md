---
field: fnd2_dfdtxastxcrcarryfwd
dataset: fundamental2
best_template: rank_value_norm
best_sharpe: 0.77
best_fitness: 0.49
best_universe: TOP500
grade: INFERIOR
submittability: blocked_LOW_SHARPE
n_sims: 26
regime_profile: bull-only
n_variations_with_pnl: 9
max_drawdown: 0.0887
ann_vol: 0.0661
hit_rate: 0.5134
rolling_sharpe_min: -1.049
rolling_sharpe_max: 2.294
negated_best_sharpe: 0.22
negated_best_template: rank_neg_delta
negated_best_fitness: 0.07
n_negated_sims: 4
direction_gap: -0.55
---
# fnd2_dfdtxastxcrcarryfwd (fundamental2)

*Amount, before allocation of a valuation allowance, of deferred tax assets attributable to deductible tax credit carryforwards including, but not limited to, research, foreign, general business, alternative minimum tax, and other deductible tax credit carryforwards*

## Signal Profile
- `rank(fnd2_dfdtxastxcrcarryfwd)`: S=0.80, F=0.45, T=0.8%, INFERIOR (TOP3000)
- `rank(fnd2_dfdtxastxcrcarryfwd / close)`: S=0.77, F=0.49, T=1.8%, INFERIOR (TOP500)
- `rank(ts_delta(fnd2_dfdtxastxcrcarryfwd, 5))`: S=0.55, F=0.31, T=31.1%, INFERIOR (TOP500)
- `-rank(fnd2_dfdtxastxcrcarryfwd)`: S=-0.17, F=-0.05, T=1.4%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxastxcrcarryfwd, 5))`: S=0.22, F=0.07, T=32.9%, INFERIOR (TOP3000)
- `ts_zscore(fnd2_dfdtxastxcrcarryfwd, 22)`: S=0.07, F=0.02, T=15.0%, INFERIOR (TOP3000)
- `ts_mean(fnd2_dfdtxastxcrcarryfwd, 10)`: S=-0.67, F=-0.49, T=0.8%, INFERIOR (TOP3000)
- `rank(ts_rank(fnd2_dfdtxastxcrcarryfwd, 22))`: S=0.09, F=0.02, T=16.3%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxastxcrcarryfwd)`: S=-0.80, F=-0.45, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxastxcrcarryfwd / close)`: S=-0.77, F=-0.45, T=1.2%, INFERIOR (TOP3000)

## Check Summary
- CONCENTRATED_WEIGHT: 10F/16P
- LOW_FITNESS: 26F/0P
- LOW_SHARPE: 26F/0P
- LOW_SUB_UNIVERSE_SHARPE: 9F/14P
- LOW_TURNOVER: 3F/23P

## Temporal Behavior
Headline (rank_value_norm): Overall Sharpe 0.78, Consistency 80% positive years (4/5)
Yearly breakdown:
  - 2019: S=1.43 (moderate), ret=+6.3%
  - 2020: S=-0.39 (negative), ret=-2.6%
  - 2021: S=0.43 (weak), ret=+3.9%
  - 2022: S=1.66 (strong), ret=+10.2%
  - 2023: S=1.52 (strong), ret=+7.4%

## Risk & Drawdown
- Max drawdown: 8.87% over 545 days (recovered)
- Annualized: return +5.1%, volatility 6.6% (fraction of booksize)
- Hit rate: 51.3% positive days
- Tail shape: skew +0.03, excess kurtosis +1.69

## Rolling Sharpe
Rolling 1-year Sharpe (headline curve): min -1.05, max 2.29, latest 1.59

## Yearly & Monthly Returns
Best year (by Sharpe): 2022; worst year: 2020
Best month: +6.86%; worst month: -4.56%
Positive months: 58%

## Regime Profile
Regime profile: **bull-only**
- Bull: S=1.98
- Sideways: S=1.39
- Bear: S=-1.03

## Negated Direction
Best negated: `rank(-1 * ts_delta(fnd2_dfdtxastxcrcarryfwd, 5))` S=0.22, F=0.07, INFERIOR
Direction gap: -0.55 (negated - positive best Sharpe). Positive direction dominant.

Negated template variants:
- `rank(-1 * fnd2_dfdtxastxcrcarryfwd)`: S=-0.80, F=-0.45, T=0.8%, INFERIOR (TOP3000)
- `rank(-1 * fnd2_dfdtxastxcrcarryfwd / close)`: S=-0.77, F=-0.45, T=1.2%, INFERIOR (TOP3000)
- `rank(-1 * ts_delta(fnd2_dfdtxastxcrcarryfwd, 5))`: S=0.22, F=0.07, T=32.9%, INFERIOR (TOP3000)

## Variation Breakdown
| Expression | Universe | S | F | MaxDD | Consist | Regime |
|---|---|---|---|---|---|---|
| `rank(fnd2_dfdtxastxcrcarryfwd / close)` | TOP500 | 0.78 | 0.49 | 8.9% | 80% | bull-only |
| `rank(fnd2_dfdtxastxcrcarryfwd / close)` | TOP3000 | 0.76 | 0.45 | 8.8% | 80% | all-weather |
| `rank(fnd2_dfdtxastxcrcarryfwd)` | TOP3000 | 0.79 | 0.45 | 10.9% | 80% | bull-only |
| `rank(ts_delta(fnd2_dfdtxastxcrcarryfwd, 5))` | TOP500 | 0.56 | 0.31 | 20.8% | 80% | mixed |
| `rank(fnd2_dfdtxastxcrcarryfwd / close)` | TOP1000 | 0.57 | 0.29 | 7.0% | 80% | mixed |
| `rank(ts_delta(fnd2_dfdtxastxcrcarryfwd, 5))` | TOP200 | 0.40 | 0.24 | 33.4% | 40% | mixed |
| `rank(fnd2_dfdtxastxcrcarryfwd / close)` | TOP200 | 0.27 | 0.12 | 17.6% | 80% | bull-only |
| `rank(fnd2_dfdtxastxcrcarryfwd)` | TOP500 | 0.15 | 0.05 | 28.2% | 80% | bull-only |
| `rank(fnd2_dfdtxastxcrcarryfwd)` | TOP1000 | 0.16 | 0.05 | 21.1% | 80% | bull-only |

## Correlation Notes
Top correlates:
- fnd6_newa2v1300_stkco: 0.729 (strongly positively correlated)
- fnd6_ch: 0.704 (strongly positively correlated)
- fnd6_newa1v1300_che: 0.701 (strongly positively correlated)
- fnd6_newqv1300_chq: 0.662 (moderately positively correlated)
- fnd6_mfmq_cheq: 0.653 (moderately positively correlated)

## Merge Candidates
No positive-diversification merge partners found (Sharpe >= 0.8 pool).

## Actionability
Blocked by LOW_SHARPE. Consider template changes or neutralization adjustment.
Untried templates: decay_linear, trade_when
