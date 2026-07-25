---
id: "20260715-002"
date: "2026-07-15"
strategy: "EXPLORE"
research_question: "Do genuinely novel operator-tree shapes (IV call-put spread MOMENTUM at non-270 tenors, guidance x IV-momentum cross-family blend, guidance x analyst-flag product interaction, MARKET-neutral regime-divergence, volatility-gated event-magnitude) combined with fresh untested anchor fields (fn_derivative_notional_amount_q, fnd6_pstkrv, fn_op_lease_min_pay_due_after_5y_a, fnd6_newqv1300_mibnq) produce a decorrelated EXCELLENT+ alpha, per novelty-required.md? Also: does dropping BOTH the leverage leg AND the buzz*(-returns) reversal driver (the #1 correlation driver per flag-ret-correlation.md) from the saturated event-magnitude skeleton, replacing with sales_estimate_count_quarterly as a correlation-neutral densifier, unlock a lower self-corr floor than the already-known leverage-free MARKET escape (O0Z6NE0b, draft PR #88)?"
budget_used: 46
budget_cap: null
trigger: "manual (user-initiated, no budget constraint, find minimal submittable EXCELLENT+; do not submit, present + draft PR)"
gate_passers: 13
submissions: 0
submittable_candidates: 0
status: "superseded_post_session"
correction: "This session recorded N1rlJ7mq as BLOCKED at self-corr 0.796. That reading belonged to oml0kV52 and was misattributed (both were checked together on the platform UI with no per-alpha API response). Session 20260719-001 re-checked them individually via /alphas/{id}/check: N1rlJ7mq is 0.6903 PASS (now ACTIVE), oml0kV52 is 0.796 FAIL. The candidate records below are corrected; the prose narrative is left as written at session time. See data/knowledge/rules/pstkrv-family-multiplier-exception.md."
tags:
  - "session_20260715-002"
  - "EXPLORE"
  - "novel_structure"
  - "market_neutral_escape"
candidates:
  - id: "N1rlJ7mq"
    grade: "EXCELLENT"
    sharpe: 2.32
    fitness: 2.07
    self_corr_value: 0.6903
    self_corr_result: "PASS (authoritative BRAIN /alphas/N1rlJ7mq/check, resolved in session 20260719-001: 0.6903 < 0.70). The 0.796 FAIL originally recorded here was oml0kV52's value, misattributed."
    verdict: "SUBMITTED (submitted in session 20260719-001; this session's BLOCKED verdict was based on a misattributed reading)"
  - id: "oml0kV52"
    grade: "SPECTACULAR"
    sharpe: 2.55
    fitness: 2.55
    self_corr_value: 0.796
    self_corr_result: "FAIL (CONFIRMED by human on BRAIN platform post-session: 0.796 > 0.70 cutoff, Sharpe premium not met)"
    verdict: "BLOCKED — confirmed"
  - id: "kq06YLrd"
    grade: "EXCELLENT"
    sharpe: 1.99
    fitness: 2.06
    self_corr_value: 0.813
    self_corr_result: "estimated BLOCKED (local, not individually confirmed but expected to fail for the same reason as the other two)"
    verdict: "DEPRIORITIZED"
  - id: "np25eXrE"
    grade: "GOOD"
    sharpe: 2.19
    fitness: 2.00
    self_corr_value: null
    self_corr_result: "not checked (borderline EXCELLENT/GOOD boundary, deprioritized)"
    verdict: "NOT PURSUED"
best_alpha: null
best_grade: null
best_sharpe: null
best_fitness: null
best_self_corr: null
best_self_corr_peer: null
best_self_corr_method: "CORRECTED: this session originally concluded all EXCELLENT+ candidates were BLOCKED. In fact N1rlJ7mq is authoritatively 0.6903 PASS (BRAIN /check, session 20260719-001) and was submitted; only oml0kV52 (0.796) and kq06YLrd (0.813 est.) are blocked. The local estimate for N1rlJ7mq (0.691) matched the authoritative value almost exactly, so this family's ~1.0x local-to-authoritative multiplier held rather than breaking. See data/knowledge/rules/pstkrv-family-multiplier-exception.md."
---

# Session 20260715-002: EXPLORE — IV-Momentum, Guidance x Analyst Interactions, Leverage/Buzz-Free MARKET Escape

> **Correction (added 20260719-001).** Everything below is preserved as written
> at session time, but its central post-session conclusion was wrong.
> `N1rlJ7mq` was **not** blocked: its authoritative self-correlation is
> **0.6903 PASS**, and it is now ACTIVE. The 0.796 recorded throughout this
> document was `oml0kV52`'s value — both alphas were read from the same
> platform message, and the value was attributed to both. `oml0kV52` (0.796)
> and `kq06YLrd` (0.813 est.) remain correctly blocked. Read the narrative
> below as a record of what the session believed, not as current fact; see
> `data/knowledge/rules/pstkrv-family-multiplier-exception.md`.

## Context Assessment (Phase 0)

- Book: 46 ACTIVE + 10 PENDING across 53 mechanism families.
  This is a SECOND session today; session `20260715-001` (merged as PR #90) already
  submitted `lelNqEZl` (fair-value-ASSET event-magnitude, self-corr 0.567 PASS)
  earlier today via the standard `leverage + ivaco + drlt + buzz` skeleton.
- Three OPEN unmerged draft PRs from prior days carry unreviewed candidates that
  inform this session's priors (not this session's output, but relevant context):
  - PR #87 (`session-20260712-001`): `VkPdaQ2b` SPECTACULAR S=2.18 F=2.65,
    self-corr 0.697 PASS (auto, `cptmfmq` debt-capital-markets + IV + gric family).
  - PR #88 (`exp/20260713-001`): `O0Z6NE0b` EXCELLENT S=2.10 F=2.02, self-corr
    0.528 local/PENDING-BRAIN (MARKET-neutral, leverage-dropped escape from the
    saturated event-magnitude skeleton, anchor `fnd6_newqv1300_msaq`). Also
    confirms `KP9V7YLz` EXCELLENT via Sharpe-premium escape (corr 0.8015).
  - PR #89 (`mining/20260714-001`): re-validates `KP9V7YLz` only, no new work.
- Confirmed via direct HF DB query that the standard `leverage(-1*equity/assets)
  + ivaco + drlt + buzz*(-ret)` additive skeleton is now saturated regardless of
  anchor freshness: `fnd6_dpvieb` (EXCELLENT S=1.98 F=2.12 aggregate) self-corr
  **0.8198 FAIL**; the multi-horizon-spread variant on `fnd6_dcvsub`
  (`VkPR1LYJ`, GOOD S=2.62 F=1.93) self-corr **0.848 FAIL**. Both already
  BLOCKED in session 001's own results, confirming the skeleton itself (not
  anchor choice) is the correlation driver now.
- No qualifying HYPOTHESIS opportunity (all non-submit-candidate entries in
  `data/knowledge/opportunities/` are closed/exhausted or static reference
  data). HF server healthy (53235 results, 0 pending, budget 5000, idle). No
  genuinely-new-family 24h gate-passer to trigger EXPLOIT. Per the mining-session
  decision tree, falls through to the EXPLORE default.
- Strategy: EXPLORE, prioritizing genuinely novel operator-tree shapes
  (>=50% of budget per `novelty-required.md`) over further exploitation of the
  now-saturated event-magnitude skeleton. Where the skeleton is reused as
  backstop, drop the `leverage` leg (proven MARKET-neutral escape from PR #88)
  AND test dropping the `buzz*(-ret)` reversal driver too (the #1 correlation
  driver per `flag-ret-correlation.md`), replacing it with a correlation-neutral
  densifier (`sales_estimate_count_quarterly`) — an escape lever not yet tried.

## Fresh Anchor Fields Selected (zero coverage in data/book, data/factors)

- `fn_derivative_notional_amount_q` (fundamental2, redundancy cluster #34, size 4)
- `fnd6_pstkrv` (fundamental6, preferred-stock redemption value, cluster #81, size 2)
- `fn_op_lease_min_pay_due_after_5y_a` (fundamental2, operating-lease long-tail, cluster #46, size 6)
- `fnd6_newqv1300_mibnq` (fundamental6, minority interest, cluster #100, size 2)

## Novel Structures Targeted

1. IV call-put spread MOMENTUM (`ts_delta` of the spread, not the level) at
   non-270 tenors (60, 180) — avoids the confirmed `iv270-spread-family` dead
   zone; the pattern's own "still viable" section flags IV rank/momentum as
   unknown territory.
2. Guidance x IV-90-momentum additive blend — untested cross-family combo
   from `theme-blend-candidates.md` (option8/analyst4, div+0.53).
3. Guidance x analyst-flag product interaction (`rank(min_net_debt_guidance) *
   rank(anl4_cfi_flag)`) — untested combo from the signal-generation cross-family grid.
4. Options x reversal interaction (`rank(IV_spread) * rank(-1*returns)`) at a
   non-270 tenor — untested combo from the same grid.
5. Volatility-gated event-magnitude on a fresh anchor (novel combination of
   the proven `volatility-gate-fixes-sub-universe` pattern with the
   event-magnitude template, not yet tried together).
6. Regime-divergence (`zscore(F,10)-zscore(F,60)`) and multi-horizon spread
   (`ts_delta(F,5)-ts_delta(F,22)`) on a fresh anchor, MARKET neutralization,
   no leverage/drlt — retesting these structures (AVERAGE/BLOCKED on their
   only prior trials) under the leverage-free MARKET escape.
7. Guidance-field event-magnitude anchor (`abs(ts_delta(guidance_field/close,3))`)
   — the event-magnitude transform has never been applied to a `company_guidance`
   dataset field before (only fundamental6/fundamental2 anchors so far).

## Outcome

**UPDATE 2026-07-16 (post-session, human-confirmed on BRAIN platform): both
EXCELLENT+ candidates from this session are BLOCKED.** The human checked
directly on the platform (the API's own `/check` endpoint never resolved
during the session — see original note below) and obtained the authoritative
result for both `N1rlJ7mq` and `oml0kV52`: **"Self-correlation 0.796 is above
cutoff of 0.7 and Sharpe not better by 10.0% or more."** Neither is
submittable. This session produced **zero submittable EXCELLENT+
candidates** — a genuine dead end, not just an unconfirmed risk.

The most important lesson from this outcome: `N1rlJ7mq`'s local PnL
correlation estimate (0.691) UNDERESTIMATED the confirmed authoritative
value (0.796) by ~0.10 — breaking the ~1.0x local-to-authoritative
multiplier this exact template family had shown in 4 prior confirmed cases
(`lelNqEZl`, `WjGVJ7bN`, `YP0bLdzA`, `wpl5eP5v`). See the new rule
`data/knowledge/rules/pstkrv-family-multiplier-exception.md`. Both `data/book/N1rlJ7mq.md`
and `data/knowledge/opportunities/submit-n1rlj7mq.md` have been updated to
`REJECTED`/`BLOCKED` accordingly.

---

**Original (pre-confirmation) note, retained for context:**

Found [N1rlJ7mq](https://platform.worldquantbrain.com/alpha/N1rlJ7mq) —
EXCELLENT, S=2.32, F=2.07, T=11.1%, all 7 computable BRAIN checks PASS. Local
PnL self-corr estimate vs the 47-alpha ACTIVE book was **0.691** (top peer
`1YJagrVk`, `conglomerate_revision` family, shared leg `fnd6_ivaco`) — just
0.009 under the 0.70 auto-pass threshold, which looked favorable at the time.
BRAIN's authoritative `/alphas/N1rlJ7mq/check` SELF_CORRELATION sub-check did
not resolve during the session itself — it returned `PENDING` on every one
of 8+ polls spread across over 75 minutes, alongside repeated `HTTP
502`/`HTTP 429` errors on other, unrelated BRAIN API calls, consistent with
platform-side degradation on 2026-07-15/16 rather than the normal
~9-minute async lag. The candidate was presented to the user as `RISKY, not
SAFE` pending confirmation — which is now resolved (see update above).

## Discovery Path (7 rounds, 46 simulations)

1. **Round 1 (20 sims, ~65% novel structure per novelty-required.md)**:
   tested IV call-put-spread MOMENTUM at non-270 tenors (60d, 180d — both
   dead: pure momentum form produces near-zero/negative Sharpe), guidance x
   IV-90-momentum additive blend (AVERAGE, high turnover), guidance x
   analyst-flag product/additive interaction (AVERAGE, very low turnover
   ~2.9%), sentiment x options and options x reversal interactions (both
   dead/weak), a guidance-field event-magnitude anchor (weak — guidance
   fields don't respond to the abs-delta transform the way fundamentals do),
   and the leverage-free MARKET-neutral event-magnitude escape (proven in
   unmerged draft PR #88's `O0Z6NE0b`) applied to four fresh anchors
   (`fn_derivative_notional_amount_q`, `fnd6_pstkrv`,
   `fn_op_lease_min_pay_due_after_5y_a`, `fnd6_newqv1300_mibnq`). Best:
   `fnd6_pstkrv` MARKET backstop reached GOOD (S=1.60, F=1.65) — the
   strongest anchor of the four. 2 jobs hit known operator errors (`zscore`
   is cross-sectional single-input, not `ts_zscore`; a `trade_when` unit
   mismatch on `ts_std_dev(returns,20)` under this specific leg combination)
   and were dropped without retry. Confirmed via direct HF-DB query that the
   standard `leverage + ivaco + drlt + buzz` skeleton is now saturated
   regardless of anchor freshness — two of session `20260715-001`'s own
   unreported gate-passers (`fnd6_dpvieb` aggregate-EXCELLENT, `fnd6_dcvsub`
   multi-horizon-spread aggregate-GOOD) were confirmed self-corr FAIL at
   0.82/0.85 once queried directly.
2. **Round 2 (17 sims)**: mutated the `fnd6_pstkrv`/`fnd6_newqv1300_mibnq`
   MARKET backstops (analyst-flag swaps, leverage add-back, buzz-window and
   decay sweeps) and pushed the guidance x analyst-flag blend with a 3rd
   leg. **`N1rlJ7mq`** — the SUBINDUSTRY control variant of the round-1
   `fnd6_pstkrv` backstop (same 5 legs, neutralization switched from MARKET
   back to SUBINDUSTRY) — reached **EXCELLENT (S=2.32, F=2.07, T=11.1%)**,
   directly confirming the `market-neut-tradeoff` rule's Sharpe cost on this
   exact leg set (MARKET: F=1.65 -> SUBINDUSTRY: F=2.07).
   `fnd6_newqv1300_mibnq`'s SUBINDUSTRY analog reached GOOD (F=2.00,
   borderline).
3. **Rounds 3-4 (14 sims)**: attempted to lower `N1rlJ7mq`'s self-corr by
   dropping individual legs from the 5-factor skeleton (buzz, ivaco, or drlt
   alone) — all degraded to AVERAGE/GOOD (best F=1.47), confirming every leg
   is load-bearing for fitness (consistent with PR #88's own finding that
   `ivaco` is "load-bearing, not decorative"). In parallel, pushed the
   guidance x `anl4_cfi_flag` structure toward EXCELLENT by adding
   `ivaco`+`drlt` — succeeded (`oml0kV52` SPECTACULAR S=2.55 F=2.55) — but
   once self-corr was checked, both `oml0kV52` (0.796) and a `fatl`-based
   variant `kq06YLrd` (EXCELLENT S=1.99 F=2.06, corr 0.813) showed markedly
   WORSE local self-corr than `N1rlJ7mq`, despite `oml0kV52`'s superior
   fitness — deprioritized per the submission-priority-long-term rule
   (lowest self-corr first).
4. **Rounds 5-7 (12 sims)**: tested whether the analyst4-flag leg could be
   dropped entirely or replaced with a non-flag stabilizer (`fnd6_fatl`,
   plain buzz LEVEL instead of buzz-reversal, `sales_estimate_count_quarterly`)
   to escape the 127-member analyst4-flag redundancy super-cluster
   (`factor-themes-redundancy.md` cluster #13, which `anl4_fcf_flag` and
   `anl4_cfi_flag` both belong to alongside several already-ACTIVE flags).
   All flag-free variants capped at GOOD/AVERAGE (best F=1.99, local corr
   still 0.803) — removing the flag did not measurably improve correlation
   while it did cost fitness, so `N1rlJ7mq` (lowest local self-corr among
   all EXCELLENT+ results this session) was retained as the primary
   candidate and the session concluded per the satisficing directive.

## Key Findings

1. **The `leverage + ivaco + drlt + buzz*(-ret)` event-magnitude skeleton is
   now saturated on essentially ANY anchor field** — confirmed on `dpvieb`
   (0.82 FAIL), `dcvsub` (0.85 FAIL) from the prior session's own unexamined
   results, and directly reproduced here. Field freshness alone no longer
   guarantees decorrelation once the skeleton is reused verbatim.
2. **`buzz*(-1*returns)` (the "buzz-reversal stabilizer") appears to be a
   correlation driver in its own right, not just `ivaco`/`drlt`** — local
   self-corr stayed in the 0.80-0.81 range even for candidates built entirely
   from fresh legs (`min_net_debt_guidance`, `anl4_cfi_flag`, `fnd6_fatl`)
   whenever buzz-reversal was included, and a buzz-free 4-leg variant
   (`np25lW8a`, GOOD F=1.99) still showed 0.803 local corr — suggesting the
   analyst4-flag mega-cluster (see finding 3) is the dominant remaining
   driver, with buzz-reversal a secondary contributor. Recorded as an update
   to the `flag-ret-correlation` rule's scope (worth a dedicated
   investigation in a future session).
3. **The analyst4 flag redundancy cluster (#13, 127 members, mean |rho|
   0.82) is effectively a single mega-cluster spanning nearly the entire
   `anl4_*_flag` universe** — `anl4_fcf_flag`, `anl4_cfi_flag`,
   `anl4_capex_flag`, and `anl4_totassets_flag` are ALL members alongside
   several already-ACTIVE flags (`anl4_bvps_flag`, `anl4_ptpr_flag`,
   `anl4_netdebt_flag`, `anl4_cff_flag`). Any new analyst4-flag choice likely
   inherits correlation with the existing analyst-revision-heavy book
   regardless of which specific flag is picked.
4. **The MARKET-neutral leverage-drop escape (PR #88's technique) reliably
   trades ~0.4 fitness for decorrelation on this family** (`fnd6_pstkrv`:
   MARKET F=1.65 vs SUBINDUSTRY F=2.07 on the identical 5-leg set) — useful
   when GOOD grade is the target, but insufficient alone to reach EXCELLENT
   without the SUBINDUSTRY fitness premium, which reintroduces correlation
   risk.
5. **IV call-put spread MOMENTUM (delta of the spread, not the level) is a
   dead end** at both 60d and 180d tenors (S=0.30 and S=-0.24 respectively,
   pure form) — closes the "unknown territory" flagged in
   `iv270-spread-family.md`'s "still viable" section. New dead zone
   recorded.
6. **Guidance-dataset fields do not respond to the event-magnitude
   (`abs(ts_delta(F/close,3))`) transform** the way fundamental6/fundamental2
   fields do (S=0.72, F=0.62 on `max_adjusted_net_income_guidance`) — the
   transform's edge appears specific to balance-sheet/cash-flow items with
   genuine "shock" dynamics, not analyst forecast levels which already
   update discretely.

## Next Steps

- **This session's stated goal (minimal submittable EXCELLENT+ candidate) was
  NOT achieved** — both EXCELLENT+ candidates are confirmed/expected BLOCKED.
  A follow-up session is needed to find a genuinely submittable candidate.
- `kq06YLrd` (EXCELLENT, `fatl`-based, local est. 0.813) was not individually
  confirmed but shares the same blocking stabilizer combination as the other
  two — treat as BLOCKED by inference, not worth a dedicated re-check.
- The `buzz-reversal-is-a-correlation-driver` finding and the
  `analyst4-flag-mega-cluster` finding both hold up and are now REINFORCED
  by the confirmed results: two different anchors (`fnd6_pstkrv`,
  `min_net_debt_guidance`) sharing the `ivaco + drlt/fatl + analyst4_flag +
  buzz*(-ret)` stabilizer combination BOTH landed at the identical 0.796
  self-corr — strong evidence the stabilizer combination itself, not the
  anchor, is now the hard correlation ceiling for this family. A future
  session should prioritize finding an EXCELLENT-fitness leg combination
  that avoids ALL of {`ivaco`, `drlt`, `fatl`, any `anl4_*_flag`,
  `buzz*(-ret)`} simultaneously — this session's flag-free/buzz-free
  variants (rounds 5-7) only reached GOOD (F<=1.99), so this remains an
  open, unsolved problem.
- **New critical lesson**: do not trust a local PnL self-corr estimate in
  the 0.60-0.70 range as "probably SAFE" for this family — treat anything
  above 0.60 as inconclusive pending authoritative confirmation (see
  `pstkrv-family-multiplier-exception.md`).
- `fnd6_pstkrv` (preferred-stock redemption value) remains a validated fresh
  anchor field, but the specific stabilizer combination tested here is now a
  confirmed dead end on it — a future session should pair it with a
  genuinely different stabilizer set.
