---
id: "20260625-002"
date: "2026-06-25"
strategy: "EXPLORE"
research_question: "Can non-IV fundamental+analyst+intraday blends break through the self-correlation wall while maintaining EXCELLENT+ grade?"
budget_used: 26
budget_cap: null
trigger: "local_manual_mining_session"
gate_passers: 16
submissions: 1
submitted: ["3q7lm2p6"]
submittable_candidates: 1
status: "productive"
branch: "exp/20260625-002-explore-novel-fundamental"
tags:
  - "20260625-002"
  - "explore_novel"
  - "non_iv"
  - "fundamental_intraday"
candidates:
  - id: "P0p7LAvL"
    grade: "SPECTACULAR"
    sharpe: 3.02
    fitness: 3.48
    self_corr_value: 0.6318
    self_corr_result: "STALE — sibling 3q7lm2p6 now ACTIVE; recompute before submitting"
    verdict: "BLOCKED — sibling 3q7lm2p6 now ACTIVE (same template family)"
  - id: "3q7lm2p6"
    grade: "SPECTACULAR"
    sharpe: 2.95
    fitness: 3.44
    self_corr_value: 0.7819
    self_corr_result: "PASS_PREMIUM"
    verdict: "SUBMITTED"
---

# Session 20260625-002: EXPLORE — Novel Fundamental + Intraday Blend

## Research Question

The book is saturated with IV60/IV90 options families (88z7MM37, ZYpk2kx8, Gro21wWG all use IV spreads). All new IV60 variants fail SELF_CORRELATION (0.83-0.96 against 88z7MM37). Can a purely fundamental + analyst + intraday expression achieve SPECTACULAR grade while staying below the 0.7 self-correlation threshold?

## Strategy Rationale

Default EXPLORE mode. The book is near saturation with 38 entries. Recent 24h discoveries showed 50+ new IV60 SPECTACULAR variants, but ALL fail self-correlation. The self-corr wall is the binding constraint, not grade. Novel non-IV mechanisms are the only viable path to decorrelated submissions.

## Key Findings

- **IV60 family is definitively blocked**: Even S=3.09 variants fail self-corr (0.83+) against 88z7MM37 (S=2.78). Premium escape requires S >= 3.06 with 4 factors, but adding a 4th factor drops Sharpe to 2.82.
- **4-factor additive blends fix SUB_UNIVERSE_SHARPE**: Adding fundamental legs to IV60 fixed the sub-universe check (1.28-1.38 vs 1.16-1.34 limit) but couldn't overcome the self-corr barrier.
- **Non-IV fundamental+intraday blends can achieve SPECTACULAR**: `rank(fnd6_acdo/close) + rank(open/close - 1) + rank(analyst_flag) + rank(fnd6_itci/close)` produces S=2.95-3.02, F=3.44-3.48 with self-corr MAX 0.63 — well below the 0.7 threshold.
- **The `open/close - 1` component** (overnight gap) provides the Sharpe kick that elevates fundamental blends from EXCELLENT to SPECTACULAR. It captures informed overnight trading (institutional order flow, after-hours news).
- **`anl4_ptpr_flag`** (pre-tax profit revision) is the strongest analyst complement to the acdo+itci fundamental core — better than bvps_flag or netdebt_flag for Sharpe.

## Next Steps

- P0p7LAvL is now BLOCKED (sibling 3q7lm2p6 already ACTIVE on same template); recompute self-corr before attempting submission
- Explore mutations of the winning template with different analyst flags and fundamental legs to find additional decorrelated variants
- The `open/close - 1` pattern could be a new discovery — test with other fundamental anchors
