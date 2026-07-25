---
alpha_id: "lelNqEZl"
name: "fair_val_assets_event_magnitude_leverage_cff_ivaco_drlt_buzz"
status: "ACTIVE"
submitted: "2026-07-15"
grade: "EXCELLENT"
sharpe: 2.01
fitness: 2.01
turnover: 0.1104
returns: 0.1246
family: "fair_val_assets_event_magnitude_leverage_blend"
mechanism: "Event-magnitude transform on Level-2 fair-value-ASSET changes, blended with leverage premium, financing-cashflow revision flag, investing-activities-other, deferred-revenue stabilizer, and a buzz-reversal stabilizer"
fields:
  - "fn_assets_fair_val_l2_q"
  - "equity"
  - "assets"
  - "anl4_cff_flag"
  - "fnd6_drlt"
  - "fnd6_ivaco"
  - "scl12_buzz"
  - "returns"
expression: "ts_decay_linear(rank(abs(ts_delta(fn_assets_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_cff_flag) + rank(fnd6_drlt / close) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)"
neutralization: "SUBINDUSTRY"
decay: 6
delay: 1
truncation: 0.08
region: "USA"
universe: "TOP3000"
self_corr_max: 0.5666
self_corr_peer: "YP0bLdzA"
self_corr_result: "PASS (AUTHORITATIVE — confirmed via BRAIN /alphas/lelNqEZl/check: SELF_CORRELATION {result: PASS, value: 0.5666, limit: 0.7}; comfortable margin below 0.70, no Sharpe-premium escape needed)"
self_corr_method: "brain_api_check_endpoint (authoritative, ground truth). Returned PENDING for the first ~9 minutes post-simulation (consistent with the known async-lag issue documented in session 20260711-001), then resolved to a real value; confirmed stable and consistent across 3 independent polls ~3.5 min apart. The local PnL pre-submission estimate (0.567) matched the authoritative BRAIN value (0.5666) almost exactly -- no correction multiplier needed for this template family, consistent with prior findings for wpl5eP5v/WjGVJ7bN/YP0bLdzA."
session: "20260715-001"
brain_url: "https://platform.worldquantbrain.com/alpha/lelNqEZl"
tags:
  - "fn_assets_fair_val_l2_q"
  - "anl4_cff_flag"
  - "event_magnitude"
  - "fair_value_asset"
  - "leverage_premium"
  - "buzz_stabilizer"
  - "session_20260715-001"
---

# lelNqEZl — Fair-Value-Asset Event-Magnitude + Leverage + Financing-Cashflow-Revision + Investing-Activities + Deferred-Revenue Blend

## Expression

`ts_decay_linear(rank(abs(ts_delta(fn_assets_fair_val_l2_q / close, 3))) + rank(-1 * equity / assets) + rank(anl4_cff_flag) + rank(fnd6_drlt / close) + rank(fnd6_ivaco / close) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`

## Mechanism

Six-factor blend extending the proven `event-magnitude-abs-ts-delta` template
(previously validated on `fnd6_itci`, `fnd6_newqv1300_ppegtq`, `fnd6_tlcf`,
`fnd6_txw`, `fn_liab_fair_val_l2_q`) to a genuinely fresh anchor field from a
different, much smaller redundancy cluster than every prior anchor:

1. **Fair-value-asset event magnitude** (`rank(abs(ts_delta(fn_assets_fair_val_l2_q / close, 3)))`):
   `fn_assets_fair_val_l2_q` measures Level-2 (model-priced, not quoted-market)
   recurring fair-value **assets** — the balance-sheet counterpart to the
   already-ACTIVE `fn_liab_fair_val_l2_q` (`YP0bLdzA`), but tracking the asset
   side of re-marked derivatives/structured instruments rather than the
   liability side. Large 3-day swings signal a re-marking event (rate/credit-
   spread shock, hedge restructuring, or valuation-model change) that the
   market underreacts to, independent of direction. Per
   `data/knowledge/opportunities/factor-themes-redundancy.md`, this field
   belongs to redundancy cluster #21 (only 2 members, mean |rho| 0.82) —
   economically and statistically much more orthogonal to the book's dominant
   fundamental-value/analyst-revision mega-clusters (#1, #13) than any other
   anchor previously used in this template family.
2. **Leverage premium** (`rank(-1 * equity / assets)`): high-leverage firms earn
   a subindustry risk premium (see pattern `leverage-premium.md`).
3. **Financing-cashflow revision flag** (`rank(anl4_cff_flag)`): analyst4
   forecast-type flag for financing cashflow (revision/new estimate).
   Standalone INFERIOR (S=1.14, blocked_LOW_SHARPE per
   `data/knowledge/factor_profiles/anl4_cff_flag.md`); used here in raw
   `rank()` form purely as an analyst-conviction / sub-universe densifier, the
   same role `anl4_gric_flag` played in `YP0bLdzA`. Never used in any prior
   book entry.
4. **Deferred-revenue stabilizer** (`rank(fnd6_drlt / close)`): proven
   `LOW_SUB_UNIVERSE_SHARPE` fix and the family's most common stabilizer leg.
5. **Investing-activities-other** (`rank(fnd6_ivaco / close)`): conglomerate /
   non-core capital-allocation quality, the family's second most common
   stabilizer leg. Combining BOTH `drlt` and `ivaco` (a 6-factor form not
   previously tried in this family, which had only ever used one or the
   other alongside a single fresh flag) lifted fitness to EXCELLENT while
   the fresh anchor + fresh flag combination kept correlation well clear of
   the 0.70 threshold.
6. **Buzz-reversal stabilizer** (`rank(ts_mean(scl12_buzz, 5) * (-1 * returns))`):
   100%-coverage sentiment-reversal factor; the family's standard fitness
   booster (see `event-magnitude-buzz-boost.md`).

## Discovery Path (session 20260715-001)

- Round 1 (15 sims, ~80% genuinely novel operator-tree shapes per
  `novelty-required.md`): tested `ts_arg_max` recency-of-shock, signal-to-noise
  ratio (`ts_delta/ts_std_dev`), regime-divergence (`zscore` spread — 2 sims
  failed on an operator-arity error, `zscore` is cross-sectional single-input,
  fixed to `ts_zscore` in round 2), sign-preserving convex tilt, fundamental-
  trend-gated `trade_when`, and buzz-level x event-magnitude products — on
  three fresh anchors (`fnd6_mrct`, `fn_assets_fair_val_l2_q`, `fnd6_dpvieb`)
  plus a 20% backstop batch applying the proven event-magnitude template to
  the same fresh anchors with fresh analyst4 flags (`anl4_cfo_flag`,
  `anl4_cff_flag`) as the stabilizer. The `fn_assets_fair_val_l2_q` backstop
  (`N1r20nKL`) reached GOOD (S=1.79, F=1.75) with self-corr **PASS 0.572** —
  the lowest correlation of any candidate this round, and the strongest signal
  that this anchor's small redundancy cluster (#21) genuinely decorrelates it
  from the book, confirming it as the priority target for round 2.
- Round 2 (10 sims): pushed `fn_assets_fair_val_l2_q` toward EXCELLENT via (a)
  buzz-boosting the novel `ts_arg_max` recency structure, (b) adding `ivaco` as
  a 6th leg to the backstop template, (c) window sweeps (d=5, 40), and (d) the
  fixed multi-horizon-spread / regime-divergence novel structures. Two
  EXCELLENT results emerged: `blqKkP2l` (`ts_arg_max` recency + leverage +
  ivaco + drlt + buzz, S=2.55 F=2.03) correlates 0.701 vs `YP0bLdzA` — BLOCKED
  (over threshold, Sharpe 2.55 falls 0.002 short of the 1.10x=2.552 premium
  escape) — and **`lelNqEZl`** (this alpha), the 6-factor backstop variant,
  which reached EXCELLENT (S=2.01, F=2.01) while holding correlation at 0.567,
  comfortably SAFE.

## Self-Correlation

**AUTHORITATIVE, CONFIRMED**: BRAIN's `/alphas/lelNqEZl/check` endpoint
returns `SELF_CORRELATION: {result: PASS, value: 0.5666, limit: 0.7}` —
comfortably below the 0.70 auto-pass threshold, no Sharpe premium needed.
This is the ground-truth platform verdict, not an estimate. The endpoint
initially returned `PENDING` for the first ~9 minutes after simulation
completed (consistent with the known async-computation lag documented in
session 20260711-001), then resolved and was confirmed stable/consistent
across 3 independent polls spaced ~3.5 minutes apart.

Pre-resolution, a local PnL correlation estimate of 0.567 vs `YP0bLdzA`
(fair-value-**liability** event-magnitude, S=2.32 — the closest economic
sibling: same fair-value-L2 event-magnitude mechanism, opposite balance-sheet
side) had been computed as a fallback while waiting for BRAIN's authoritative
response; it matched the resolved authoritative value (0.5666) almost
exactly, reconfirming that this template family (event-magnitude-abs-ts-delta
+ leverage + ivaco/drlt + buzz) tracks local-PnL estimates at ~1.0x (no
correction multiplier), consistent with prior findings for `wpl5eP5v`,
`WjGVJ7bN`, and `YP0bLdzA`.

Next-highest peers (family-representative, from local `pnl_correlation.py --vs-book`,
useful as directional context even though the headline number above is now
the authoritative one):

| Peer (family) | Local Corr |
|------|------|
| `YP0bLdzA` (fair_val_liab_event_magnitude_leverage_blend) | 0.567 |
| `WjGVJ7bN` (excise_tax_event_magnitude_leverage) | 0.560 |
| deferred_revenue family rep | 0.534 |
| guidance_analyst family rep | 0.528 |
| `blqKkP2l` (this session's other candidate, same anchor) | 0.694 (mutual, not a book entry) |

## BRAIN Checks

**All 8 checks PASS** (verified via authoritative `/alphas/lelNqEZl/check`):

| Check | Result | Value | Limit |
|-------|--------|-------|-------|
| LOW_SHARPE | PASS | 2.01 | 1.25 |
| LOW_FITNESS | PASS | 2.01 | 1.00 |
| LOW_TURNOVER | PASS | 0.1104 | 0.01 |
| HIGH_TURNOVER | PASS | 0.1104 | 0.70 |
| CONCENTRATED_WEIGHT | PASS | — | — |
| LOW_SUB_UNIVERSE_SHARPE | PASS | 1.61 | 0.87 |
| MATCHES_COMPETITION | PASS | — | — |
| **SELF_CORRELATION** | **PASS (authoritative)** | **0.5666** | **0.70** |

## Post-Submission

**Submitted 2026-07-15 and confirmed ACTIVE on the BRAIN platform.**
`/alphas/lelNqEZl/check` returns `status: ACTIVE`, grade EXCELLENT, S=2.01,
F=2.01, all 7 remaining computable checks PASS. Submission itself reported
`Self-correlation: PASS (value: 0.5666)`, matching the authoritative
pre-submission `/check` confirmation. Consistent with prior submissions in
this family, `SELF_CORRELATION` is no longer listed as a distinct check
post-submission — platform acceptance is itself the final confirmation.
