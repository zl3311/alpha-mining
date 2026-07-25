---
type: "submit-candidate"
alpha_id: "VkPdaQ2b"
grade: "SPECTACULAR"
sharpe: 2.18
fitness: 2.65
turnover: 0.0721
self_corr: 0.697
self_corr_peer: "npWYoqQz"
self_corr_result: "PASS (local estimate ≤ 0.70 auto-pass threshold)"
session: "20260712-001"
status: "pending_review"
priority: "high"
long_term_value: "MEDIUM (SPECTACULAR grade but RISKY self-corr margin: 0.697 vs 0.70 threshold)"
brain_url: "https://platform.worldquantbrain.com/alpha/VkPdaQ2b"
---

# Submit Candidate: VkPdaQ2b — cptmfmq Event-Magnitude × IV Spread × Gric Blend

## Expression

`ts_decay_linear(rank(abs(ts_delta(fnd6_cptmfmq_dlttq / close, 3))) + rank(-1 * equity / assets) + zscore(ts_mean(implied_volatility_call_270 - implied_volatility_put_270, 22)) + rank(anl4_gric_flag), 5)`

## Why Submit

- SPECTACULAR grade (S=2.18, F=2.65, T=7.2%) — meets EXCELLENT+ threshold
- All 7 computable BRAIN checks PASS
- Novel cross-dataset mechanism: fundamental event-magnitude (long-term debt capital markets) × options IV × leverage × analyst revision flag
- First book entry in the `cptmfmq_event_magnitude_iv_gric_blend` family
- Self-corr 0.697 < 0.70 auto-pass threshold (max peer: npWYoqQz, iv_fundamental_analyst_blend, S=2.09)

## Submission Order Note

Per `submission-priority-long-term.md`, submit candidates with lowest self-corr first. VkPdaQ2b at 0.697 is borderline — submit only after verifying BRAIN authoritative self-corr resolves to PASS (check `/alphas/VkPdaQ2b/check` endpoint for SELF_CORRELATION status before submitting).

## Pre-Submission Checklist

- [ ] BRAIN `/alphas/VkPdaQ2b/check` → SELF_CORRELATION shows PASS (not PENDING)
- [ ] All other 7 checks still PASS
- [ ] No new ACTIVE alphas submitted since this session (which would need to be added to the self-corr universe)
