---
type: factor_themes_redundancy
generated: '2026-06-15'
method: greedy clustering on field-level PnL correlation (|rho| >= 0.7)
n_clusters: 100
note: Members of a cluster are largely redundant (same theme). Keep the representative;
  treat the rest as self-correlation risk, not blend sources.
---
# Factor Redundancy / Theme Clusters

Fields grouped when their average pairwise PnL correlation is >= 0.7. Each cluster is one theme; the representative is the highest-Sharpe member.

Members are truncated to the top 15 by Sharpe; see `analysis_output/factor_redundancy_clusters.csv` for the full membership.

| # | Size | Representative | Rep S | Mean |rho| | Families | Top members |
|---|---|---|---|---|---|---|
| 1 | 232 | min_adjusted_net_income_guidance | 2.21 | 0.81 | analyst4,company_guidance,fundamental2,fundamental6,fundamental_capital_intensity,fundamental_cost_structure,fundamental_value | min_adjusted_net_income_guidance, fnd6_newqv1300_ppegtq, fnd6_fate, fnd6_fatl, fnd6_newqv1300_cogsq, cogs, fnd6_mfmq_cogsq, fnd6_newa1v1300_dltt, debt_lt, fnd6_cptnewqv1300_dlttq, fn_proceeds_from_issuance_of_debt_a, fn_def_tax_assets_net_a, fn_repayments_of_debt_a, fnd6_cptmfmq_dlttq, fnd6_dxd5, +217 more |
| 13 | 127 | anl4_bvps_flag | 1.30 | 0.82 | analyst4,analyst_revision,data_artifact,fundamental2,fundamental6,option8,pv13 | anl4_bvps_flag, anl4_ptpr_flag, anl4_netdebt_flag, rel_num_part, actuals_value_currency_code, rel_num_all, rel_num_comp, implied_volatility_mean_skew_180, anl4_tot_gw_ft, implied_volatility_mean_skew_270, fnd6_xrent, min_capital_expenditure_guidance, anl4_fcf_median, anl4_fcf_mean, fnd6_mrc2, +112 more |
| 4 | 26 | implied_volatility_put_90 | 1.73 | 0.84 | option8 | implied_volatility_put_90, implied_volatility_mean_90, implied_volatility_put_120, implied_volatility_mean_150, implied_volatility_call_1080, implied_volatility_mean_120, implied_volatility_call_720, implied_volatility_put_150, implied_volatility_call_360, implied_volatility_mean_180, implied_volatility_call_150, implied_volatility_mean_1080, implied_volatility_put_60, implied_volatility_mean_720, implied_volatility_call_180, +11 more |
| 40 | 20 | net_profit_adjusted_min_guidance | 0.94 | 0.90 | analyst4,pv1 | net_profit_adjusted_min_guidance, max_adjusted_net_profit_guidance, max_adjusted_eps_guidance_2, min_net_profit_guidance, max_net_profit_guidance, pretax_income_reported_min_guidance, dividend_max_guidance_quarterly, dividend_min_guidance_quarterly, max_reported_pretax_income_guidance_2, max_stock_option_expense_guidance, min_stock_option_expense_guidance_2, max_operating_cashflow_guidance, min_operating_cashflow_guidance, adjfactor, tangible_book_value_per_share_max_guidance, +5 more |
| 31 | 14 | fnd6_fopo | 1.08 | 0.80 | fundamental6 | fnd6_fopo, fnd6_newa1v1300_che, fnd6_newa1v1300_cshi, fnd6_newqv1300_chq, fnd6_mfmq_cheq, cash_st, fnd6_newqv1300_stkcoq, fnd6_newa2v1300_stkco, fnd6_ch, fnd6_newa1v1300_csho, fnd6_mfma1_csho, fnd6_cshpri, fnd6_newa1v1300_cshfd, fnd6_newqv1300_cshoq |
| 12 | 12 | fnd6_dlto | 1.34 | 0.75 | analyst4,fundamental2,fundamental6,fundamental_debt,fundamental_depreciation | fnd6_dlto, fnd6_newqv1300_dpactq, fnd6_dltis, fnd6_dm, fn_op_lease_min_pay_due_a, anl4_bvps_low, anl4_bvps_mean, anl4_bvps_median, anl4_bvps_high, fn_comp_options_exercisable_weighted_avg_a, fnd2_a_seniornotes, fnd2_q_seniornotes |
| 17 | 12 | fnd6_newqv1300_aol2q | 1.28 | 0.77 | analyst4,fundamental2,fundamental6 | fnd6_newqv1300_aol2q, fnd6_newa1v1300_aol2, fnd6_newa1v1300_caps, fnd6_newa2v1300_wcap, research_development_expense_reported_value, research_development_expense_actual_value, fnd6_txtubposinc, fnd6_newqv1300_xrdq, fn_comp_not_rec_q, fnd6_newqv1300_wcapq, working_capital, fnd6_tfva |
| 33 | 12 | anl4_afv4_eps_high | 1.05 | 0.79 | analyst4,fundamental2,fundamental6 | anl4_afv4_eps_high, fnd6_optprcby, fnd2_dfdtxastxdfdexpcompbnf, fn_op_lease_min_pay_due_in_5y_a, fnd6_optprcwa, fnd6_optprcca, fnd6_optprcey, fnd2_a_ptoacqbnsesg, fn_comp_options_out_weighted_avg_a, fnd2_a_sbcpnargtbysbpmtwpwrr, est_sga, fnd6_optprcgr |
| 32 | 9 | fnd6_fopox | 1.06 | 0.77 | analyst4,fundamental2,fundamental6 | fnd6_fopox, fnd6_newqv1300_capsq, anl4_ebit_std, anl4_gric_std, sales_estimate_dispersion, anl4_dts_ptp, anl4_netprofit_std, fnd2_itxreexftfedstyitxrt, fnd6_xad |
| 43 | 8 | relative_valuation_rank_derivative | 0.93 | 0.99 | model16 | relative_valuation_rank_derivative, earnings_certainty_rank_derivative, analyst_revision_rank_derivative, growth_potential_rank_derivative, multi_factor_static_score_derivative, cashflow_efficiency_rank_derivative, multi_factor_acceleration_score_derivative, composite_factor_score_derivative |
| 76 | 8 | max_shareholders_equity_guidance | 0.68 | 1.00 | analyst4 | max_shareholders_equity_guidance, min_shareholders_equity_guidance, min_basic_shares_guidance, max_shares_outstanding_guidance, min_share_count_guidance, basic_shares_max_guidance_qtr, shares_outstanding_max_guidance, min_shares_outstanding_guidance |
| 18 | 7 | anl4_totassets_flag | 1.27 | 0.82 | analyst4,analyst_revision | anl4_totassets_flag, anl4_cfi_flag, anl4_cff_flag, anl4_cfo_flag, anl4_capex_flag, anl4_fcf_flag, anl4_fcfps_flag |
| 46 | 6 | fn_op_lease_min_pay_due_after_5y_a | 0.92 | 0.74 | analyst4,fundamental2 | fn_op_lease_min_pay_due_after_5y_a, fnd2_a_ltrmdmrepopliny5, fnd2_a_sbcpnatqsttotnsvdptfv, capital_expenditure_guidance_value, fn_comp_not_rec_a, fn_allocated_share_based_compensation_expense_a |
| 15 | 5 | implied_volatility_put_10 | 1.29 | 0.85 | option8 | implied_volatility_put_10, implied_volatility_mean_10, implied_volatility_put_20, implied_volatility_mean_20, implied_volatility_call_10 |
| 75 | 5 | fn_debt_instrument_interest_rate_stated_percentage_a | 0.69 | 0.83 | analyst4,fundamental2,fundamental6 | fn_debt_instrument_interest_rate_stated_percentage_a, fn_debt_instrument_interest_rate_stated_percentage_q, fnd6_beta, anl4_qfd1_az_div_number, anl4_qf_az_div_number |
| 20 | 5 | implied_volatility_call_20 | 1.26 | 0.91 | option8 | implied_volatility_call_20, implied_volatility_call_30, implied_volatility_put_30, implied_volatility_mean_30, implied_volatility_call_60 |
| 5 | 5 | sales_estimate_count_quarterly | 1.59 | 0.77 | analyst4 | sales_estimate_count_quarterly, anl4_qf_az_eps_number, anl4_qfd1_az_eps_number, anl4_netprofit_number, anl4_ebit_number |
| 29 | 5 | anl4_tbvps_high | 1.09 | 0.88 | analyst4 | anl4_tbvps_high, anl4_tbvps_mean, anl4_tbvps_median, anl4_tbvps_low, est_bookvalue_ps |
| 48 | 4 | parkinson_volatility_120 | 0.89 | 0.74 | option8 | parkinson_volatility_120, parkinson_volatility_90, historical_volatility_90, historical_volatility_120 |
| 78 | 4 | min_financing_cashflow_guidance | 0.66 | 0.99 | analyst4 | min_financing_cashflow_guidance, max_financing_cashflow_guidance, min_investing_cashflow_guidance, max_investing_cashflow_guidance |
| 36 | 4 | anl4_fcf_high | 1.02 | 0.73 | analyst4,fundamental6 | anl4_fcf_high, fnd6_newqv1300_tstknq, fnd6_intc, anl4_fcfps_low |
| 34 | 4 | fn_derivative_notional_amount_q | 1.03 | 0.71 | fundamental2 | fn_derivative_notional_amount_q, fn_derivative_fair_value_of_derivative_asset_a, fnd2_a_ltrmdmrepoplay5, fnd2_a_ltrmdmrepoplinythree |
| 9 | 4 | anl4_qfd1_az_wol_spfc | 1.45 | 0.78 | analyst4 | anl4_qfd1_az_wol_spfc, anl4_qf_az_wol_spfc, cashflow_per_share_minimum, est_cashflow_ps |
| 94 | 4 | fnd6_newa1v1300_ibadj | 0.57 | 0.88 | fundamental6 | fnd6_newa1v1300_ibadj, fnd6_dilavx, fnd6_newa1v1300_epsfx, fnd6_newa1v1300_epsfi |
| 28 | 4 | implied_volatility_mean_skew_360 | 1.10 | 0.90 | option8 | implied_volatility_mean_skew_360, implied_volatility_mean_skew_1080, implied_volatility_mean_skew_720, implied_volatility_mean_skew_10 |
| 7 | 3 | max_adjusted_net_income_guidance | 1.49 | 0.86 | analyst4,company_guidance | max_adjusted_net_income_guidance, min_net_income_guidance, max_net_income_guidance |
| 27 | 3 | fnd6_tlcf | 1.10 | 0.78 | fundamental2,fundamental6 | fnd6_tlcf, fnd6_cshtr, fnd2_a_dfdtxava |
| 80 | 3 | fnd6_newqv1300_optrfrq | 0.65 | 0.76 | fundamental6 | fnd6_newqv1300_optrfrq, fnd6_optvolq, fnd6_optlifeq |
| 62 | 3 | news_session_range | 0.77 | 0.86 | news12 | news_session_range, news_range_stddev, news_atr_ratio |
| 82 | 3 | pcr_oi_10 | 0.64 | 0.84 | option9 | pcr_oi_10, pcr_oi_1080, pcr_oi_720 |
| 83 | 3 | fnd2_a_alsbcmpexrsus | 0.64 | 0.76 | fundamental2,fundamental6 | fnd2_a_alsbcmpexrsus, fnd6_stkcpa, fnd6_newa2v1300_xrd |
| 50 | 3 | sales_estimate_stddev_quarterly | 0.88 | 0.82 | analyst4,fundamental6 | sales_estimate_stddev_quarterly, sales_estimate_standard_deviation, fnd6_siv |
| 39 | 3 | ebit | 0.96 | 1.00 | fundamental6 | ebit, fnd6_newa2v1300_oiadp, fnd6_newa1v1300_ebit |
| 2 | 3 | rank(fnd6_acdo) + rank(open/close - 1) | 2.02 | 0.93 | socialmedia12,unknown | rank(fnd6_acdo) + rank(open/close - 1), rank(fnd6_acdo) * rank(-1 * returns), rank(scl12_buzz * (-1 * returns)) |
| 72 | 3 | anl4_afv4_eps_number | 0.72 | 0.78 | analyst4 | anl4_afv4_eps_number, anl4_epsa_flag, anl4_capex_number |
| 89 | 3 | news_pct_120min | 0.61 | 0.84 | news12 | news_pct_120min, news_pct_90min, news_pct_60min |
| 60 | 3 | fnd2_dfdtxasoprlcarryfwd | 0.79 | 0.72 | fundamental2 | fnd2_dfdtxasoprlcarryfwd, fn_comp_non_opt_vested_a, fnd2_propplteqmuflmblgland |
| 22 | 3 | anl4_qfd1_az_dts_spe | 1.18 | 0.81 | analyst4 | anl4_qfd1_az_dts_spe, anl4_qf_az_dts_spe, anl4_dts_rspe |
| 23 | 3 | pcr_vol_20 | 1.13 | 0.88 | option9 | pcr_vol_20, pcr_vol_30, pcr_vol_all |
| 77 | 2 | pcr_oi_180 | 0.68 | 0.86 | option9 | pcr_oi_180, pcr_oi_150 |
| 69 | 2 | pv13_ustomergraphrank_hub_rank | 0.74 | 0.78 | pv13 | pv13_ustomergraphrank_hub_rank, pv13_ustomergraphrank_auth_rank |
| 70 | 2 | min_adjusted_funds_from_operations_guidance | 0.74 | 1.00 | analyst4 | min_adjusted_funds_from_operations_guidance, max_adjusted_funds_from_operations_guidance |
| 71 | 2 | fn_antidilutive_securities_excl_from_eps_q | 0.74 | 0.88 | fundamental2 | fn_antidilutive_securities_excl_from_eps_q, fn_antidilutive_securities_excl_from_eps_a |
| 74 | 2 | min_research_development_expense_guidance | 0.72 | 1.00 | analyst4 | min_research_development_expense_guidance, max_research_development_expense_guidance |
| 68 | 2 | max_free_cashflow_guidance | 0.75 | 1.00 | analyst4 | max_free_cashflow_guidance, min_free_cashflow_guidance |
| 73 | 2 | pretax_income_reported_min_guidance_qtr | 0.72 | 1.00 | analyst4 | pretax_income_reported_min_guidance_qtr, max_reported_pretax_income_guidance |
| 85 | 2 | free_cash_flow_per_share_reported_value | 0.63 | 1.00 | analyst4 | free_cash_flow_per_share_reported_value, free_cash_flow_per_share_actual_value |
| 79 | 2 | pcr_vol_1080 | 0.65 | 0.89 | option9 | pcr_vol_1080, pcr_vol_180 |
| 90 | 2 | net_debt_actual_value | 0.60 | 1.00 | analyst4 | net_debt_actual_value, net_debt_reported_value |
| 95 | 2 | cash_flow_operations_min_guidance | 0.57 | 1.00 | analyst4 | cash_flow_operations_min_guidance, max_operating_cashflow_guidance_2 |
| 97 | 2 | scl12_buzz | 0.56 | 0.76 | sentiment_reversal,socialmedia12 | scl12_buzz, scl12_buzz_fast_d1 |
| 93 | 2 | net_debt_max_guidance_qtr | 0.58 | 1.00 | analyst4 | net_debt_max_guidance_qtr, net_debt_min_guidance_qtr |
| 98 | 2 | historical_volatility_10 | 0.55 | 0.74 | option8 | historical_volatility_10, parkinson_volatility_10 |
| 92 | 2 | investing_cashflow_reported_value | 0.59 | 1.00 | analyst4 | investing_cashflow_reported_value, anl4_cfi_value |
| 91 | 2 | min_pretax_profit_guidance_2 | 0.59 | 1.00 | analyst4 | min_pretax_profit_guidance_2, max_pretax_profit_guidance |
| 88 | 2 | sg_and_admin_min_guidance_value | 0.62 | 1.00 | analyst4 | sg_and_admin_min_guidance_value, max_selling_general_admin_guidance |
| 81 | 2 | fnd6_pstkrv | 0.64 | 1.00 | fundamental6 | fnd6_pstkrv, fnd6_pstkl |
| 87 | 2 | min_sg_and_a_expense_guidance | 0.62 | 1.00 | analyst4 | min_sg_and_a_expense_guidance, selling_general_admin_expense_max_guidance_qtr |
| 66 | 2 | cashflow_per_share_min_guidance_quarterly | 0.76 | 1.00 | analyst4 | cashflow_per_share_min_guidance_quarterly, cashflow_per_share_max_guidance_quarterly |
| 86 | 2 | capital_expenditure_max_guidance_qtr | 0.62 | 1.00 | analyst4 | capital_expenditure_max_guidance_qtr, min_capex_guidance |
| 96 | 2 | fnd6_newqv1300_esoprq | 0.56 | 1.00 | fundamental6 | fnd6_newqv1300_esoprq, fnd6_esopr |
| 84 | 2 | news_mins_20_pct_up | 0.64 | 1.00 | news12 | news_mins_20_pct_up, news_mins_20_chg |
| 99 | 2 | anl4_qf_az_hgih_vid | 0.53 | 1.00 | analyst4 | anl4_qf_az_hgih_vid, anl4_qfd1_az_hgih_vid |
| 67 | 2 | fnd6_newa1v1300_aoloch | 0.75 | 1.00 | fundamental6 | fnd6_newa1v1300_aoloch, fnd6_mfma1_aoloch |
| 51 | 2 | fnd6_newqv1300_miiq | 0.87 | 0.80 | fundamental6 | fnd6_newqv1300_miiq, fnd6_newqv1300_cimiiq |
| 65 | 2 | snt_buzz_bfl | 0.76 | 0.77 | socialmedia12 | snt_buzz_bfl, snt_buzz_ret |
| 19 | 2 | fnd6_drc | 1.27 | 0.93 | fundamental6 | fnd6_drc, fnd6_newqv1300_drcq |
| 35 | 2 | min_net_debt_guidance | 1.03 | 1.00 | company_guidance | min_net_debt_guidance, max_net_debt_guidance |
| 30 | 2 | news_mins_4_chg | 1.09 | 0.80 | news12 | news_mins_4_chg, news_mins_5_chg |
| 26 | 2 | fnd6_cld4 | 1.12 | 0.85 | fundamental6 | fnd6_cld4, fnd6_cld5 |
| 25 | 2 | fn_incremental_shares_attributable_to_share_based_payment_q | 1.12 | 0.74 | fundamental2 | fn_incremental_shares_attributable_to_share_based_payment_q, fn_avg_diluted_sharesout_adj_q |
| 24 | 2 | min_funds_from_operations_guidance | 1.13 | 1.00 | analyst4 | min_funds_from_operations_guidance, funds_from_operations_max_guidance |
| 21 | 2 | fn_assets_fair_val_l2_q | 1.22 | 0.82 | fundamental2 | fn_assets_fair_val_l2_q, fn_assets_fair_val_l2_a |
| 16 | 2 | fnd6_nopio | 1.28 | 0.73 | fundamental6 | fnd6_nopio, fnd6_newa2v1300_nopi |
| 38 | 2 | operating_profit_before_depr_amort_min_guidance_qtr | 0.96 | 1.00 | analyst4 | operating_profit_before_depr_amort_min_guidance_qtr, operating_profit_before_depr_amort_max_guidance_qtr |
| 14 | 2 | fnd6_cld2 | 1.29 | 0.95 | fundamental6 | fnd6_cld2, fnd6_cld3 |
| 11 | 2 | news_mins_3_pct_dn | 1.37 | 0.75 | news12 | news_mins_3_pct_dn, news_mins_4_pct_dn |
| 10 | 2 | fn_liab_fair_val_l2_q | 1.40 | 0.74 | fundamental2 | fn_liab_fair_val_l2_q, fn_liab_fair_val_l2_a |
| 8 | 2 | fnd6_drlt | 1.45 | 0.91 | fundamental6,fundamental_deferred_revenue | fnd6_drlt, fnd6_newqv1300_drltq |
| 6 | 2 | fnd6_mrct | 1.53 | 0.71 | fundamental6 | fnd6_mrct, fnd6_mrc1 |
| 3 | 2 | implied_volatility_call_270 - implied_volatility_put_270 | 1.81 | 0.74 | option8 | implied_volatility_call_270 - implied_volatility_put_270, implied_volatility_call_30 - implied_volatility_put_30 |
| 37 | 2 | primary_sector_focused_company_count | 1.01 | 0.84 | pv13 | primary_sector_focused_company_count, single_sector_pureplay_company_count |
| 41 | 2 | operating_profit_max_guidance_qtr | 0.94 | 1.00 | analyst4 | operating_profit_max_guidance_qtr, min_ebit_guidance |
| 64 | 2 | news_mins_2_pct_dn | 0.76 | 0.73 | news12 | news_mins_2_pct_dn, news_mins_1_pct_dn |
| 55 | 2 | fnd6_newqv1300_invrmq | 0.81 | 0.82 | fundamental6 | fnd6_newqv1300_invrmq, fnd6_newqv1300_invfgq |
| 63 | 2 | fnd6_mfma1_invch | 0.77 | 0.99 | fundamental6 | fnd6_mfma1_invch, fnd6_newa1v1300_invch |
| 61 | 2 | max_ebit_guidance | 0.78 | 1.00 | analyst4 | max_ebit_guidance, min_ebit_guidance_2 |
| 59 | 2 | cashflow_invst | 0.80 | 0.99 | fundamental6 | cashflow_invst, fnd6_newa1v1300_ivncf |
| 58 | 2 | fnd6_newa2v1300_reuna | 0.80 | 0.94 | fundamental6 | fnd6_newa2v1300_reuna, fnd6_newa2v1300_re |
| 57 | 2 | fnd6_optosey | 0.80 | 0.85 | fundamental2,fundamental6 | fnd6_optosey, fn_comp_options_out_number_a |
| 56 | 2 | max_gross_income_guidance_2 | 0.80 | 1.00 | analyst4 | max_gross_income_guidance_2, min_gross_income_guidance_2 |
| 54 | 2 | min_tangible_book_value_per_share_guidance | 0.83 | 1.00 | analyst4 | min_tangible_book_value_per_share_guidance, max_tangible_book_value_per_share_guidance |
| 42 | 2 | news_low_exc_stddev | 0.94 | 0.77 | news12 | news_low_exc_stddev, news_max_dn_amt |
| 53 | 2 | fnd6_newqv1300_txdbq | 0.84 | 0.97 | fundamental6 | fnd6_newqv1300_txdbq, fnd6_newqv1300_txditcq |
| 52 | 2 | min_pretax_profit_guidance | 0.85 | 1.00 | analyst4 | min_pretax_profit_guidance, pretax_income_max_guidance_qtr |
| 49 | 2 | max_gross_income_guidance | 0.88 | 1.00 | analyst4 | max_gross_income_guidance, min_gross_income_guidance |
| 47 | 2 | fnd6_idesindq_curcd | 0.89 | 0.96 | fundamental6 | fnd6_idesindq_curcd, fnd6_adesinda_curcd |
| 45 | 2 | anl4_capex_high | 0.93 | 0.83 | analyst4 | anl4_capex_high, anl4_median_capexp |
| 44 | 2 | fnd2_q_flintasamt1expyfour | 0.93 | 0.75 | fundamental2 | fnd2_q_flintasamt1expyfour, fnd2_q_flintasamt1expythree |
| 100 | 2 | fnd6_newqv1300_mibnq | 0.51 | 0.98 | fundamental6 | fnd6_newqv1300_mibnq, fnd6_mfmq_mibtq |
