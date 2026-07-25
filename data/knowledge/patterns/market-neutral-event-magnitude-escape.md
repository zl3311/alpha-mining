---
pattern: "market-neutral-event-magnitude-escape"
discovered: "20260713-001"
applicable_to: "event-magnitude-abs-ts-delta family once the leverage+ivaco+buzz stabilizer skeleton is saturated (3+ ACTIVE siblings)"
confidence: "high (1 candidate, O0Z6NE0b, subsequently accepted by BRAIN and ACTIVE)"
best_alpha_id: "O0Z6NE0b"
best_sharpe: 2.10
best_fitness: 2.02
best_self_corr_local: 0.528
---

# Pattern: Drop Leverage, Then Switch to MARKET Neutralization to Escape the Event-Magnitude Family's Saturated Skeleton

## The problem

Per `data/knowledge/rules/event-magnitude-leverage-ivaco-skeleton-saturated.md`,
the event-magnitude family's standard `leverage(-1*equity/assets) + ivaco + buzz`
stabilizer skeleton is shared verbatim by 6+ ACTIVE book entries. New anchor
fields reliably reproduce SPECTACULAR/EXCELLENT aggregate metrics on this
skeleton but correlate 0.65-0.92 against the family under SUBINDUSTRY
neutralization, regardless of anchor freshness.

## The fix (two-step)

1. **Drop `leverage` from the blend**, keeping `ivaco + drlt` (or another
   stabilizer pair) plus a fresh flag (e.g. `anl4_ffo_flag`, unused elsewhere
   in the family) and the buzz stabilizer. This alone reduces correlation
   modestly (0.79-0.88 -> ~0.59-0.65) while preserving most of the fitness,
   because `leverage` was one of 3 shared legs but not the dominant fitness
   driver once `ivaco` is retained.
2. **Switch neutralization from SUBINDUSTRY to MARKET.** Normally MARKET is
   avoided for this family because it kills the leverage-premium component
   (`leverage-premium.md`: MARKET drops leverage-anchored Sharpe by 50%+).
   But once `leverage` has already been removed from the expression (step 1),
   that penalty no longer applies — MARKET now only provides its usual
   decorrelation benefit (`market-neut-decorrelation.md`: -0.10 to -0.20
   correlation) without the leverage-specific fitness cost.

Combined, this took a RISKY 0.646-correlated EXCELLENT candidate
(`KP9V7YLz`, SUBINDUSTRY, S=2.83 F=2.49) to a SAFE 0.528-correlated EXCELLENT
candidate (`O0Z6NE0b`, MARKET, S=2.10 F=2.02) — the fitness cost (F: 2.49 ->
2.02) stayed within the EXCELLENT grade band while the correlation dropped
below the 0.6 comfort zone.

## Concrete discovery

```
ts_decay_linear(rank(abs(ts_delta(fnd6_newqv1300_msaq / close, 3))) + rank(fnd6_ivaco / close) + rank(fnd6_drlt / close) + rank(anl4_ffo_flag) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)
```

MARKET neutralization, platform decay=6, TOP3000. `O0Z6NE0b`: EXCELLENT,
S=2.10, F=2.02, T=12.7%, all 7 computable BRAIN checks PASS, local self-corr
0.528 (SAFE). BRAIN's authoritative `SELF_CORRELATION` check was PENDING at
session end (known platform latency, see session 20260711-001 precedent); the
alpha was submitted on 2026-07-14 and is now ACTIVE, so the check resolved in
its favour.

## When to use

- Any event-magnitude-family candidate whose SUBINDUSTRY correlation lands in
  the 0.6-0.7 RISKY band due to the shared `leverage+ivaco+buzz` skeleton.
- Only after confirming `leverage` has been dropped from the expression first
  — applying MARKET while `leverage` is still present will cost far more
  fitness than the decorrelation is worth (per `leverage-premium.md`).

## Caveats

- Local PnL correlation is a pre-filter; this family's historical multiplier
  vs BRAIN's authoritative check has ranged 1.0x-1.12x (not the extreme
  1.6x seen for IV270-anchored candidates), so 0.528 local plausibly maps to
  ~0.53-0.59 on BRAIN — still comfortably SAFE, but re-verify with `/check`
  before treating as submission-final.
- Fitness ceiling for this leverage-free, MARKET-neutralized sub-family
  appears to be ~2.0-2.1 (F=2.02 best found); do not expect SPECTACULAR grade
  from this specific escape route.
