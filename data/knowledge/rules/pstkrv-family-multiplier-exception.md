---
rule: "RETRACTED -- the claimed 1.15x local-to-authoritative self-corr multiplier for N1rlJ7mq/fnd6_pstkrv never existed; it was a misattributed platform reading. The family's ~1.0x multiplier holds. Surviving lesson: attribute every self-corr reading to a specific alpha ID."
category: "rule"
severity: "high"
status: "retracted"
discovered: "20260715-002 (post-session human confirmation)"
retracted: "20260719-001 (BRAIN /check, per-alpha)"
confidence: "high"
evidence: "BRAIN /alphas/N1rlJ7mq/check returned SELF_CORRELATION {result: PASS, value: 0.6903, limit: 0.7} in session 20260719-001, matching the 0.691 local estimate (~1.0x). The 0.796 previously recorded for N1rlJ7mq is oml0kV52's value, confirmed separately at 0.796 FAIL in the same session."
---

# RETRACTED: There Was No pstkrv Multiplier Exception

## What this file used to claim

That `N1rlJ7mq` (`fnd6_pstkrv` anchor) broke the
`event-magnitude + ivaco + drlt + buzz*(-ret)` family's established ~1.0x
local-to-authoritative self-correlation multiplier, coming in at ~1.15x
(local 0.691 vs an authoritative 0.796), and that the "local SAFE" bar for
this family should therefore be tightened from <0.70 to <0.60.

**All of that was wrong.** Do not apply it.

## What actually happened

Session `20260715-002` produced two EXCELLENT+ candidates that were checked
together on the BRAIN platform UI after the session ended (the API's own
`/check` endpoint never resolved during the session, so there was no per-alpha
API response to attribute the reading to). A single platform message —
*"Self-correlation 0.796 is above cutoff of 0.7 and Sharpe not better by 10.0%
or more"* — was recorded against **both** candidates.

Session `20260719-001` checked them individually through
`/alphas/{id}/check`, which returns the alpha ID alongside the value:

| Alpha | Anchor | Local est. | Authoritative | Multiplier | Verdict |
|-------|--------|-----------|---------------|------------|---------|
| `N1rlJ7mq` | `fnd6_pstkrv` | 0.691 | **0.6903 PASS** | ~1.00x | SUBMITTABLE |
| `oml0kV52` | `min_net_debt_guidance` | 0.796 | **0.796 FAIL** | ~1.00x | BLOCKED |

The 0.796 belonged to `oml0kV52` alone. `N1rlJ7mq` was never blocked, and the
family's ~1.0x multiplier held in both cases — this is now a fifth and sixth
confirming case, not an exception.

Session `20260715-002`'s own write-up flagged the tell: it noted that two
different anchors with different flags landing on the *identical* 0.796 was
"strong evidence" of a shared correlation ceiling. The simpler explanation was
that it was one number read twice.

## Surviving lesson: attribute every self-corr reading to an alpha ID

The cost of this error was four days of misdirected mining. Three knowledge
files were written on the false premise, two of which declared the exact
`pstkrv` + stabilizer combination a dead end — while that expression was in
fact submittable, and is now ACTIVE as `N1rlJ7mq`. Sessions `20260715-003` and
`20260716-001` both opened with research questions built on it.

- Prefer `/alphas/{id}/check`, whose response carries the alpha ID, over a
  platform-UI reading taken while several candidates are open.
- When a UI reading is the only option, check one alpha at a time and record
  the ID with the value.
- Treat two candidates reporting a self-corr identical to 3+ decimal places as
  a suspected duplicate reading, not as evidence of a shared ceiling.
- A local estimate remains a reliable ~1.0x guide for this family. The
  <0.70 local-SAFE bar stands; the <0.60 tightening this file used to
  recommend was never justified.
