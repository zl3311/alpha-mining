---
category: "dead_zone"
entity_type: "template"
template: "trade_when(ts_delta(FUNDAMENTAL, d) > 0, signal, ts_delta(FUNDAMENTAL, d) <= 0)"
discovered: "20260715-001"
expressions_tested: 1
best_sharpe: 0.01
status: "dead_end"
confidence: "low (single expression tested)"
---

# Template: `trade_when` Gated by a Slow Fundamental's Own Trend

Gating an event-magnitude signal's exposure by the sign of a DIFFERENT slow
fundamental's recent trend (as opposed to the known price/volume-momentum
directional-gating dead end in `template-directional-gating-sign-delta.md`,
or the proven realized-volatility regime gate in
`volatility-gate-fixes-sub-universe.md`) collapses the signal to
near-zero.

## Evidence (session 20260715-001)

`trade_when(ts_delta(fnd6_ivaco, 20) > 0, ts_decay_linear(rank(abs(ts_delta(fnd6_mrct / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_drlt / close), 5), ts_delta(fnd6_ivaco, 20) <= 0)`
→ S=0.01, F=0.00, T=23.3% (INFERIOR — the expression completed without a
unit error this time, unlike the permanent BRAIN unit-type error hit by
realized-vol `trade_when` gating on the sibling `fn_liab_fair_val_l2_q`
anchor per `event-magnitude-fresh-stabilizer.md`, but the resulting signal is
economically dead).

## Why it likely fails

`ts_delta(fnd6_ivaco, 20) > 0` is a slow, roughly-50/50 coin-flip condition
with no established economic link to whether the `mrct` event-magnitude
signal is currently informative — unlike the realized-volatility gate (which
concentrates exposure into genuinely higher-Sharpe regimes for THIS signal
family, per `volatility-gate-fixes-sub-universe.md`), gating by an unrelated
fundamental's trend appears to just excise roughly half of the trading days
at random with respect to the signal's actual edge, destroying rather than
concentrating the Sharpe.

## Rule

Do not gate an event-magnitude / fundamental blend by the trend of an
UNRELATED slow fundamental field. If regime-gating is revisited for this
family, only the realized-volatility gate (`ts_std_dev(returns, 20)`) has
been shown to work, and even that failed with a permanent unit error on the
`fair_val_l2` anchors specifically — treat `trade_when` gating of this
family as low-probability in general, not a reliable lever.

## Caveat

Only ONE variant tested (single anchor, single gate field, single window).
Confidence is LOW; this is a discouraging data point, not a rigorously
confirmed dead end. Do not invest further budget without a specific reason
to believe a different gate field/window would behave differently.
