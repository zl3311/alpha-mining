---
type: factor_merge_candidates
generated: '2026-06-15'
method: field-level equal-weight PnL blend screen (headline curve per field)
min_standalone_sharpe: 0.8
n_pairs: 40
n_triples: 15
caveat: S_combined is an equal-weight screening estimate; a real BRAIN blend re-ranks/re-neutralizes.
  Verify with a sim + self-corr check before submission.
---
# Factor Merge Candidates (cross-family blend sources)

Ranked decorrelated / temporally complementary factor pairs where both members are standalone Sharpe >= 0.8 and come from different families. `S_combined` is an equal-weight screening estimate (see caveat).

## Top Pairs

| A | B | Families | S_a | S_b | rho | S_comb | div+ | temporal_rho | blend |
|---|---|---|---|---|---|---|---|---|---|
| implied_volatility_mean_skew_1080 | news_open_vol | option8/news12 | 1.02 | 0.93 | -0.60 | 2.08 | +1.07 | -0.35 | `ts_decay_linear((rank(implied_volatility_mean_skew_1080)) + (rank(news_open_vol)), 5)` |
| implied_volatility_mean_skew_720 | news_open_vol | option8/news12 | 1.01 | 0.93 | -0.60 | 2.09 | +1.07 | -0.28 | `ts_decay_linear((rank(implied_volatility_mean_skew_720)) + (rank(news_open_vol)), 5)` |
| implied_volatility_mean_skew_360 | news_open_vol | option8/news12 | 1.10 | 0.93 | -0.58 | 2.20 | +1.10 | +0.12 | `ts_decay_linear((rank(implied_volatility_mean_skew_360)) + (rank(news_open_vol)), 5)` |
| implied_volatility_mean_skew_270 | news_open_vol | option8/news12 | 1.03 | 0.93 | -0.56 | 2.09 | +1.06 | +0.17 | `ts_decay_linear((rank(implied_volatility_mean_skew_270)) + (rank(news_open_vol)), 5)` |
| rank(scl12_buzz * (-1 * returns)) | anl4_bvps_flag | socialmedia12/analyst_revision | 1.63 | 1.30 | -0.34 | 2.55 | +0.93 | -0.76 | `ts_decay_linear((rank(scl12_buzz * (-1 * returns))) + (rank(anl4_bvps_flag)), 5)` |
| rank(fnd6_acdo) + rank(open/close - 1) | anl4_bvps_flag | unknown/analyst_revision | 2.02 | 1.30 | -0.35 | 2.96 | +0.93 | -0.68 | `ts_decay_linear((rank(fnd6_acdo) + rank(open/close - 1)) + (rank(anl4_bvps_flag)), 5)` |
| implied_volatility_mean_skew_180 | news_open_vol | option8/news12 | 1.06 | 0.93 | -0.53 | 2.06 | +0.99 | +0.15 | `ts_decay_linear((rank(implied_volatility_mean_skew_180)) + (rank(news_open_vol)), 5)` |
| fnd6_cptmfmq_dlttq | anl4_epsr_flag | fundamental6/analyst4 | 1.19 | 1.18 | -0.36 | 2.07 | +0.89 | -0.84 | `ts_decay_linear((rank(fnd6_cptmfmq_dlttq / close)) + (rank(anl4_epsr_flag)), 5)` |
| debt_lt | anl4_epsr_flag | fundamental6/analyst4 | 1.20 | 1.18 | -0.36 | 2.08 | +0.88 | -0.84 | `ts_decay_linear((rank(debt_lt / close)) + (rank(anl4_epsr_flag)), 5)` |
| fnd6_cptnewqv1300_dlttq | anl4_epsr_flag | fundamental6/analyst4 | 1.20 | 1.18 | -0.36 | 2.08 | +0.88 | -0.84 | `ts_decay_linear((rank(fnd6_cptnewqv1300_dlttq / close)) + (rank(anl4_epsr_flag)), 5)` |
| rank(fnd6_acdo) + rank(open/close - 1) | rel_num_all | unknown/pv13 | 2.02 | 1.22 | -0.36 | 2.90 | +0.88 | -0.74 | `ts_decay_linear((rank(fnd6_acdo) + rank(open/close - 1)) + (rank(rel_num_all)), 5)` |
| anl4_rd_exp_flag | fnd6_txs | analyst4/fundamental6 | 1.02 | 0.84 | -0.52 | 1.90 | +0.87 | -0.73 | `ts_decay_linear((rank(anl4_rd_exp_flag)) + (rank(fnd6_txs / close)), 5)` |
| fnd6_newa1v1300_dltt | anl4_epsr_flag | fundamental6/analyst4 | 1.20 | 1.18 | -0.36 | 2.07 | +0.87 | -0.71 | `ts_decay_linear((rank(fnd6_newa1v1300_dltt / close)) + (rank(anl4_epsr_flag)), 5)` |
| rank(fnd6_acdo) * rank(-1 * returns) | anl4_bvps_flag | unknown/analyst_revision | 1.87 | 1.30 | -0.33 | 2.74 | +0.87 | -0.73 | `ts_decay_linear((rank(fnd6_acdo) * rank(-1 * returns)) + (rank(anl4_bvps_flag)), 5)` |
| rank(scl12_buzz * (-1 * returns)) | rel_num_all | socialmedia12/pv13 | 1.63 | 1.22 | -0.34 | 2.49 | +0.86 | -0.83 | `ts_decay_linear((rank(scl12_buzz * (-1 * returns))) + (rank(rel_num_all)), 5)` |
| news_open_vol | implied_volatility_mean_skew_150 | news12/option8 | 0.93 | 0.85 | -0.55 | 1.86 | +0.94 | +0.05 | `ts_decay_linear((rank(news_open_vol)) + (rank(implied_volatility_mean_skew_150)), 5)` |
| anl4_rd_exp_flag | fnd6_dn | analyst4/fundamental6 | 1.02 | 0.89 | -0.51 | 1.88 | +0.86 | -0.82 | `ts_decay_linear((rank(anl4_rd_exp_flag)) + (rank(fnd6_dn / close)), 5)` |
| implied_volatility_mean_skew_180 | anl4_rd_exp_flag | option8/analyst4 | 1.06 | 1.02 | -0.42 | 1.90 | +0.83 | -0.98 | `ts_decay_linear((rank(implied_volatility_mean_skew_180)) + (rank(anl4_rd_exp_flag)), 5)` |
| anl4_rd_exp_flag | fnd2_currstatelocaltxexp | analyst4/fundamental2 | 1.02 | 0.84 | -0.52 | 1.86 | +0.84 | -0.92 | `ts_decay_linear((rank(anl4_rd_exp_flag)) + (rank(fnd2_currstatelocaltxexp / close)), 5)` |
| anl4_bvps_flag | anl4_afv4_dts_spe | analyst_revision/analyst4 | 1.30 | 1.00 | -0.48 | 2.21 | +0.90 | -0.27 | `ts_decay_linear((rank(anl4_bvps_flag)) + (rank(anl4_afv4_dts_spe / close)), 5)` |
| fnd6_newa1v1300_dpact | anl4_rd_exp_flag | fundamental6/analyst4 | 1.03 | 1.02 | -0.41 | 1.89 | +0.86 | -0.58 | `ts_decay_linear((rank(fnd6_newa1v1300_dpact / close)) + (rank(anl4_rd_exp_flag)), 5)` |
| fnd6_dpvieb | anl4_rd_exp_flag | fundamental6/analyst4 | 1.04 | 1.02 | -0.41 | 1.90 | +0.86 | -0.58 | `ts_decay_linear((rank(fnd6_dpvieb / close)) + (rank(anl4_rd_exp_flag)), 5)` |
| implied_volatility_mean_skew_180 | anl4_afv4_dts_spe | option8/analyst4 | 1.06 | 1.00 | -0.47 | 1.98 | +0.92 | -0.01 | `ts_decay_linear((rank(implied_volatility_mean_skew_180)) + (rank(anl4_afv4_dts_spe / close)), 5)` |
| rank(scl12_buzz * (-1 * returns)) | anl4_netdebt_flag | socialmedia12/analyst_revision | 1.63 | 1.28 | -0.31 | 2.48 | +0.85 | -0.60 | `ts_decay_linear((rank(scl12_buzz * (-1 * returns))) + (rank(anl4_netdebt_flag)), 5)` |
| implied_volatility_mean_skew_270 | anl4_rd_exp_flag | option8/analyst4 | 1.03 | 1.02 | -0.43 | 1.83 | +0.81 | -0.97 | `ts_decay_linear((rank(implied_volatility_mean_skew_270)) + (rank(anl4_rd_exp_flag)), 5)` |
| rank(scl12_buzz * (-1 * returns)) | anl4_ptpr_flag | socialmedia12/analyst_revision | 1.63 | 1.28 | -0.31 | 2.45 | +0.82 | -0.79 | `ts_decay_linear((rank(scl12_buzz * (-1 * returns))) + (rank(anl4_ptpr_flag)), 5)` |
| anl4_epsr_flag | fnd6_dd1q | analyst4/fundamental6 | 1.18 | 1.12 | -0.35 | 1.98 | +0.81 | -0.96 | `ts_decay_linear((rank(anl4_epsr_flag)) + (rank(fnd6_dd1q / close)), 5)` |
| rank(fnd6_acdo) + rank(open/close - 1) | anl4_netdebt_flag | unknown/analyst_revision | 2.02 | 1.28 | -0.33 | 2.87 | +0.85 | -0.46 | `ts_decay_linear((rank(fnd6_acdo) + rank(open/close - 1)) + (rank(anl4_netdebt_flag)), 5)` |
| anl4_epsr_flag | fn_accrued_liab_q | analyst4/fundamental2 | 1.18 | 1.16 | -0.35 | 2.02 | +0.85 | -0.50 | `ts_decay_linear((rank(anl4_epsr_flag)) + (rank(fn_accrued_liab_q / close)), 5)` |
| fnd6_newa1v1300_cogs | anl4_epsr_flag | fundamental6/analyst4 | 1.18 | 1.18 | -0.35 | 2.04 | +0.86 | -0.34 | `ts_decay_linear((rank(fnd6_newa1v1300_cogs / close)) + (rank(anl4_epsr_flag)), 5)` |
| anl4_rd_exp_flag | fn_accum_depr_depletion_and_amortization_ppne_q | analyst4/fundamental2 | 1.02 | 0.99 | -0.42 | 1.86 | +0.83 | -0.63 | `ts_decay_linear((rank(anl4_rd_exp_flag)) + (rank(fn_accum_depr_depletion_and_amortization_ppne_q / close)), 5)` |
| fnd6_newqv1300_ppegtq | anl4_epsr_flag | fundamental6/analyst4 | 1.26 | 1.18 | -0.32 | 2.08 | +0.82 | -0.69 | `ts_decay_linear((rank(fnd6_newqv1300_ppegtq / close)) + (rank(anl4_epsr_flag)), 5)` |
| fnd6_fatl | anl4_epsr_flag | fundamental_capital_intensity/analyst4 | 1.24 | 1.18 | -0.34 | 2.07 | +0.83 | -0.59 | `ts_decay_linear((rank(fnd6_fatl / close)) + (rank(anl4_epsr_flag)), 5)` |
| fnd6_newqv1300_dpactq | anl4_rd_exp_flag | fundamental_depreciation/analyst4 | 1.29 | 1.02 | -0.40 | 2.10 | +0.81 | -0.76 | `ts_decay_linear((rank(fnd6_newqv1300_dpactq / close)) + (rank(anl4_rd_exp_flag)), 5)` |
| fnd6_fate | anl4_epsr_flag | fundamental_capital_intensity/analyst4 | 1.25 | 1.18 | -0.32 | 2.08 | +0.84 | -0.50 | `ts_decay_linear((rank(fnd6_fate / close)) + (rank(anl4_epsr_flag)), 5)` |
| rank(fnd6_acdo) * rank(-1 * returns) | rel_num_all | unknown/pv13 | 1.87 | 1.22 | -0.33 | 2.67 | +0.80 | -0.79 | `ts_decay_linear((rank(fnd6_acdo) * rank(-1 * returns)) + (rank(rel_num_all)), 5)` |
| implied_volatility_mean_skew_1080 | fnd6_cshtr | option8/fundamental6 | 1.02 | 1.01 | -0.41 | 1.87 | +0.86 | -0.26 | `ts_decay_linear((rank(implied_volatility_mean_skew_1080)) + (rank(fnd6_cshtr)), 5)` |
| rank(fnd6_acdo) + rank(open/close - 1) | anl4_ptpr_flag | unknown/analyst_revision | 2.02 | 1.28 | -0.32 | 2.83 | +0.81 | -0.74 | `ts_decay_linear((rank(fnd6_acdo) + rank(open/close - 1)) + (rank(anl4_ptpr_flag)), 5)` |
| fnd6_dlto | anl4_epsr_flag | fundamental_debt/analyst4 | 1.34 | 1.18 | -0.38 | 2.17 | +0.84 | -0.41 | `ts_decay_linear((rank(fnd6_dlto / close)) + (rank(anl4_epsr_flag)), 5)` |
| anl4_epsr_flag | debt | analyst4/fundamental6 | 1.18 | 1.08 | -0.35 | 1.97 | +0.79 | -0.85 | `ts_decay_linear((rank(anl4_epsr_flag)) + (rank(debt / close)), 5)` |

## Top Triples

| A | B | C | Families | S_comb | div+ | max_pair_rho |
|---|---|---|---|---|---|---|
| rank(fnd6_acdo) + rank(open/close - 1) | anl4_bvps_flag | fnd6_itci | unknown/analyst_revision/fundamental_tax_credit | 3.36 | +1.34 | -0.35 |
| rank(scl12_buzz * (-1 * returns)) | fnd6_newqv1300_dpactq | anl4_epsr_flag | socialmedia12/fundamental_depreciation/analyst4 | 2.95 | +1.33 | -0.30 |
| rank(fnd6_acdo) + rank(open/close - 1) | anl4_ptpr_flag | fnd6_itci | unknown/analyst_revision/fundamental_tax_credit | 3.33 | +1.31 | -0.32 |
| rank(fnd6_acdo) + rank(open/close - 1) | anl4_netdebt_flag | fnd6_itci | unknown/analyst_revision/fundamental_tax_credit | 3.33 | +1.31 | -0.33 |
| anl4_bvps_flag | fn_comp_options_forfeitures_and_expirations_a | rank(fnd6_acdo) + rank(open/close - 1) | analyst_revision/fundamental2/unknown | 3.33 | +1.30 | -0.35 |
| rank(fnd6_acdo) + rank(open/close - 1) | rel_num_part | fnd6_itci | unknown/pv13/fundamental_tax_credit | 3.31 | +1.28 | -0.33 |
| rank(fnd6_acdo) + rank(open/close - 1) | rel_num_all | fnd6_itci | unknown/pv13/fundamental_tax_credit | 3.30 | +1.28 | -0.36 |
| fnd6_newqv1300_dpactq | anl4_epsr_flag | rank(fnd6_acdo) + rank(open/close - 1) | fundamental_depreciation/analyst4/unknown | 3.26 | +1.24 | -0.30 |
| rank(fnd6_acdo) + rank(open/close - 1) | rel_num_comp | fnd6_itci | unknown/pv13/fundamental_tax_credit | 3.25 | +1.22 | -0.36 |
| rel_num_all | fn_comp_options_forfeitures_and_expirations_a | rank(fnd6_acdo) + rank(open/close - 1) | pv13/fundamental2/unknown | 3.23 | +1.21 | -0.36 |
| anl4_netdebt_flag | fn_comp_options_forfeitures_and_expirations_a | rank(fnd6_acdo) + rank(open/close - 1) | analyst_revision/fundamental2/unknown | 3.22 | +1.20 | -0.33 |
| rank(scl12_buzz * (-1 * returns)) | anl4_totassets_flag | fnd6_acdo | socialmedia12/analyst_revision/fundamental_discontinued_ops | 2.82 | +1.19 | -0.22 |
| rank(fnd6_acdo) + rank(open/close - 1) | actuals_value_currency_code | fnd6_itci | unknown/data_artifact/fundamental_tax_credit | 3.21 | +1.19 | -0.28 |
| fnd6_fate | anl4_epsr_flag | rank(fnd6_acdo) + rank(open/close - 1) | fundamental_capital_intensity/analyst4/unknown | 3.19 | +1.17 | -0.32 |
| rank(fnd6_acdo) * rank(-1 * returns) | anl4_bvps_flag | fnd6_itci | unknown/analyst_revision/fundamental_tax_credit | 3.17 | +1.17 | -0.33 |

## Dead zone warnings

Some candidates above involve factors from known dead zones:
- **news12 (`news_open_vol`)**: dataset-news12 dead zone — standalone news12 is weak/blocked.
  Pairs using `news_open_vol` may still work as blends but verify carefully.
- **`anl4_rd_exp_flag`**: family-rd-tax-option9-connectors dead zone — 12 R&D/tax
  connector expressions tested, best S=1.19. Blend paths using `rd_exp_flag` as one
  leg may still differ but carry elevated dead-zone risk.

## How to use

1. Pick a pair/triple from distinct families (lower BRAIN self-corr risk).
2. Check dead zone warnings above; skip or deprioritize candidates from blocked families.
3. Use the `blend` expression directly, or recompose via `data/knowledge/patterns/blend-template.md`.
4. Simulate, then run the self-correlation check before submitting.
