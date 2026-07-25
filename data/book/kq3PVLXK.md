---
alpha_id: "kq3PVLXK"
grade: "SPECTACULAR"
status: "PENDING"
sharpe: 2.91
fitness: 4.93
turnover: 0.065
family: "iv60_guidance_revision"
mechanism: "4-factor cross-dataset blend: IV60 call-put spread zscore (44d smoothing) + max adjusted net income guidance + BVPS revision flag + total assets revision flag."
expression: "ts_decay_linear(zscore(ts_mean(implied_volatility_call_60 - implied_volatility_put_60, 44)) + rank(max_adjusted_net_income_guidance) + rank(anl4_bvps_flag) + rank(anl4_totassets_flag), 5)"
neutralization: "SUBINDUSTRY"
decay: 6
universe: "TOP3000"
region: "USA"
self_corr_value: 0.7344
self_corr_result: "PASS"
self_corr_method: "sharpe_premium_escape"
top_corr_peer: "Gro21wWG"
top_corr_peer_sharpe: 2.59
brain_checks_pass: true
session: "20260625-001"
discovered: "2026-06-25"
platform_url: "https://platform.worldquantbrain.com/alpha/kq3PVLXK"
---

# kq3PVLXK — IV60 44d Guidance + BVPS + TotAssets Revision (Backup)

SPECTACULAR backup candidate. Lower Sharpe than QPaG3OGM but also lower
self-corr (0.734 vs 0.821), providing more correlation headroom for future
book additions.
