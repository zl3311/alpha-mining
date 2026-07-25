# Batch 1: Intra-Cluster Alpha Expressions

**Generated**: 2026-05-16
**Server config**: USA TOP3000, decay=6, SUBINDUSTRY, priority=2
**Purpose**: Systematic exploration of each cluster before inter-cluster aggregation

## Cluster 1: fundamental6 other balance sheet

_Miscellaneous balance sheet items. value_ratio = F/close for size-normalizing._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(cash)` | level | cash |
| 2 | `rank(-1 * cash)` | neg_level | cash |
| 3 | `rank(ts_delta(cash, 5))` | delta_5d | cash |
| 4 | `rank(-1 * ts_delta(cash, 5))` | neg_delta_5d | cash |
| 5 | `rank(cash / close)` | value_ratio | cash |
| 6 | `ts_decay_linear(rank(cash), 5)` | decay_linear | cash |
| 7 | `trade_when(ts_std_dev(returns,20)>0.02, rank(cash), ts_std_dev(returns,20)<0.01)` | trade_when | cash |
| 8 | `rank(fnd6_acdo)` | level | fnd6_acdo |
| 9 | `rank(-1 * fnd6_acdo)` | neg_level | fnd6_acdo |
| 10 | `rank(ts_delta(fnd6_acdo, 5))` | delta_5d | fnd6_acdo |
| 11 | `rank(-1 * ts_delta(fnd6_acdo, 5))` | neg_delta_5d | fnd6_acdo |
| 12 | `rank(fnd6_acdo / close)` | value_ratio | fnd6_acdo |
| 13 | `ts_decay_linear(rank(fnd6_acdo), 5)` | decay_linear | fnd6_acdo |
| 14 | `trade_when(ts_std_dev(returns,20)>0.02, rank(fnd6_acdo), ts_std_dev(returns,20)<0.01)` | trade_when | fnd6_acdo |
| 15 | `rank(fnd6_fopo)` | level | fnd6_fopo |
| 16 | `rank(-1 * fnd6_fopo)` | neg_level | fnd6_fopo |
| 17 | `rank(ts_delta(fnd6_fopo, 5))` | delta_5d | fnd6_fopo |
| 18 | `rank(-1 * ts_delta(fnd6_fopo, 5))` | neg_delta_5d | fnd6_fopo |
| 19 | `rank(fnd6_fopo / close)` | value_ratio | fnd6_fopo |
| 20 | `ts_decay_linear(rank(fnd6_fopo), 5)` | decay_linear | fnd6_fopo |
| 21 | `trade_when(ts_std_dev(returns,20)>0.02, rank(fnd6_fopo), ts_std_dev(returns,20)<0.01)` | trade_when | fnd6_fopo |
| 22 | `rank(fnd6_drlt)` | level | fnd6_drlt |
| 23 | `rank(-1 * fnd6_drlt)` | neg_level | fnd6_drlt |
| 24 | `rank(ts_delta(fnd6_drlt, 5))` | delta_5d | fnd6_drlt |
| 25 | `rank(-1 * ts_delta(fnd6_drlt, 5))` | neg_delta_5d | fnd6_drlt |
| 26 | `rank(fnd6_drlt / close)` | value_ratio | fnd6_drlt |
| 27 | `ts_decay_linear(rank(fnd6_drlt), 5)` | decay_linear | fnd6_drlt |
| 28 | `trade_when(ts_std_dev(returns,20)>0.02, rank(fnd6_drlt), ts_std_dev(returns,20)<0.01)` | trade_when | fnd6_drlt |
| 29 | `rank(return_equity)` | level | return_equity |
| 30 | `rank(-1 * return_equity)` | neg_level | return_equity |
| 31 | `rank(ts_delta(return_equity, 5))` | delta_5d | return_equity |
| 32 | `rank(-1 * ts_delta(return_equity, 5))` | neg_delta_5d | return_equity |
| 33 | `rank(return_equity / close)` | value_ratio | return_equity |
| 34 | `ts_decay_linear(rank(return_equity), 5)` | decay_linear | return_equity |
| 35 | `trade_when(ts_std_dev(returns,20)>0.02, rank(return_equity), ts_std_dev(returns,20)<0.01)` | trade_when | return_equity |
| 36 | `rank(cash_st)` | level | cash_st |
| 37 | `rank(-1 * cash_st)` | neg_level | cash_st |
| 38 | `rank(ts_delta(cash_st, 5))` | delta_5d | cash_st |
| 39 | `rank(-1 * ts_delta(cash_st, 5))` | neg_delta_5d | cash_st |
| 40 | `rank(cash_st / close)` | value_ratio | cash_st |
| 41 | `ts_decay_linear(rank(cash_st), 5)` | decay_linear | cash_st |
| 42 | `trade_when(ts_std_dev(returns,20)>0.02, rank(cash_st), ts_std_dev(returns,20)<0.01)` | trade_when | cash_st |
| 43 | `rank(receivable)` | level | receivable |
| 44 | `rank(-1 * receivable)` | neg_level | receivable |
| 45 | `rank(ts_delta(receivable, 5))` | delta_5d | receivable |
| 46 | `rank(-1 * ts_delta(receivable, 5))` | neg_delta_5d | receivable |
| 47 | `rank(receivable / close)` | value_ratio | receivable |
| 48 | `ts_decay_linear(rank(receivable), 5)` | decay_linear | receivable |
| 49 | `trade_when(ts_std_dev(returns,20)>0.02, rank(receivable), ts_std_dev(returns,20)<0.01)` | trade_when | receivable |
| 50 | `rank(sales_growth)` | level | sales_growth |
| 51 | `rank(-1 * sales_growth)` | neg_level | sales_growth |
| 52 | `rank(ts_delta(sales_growth, 5))` | delta_5d | sales_growth |
| 53 | `rank(-1 * ts_delta(sales_growth, 5))` | neg_delta_5d | sales_growth |
| 54 | `rank(sales_growth / close)` | value_ratio | sales_growth |
| 55 | `ts_decay_linear(rank(sales_growth), 5)` | decay_linear | sales_growth |
| 56 | `trade_when(ts_std_dev(returns,20)>0.02, rank(sales_growth), ts_std_dev(returns,20)<0.01)` | trade_when | sales_growth |

**Count**: 56 expressions

---

## Cluster 2: fundamental6 income earnings

_Income statement earnings. value_ratio = F/close for earnings yield._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(ebitda)` | level | ebitda |
| 2 | `rank(-1 * ebitda)` | neg_level | ebitda |
| 3 | `rank(ts_delta(ebitda, 5))` | delta_5d | ebitda |
| 4 | `rank(-1 * ts_delta(ebitda, 5))` | neg_delta_5d | ebitda |
| 5 | `rank(ebitda / close)` | value_ratio | ebitda |
| 6 | `ts_decay_linear(rank(ebitda), 5)` | decay_linear | ebitda |
| 7 | `trade_when(ts_std_dev(returns,20)>0.02, rank(ebitda), ts_std_dev(returns,20)<0.01)` | trade_when | ebitda |
| 8 | `rank(ebit)` | level | ebit |
| 9 | `rank(-1 * ebit)` | neg_level | ebit |
| 10 | `rank(ts_delta(ebit, 5))` | delta_5d | ebit |
| 11 | `rank(-1 * ts_delta(ebit, 5))` | neg_delta_5d | ebit |
| 12 | `rank(ebit / close)` | value_ratio | ebit |
| 13 | `ts_decay_linear(rank(ebit), 5)` | decay_linear | ebit |
| 14 | `trade_when(ts_std_dev(returns,20)>0.02, rank(ebit), ts_std_dev(returns,20)<0.01)` | trade_when | ebit |
| 15 | `rank(eps)` | level | eps |
| 16 | `rank(-1 * eps)` | neg_level | eps |
| 17 | `rank(ts_delta(eps, 5))` | delta_5d | eps |
| 18 | `rank(-1 * ts_delta(eps, 5))` | neg_delta_5d | eps |
| 19 | `rank(eps / close)` | value_ratio | eps |
| 20 | `ts_decay_linear(rank(eps), 5)` | decay_linear | eps |
| 21 | `trade_when(ts_std_dev(returns,20)>0.02, rank(eps), ts_std_dev(returns,20)<0.01)` | trade_when | eps |
| 22 | `rank(income)` | level | income |
| 23 | `rank(-1 * income)` | neg_level | income |
| 24 | `rank(ts_delta(income, 5))` | delta_5d | income |
| 25 | `rank(-1 * ts_delta(income, 5))` | neg_delta_5d | income |
| 26 | `rank(income / close)` | value_ratio | income |
| 27 | `ts_decay_linear(rank(income), 5)` | decay_linear | income |
| 28 | `trade_when(ts_std_dev(returns,20)>0.02, rank(income), ts_std_dev(returns,20)<0.01)` | trade_when | income |
| 29 | `rank(operating_expense)` | level | operating_expense |
| 30 | `rank(-1 * operating_expense)` | neg_level | operating_expense |
| 31 | `rank(ts_delta(operating_expense, 5))` | delta_5d | operating_expense |
| 32 | `rank(-1 * ts_delta(operating_expense, 5))` | neg_delta_5d | operating_expense |
| 33 | `rank(operating_expense / close)` | value_ratio | operating_expense |
| 34 | `ts_decay_linear(rank(operating_expense), 5)` | decay_linear | operating_expense |
| 35 | `trade_when(ts_std_dev(returns,20)>0.02, rank(operating_expense), ts_std_dev(returns,20)<0.01)` | trade_when | operating_expense |
| 36 | `rank(pretax_income)` | level | pretax_income |
| 37 | `rank(-1 * pretax_income)` | neg_level | pretax_income |
| 38 | `rank(ts_delta(pretax_income, 5))` | delta_5d | pretax_income |
| 39 | `rank(-1 * ts_delta(pretax_income, 5))` | neg_delta_5d | pretax_income |
| 40 | `rank(pretax_income / close)` | value_ratio | pretax_income |
| 41 | `ts_decay_linear(rank(pretax_income), 5)` | decay_linear | pretax_income |
| 42 | `trade_when(ts_std_dev(returns,20)>0.02, rank(pretax_income), ts_std_dev(returns,20)<0.01)` | trade_when | pretax_income |

**Count**: 42 expressions

---

## Cluster 3: analyst4 earnings estimates

_Analyst estimates and revision flags. No value_ratio (flags are categorical-like)._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(anl4_adjusted_netincome_ft)` | level | anl4_adjusted_netincome_ft |
| 2 | `rank(-1 * anl4_adjusted_netincome_ft)` | neg_level | anl4_adjusted_netincome_ft |
| 3 | `rank(ts_delta(anl4_adjusted_netincome_ft, 5))` | delta_5d | anl4_adjusted_netincome_ft |
| 4 | `rank(-1 * ts_delta(anl4_adjusted_netincome_ft, 5))` | neg_delta_5d | anl4_adjusted_netincome_ft |
| 5 | `ts_decay_linear(rank(anl4_adjusted_netincome_ft), 5)` | decay_linear | anl4_adjusted_netincome_ft |
| 6 | `rank(anl4_ptp_flag)` | level | anl4_ptp_flag |
| 7 | `rank(-1 * anl4_ptp_flag)` | neg_level | anl4_ptp_flag |
| 8 | `rank(ts_delta(anl4_ptp_flag, 5))` | delta_5d | anl4_ptp_flag |
| 9 | `rank(-1 * ts_delta(anl4_ptp_flag, 5))` | neg_delta_5d | anl4_ptp_flag |
| 10 | `ts_decay_linear(rank(anl4_ptp_flag), 5)` | decay_linear | anl4_ptp_flag |
| 11 | `rank(anl4_epsr_flag)` | level | anl4_epsr_flag |
| 12 | `rank(-1 * anl4_epsr_flag)` | neg_level | anl4_epsr_flag |
| 13 | `rank(ts_delta(anl4_epsr_flag, 5))` | delta_5d | anl4_epsr_flag |
| 14 | `rank(-1 * ts_delta(anl4_epsr_flag, 5))` | neg_delta_5d | anl4_epsr_flag |
| 15 | `ts_decay_linear(rank(anl4_epsr_flag), 5)` | decay_linear | anl4_epsr_flag |
| 16 | `rank(anl4_netprofit_flag)` | level | anl4_netprofit_flag |
| 17 | `rank(-1 * anl4_netprofit_flag)` | neg_level | anl4_netprofit_flag |
| 18 | `rank(ts_delta(anl4_netprofit_flag, 5))` | delta_5d | anl4_netprofit_flag |
| 19 | `rank(-1 * ts_delta(anl4_netprofit_flag, 5))` | neg_delta_5d | anl4_netprofit_flag |
| 20 | `ts_decay_linear(rank(anl4_netprofit_flag), 5)` | decay_linear | anl4_netprofit_flag |
| 21 | `rank(est_eps)` | level | est_eps |
| 22 | `rank(-1 * est_eps)` | neg_level | est_eps |
| 23 | `rank(ts_delta(est_eps, 5))` | delta_5d | est_eps |
| 24 | `rank(-1 * ts_delta(est_eps, 5))` | neg_delta_5d | est_eps |
| 25 | `ts_decay_linear(rank(est_eps), 5)` | decay_linear | est_eps |
| 26 | `rank(anl4_qf_az_eps_number)` | level | anl4_qf_az_eps_number |
| 27 | `rank(-1 * anl4_qf_az_eps_number)` | neg_level | anl4_qf_az_eps_number |
| 28 | `rank(ts_delta(anl4_qf_az_eps_number, 5))` | delta_5d | anl4_qf_az_eps_number |
| 29 | `rank(-1 * ts_delta(anl4_qf_az_eps_number, 5))` | neg_delta_5d | anl4_qf_az_eps_number |
| 30 | `ts_decay_linear(rank(anl4_qf_az_eps_number), 5)` | decay_linear | anl4_qf_az_eps_number |
| 31 | `rank(anl4_eaz2lrec_ratingvalue)` | level | anl4_eaz2lrec_ratingvalue |
| 32 | `rank(-1 * anl4_eaz2lrec_ratingvalue)` | neg_level | anl4_eaz2lrec_ratingvalue |
| 33 | `rank(ts_delta(anl4_eaz2lrec_ratingvalue, 5))` | delta_5d | anl4_eaz2lrec_ratingvalue |
| 34 | `rank(-1 * ts_delta(anl4_eaz2lrec_ratingvalue, 5))` | neg_delta_5d | anl4_eaz2lrec_ratingvalue |
| 35 | `ts_decay_linear(rank(anl4_eaz2lrec_ratingvalue), 5)` | decay_linear | anl4_eaz2lrec_ratingvalue |
| 36 | `rank(anl4_tbve_ft)` | level | anl4_tbve_ft |
| 37 | `rank(-1 * anl4_tbve_ft)` | neg_level | anl4_tbve_ft |
| 38 | `rank(ts_delta(anl4_tbve_ft, 5))` | delta_5d | anl4_tbve_ft |
| 39 | `rank(-1 * ts_delta(anl4_tbve_ft, 5))` | neg_delta_5d | anl4_tbve_ft |
| 40 | `ts_decay_linear(rank(anl4_tbve_ft), 5)` | decay_linear | anl4_tbve_ft |

**Count**: 40 expressions

---

## Cluster 4: fundamental6 balance sheet assets

_Asset items. value_ratio = F/close normalizes by price._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(assets)` | level | assets |
| 2 | `rank(-1 * assets)` | neg_level | assets |
| 3 | `rank(ts_delta(assets, 5))` | delta_5d | assets |
| 4 | `rank(-1 * ts_delta(assets, 5))` | neg_delta_5d | assets |
| 5 | `rank(assets / close)` | value_ratio | assets |
| 6 | `ts_decay_linear(rank(assets), 5)` | decay_linear | assets |
| 7 | `trade_when(ts_std_dev(returns,20)>0.02, rank(assets), ts_std_dev(returns,20)<0.01)` | trade_when | assets |
| 8 | `rank(assets_curr)` | level | assets_curr |
| 9 | `rank(-1 * assets_curr)` | neg_level | assets_curr |
| 10 | `rank(ts_delta(assets_curr, 5))` | delta_5d | assets_curr |
| 11 | `rank(-1 * ts_delta(assets_curr, 5))` | neg_delta_5d | assets_curr |
| 12 | `rank(assets_curr / close)` | value_ratio | assets_curr |
| 13 | `ts_decay_linear(rank(assets_curr), 5)` | decay_linear | assets_curr |
| 14 | `trade_when(ts_std_dev(returns,20)>0.02, rank(assets_curr), ts_std_dev(returns,20)<0.01)` | trade_when | assets_curr |
| 15 | `rank(goodwill)` | level | goodwill |
| 16 | `rank(-1 * goodwill)` | neg_level | goodwill |
| 17 | `rank(ts_delta(goodwill, 5))` | delta_5d | goodwill |
| 18 | `rank(-1 * ts_delta(goodwill, 5))` | neg_delta_5d | goodwill |
| 19 | `rank(goodwill / close)` | value_ratio | goodwill |
| 20 | `ts_decay_linear(rank(goodwill), 5)` | decay_linear | goodwill |
| 21 | `trade_when(ts_std_dev(returns,20)>0.02, rank(goodwill), ts_std_dev(returns,20)<0.01)` | trade_when | goodwill |
| 22 | `rank(ppent)` | level | ppent |
| 23 | `rank(-1 * ppent)` | neg_level | ppent |
| 24 | `rank(ts_delta(ppent, 5))` | delta_5d | ppent |
| 25 | `rank(-1 * ts_delta(ppent, 5))` | neg_delta_5d | ppent |
| 26 | `rank(ppent / close)` | value_ratio | ppent |
| 27 | `ts_decay_linear(rank(ppent), 5)` | decay_linear | ppent |
| 28 | `trade_when(ts_std_dev(returns,20)>0.02, rank(ppent), ts_std_dev(returns,20)<0.01)` | trade_when | ppent |
| 29 | `rank(inventory)` | level | inventory |
| 30 | `rank(-1 * inventory)` | neg_level | inventory |
| 31 | `rank(ts_delta(inventory, 5))` | delta_5d | inventory |
| 32 | `rank(-1 * ts_delta(inventory, 5))` | neg_delta_5d | inventory |
| 33 | `rank(inventory / close)` | value_ratio | inventory |
| 34 | `ts_decay_linear(rank(inventory), 5)` | decay_linear | inventory |
| 35 | `trade_when(ts_std_dev(returns,20)>0.02, rank(inventory), ts_std_dev(returns,20)<0.01)` | trade_when | inventory |
| 36 | `rank(receivable)` | level | receivable |
| 37 | `rank(-1 * receivable)` | neg_level | receivable |
| 38 | `rank(ts_delta(receivable, 5))` | delta_5d | receivable |
| 39 | `rank(-1 * ts_delta(receivable, 5))` | neg_delta_5d | receivable |
| 40 | `rank(receivable / close)` | value_ratio | receivable |
| 41 | `ts_decay_linear(rank(receivable), 5)` | decay_linear | receivable |
| 42 | `trade_when(ts_std_dev(returns,20)>0.02, rank(receivable), ts_std_dev(returns,20)<0.01)` | trade_when | receivable |

**Count**: 42 expressions

---

## Cluster 5: fundamental6 balance sheet liabilities

_Liability items. value_ratio = F/close for leverage normalization._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(liabilities)` | level | liabilities |
| 2 | `rank(-1 * liabilities)` | neg_level | liabilities |
| 3 | `rank(ts_delta(liabilities, 5))` | delta_5d | liabilities |
| 4 | `rank(-1 * ts_delta(liabilities, 5))` | neg_delta_5d | liabilities |
| 5 | `rank(liabilities / close)` | value_ratio | liabilities |
| 6 | `ts_decay_linear(rank(liabilities), 5)` | decay_linear | liabilities |
| 7 | `trade_when(ts_std_dev(returns,20)>0.02, rank(liabilities), ts_std_dev(returns,20)<0.01)` | trade_when | liabilities |
| 8 | `rank(debt)` | level | debt |
| 9 | `rank(-1 * debt)` | neg_level | debt |
| 10 | `rank(ts_delta(debt, 5))` | delta_5d | debt |
| 11 | `rank(-1 * ts_delta(debt, 5))` | neg_delta_5d | debt |
| 12 | `rank(debt / close)` | value_ratio | debt |
| 13 | `ts_decay_linear(rank(debt), 5)` | decay_linear | debt |
| 14 | `trade_when(ts_std_dev(returns,20)>0.02, rank(debt), ts_std_dev(returns,20)<0.01)` | trade_when | debt |
| 15 | `rank(debt_lt)` | level | debt_lt |
| 16 | `rank(-1 * debt_lt)` | neg_level | debt_lt |
| 17 | `rank(ts_delta(debt_lt, 5))` | delta_5d | debt_lt |
| 18 | `rank(-1 * ts_delta(debt_lt, 5))` | neg_delta_5d | debt_lt |
| 19 | `rank(debt_lt / close)` | value_ratio | debt_lt |
| 20 | `ts_decay_linear(rank(debt_lt), 5)` | decay_linear | debt_lt |
| 21 | `trade_when(ts_std_dev(returns,20)>0.02, rank(debt_lt), ts_std_dev(returns,20)<0.01)` | trade_when | debt_lt |
| 22 | `rank(liabilities_curr)` | level | liabilities_curr |
| 23 | `rank(-1 * liabilities_curr)` | neg_level | liabilities_curr |
| 24 | `rank(ts_delta(liabilities_curr, 5))` | delta_5d | liabilities_curr |
| 25 | `rank(-1 * ts_delta(liabilities_curr, 5))` | neg_delta_5d | liabilities_curr |
| 26 | `rank(liabilities_curr / close)` | value_ratio | liabilities_curr |
| 27 | `ts_decay_linear(rank(liabilities_curr), 5)` | decay_linear | liabilities_curr |
| 28 | `trade_when(ts_std_dev(returns,20)>0.02, rank(liabilities_curr), ts_std_dev(returns,20)<0.01)` | trade_when | liabilities_curr |
| 29 | `rank(debt_st)` | level | debt_st |
| 30 | `rank(-1 * debt_st)` | neg_level | debt_st |
| 31 | `rank(ts_delta(debt_st, 5))` | delta_5d | debt_st |
| 32 | `rank(-1 * ts_delta(debt_st, 5))` | neg_delta_5d | debt_st |
| 33 | `rank(debt_st / close)` | value_ratio | debt_st |
| 34 | `ts_decay_linear(rank(debt_st), 5)` | decay_linear | debt_st |
| 35 | `trade_when(ts_std_dev(returns,20)>0.02, rank(debt_st), ts_std_dev(returns,20)<0.01)` | trade_when | debt_st |

**Count**: 35 expressions

---

## Cluster 6: fundamental6 income expense

_Expense and investment items._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(operating_income)` | level | operating_income |
| 2 | `rank(-1 * operating_income)` | neg_level | operating_income |
| 3 | `rank(ts_delta(operating_income, 5))` | delta_5d | operating_income |
| 4 | `rank(-1 * ts_delta(operating_income, 5))` | neg_delta_5d | operating_income |
| 5 | `rank(operating_income / close)` | value_ratio | operating_income |
| 6 | `ts_decay_linear(rank(operating_income), 5)` | decay_linear | operating_income |
| 7 | `trade_when(ts_std_dev(returns,20)>0.02, rank(operating_income), ts_std_dev(returns,20)<0.01)` | trade_when | operating_income |
| 8 | `rank(cogs)` | level | cogs |
| 9 | `rank(-1 * cogs)` | neg_level | cogs |
| 10 | `rank(ts_delta(cogs, 5))` | delta_5d | cogs |
| 11 | `rank(-1 * ts_delta(cogs, 5))` | neg_delta_5d | cogs |
| 12 | `rank(cogs / close)` | value_ratio | cogs |
| 13 | `ts_decay_linear(rank(cogs), 5)` | decay_linear | cogs |
| 14 | `trade_when(ts_std_dev(returns,20)>0.02, rank(cogs), ts_std_dev(returns,20)<0.01)` | trade_when | cogs |
| 15 | `rank(capex)` | level | capex |
| 16 | `rank(-1 * capex)` | neg_level | capex |
| 17 | `rank(ts_delta(capex, 5))` | delta_5d | capex |
| 18 | `rank(-1 * ts_delta(capex, 5))` | neg_delta_5d | capex |
| 19 | `rank(capex / close)` | value_ratio | capex |
| 20 | `ts_decay_linear(rank(capex), 5)` | decay_linear | capex |
| 21 | `trade_when(ts_std_dev(returns,20)>0.02, rank(capex), ts_std_dev(returns,20)<0.01)` | trade_when | capex |
| 22 | `rank(sga_expense)` | level | sga_expense |
| 23 | `rank(-1 * sga_expense)` | neg_level | sga_expense |
| 24 | `rank(ts_delta(sga_expense, 5))` | delta_5d | sga_expense |
| 25 | `rank(-1 * ts_delta(sga_expense, 5))` | neg_delta_5d | sga_expense |
| 26 | `rank(sga_expense / close)` | value_ratio | sga_expense |
| 27 | `ts_decay_linear(rank(sga_expense), 5)` | decay_linear | sga_expense |
| 28 | `trade_when(ts_std_dev(returns,20)>0.02, rank(sga_expense), ts_std_dev(returns,20)<0.01)` | trade_when | sga_expense |
| 29 | `rank(depre_amort)` | level | depre_amort |
| 30 | `rank(-1 * depre_amort)` | neg_level | depre_amort |
| 31 | `rank(ts_delta(depre_amort, 5))` | delta_5d | depre_amort |
| 32 | `rank(-1 * ts_delta(depre_amort, 5))` | neg_delta_5d | depre_amort |
| 33 | `rank(depre_amort / close)` | value_ratio | depre_amort |
| 34 | `ts_decay_linear(rank(depre_amort), 5)` | decay_linear | depre_amort |
| 35 | `trade_when(ts_std_dev(returns,20)>0.02, rank(depre_amort), ts_std_dev(returns,20)<0.01)` | trade_when | depre_amort |

**Count**: 35 expressions

---

## Cluster 7: option8 implied volatility

_Implied vol at different tenors. No value_ratio (already normalized). Added term structure spreads._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(implied_volatility_call_270)` | level | implied_volatility_call_270 |
| 2 | `rank(-1 * implied_volatility_call_270)` | neg_level | implied_volatility_call_270 |
| 3 | `rank(ts_delta(implied_volatility_call_270, 5))` | delta_5d | implied_volatility_call_270 |
| 4 | `rank(-1 * ts_delta(implied_volatility_call_270, 5))` | neg_delta_5d | implied_volatility_call_270 |
| 5 | `rank(implied_volatility_call_30)` | level | implied_volatility_call_30 |
| 6 | `rank(-1 * implied_volatility_call_30)` | neg_level | implied_volatility_call_30 |
| 7 | `rank(ts_delta(implied_volatility_call_30, 5))` | delta_5d | implied_volatility_call_30 |
| 8 | `rank(-1 * ts_delta(implied_volatility_call_30, 5))` | neg_delta_5d | implied_volatility_call_30 |
| 9 | `rank(implied_volatility_put_270)` | level | implied_volatility_put_270 |
| 10 | `rank(-1 * implied_volatility_put_270)` | neg_level | implied_volatility_put_270 |
| 11 | `rank(ts_delta(implied_volatility_put_270, 5))` | delta_5d | implied_volatility_put_270 |
| 12 | `rank(-1 * ts_delta(implied_volatility_put_270, 5))` | neg_delta_5d | implied_volatility_put_270 |
| 13 | `rank(implied_volatility_put_30)` | level | implied_volatility_put_30 |
| 14 | `rank(-1 * implied_volatility_put_30)` | neg_level | implied_volatility_put_30 |
| 15 | `rank(ts_delta(implied_volatility_put_30, 5))` | delta_5d | implied_volatility_put_30 |
| 16 | `rank(-1 * ts_delta(implied_volatility_put_30, 5))` | neg_delta_5d | implied_volatility_put_30 |
| 17 | `rank(implied_volatility_call_1080)` | level | implied_volatility_call_1080 |
| 18 | `rank(-1 * implied_volatility_call_1080)` | neg_level | implied_volatility_call_1080 |
| 19 | `rank(ts_delta(implied_volatility_call_1080, 5))` | delta_5d | implied_volatility_call_1080 |
| 20 | `rank(-1 * ts_delta(implied_volatility_call_1080, 5))` | neg_delta_5d | implied_volatility_call_1080 |
| 21 | `rank(implied_volatility_call_30 - implied_volatility_call_270)` | IV term structure slope (short - long) | composite |
| 22 | `rank(-1 * (implied_volatility_call_30 - implied_volatility_call_270))` | IV term structure slope (inverted) | composite |
| 23 | `rank(implied_volatility_call_270 - implied_volatility_put_270)` | Call-put IV spread (270d) | composite |
| 24 | `rank(implied_volatility_call_30 - implied_volatility_put_30)` | Call-put IV spread (30d) | composite |
| 25 | `ts_decay_linear(rank(implied_volatility_call_270), 5)` | Smoothed long-term IV | composite |
| 26 | `ts_decay_linear(rank(-1 * implied_volatility_call_30), 5)` | Smoothed negative short-term IV | composite |

**Count**: 26 expressions

---

## Cluster 8: fundamental6 cash flow

_Cash flow statement items._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(cashflow_op)` | level | cashflow_op |
| 2 | `rank(-1 * cashflow_op)` | neg_level | cashflow_op |
| 3 | `rank(ts_delta(cashflow_op, 5))` | delta_5d | cashflow_op |
| 4 | `rank(-1 * ts_delta(cashflow_op, 5))` | neg_delta_5d | cashflow_op |
| 5 | `rank(cashflow_op / close)` | value_ratio | cashflow_op |
| 6 | `ts_decay_linear(rank(cashflow_op), 5)` | decay_linear | cashflow_op |
| 7 | `rank(cashflow)` | level | cashflow |
| 8 | `rank(-1 * cashflow)` | neg_level | cashflow |
| 9 | `rank(ts_delta(cashflow, 5))` | delta_5d | cashflow |
| 10 | `rank(-1 * ts_delta(cashflow, 5))` | neg_delta_5d | cashflow |
| 11 | `rank(cashflow / close)` | value_ratio | cashflow |
| 12 | `ts_decay_linear(rank(cashflow), 5)` | decay_linear | cashflow |
| 13 | `rank(cashflow_fin)` | level | cashflow_fin |
| 14 | `rank(-1 * cashflow_fin)` | neg_level | cashflow_fin |
| 15 | `rank(ts_delta(cashflow_fin, 5))` | delta_5d | cashflow_fin |
| 16 | `rank(-1 * ts_delta(cashflow_fin, 5))` | neg_delta_5d | cashflow_fin |
| 17 | `rank(cashflow_fin / close)` | value_ratio | cashflow_fin |
| 18 | `ts_decay_linear(rank(cashflow_fin), 5)` | decay_linear | cashflow_fin |
| 19 | `rank(cashflow_dividends)` | level | cashflow_dividends |
| 20 | `rank(-1 * cashflow_dividends)` | neg_level | cashflow_dividends |
| 21 | `rank(ts_delta(cashflow_dividends, 5))` | delta_5d | cashflow_dividends |
| 22 | `rank(-1 * ts_delta(cashflow_dividends, 5))` | neg_delta_5d | cashflow_dividends |
| 23 | `rank(cashflow_dividends / close)` | value_ratio | cashflow_dividends |
| 24 | `ts_decay_linear(rank(cashflow_dividends), 5)` | decay_linear | cashflow_dividends |
| 25 | `rank(cashflow_invst)` | level | cashflow_invst |
| 26 | `rank(-1 * cashflow_invst)` | neg_level | cashflow_invst |
| 27 | `rank(ts_delta(cashflow_invst, 5))` | delta_5d | cashflow_invst |
| 28 | `rank(-1 * ts_delta(cashflow_invst, 5))` | neg_delta_5d | cashflow_invst |
| 29 | `rank(cashflow_invst / close)` | value_ratio | cashflow_invst |
| 30 | `ts_decay_linear(rank(cashflow_invst), 5)` | decay_linear | cashflow_invst |

**Count**: 30 expressions

---

## Cluster 9: analyst4 cash flow estimates

_Analyst cash flow estimates and revision flags._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(anl4_capex_high)` | level | anl4_capex_high |
| 2 | `rank(-1 * anl4_capex_high)` | neg_level | anl4_capex_high |
| 3 | `rank(ts_delta(anl4_capex_high, 5))` | delta_5d | anl4_capex_high |
| 4 | `rank(-1 * ts_delta(anl4_capex_high, 5))` | neg_delta_5d | anl4_capex_high |
| 5 | `ts_decay_linear(rank(anl4_capex_high), 5)` | decay_linear | anl4_capex_high |
| 6 | `rank(anl4_cfo_low)` | level | anl4_cfo_low |
| 7 | `rank(-1 * anl4_cfo_low)` | neg_level | anl4_cfo_low |
| 8 | `rank(ts_delta(anl4_cfo_low, 5))` | delta_5d | anl4_cfo_low |
| 9 | `rank(-1 * ts_delta(anl4_cfo_low, 5))` | neg_delta_5d | anl4_cfo_low |
| 10 | `ts_decay_linear(rank(anl4_cfo_low), 5)` | decay_linear | anl4_cfo_low |
| 11 | `rank(anl4_cfo_value)` | level | anl4_cfo_value |
| 12 | `rank(-1 * anl4_cfo_value)` | neg_level | anl4_cfo_value |
| 13 | `rank(ts_delta(anl4_cfo_value, 5))` | delta_5d | anl4_cfo_value |
| 14 | `rank(-1 * ts_delta(anl4_cfo_value, 5))` | neg_delta_5d | anl4_cfo_value |
| 15 | `ts_decay_linear(rank(anl4_cfo_value), 5)` | decay_linear | anl4_cfo_value |
| 16 | `rank(anl4_capex_flag)` | level | anl4_capex_flag |
| 17 | `rank(-1 * anl4_capex_flag)` | neg_level | anl4_capex_flag |
| 18 | `rank(ts_delta(anl4_capex_flag, 5))` | delta_5d | anl4_capex_flag |
| 19 | `rank(-1 * ts_delta(anl4_capex_flag, 5))` | neg_delta_5d | anl4_capex_flag |
| 20 | `ts_decay_linear(rank(anl4_capex_flag), 5)` | decay_linear | anl4_capex_flag |
| 21 | `rank(anl4_fcf_flag)` | level | anl4_fcf_flag |
| 22 | `rank(-1 * anl4_fcf_flag)` | neg_level | anl4_fcf_flag |
| 23 | `rank(ts_delta(anl4_fcf_flag, 5))` | delta_5d | anl4_fcf_flag |
| 24 | `rank(-1 * ts_delta(anl4_fcf_flag, 5))` | neg_delta_5d | anl4_fcf_flag |
| 25 | `ts_decay_linear(rank(anl4_fcf_flag), 5)` | decay_linear | anl4_fcf_flag |
| 26 | `rank(anl4_cff_flag)` | level | anl4_cff_flag |
| 27 | `rank(-1 * anl4_cff_flag)` | neg_level | anl4_cff_flag |
| 28 | `rank(ts_delta(anl4_cff_flag, 5))` | delta_5d | anl4_cff_flag |
| 29 | `rank(-1 * ts_delta(anl4_cff_flag, 5))` | neg_delta_5d | anl4_cff_flag |
| 30 | `ts_decay_linear(rank(anl4_cff_flag), 5)` | decay_linear | anl4_cff_flag |

**Count**: 30 expressions

---

## Cluster 10: fundamental6 balance sheet equity

_Equity items. bookvalue_ps/close = classic book-to-price ratio._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(equity)` | level | equity |
| 2 | `rank(-1 * equity)` | neg_level | equity |
| 3 | `rank(ts_delta(equity, 5))` | delta_5d | equity |
| 4 | `rank(-1 * ts_delta(equity, 5))` | neg_delta_5d | equity |
| 5 | `rank(equity / close)` | value_ratio | equity |
| 6 | `ts_decay_linear(rank(equity), 5)` | decay_linear | equity |
| 7 | `rank(bookvalue_ps)` | level | bookvalue_ps |
| 8 | `rank(-1 * bookvalue_ps)` | neg_level | bookvalue_ps |
| 9 | `rank(ts_delta(bookvalue_ps, 5))` | delta_5d | bookvalue_ps |
| 10 | `rank(-1 * ts_delta(bookvalue_ps, 5))` | neg_delta_5d | bookvalue_ps |
| 11 | `rank(bookvalue_ps / close)` | value_ratio | bookvalue_ps |
| 12 | `ts_decay_linear(rank(bookvalue_ps), 5)` | decay_linear | bookvalue_ps |
| 13 | `rank(retained_earnings)` | level | retained_earnings |
| 14 | `rank(-1 * retained_earnings)` | neg_level | retained_earnings |
| 15 | `rank(ts_delta(retained_earnings, 5))` | delta_5d | retained_earnings |
| 16 | `rank(-1 * ts_delta(retained_earnings, 5))` | neg_delta_5d | retained_earnings |
| 17 | `rank(retained_earnings / close)` | value_ratio | retained_earnings |
| 18 | `ts_decay_linear(rank(retained_earnings), 5)` | decay_linear | retained_earnings |
| 19 | `rank(sharesout)` | level | sharesout |
| 20 | `rank(-1 * sharesout)` | neg_level | sharesout |
| 21 | `rank(ts_delta(sharesout, 5))` | delta_5d | sharesout |
| 22 | `rank(-1 * ts_delta(sharesout, 5))` | neg_delta_5d | sharesout |
| 23 | `rank(sharesout / close)` | value_ratio | sharesout |
| 24 | `ts_decay_linear(rank(sharesout), 5)` | decay_linear | sharesout |

**Count**: 24 expressions

---

## Cluster 11: fundamental6 income revenue

_Revenue items. sales_ps/close = price-to-sales inverted._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(sales)` | level | sales |
| 2 | `rank(-1 * sales)` | neg_level | sales |
| 3 | `rank(ts_delta(sales, 5))` | delta_5d | sales |
| 4 | `rank(-1 * ts_delta(sales, 5))` | neg_delta_5d | sales |
| 5 | `rank(sales / close)` | value_ratio | sales |
| 6 | `ts_decay_linear(rank(sales), 5)` | decay_linear | sales |
| 7 | `trade_when(ts_std_dev(returns,20)>0.02, rank(sales), ts_std_dev(returns,20)<0.01)` | trade_when | sales |
| 8 | `rank(revenue)` | level | revenue |
| 9 | `rank(-1 * revenue)` | neg_level | revenue |
| 10 | `rank(ts_delta(revenue, 5))` | delta_5d | revenue |
| 11 | `rank(-1 * ts_delta(revenue, 5))` | neg_delta_5d | revenue |
| 12 | `rank(revenue / close)` | value_ratio | revenue |
| 13 | `ts_decay_linear(rank(revenue), 5)` | decay_linear | revenue |
| 14 | `trade_when(ts_std_dev(returns,20)>0.02, rank(revenue), ts_std_dev(returns,20)<0.01)` | trade_when | revenue |
| 15 | `rank(sales_ps)` | level | sales_ps |
| 16 | `rank(-1 * sales_ps)` | neg_level | sales_ps |
| 17 | `rank(ts_delta(sales_ps, 5))` | delta_5d | sales_ps |
| 18 | `rank(-1 * ts_delta(sales_ps, 5))` | neg_delta_5d | sales_ps |
| 19 | `rank(sales_ps / close)` | value_ratio | sales_ps |
| 20 | `ts_decay_linear(rank(sales_ps), 5)` | decay_linear | sales_ps |
| 21 | `trade_when(ts_std_dev(returns,20)>0.02, rank(sales_ps), ts_std_dev(returns,20)<0.01)` | trade_when | sales_ps |

**Count**: 21 expressions

---

## Cluster 12: socialmedia12 sentiment

_Social media sentiment and buzz. 100% coverage._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(scl12_buzz)` | level | scl12_buzz |
| 2 | `rank(-1 * scl12_buzz)` | neg_level | scl12_buzz |
| 3 | `rank(ts_delta(scl12_buzz, 5))` | delta_5d | scl12_buzz |
| 4 | `rank(-1 * ts_delta(scl12_buzz, 5))` | neg_delta_5d | scl12_buzz |
| 5 | `ts_decay_linear(rank(scl12_buzz), 5)` | decay_linear | scl12_buzz |
| 6 | `rank(snt_buzz)` | level | snt_buzz |
| 7 | `rank(-1 * snt_buzz)` | neg_level | snt_buzz |
| 8 | `rank(ts_delta(snt_buzz, 5))` | delta_5d | snt_buzz |
| 9 | `rank(-1 * ts_delta(snt_buzz, 5))` | neg_delta_5d | snt_buzz |
| 10 | `ts_decay_linear(rank(snt_buzz), 5)` | decay_linear | snt_buzz |
| 11 | `rank(scl12_sentiment)` | level | scl12_sentiment |
| 12 | `rank(-1 * scl12_sentiment)` | neg_level | scl12_sentiment |
| 13 | `rank(ts_delta(scl12_sentiment, 5))` | delta_5d | scl12_sentiment |
| 14 | `rank(-1 * ts_delta(scl12_sentiment, 5))` | neg_delta_5d | scl12_sentiment |
| 15 | `ts_decay_linear(rank(scl12_sentiment), 5)` | decay_linear | scl12_sentiment |
| 16 | `rank(snt_value)` | level | snt_value |
| 17 | `rank(-1 * snt_value)` | neg_level | snt_value |
| 18 | `rank(ts_delta(snt_value, 5))` | delta_5d | snt_value |
| 19 | `rank(-1 * ts_delta(snt_value, 5))` | neg_delta_5d | snt_value |
| 20 | `ts_decay_linear(rank(snt_value), 5)` | decay_linear | snt_value |
| 21 | `rank(scl12_sentiment * (-1 * returns))` | Contrarian: sentiment x reversal | composite |
| 22 | `rank(scl12_buzz * (-1 * returns))` | Buzz-weighted reversal | composite |
| 23 | `rank(ts_delta(scl12_sentiment, 5) * (volume/adv20))` | Sentiment momentum x volume | composite |
| 24 | `rank(-1 * scl12_buzz * scl12_sentiment)` | High buzz + negative sentiment | composite |

**Count**: 24 expressions

---

## Cluster 13: option8 historical volatility

_Realized volatility at different horizons and estimators._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(historical_volatility_180)` | level | historical_volatility_180 |
| 2 | `rank(-1 * historical_volatility_180)` | neg_level | historical_volatility_180 |
| 3 | `rank(ts_delta(historical_volatility_180, 5))` | delta_5d | historical_volatility_180 |
| 4 | `rank(-1 * ts_delta(historical_volatility_180, 5))` | neg_delta_5d | historical_volatility_180 |
| 5 | `rank(historical_volatility_10)` | level | historical_volatility_10 |
| 6 | `rank(-1 * historical_volatility_10)` | neg_level | historical_volatility_10 |
| 7 | `rank(ts_delta(historical_volatility_10, 5))` | delta_5d | historical_volatility_10 |
| 8 | `rank(-1 * ts_delta(historical_volatility_10, 5))` | neg_delta_5d | historical_volatility_10 |
| 9 | `rank(parkinson_volatility_120)` | level | parkinson_volatility_120 |
| 10 | `rank(-1 * parkinson_volatility_120)` | neg_level | parkinson_volatility_120 |
| 11 | `rank(ts_delta(parkinson_volatility_120, 5))` | delta_5d | parkinson_volatility_120 |
| 12 | `rank(-1 * ts_delta(parkinson_volatility_120, 5))` | neg_delta_5d | parkinson_volatility_120 |
| 13 | `rank(historical_volatility_10 - historical_volatility_180)` | Vol term structure (short - long realized) | composite |
| 14 | `rank(-1 * (historical_volatility_10 - historical_volatility_180))` | Vol term structure inverted | composite |

**Count**: 14 expressions

---

## Cluster 14: model51 systematic risk

_Risk decomposition: beta, idiosyncratic risk._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(unsystematic_risk_last_360_days)` | level | unsystematic_risk_last_360_days |
| 2 | `rank(-1 * unsystematic_risk_last_360_days)` | neg_level | unsystematic_risk_last_360_days |
| 3 | `rank(ts_delta(unsystematic_risk_last_360_days, 5))` | delta_5d | unsystematic_risk_last_360_days |
| 4 | `rank(-1 * ts_delta(unsystematic_risk_last_360_days, 5))` | neg_delta_5d | unsystematic_risk_last_360_days |
| 5 | `rank(unsystematic_risk_last_90_days)` | level | unsystematic_risk_last_90_days |
| 6 | `rank(-1 * unsystematic_risk_last_90_days)` | neg_level | unsystematic_risk_last_90_days |
| 7 | `rank(ts_delta(unsystematic_risk_last_90_days, 5))` | delta_5d | unsystematic_risk_last_90_days |
| 8 | `rank(-1 * ts_delta(unsystematic_risk_last_90_days, 5))` | neg_delta_5d | unsystematic_risk_last_90_days |
| 9 | `rank(beta_last_60_days_spy)` | level | beta_last_60_days_spy |
| 10 | `rank(-1 * beta_last_60_days_spy)` | neg_level | beta_last_60_days_spy |
| 11 | `rank(ts_delta(beta_last_60_days_spy, 5))` | delta_5d | beta_last_60_days_spy |
| 12 | `rank(-1 * ts_delta(beta_last_60_days_spy, 5))` | neg_delta_5d | beta_last_60_days_spy |
| 13 | `rank(-1 * beta_last_60_days_spy * returns)` | Beta-adjusted reversal | composite |
| 14 | `rank(unsystematic_risk_last_360_days - unsystematic_risk_last_90_days)` | Idiosyncratic risk change | composite |
| 15 | `ts_decay_linear(rank(-1 * beta_last_60_days_spy), 5)` | Smoothed low-beta | composite |

**Count**: 15 expressions

---

## Cluster 15: news12 news signals

_News-derived signals. Mixed coverage._

| # | Expression | Template | Field |
|---|-----------|----------|-------|
| 1 | `rank(news_tot_ticks)` | level | news_tot_ticks |
| 2 | `rank(-1 * news_tot_ticks)` | neg_level | news_tot_ticks |
| 3 | `rank(ts_delta(news_tot_ticks, 5))` | delta_5d | news_tot_ticks |
| 4 | `rank(-1 * ts_delta(news_tot_ticks, 5))` | neg_delta_5d | news_tot_ticks |
| 5 | `rank(news_atr14)` | level | news_atr14 |
| 6 | `rank(-1 * news_atr14)` | neg_level | news_atr14 |
| 7 | `rank(ts_delta(news_atr14, 5))` | delta_5d | news_atr14 |
| 8 | `rank(-1 * ts_delta(news_atr14, 5))` | neg_delta_5d | news_atr14 |
| 9 | `rank(news_pe_ratio)` | level | news_pe_ratio |
| 10 | `rank(-1 * news_pe_ratio)` | neg_level | news_pe_ratio |
| 11 | `rank(ts_delta(news_pe_ratio, 5))` | delta_5d | news_pe_ratio |
| 12 | `rank(-1 * ts_delta(news_pe_ratio, 5))` | neg_delta_5d | news_pe_ratio |
| 13 | `rank(news_max_up_ret)` | level | news_max_up_ret |
| 14 | `rank(-1 * news_max_up_ret)` | neg_level | news_max_up_ret |
| 15 | `rank(ts_delta(news_max_up_ret, 5))` | delta_5d | news_max_up_ret |
| 16 | `rank(-1 * ts_delta(news_max_up_ret, 5))` | neg_delta_5d | news_max_up_ret |
| 17 | `rank(news_indx_perf)` | level | news_indx_perf |
| 18 | `rank(-1 * news_indx_perf)` | neg_level | news_indx_perf |
| 19 | `rank(ts_delta(news_indx_perf, 5))` | delta_5d | news_indx_perf |
| 20 | `rank(-1 * ts_delta(news_indx_perf, 5))` | neg_delta_5d | news_indx_perf |
| 21 | `rank(news_indx_perf * (-1 * returns))` | Relative performance x reversal | composite |
| 22 | `ts_decay_linear(rank(-1 * news_atr14), 5)` | Smoothed low-ATR | composite |

**Count**: 22 expressions

---

## Summary

**Total expressions**: 456
**Clusters**: 15
**Estimated BRAIN budget**: 456 sims = 9.1% of daily budget
**Estimated wall time**: 152 min at 3 concurrent slots