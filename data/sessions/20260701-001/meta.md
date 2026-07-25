---
id: "20260701-001"
date: "2026-07-01"
strategy: "EXPLORE"
trigger: "local_manual_mining_session"
budget_used: 48
budget_cap: null
target_grade: "EXCELLENT+"
status: "productive"
result: "1 SPECTACULAR submittable candidate from novel PP&E capital intensity family"
gate_passers: 28
submissions: 1
submitted: ["ZYpVLGZj"]
branch: "session/20260701-001-explore-novel-anchors"
tags:
  - "20260701-001"
  - "explore_novel"
  - "novel_anchors"
  - "ppe_family"
candidates:
  - id: "ZYpVLGZj"
    grade: "SPECTACULAR"
    sharpe: 2.84
    fitness: 3.21
    turnover: 0.178
    self_corr_value: 0.7943
    self_corr_result: "PASS"
    verdict: "SUBMITTED"
  - id: "pw6br7Jo"
    grade: "SPECTACULAR"
    sharpe: 2.75
    fitness: 3.30
    turnover: 0.151
    self_corr_value: 0.7779
    self_corr_result: "FAIL"
    verdict: "BLOCKED — premium escape fails (2.75 < 2.838)"
  - id: "gJ1NEenJ"
    grade: "SPECTACULAR"
    sharpe: 2.35
    fitness: 2.63
    turnover: 0.150
    self_corr_value: 0.7956
    self_corr_result: "FAIL"
    verdict: "BLOCKED by 3q7JQK16 (shared bvps+drlt+gap)"
best_alpha: "ZYpVLGZj"
best_sharpe: 2.84
best_fitness: 3.21
best_self_corr: 0.7943
---

# Session 20260701-001: EXPLORE — PP&E Capital Intensity Discovery

## Research Question

Can novel anchor fields from under-explored datasets (option8 IV mean skew, fnd6 PP&E gross, analyst coverage counts) produce EXCELLENT+ alphas that pass the self-correlation wall?

## Strategy Rationale

EXPLORE mode (default for saturated book). Book has 46 entries with 17+ SPECTACULAR across 39+ mechanism families. Field exploration is largely complete for known strong fields. This session focused on:
- option8 implied_volatility_mean_skew (never used as primary anchor in book)
- fnd6_newqv1300_ppegtq (PP&E gross total, novel capital intensity signal)
- sales_estimate_count_quarterly (analyst coverage breadth)
- Various novel analyst4 fields (afv4_dts_spe, tbvps_high, fcf_high)

## Key Findings

1. **PP&E gross (fnd6_newqv1300_ppegtq) is a powerful novel anchor**: When combined with analyst revision and overnight gap, produces SPECTACULAR grade (S=2.75-2.84) with ALL 7 BRAIN checks passing.

2. **Decay=8 is the critical lever**: The same PP&E expression at decay=6 (S=2.75) fails self-corr premium escape, but at decay=8 (S=2.84) it barely passes (margin +0.002). Higher decay reduces turnover (17.8% vs 15.1%) and increases Sharpe enough to clear the threshold.

3. **Self-corr wall requires careful field selection**: PP&E + bvps + drlt + gap (gJ1NEenJ) has BRAIN self-corr 0.796 vs 3q7JQK16 (shares 3/4 fields). PP&E + ptpr + itci + gap (pw6br7Jo) has self-corr 0.778 vs MPbgqZ7o (shares itci). Only the decay=8 variant achieves high enough Sharpe for premium escape.

4. **IV mean skew (option8) disappoints as anchor**: AVERAGE to GOOD only (S=1.27-2.25). The smoothed zscore variant is slightly better but still GOOD. IV mean skew captures different information than IV call-put spreads but isn't strong enough alone for EXCELLENT+.

5. **Sales estimate count reaches EXCELLENT but fails SUB_UNIVERSE**: Coverage breadth + revision + fundamentals produces S=2.10-2.32 but consistently fails LOW_SUB_UNIVERSE_SHARPE (0.78-0.90 vs 1.0 limit). Coverage breadth is structurally uneven across sub-industries.

6. **Zero-overlap candidates (novel analyst + novel fundamental) stay GOOD**: PP&E with tbvps_high, fcf_high, eps_number, or dd1q as legs only reaches GOOD (S=1.48-1.76). The novel analyst fields are too weak to boost beyond EXCELLENT.

## Round-by-Round Summary

| Round | Sims | Strategy | Best Result | Outcome |
|-------|------|----------|-------------|---------|
| R1 (batch_r1) | 20 | Novel anchors (IV skew, PP&E, coverage) + novel structures | pw6br7Jo SPECTACULAR S=2.75 | BLOCKED (self-corr 0.778 vs MPbgqZ7o) |
| R2 (batch_r2) | 15 | PP&E mutations (replace itci to decorrelate) | gJ1NEenJ SPECTACULAR S=2.35 | BLOCKED (self-corr 0.796 vs 3q7JQK16) |
| R3 (batch_r3) | 13 | Zero-overlap PP&E + decay sweep + MARKET neut | **ZYpVLGZj SPECTACULAR S=2.84 ALL PASS** | **WINNER!** |

## Submission Recommendation

Submit **ZYpVLGZj** (SPECTACULAR, S=2.84, F=3.21, self-corr PASS via premium). Risk: razor-thin margin (+0.002) — submit promptly before peer Sharpe fluctuations could block.

**UPDATE**: Submitted and ACTIVE on BRAIN as of 2026-07-01.

## Next Steps

- Submit ZYpVLGZj promptly (premium escape margin is minimal)
- PP&E (ppegtq) is confirmed as a productive novel anchor — future sessions can explore different PP&E combinations with lower self-corr (e.g., different neutralization, non-overlapping fundamental legs)
- IV mean skew and sales estimate count are secondary signals — best used as blend legs, not primary anchors
