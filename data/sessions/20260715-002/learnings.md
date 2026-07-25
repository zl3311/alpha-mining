---
id: "20260715-002-learnings"
session: "20260715-002"
category: "discovery"
confidence: "medium"
actionable: true
---

# Learnings: Session 20260715-002

> **Correction (added 20260719-001).** The learnings below are preserved as
> written, but the ones about `N1rlJ7mq` being blocked at 0.796 are void. Its
> authoritative self-correlation is **0.6903 PASS** and it is now ACTIVE; the
> 0.796 was `oml0kV52`'s value, misattributed from a shared platform reading.
> The claim that this family's ~1.0x local-to-authoritative multiplier broke is
> also void — the local estimate (0.691) matched. See
> `data/knowledge/rules/pstkrv-family-multiplier-exception.md`.

## What Worked (fitness-wise; ultimately blocked on self-corr — see below)

- `fnd6_pstkrv` (preferred-stock redemption value) is a genuinely fresh
  event-magnitude anchor (redundancy cluster #81, only 2 members) that
  reaches EXCELLENT fitness (S=2.32, F=2.07) on the standard
  `event-magnitude + ivaco + drlt + flag + buzz` template. **UPDATE:**
  human-confirmed on the BRAIN platform post-session that this specific
  combination (`N1rlJ7mq`) is self-corr BLOCKED at 0.796 — the fresh anchor
  was NOT sufficient to decorrelate from the shared stabilizer legs.
- The MARKET-neutral, leverage-drop escape from unmerged draft PR #88
  reproduces reliably on a new anchor (`fnd6_pstkrv`: MARKET F=1.65) — a
  useful GOOD-grade fallback when EXCELLENT-grade self-corr risk is
  unacceptable. (Not itself confirmed BLOCKED — only the higher-fitness
  SUBINDUSTRY variant was checked.)
- `min_net_debt_guidance + anl4_cfi_flag` (guidance x analyst-flag additive)
  is a genuinely novel, untested cross-family combo with very low turnover
  (2.5-4.3%) — capped at AVERAGE alone but reaches SPECTACULAR (S=2.55,
  F=2.55) once `ivaco + drlt + buzz` are added. **UPDATE:** also
  human-confirmed BLOCKED at self-corr 0.796, the identical value and
  failure reason as `N1rlJ7mq` — strong evidence the `ivaco + drlt +
  analyst4_flag + buzz*(-ret)` stabilizer combination itself is now a hard
  correlation ceiling, independent of the anchor/primary legs.

## What Didn't Work

- IV call-put spread MOMENTUM (`ts_delta` of the spread, any tenor) — dead
  end, new dead zone recorded (`template-iv-spread-momentum.md`).
- Sentiment x options product interaction (`buzz * IV_spread`) — dead.
- Event-magnitude transform on a `company_guidance` dataset field — weak
  (S=0.72), confirming the transform's edge is specific to
  fundamental6/fundamental2 balance-sheet items, not analyst forecast levels.
- Dropping any single leg from the 5-factor `event-magnitude + ivaco + drlt
  + flag + buzz` skeleton (tested on `fnd6_pstkrv`) degrades grade from
  EXCELLENT to AVERAGE/GOOD — every leg is load-bearing for fitness on this
  anchor, consistent with the `ivaco`-is-load-bearing finding from PR #88.
- Replacing the analyst4-flag leg with a non-flag densifier (`fnd6_fatl`,
  plain buzz level, `sales_estimate_count_quarterly`) did not measurably
  reduce self-corr (still 0.80+ local) while costing fitness — the
  correlation driver in this family appears to be `ivaco`/`drlt`/
  `buzz*(-ret)`, not the specific flag choice.

## New Rules Discovered

- `analyst4-flag-mega-cluster.md`: the `anl4_*_flag` universe is effectively
  one large redundancy cluster (127+7 members); a "never-used" flag is not
  evidence of low self-corr risk if it shares a cluster with an ACTIVE flag.
- `pstkrv-family-multiplier-exception.md` (added post-session, after human
  confirmation on the platform): the event-magnitude+ivaco+drlt+buzz
  family's previously-reliable ~1.0x local-to-authoritative self-corr
  multiplier is NOT universal. `N1rlJ7mq` broke it (0.691 local -> 0.796
  confirmed, ~1.15x). Treat any local estimate above 0.60 for this family as
  inconclusive, not favorable, going forward.

## New Dead Zones

- `template-iv-spread-momentum.md`: `ts_delta` of the IV call-put spread
  (any tenor) produces no signal.

## New Patterns

- None promoted to `data/knowledge/patterns/` this session — the
  MARKET-neutral leverage-drop escape and the event-magnitude-dual-stabilizer
  pattern are both already documented from prior sessions (PR #88 and
  session `20260715-001` respectively); this session only reproduced them on
  a new anchor field, which is recorded in `data/factors/fnd6_pstkrv.md`
  rather than as a new pattern.

## Mechanism Insights

- The event-magnitude family's self-corr floor appears to be set primarily
  by the SHARED STABILIZER LEGS (`ivaco`, `drlt`, `buzz*(-ret)`), not by the
  anchor field or the analyst-flag choice. Every combination tested this
  session that included 2+ of these three legs landed in the 0.69-0.85 local
  self-corr range regardless of anchor/flag freshness. This suggests the
  family's remaining EXCELLENT+ headroom (via this specific stabilizer set)
  is nearly exhausted — future sessions targeting this family should
  prioritize finding an entirely different stabilizer combination over
  further anchor-field swaps.
- BRAIN's authoritative self-correlation check exhibited unusually severe
  latency this session (60+ minutes PENDING across 6+ polls, plus
  concurrent HTTP 502/429 errors on unrelated calls) — well beyond the
  documented ~9-minute lag from sessions `20260711-001`/`20260715-001`.
  Treat as likely platform-side degradation on 2026-07-15/16 rather than a
  new steady-state latency; worth checking again in future sessions to see
  if it has returned to normal.
