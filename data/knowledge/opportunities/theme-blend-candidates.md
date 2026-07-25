---
type: theme_blend_candidates
generated: '2026-06-15'
method: 'cluster-of-clusters: unit-vol theme composites blended pairwise (screening
  estimate)'
n_blends: 20
caveat: Composite Sharpe pools many redundant members (noise-reduced theme portfolio).
  A real BRAIN alpha blends a few representative members and must pass checks + self-corr.
  Use as research direction, not a finished alpha.
---
# Theme-Blend Candidates (cluster x cluster research directions)

Each redundancy cluster is pooled into a noise-reduced theme composite; the table ranks decorrelated cross-family theme pairs. These are higher-level research directions than single-pair blends -- combine two orthogonal themes to add marginal PnL where the analyst x fundamental core is saturated.

| Theme A (rep) | Theme B (rep) | Families | rho | S_a | S_b | S_comb | div+ | starter blend (representatives) |
|---|---|---|---|---|---|---|---|---|
| C82 (pcr_oi_10) | C60 (fnd2_dfdtxasoprlcarryfwd) | option9/fundamental2 | -0.64 | 0.64 | 0.70 | 1.57 | +0.87 | `ts_decay_linear((rank(pcr_oi_10)) + (rank(fnd2_dfdtxasoprlcarryfwd / close)), 5)` |
| C75 (fn_debt_instrument_interest_rate_stated_percentage_a) | C82 (pcr_oi_10) | analyst4/option9 | -0.55 | 0.70 | 0.64 | 1.41 | +0.71 | `ts_decay_linear((rank(fn_debt_instrument_interest_rate_stated_percentage_a / close)) + (rank(pcr_oi_10)), 5)` |
| C75 (fn_debt_instrument_interest_rate_stated_percentage_a) | C23 (pcr_vol_20) | analyst4/option9 | -0.49 | 0.70 | 1.03 | 1.72 | +0.69 | `ts_decay_linear((rank(fn_debt_instrument_interest_rate_stated_percentage_a / close)) + (rank(pcr_vol_20)), 5)` |
| C7 (max_adjusted_net_income_guidance) | C2 (rank(fnd6_acdo) + rank(open/close - 1)) | analyst4/socialmedia12 | -0.14 | 1.44 | 1.88 | 2.53 | +0.65 | `ts_decay_linear((rank(max_adjusted_net_income_guidance)) + (rank(fnd6_acdo) + rank(open/close - 1)), 5)` |
| C13 (anl4_bvps_flag) | C60 (fnd2_dfdtxasoprlcarryfwd) | analyst4/fundamental2 | -0.44 | 0.80 | 0.70 | 1.41 | +0.61 | `ts_decay_linear((rank(anl4_bvps_flag)) + (rank(fnd2_dfdtxasoprlcarryfwd / close)), 5)` |
| C17 (fnd6_newqv1300_aol2q) | C75 (fn_debt_instrument_interest_rate_stated_percentage_a) | analyst4/analyst4 | -0.43 | 0.84 | 0.70 | 1.45 | +0.60 | `ts_decay_linear((rank(fnd6_newqv1300_aol2q / close)) + (rank(fn_debt_instrument_interest_rate_stated_percentage_a / close)), 5)` |
| C28 (implied_volatility_mean_skew_360) | C27 (fnd6_tlcf) | option8/fundamental2 | -0.27 | 0.94 | 1.10 | 1.69 | +0.59 | `ts_decay_linear((rank(implied_volatility_mean_skew_360)) + (rank(fnd6_tlcf)), 5)` |
| C43 (relative_valuation_rank_derivative) | C28 (implied_volatility_mean_skew_360) | model16/option8 | -0.30 | 0.87 | 0.94 | 1.53 | +0.58 | `ts_decay_linear((rank(ts_delta(relative_valuation_rank_derivative, 5))) + (rank(implied_volatility_mean_skew_360)), 5)` |
| C5 (sales_estimate_count_quarterly) | C29 (anl4_tbvps_high) | analyst4/analyst4 | -0.23 | 1.36 | 1.03 | 1.92 | +0.57 | `ts_decay_linear((rank(sales_estimate_count_quarterly)) + (rank(anl4_tbvps_high / close)), 5)` |
| C18 (anl4_totassets_flag) | C2 (rank(fnd6_acdo) + rank(open/close - 1)) | analyst4/socialmedia12 | -0.20 | 1.19 | 1.88 | 2.45 | +0.57 | `ts_decay_linear((rank(anl4_totassets_flag)) + (rank(fnd6_acdo) + rank(open/close - 1)), 5)` |
| C60 (fnd2_dfdtxasoprlcarryfwd) | C23 (pcr_vol_20) | fundamental2/option9 | -0.41 | 0.70 | 1.03 | 1.59 | +0.57 | `ts_decay_linear((rank(fnd2_dfdtxasoprlcarryfwd / close)) + (rank(pcr_vol_20)), 5)` |
| C29 (anl4_tbvps_high) | C23 (pcr_vol_20) | analyst4/option9 | -0.16 | 1.03 | 1.03 | 1.59 | +0.56 | `ts_decay_linear((rank(anl4_tbvps_high / close)) + (rank(pcr_vol_20)), 5)` |
| C36 (anl4_fcf_high) | C2 (rank(fnd6_acdo) + rank(open/close - 1)) | analyst4/socialmedia12 | -0.30 | 0.97 | 1.88 | 2.44 | +0.56 | `ts_decay_linear((rank(anl4_fcf_high / close)) + (rank(fnd6_acdo) + rank(open/close - 1)), 5)` |
| C82 (pcr_oi_10) | C72 (anl4_afv4_eps_number) | option9/analyst4 | -0.43 | 0.64 | 0.66 | 1.22 | +0.56 | `ts_decay_linear((rank(pcr_oi_10)) + (rank(anl4_afv4_eps_number / close)), 5)` |
| C13 (anl4_bvps_flag) | C43 (relative_valuation_rank_derivative) | analyst4/model16 | -0.31 | 0.80 | 0.87 | 1.41 | +0.55 | `ts_decay_linear((rank(anl4_bvps_flag)) + (rank(ts_delta(relative_valuation_rank_derivative, 5))), 5)` |
| C43 (relative_valuation_rank_derivative) | C36 (anl4_fcf_high) | model16/analyst4 | -0.27 | 0.87 | 0.97 | 1.52 | +0.55 | `ts_decay_linear((rank(ts_delta(relative_valuation_rank_derivative, 5))) + (rank(anl4_fcf_high / close)), 5)` |
| C28 (implied_volatility_mean_skew_360) | C60 (fnd2_dfdtxasoprlcarryfwd) | option8/fundamental2 | -0.39 | 0.94 | 0.70 | 1.49 | +0.54 | `ts_decay_linear((rank(implied_volatility_mean_skew_360)) + (rank(fnd2_dfdtxasoprlcarryfwd / close)), 5)` |
| C5 (sales_estimate_count_quarterly) | C2 (rank(fnd6_acdo) + rank(open/close - 1)) | analyst4/socialmedia12 | -0.10 | 1.36 | 1.88 | 2.42 | +0.54 | `ts_decay_linear((rank(sales_estimate_count_quarterly)) + (rank(fnd6_acdo) + rank(open/close - 1)), 5)` |
| C17 (fnd6_newqv1300_aol2q) | C60 (fnd2_dfdtxasoprlcarryfwd) | analyst4/fundamental2 | -0.38 | 0.84 | 0.70 | 1.38 | +0.54 | `ts_decay_linear((rank(fnd6_newqv1300_aol2q / close)) + (rank(fnd2_dfdtxasoprlcarryfwd / close)), 5)` |
| C4 (implied_volatility_put_90) | C7 (max_adjusted_net_income_guidance) | option8/analyst4 | +0.01 | 1.61 | 1.44 | 2.15 | +0.53 | `ts_decay_linear((rank(ts_delta(implied_volatility_put_90, 5))) + (rank(max_adjusted_net_income_guidance)), 5)` |

## How to use

1. Each row is two orthogonal *themes*; the composite Sharpe is the pooled diversification ceiling, not a single alpha.
2. Start from the `starter blend` (theme representatives) or pool 2-3 top members of each theme, then simulate.
3. Prioritize themes whose raw fields are NOT already in the submitted book (lower self-corr; see the over-concentration note in patterns/).
