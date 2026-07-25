---
id: "20260715-003"
date: "2026-07-15"
strategy: "EXPLORE"
research_question: "Session 20260715-002 confirmed that TWO different anchors (fnd6_pstkrv, min_net_debt_guidance) sharing the same ivaco + drlt/fatl + analyst4_flag + buzz*(-ret) stabilizer combination BOTH landed at the identical self-corr 0.796 -- strong evidence this stabilizer combination itself is now a hard correlation ceiling for the event-magnitude family. Can a genuinely different stabilizer set (avoiding ALL of ivaco, drlt, fatl, any anl4_*_flag, and buzz*(-returns) simultaneously -- e.g. volume/adv20 participation, sales_estimate_count_quarterly coverage breadth (non-flag), historical_volatility, pv13 network-centrality fields, or fresh fundamental6 densifiers fnd6_fopo/fopox) reach EXCELLENT fitness while staying decorrelated from the 47-alpha ACTIVE book?"
budget_used: 55
budget_cap: null
trigger: "manual (user-initiated continuation of session 20260715-002, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR)"
gate_passers: 2
submissions: 0
submittable_candidates: 0
status: "dead_end_with_diagnostic_insight"
tags:
  - "session_20260715-003"
  - "EXPLORE"
  - "stabilizer_escape"
candidates:
  - id: "d50Jdpg2"
    grade: "SPECTACULAR"
    sharpe: 2.15
    fitness: 3.06
    self_corr_value: 0.824
    self_corr_result: "estimated BLOCKED (local PnL vs book)"
    verdict: "BLOCKED"
  - id: "np2GnbLd"
    grade: "EXCELLENT"
    sharpe: 2.03
    fitness: 2.45
    self_corr_value: 0.725
    self_corr_result: "FAIL LOW_SUB_UNIVERSE_SHARPE (0.75 vs 0.88) AND estimated BLOCKED on self-corr"
    verdict: "BLOCKED"
  - id: "xAk7RElJ"
    grade: "INFERIOR"
    sharpe: 0.43
    fitness: 0.17
    self_corr_value: 0.496
    self_corr_result: "SAFE (local)"
    verdict: "DIAGNOSTIC ONLY — too weak to submit, but proves the anchor itself is decorrelated"
best_alpha: null
best_grade: null
best_sharpe: null
best_fitness: null
best_self_corr: null
best_self_corr_peer: null
best_self_corr_method: "N/A -- no submittable candidate found. Key diagnostic: the pure fnd6_pstkrv event-magnitude anchor alone is self-corr SAFE (0.496) but too weak standalone (S=0.43). Every one of 14+ distinct secondary-leg combinations tested to boost fitness (ivaco, drlt, buzz-reversal, analyst4 flags, guidance fields, IV90 options spread, volume/adv20, sales_estimate_count, historical_volatility, pv13 network centrality, a second weak anchor) pushed local self-corr to 0.69-0.85 once fitness reached GOOD+ -- strongly suggesting the 47-alpha book is now dense enough that any sufficiently potent secondary leg inherits correlation with whichever family it belongs to."
---

# Session 20260715-003: EXPLORE — Stabilizer-Set Escape from the ivaco+drlt+flag+buzz Correlation Ceiling

> **Correction (added 20260719-001).** This session's research question assumed
> that two anchors sharing the `ivaco+drlt+flag+buzz` stabilizer both landed at
> self-corr 0.796, implying a hard ceiling for the combination. That premise was
> false: the 0.796 belonged to `oml0kV52` alone and was misattributed to
> `N1rlJ7mq`, whose true value is **0.6903 PASS** (now ACTIVE). The escape this
> session searched for was therefore not needed on `fnd6_pstkrv`. Its negative
> findings on fresh-substitute and IV90 legs, and on `mibnq`, still stand. See
> `data/knowledge/rules/pstkrv-family-multiplier-exception.md`.

## Context Assessment (Phase 0)

- Direct continuation of session `20260715-002` (PR #91, now confirmed
  dead-end): both `N1rlJ7mq` (`fnd6_pstkrv` anchor) and `oml0kV52`
  (`min_net_debt_guidance` anchor) — sharing the identical `ivaco +
  drlt/fatl + analyst4_flag + buzz*(-ret)` stabilizer combination — were
  human-confirmed BLOCKED on the BRAIN platform at the **identical**
  self-corr value (0.796), despite having completely different anchor
  fields. This is strong evidence the correlation ceiling is now set by the
  STABILIZER COMBINATION itself, not the anchor.
- Book: 46 ACTIVE + 10 PENDING across 53 mechanism families.
  `N1rlJ7mq`/`oml0kV52` recorded as REJECTED in `data/book/` and
  `data/knowledge/opportunities/` respectively (session 002).
  **[Correction 20260719-001: only `oml0kV52` is genuinely blocked.
  `N1rlJ7mq` is 0.6903 PASS and is now ACTIVE in `data/book/`.]**
- New rule from session 002: `pstkrv-family-multiplier-exception.md` — local
  PnL estimates above ~0.60 for this family are inconclusive, not favorable.
  Applying a tighter local-SAFE bar (<0.60, not <0.70) for all candidates
  this session given the unresolved BRAIN API self-corr latency issues seen
  yesterday.
  **[Correction 20260719-001: that rule is RETRACTED. The multiplier it was
  based on never occurred, and the <0.60 bar was never justified — the <0.70
  bar stands. Do not carry this tightening into new sessions.]**
- Target: an EXCELLENT-fitness leg combination that avoids ALL of `ivaco`,
  `drlt`, `fatl`, every `anl4_*_flag` (per `analyst4-flag-mega-cluster.md`,
  effectively one 127+7-member cluster), and `buzz*(-1*returns)`
  simultaneously — per session 002's own Next Steps recommendation.

## Fresh Stabilizer Candidates (avoiding the blocked combination entirely)

- `rank(volume / adv20)` — pure price-volume participation/liquidity signal,
  zero overlap with any fundamental/analyst/sentiment leg in the book.
- `rank(sales_estimate_count_quarterly)` — analyst COVERAGE BREADTH (not a
  `_flag` field; redundancy cluster #5, distinct from clusters #13/#18).
- `rank(historical_volatility_90)` / `rank(parkinson_volatility_90)` —
  option8 realized-vol fields, cluster #48 (4 members), never used as a
  stabilizer leg (only as a `trade_when` GATE in prior sessions).
- `rank(pv13_ustomergraphrank_hub_rank)` — customer-relationship-network
  centrality (pv13 dataset), cluster #69 (2 members), completely untested.
- `rank(fnd6_fopo / close)` / `rank(fnd6_fopox / close)` — fresh
  fundamental6 fields (funds-from-operations variants), clusters #31/#32,
  zero book coverage.
- `rank(ts_mean(scl12_buzz, 5))` (buzz LEVEL, no `*(-1*returns)` reversal
  multiplier) — different dynamic from the blocked buzz-reversal stabilizer,
  per `flag-ret-correlation.md`'s own suggested escape route (previously
  tested alone and found weak, but not yet tested as ONE leg among several).
- Anchors: reuse `fnd6_pstkrv` and `fnd6_newqv1300_mibnq` (both already
  validated as strong, low-redundancy-cluster event-magnitude anchors from
  session 002) — the anchor is not the problem; the stabilizer set is.

## Outcome

**No submittable candidate found.** This session ran 5 rounds (55 simulations)
of genuinely different stabilizer-escape attempts and produced a clean,
comprehensive negative result — but with one valuable diagnostic insight
that should inform all future sessions on this family.

## Discovery Path (5 rounds + 1 diagnostic pair, 55 simulations)

1. **Round 1 (18 sims)**: replaced the blocked `ivaco + drlt + analyst4_flag
   + buzz*(-ret)` stabilizer set with genuinely fresh alternatives (`volume /
   adv20`, `sales_estimate_count_quarterly`, `historical_volatility_90`,
   `pv13_ustomergraphrank_hub_rank`, `fnd6_fopo`/`fnd6_fopox`, plain buzz
   LEVEL, product-interaction forms) on both `fnd6_pstkrv` and
   `fnd6_newqv1300_mibnq` anchors, plus drlt-only controls. **Comprehensive
   wipeout: all 18 INFERIOR** (best F=0.92, vs. the blocked skeleton's
   F=2.07) — confirms `ivaco`/`buzz*(-ret)` are genuinely load-bearing for
   fitness in this family; no simple substitute reaches even AVERAGE grade.
2. **Round 2 (14 sims)**: pivoted to two genuinely fresh negation-asymmetry
   fields (`fn_goodwill_acquired_during_period_a`,
   `fn_comp_options_grants_fair_value_a`, both GOOD-grade standalone via the
   raw `-ts_zscore(F, 63)` template) blended with fresh/orthogonal partners
   (`volume/adv20`, `sales_estimate_count`, `ivaco`, buzz-reversal,
   `anl4_epsr_flag`, each other). **Comprehensive wipeout: all 11 completed
   INFERIOR** — any `rank()`-wrapping of the sparse `ts_zscore` anchor
   collapses its standalone signal, extending the `fundamental2_sparse_ts_zscore`
   dead zone to these two new fields. 2 exploratory `CONCENTRATED_WEIGHT`-fix
   attempts on `fnd6_txbcof`/`fnd6_fyrc` via `trade_when` volatility-gating
   both hit the SAME unit-mismatch error seen in session `20260715-002`
   (`ts_std_dev(returns,20) > 0.02` — second occurrence this session,
   despite two documented patterns showing this exact structure working
   previously; likely today's platform instability, not a permanent
   regression).
3. **Round 3 (6 sims)**: pivoted to a genuinely different-FAMILY stabilizer —
   the options dataset (IV90 call-put spread) — paired with the
   `fnd6_pstkrv`/`fnd6_newqv1300_mibnq` event-magnitude anchors. **Hit:**
   `np2GnbLd` (`pstkrv` + `zscore(ts_mean(IV_call_90 - IV_put_90, 22))`)
   reached **EXCELLENT (S=2.03, F=2.45, T=7.7%)** — but FAILED
   `LOW_SUB_UNIVERSE_SHARPE` (0.75 vs 0.88 limit).
4. **Round 4 (9 sims)**: fixed the sub-universe failure via breadth legs
   (`volume/adv20`, `sales_estimate_count`) and MARKET neutralization, plus a
   decay sweep. **`d50Jdpg2`** (`mibnq` + IV90 spread, MARKET, decay 6)
   reached **SPECTACULAR (S=2.15, F=3.06, T=6.3%)**, all 7 computable checks
   PASS. Two GOOD-grade `pstkrv` variants also passed all checks. **However,
   self-corr checks on all three showed 0.725-0.824 (estimated BLOCKED)** —
   even this genuinely different options-family stabilizer correlates too
   much with the book's existing IV/options alphas (`npWYoqQz`, `omY3pZq2`,
   `vRm07LP3`, `Gro21wWG`).
5. **Diagnostic pair (2 sims)**: tested the `fnd6_pstkrv` and
   `fnd6_newqv1300_mibnq` event-magnitude anchors COMPLETELY ALONE (no
   secondary leg at all). **Key finding: `xAk7RElJ` (pure `pstkrv` anchor) is
   self-corr SAFE at 0.496** — weak (S=0.43, INFERIOR) but genuinely
   decorrelated. This isolates the correlation driver to the SECONDARY LEG,
   not the anchor.
6. **Round 5 (4 sims)**: tested whether blending the two independently-weak-
   but-safe anchors together (`pstkrv` + `mibnq` event-magnitude, no other
   legs) could reach a submittable fitness while staying low-corr. **All 4
   INFERIOR** (best F=0.45) — two weak signals summed are still too weak;
   this approach does not provide enough fitness lift.

## Key Findings

1. **The book (47 ACTIVE alphas) is now dense enough that essentially ANY
   secondary leg strong enough to lift a weak anchor to GOOD+ fitness
   inherits meaningful correlation with whichever family it belongs to.**
   Across 14+ distinct secondary-leg choices tested this session — spanning
   fundamental6 stabilizers, analyst4 flags, sentiment/buzz, guidance
   fields, and now options/IV spreads — every single one that produced
   GOOD+ fitness also produced local self-corr in the 0.69-0.85 range. This
   is a much stronger and more general version of the `ivaco`/`buzz`-
   specific finding from session `20260715-002`.
2. **A weak-but-genuinely-decorrelated anchor (self-corr 0.496) cannot be
   rescued into a submittable candidate by ANY secondary-leg combination
   tried so far** — every fitness-boosting attempt failed either on fitness
   (fresh/orthogonal legs, F<1.0) or on self-corr (potent/proven legs,
   corr>0.70). This suggests the "anchor + generic stabilizer" template
   family is genuinely exhausted for `fnd6_pstkrv`/`fnd6_newqv1300_mibnq`
   specifically, and possibly for the event-magnitude family as a whole
   going forward.
3. **A completely new escape route is needed, not another field/leg swap
   within the same additive-rank-blend architecture.** Candidates for a
   future session: (a) a genuinely different OPERATOR-TREE STRUCTURE (not
   `ts_decay_linear(rank(A)+rank(B)+...)`), (b) deliberate negation-direction
   exploration per `direction-diversification.md` (516 singleton fields, 34
   independent PCA dimensions — largely untapped), or (c) accepting GOOD-
   grade submissions as point-grinders while this specific EXCELLENT+ vein
   is temporarily exhausted.
4. Reconfirmed (2nd occurrence, different session) that
   `trade_when(ts_std_dev(returns, 20) > 0.02, ..., ts_std_dev(returns, 20) <
   0.01)` fails with a `TSPrice` unit-mismatch error today, despite two
   documented patterns (`iv90-vol-gated-spread.md`,
   `volatility-gate-fixes-sub-universe.md`) showing this exact condition
   structure working previously. Flagged as likely platform-side instability
   on 2026-07-15/16 (consistent with the BRAIN API degradation observed
   throughout today's sessions), not a confirmed permanent regression — but
   worth a quick sanity check in the next session before relying on this
   pattern again.

## Next Steps

- **Do not continue mutating `fnd6_pstkrv`/`fnd6_newqv1300_mibnq` +
  generic-stabilizer combinations** — this specific avenue is now
  thoroughly exhausted (73 total simulations across sessions 002+003 with
  zero SAFE EXCELLENT+ results).
- A future session should try a **structurally different operator-tree
  shape** entirely (not another additive rank-blend), or commit a full
  session to **negation-direction exploration** per
  `direction-diversification.md`, which remains the highest-value
  documented-but-untapped opportunity in the knowledge base.
- Verify whether the `trade_when(ts_std_dev(returns,20)>0.02,...)` unit
  error is transient (today's platform issue) or a permanent regression by
  re-testing a known-working example from `iv90-vol-gated-spread.md` in a
  future session when the platform seems healthy.
