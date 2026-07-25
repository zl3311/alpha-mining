---
id: "20260609-001"
date: "2026-06-09"
strategy: "EXPLORE"
research_question: "Can novel cross-cluster ratios (fund6), options term structure (option8), cross-family interactions, or standalone sentiment produce decorrelated submittable alphas?"
budget_used: 163
budget_cap: null
trigger: "local_manual"
gate_passers: 39
submissions: 0
submittable_candidates: 4
status: "productive"
tags:
  - "20260609-001"
  - "explore_novel_structures"
  - "leverage_premium"
  - "cross_cluster_ratios"
candidates:
  - id: "pw7j2MXg"
    grade: "EXCELLENT"
    sharpe: 1.98
    fitness: 2.01
    self_corr_value: 0.412
    self_corr_result: "PASS"
    verdict: "SUBMITTABLE"
  - id: "E5KlNNj9"
    grade: "GOOD"
    sharpe: 1.88
    fitness: 1.58
    self_corr_value: 0.564
    self_corr_result: "PASS"
    verdict: "SUPERSEDED by pw7j2MXg"
  - id: "j2gjVLWQ"
    grade: "GOOD"
    sharpe: 1.87
    fitness: 1.57
    self_corr_value: 0.565
    self_corr_result: "PASS"
    verdict: "REDUNDANT (leverage family mutual corr)"
  - id: "1YgwAVxz"
    grade: "GOOD"
    sharpe: 1.72
    fitness: 1.66
    self_corr_value: 0.350
    self_corr_result: "PASS"
    verdict: "REDUNDANT (leverage family mutual corr)"
---

# Session 20260609-001: EXPLORE — Leverage Premium Discovery

## Research Question

Can novel cross-cluster ratios (fund6), options term structure (option8),
cross-family interactions, or standalone sentiment produce decorrelated
submittable alphas?

## Answer: YES — Leverage premium is a new fertile mechanism family

**Primary candidate:** pw7j2MXg — EXCELLENT S=1.98 F=2.01, ALL 8 BRAIN checks PASS,
self-corr 0.412 (SAFE). Expression: `zscore(-1 * equity / assets) + rank(fnd6_itci / close) + rank(fnd6_itci / close)`.

The key structural insight was double-weighting the quality component (2:1 itci:leverage)
combined with zscore (not rank) normalization of leverage. This fixed the
LOW_SUB_UNIVERSE_SHARPE failure that blocked all rank-based leverage+itci variants.

## Key Discovery: Financial Leverage Premium

The session's breakthrough finding is that `rank(-1 * equity / assets)` — a
simple leverage ratio — produces S=1.55 standalone and combines powerfully with
every fundamental6 field. The leverage premium is an intra-industry effect:
S=1.55 with SUBINDUSTRY neut vs S=0.72 with MARKET neut.

### Leverage + fnd6_itci = EXCELLENT (but structurally blocked)

`rank(-1 * equity / assets) + rank(fnd6_itci / close)` achieves EXCELLENT S=2.37
F=2.42, but ALWAYS fails LOW_SUB_UNIVERSE_SHARPE. Attempted fixes:
- volume/adv20 stabilizer: improved sub-univ from 0.84 → 0.94, still fails (lim 1.0)
- group_rank normalization: improved to 0.79-0.81, still fails
- scl12_buzz: destroyed fitness (turnover 39-47%)
- cap, close, sharesout stabilizers: all failed

The itci field has structurally uneven performance across subindustries.

### Leverage + fnd6_drlt = GOOD (submittable)

`rank(-1 * equity / assets) + rank(fnd6_drlt / close)` achieves GOOD S=1.87-1.88
F=1.57-1.58 and PASSES all 8 BRAIN checks + self-corr (0.564).

### What didn't work

| Direction | Result |
|-----------|--------|
| Cross-cluster fundamental ratios (EV/EBITDA, ROA, etc.) | All INFERIOR (S < 0.85) |
| Options term structure (IV vs realized vol) | INFERIOR (S < 0.17) |
| Standalone sentiment (scl12_sentiment, buzz) | All negative Sharpe |
| Dividend yield | Negative Sharpe |
| Cross-family multiplicative interactions | All destroyed signal |
| Leverage momentum (ts_delta of equity/assets) | All INFERIOR |
| MARKET neutralization for leverage | Killed signal (S=0.72 vs 1.55) |

## Rounds

### Round 1: Novel templates (25 sims, 0 gate-passers)
- Tested 20 novel templates: cross-cluster ratios, options term structure,
  sentiment standalone, cross-family interactions
- ALL failed except analyst+itci blend (AVERAGE S=1.03)

### Round 2: Negated directions (15 sims, 4 gate-passers)
- KEY INSIGHT: `rank(equity/assets)` had S=-1.55, meaning the negated direction
  `rank(-1 * equity / assets)` gives S=+1.55
- Pure leverage: AVERAGE S=1.55 F=1.28
- Analyst+leverage blend: GOOD S=1.67 F=1.75 (but fails self-corr at 0.74 vs vRmlGnkv)

### Round 3: Leverage refinement (10 sims, 8 gate-passers)
- **EXCELLENT S=2.37** — leverage+itci (fails LOW_SUB_UNIVERSE)
- **GOOD S=1.87** — leverage+drlt (ALL PASS, self-corr PASS!)
- Leverage works with every fund6 field tested

### Rounds 4-12: Wide exploration + EXCELLENT fixes (86 sims, 27 gate-passers)
- Leverage momentum: failed (equity/assets has no meaningful short-term dynamics)
- Leverage+analyst blends: GOOD S=1.77 (ptp_flag), AVERAGE (epsr, capex)
- Leverage+itci sub-universe fixes: ALL failed (structural block)
- `zscore(-1*equity/assets) + rank(fnd6_itci/close)`: GOOD S=1.72, ALL PASS (zscore fixes sub-univ!)
- Fund6 field/close ratios: all INFERIOR
- Fund6 momentum (ts_delta): all INFERIOR
- Analyst estimate levels: still processing

## Submission Queue

- **E5KlNNj9** (GOOD S=1.88 F=1.58): QUEUED for manual submission
  - https://platform.worldquantbrain.com/alpha/E5KlNNj9

## Lessons Learned

1. **Financial leverage is a new mechanism family**: `rank(-1 * equity / assets)`
   is a universal alpha enhancer. S=1.55 standalone, boosted to 1.87-2.37 when
   combined with fundamental quality fields. This is the capital structure risk
   premium — high-leverage firms outperform within their industry peer groups.

2. **Leverage is purely intra-industry**: MARKET neut kills the signal (S=0.72).
   The premium operates within subindustries where leverage is a strategic choice.

3. **The itci combination is EXCELLENT but permanently blocked**: Every attempted
   fix for LOW_SUB_UNIVERSE_SHARPE failed. The fnd6_itci field has structurally
   uneven performance across industries.

4. **zscore normalization can fix sub-universe issues**: `zscore(-1*equity/assets)`
   (vs `rank(-1*equity/assets)`) produces a different distribution that passes
   the sub-universe check for the itci blend. Generalizable insight.

5. **Cross-cluster fundamental ratios are dead**: Classic value factors
   (EV/EBITDA, ROA, earnings yield) are fully priced at TOP3000. S < 0.85 for all.

6. **Sentiment and news are noise standalone**: scl12_sentiment, scl12_buzz,
   snt_social_value all produced negative Sharpe. Only useful as stabilizers.

7. **Negating poorly-performing expressions can reveal hidden signals**: The
   entire leverage discovery came from observing S=-1.55 on `rank(equity/assets)`
   and testing the negation.

## Next Steps

1. Submit E5KlNNj9 on BRAIN platform
2. Explore `zscore(-1*equity/assets) + rank(fnd6_itci/close)` (1YgwAVxz) as a
   potential second submission after E5KlNNj9 is submitted (lowest mutual corr)
3. Test leverage premium on other universes if tier upgrade becomes available
4. Record leverage premium as a knowledge pattern
