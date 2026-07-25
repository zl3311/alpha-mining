---
id: "20260715-003-learnings"
session: "20260715-003"
category: "dead_end"
confidence: "high"
actionable: true
---

# Learnings: Session 20260715-003

## What Worked (fitness-wise, but ultimately blocked)

- The options-family IV90 call-put spread (`zscore(ts_mean(implied_volatility_call_90 - implied_volatility_put_90, 22))`) is a genuinely strong stabilizer when paired with the `fnd6_pstkrv`/`fnd6_newqv1300_mibnq` event-magnitude anchors, reaching SPECTACULAR (F=3.06) — the highest fitness found in either of today's two sessions on this anchor family. Both self-correlation estimates were BLOCKED (0.725-0.824), but this is a genuinely novel cross-family combination (event-magnitude x options, never tried before) worth remembering if the options family itself ever needs a fresh fundamental partner.
- Isolating the pure anchor (no secondary leg) confirmed it is genuinely decorrelated (self-corr 0.496) — useful diagnostic technique for future sessions stuck at a correlation wall: test the anchor ALONE to determine whether the anchor or the stabilizer is the correlation driver.

## What Didn't Work

- Every "fresh" non-family stabilizer substitute for the blocked `ivaco + drlt + analyst4_flag + buzz*(-ret)` skeleton collapsed fitness to INFERIOR (18/18 in round 1) — confirms these legs are not decoratively swappable.
- `rank()`-wrapping a sparse `-ts_zscore(F, 63)` field destroys its standalone signal in every blend tested (11/11 in round 2) — this specific field's spectacular aggregate metrics are a pure rank-dilution artifact, consistent with (and now extending) the `fundamental2_sparse_ts_zscore` dead zone.
- Blending two independently-weak-but-decorrelated anchors together does not provide enough fitness lift on its own (4/4 INFERIOR in round 5).
- `trade_when(ts_std_dev(returns, 20) > 0.02, ..., ts_std_dev(returns, 20) < 0.01)` failed with a `TSPrice` unit-mismatch error for the second time today (different signal payload both times), despite two documented working examples in the knowledge base. Treated as likely platform instability today rather than a confirmed regression, but flagged for a sanity re-check in a healthier future session.

## New Rules Discovered

- (Reinforces, generalizes) the session `20260715-002` finding that the specific `ivaco/drlt/buzz/analyst4-flag` skeleton is blocked — this session shows the block generalizes to essentially ANY sufficiently-strong secondary leg (including a completely different dataset family, options/IV spreads), not just that one specific skeleton. The 47-alpha book appears dense enough now that most "family-representative" secondary legs inherit correlation with their family's existing book presence.

## New Dead Zones

- `family-pstkrv-mibnq-generic-stabilizer-exhausted.md`: 101 combined simulations (this session + `20260715-002`) on `fnd6_pstkrv`/`fnd6_newqv1300_mibnq` event-magnitude anchors, across 6+ distinct secondary-leg families, produced zero SAFE EXCELLENT+ candidates. Do not continue mutating this anchor pair with additive-rank-blend stabilizer swaps.

## Mechanism Insights

- The most important insight from this session: **decorrelation and fitness now appear to be in direct, structural tension for this template architecture** (`ts_decay_linear(rank(anchor) + rank(stabilizer...), d)`, additive rank blend). A weak-but-decorrelated anchor cannot be rescued into EXCELLENT-grade territory by adding a stabilizer without importing that stabilizer's family correlation. This suggests the book has crossed a density threshold where marginal EXCELLENT+ decorrelated alphas require either (a) a structurally different operator-tree shape (not this additive architecture), or (b) genuinely untapped dimensions like the negation direction (per `direction-diversification.md`), rather than further within-architecture field/leg substitution.
