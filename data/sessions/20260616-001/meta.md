---
id: "20260616-001"
date: "2026-06-16"
strategy: "HYPOTHESIS"
research_question: "Can option8 implied-volatility skew fields combined with news_open_vol via structurally novel cross-theme interactions produce a decorrelated gate-passing alpha without repeating saturated IV-spread or analyst-revision families?"
budget_used: 58
budget_cap: null
trigger: "manual alpha-mining session via Cursor"
gate_passers: 31
submissions: 0
submittable_candidates: 2
status: "productive"
tags:
  - "20260616-001"
  - "skew_news_open_vol"
  - "HYPOTHESIS"
candidates:
  - id: "YPpjReEW"
    grade: "AVERAGE"
    sharpe: 1.74
    fitness: 1.09
    self_corr_value: 0.4613
    self_corr_result: "PASS"
    verdict: "QUEUED"
  - id: "GrwrVP5G"
    grade: "EXCELLENT"
    sharpe: 2.04
    fitness: 2.29
    self_corr_value: 0.517
    self_corr_result: "RISKY_BRAIN_PENDING"
    verdict: "QUEUED"
  - id: "RRpJgbVn"
    grade: "AVERAGE"
    sharpe: 1.70
    fitness: 1.03
    self_corr_value: null
    self_corr_result: "not_checked_sub_universe_fail"
    verdict: "BLOCKED_LOW_SUB_UNIVERSE"
  - id: "akdr52L9"
    grade: "INFERIOR"
    sharpe: 1.66
    fitness: 1.00
    self_corr_value: null
    self_corr_result: "not_checked_sub_universe_fail"
    verdict: "BLOCKED_LOW_SUB_UNIVERSE"
---

# Session 20260616-001

Manual mining session started from the existing dirty local workspace. Branch-changing
sync to latest `main` was skipped to avoid disrupting uncommitted server submodule
changes already present in the working tree.

## Phase 0 Context

STRATEGY: HYPOTHESIS

TARGET: Test the open factor-merge opportunity around option8 implied-volatility
skew plus `news_open_vol`, using structurally novel interaction templates rather
than saturated `implied_volatility_call_* - implied_volatility_put_*` spread
variants.

BUDGET: Start with 12 simulations. Iterate only if results produce at least one
gate-passer or materially improve the tradeoff between grade, turnover, and
self-correlation versus recent orthogonal-theme tests.

CONSTRAINTS: Avoid PV reversal, COGS, sparse fundamental2 `ts_zscore`, model16,
option9 standalone, news/news18 standalone, IV270 spread variants, volume-weighted
fundamentals, `anl4_*_flag * (-1 * returns)`, and negated duplicates. Apply the
structural novelty requirement: at least half of the slate must use non-saturated
operator tree shapes such as products, ratios, directional gates, multi-horizon
spreads, dynamic correlations, or `trade_when` logic.

RATIONALE: Active merge/theme opportunity files remain open and recent sessions
show the book is saturated with analyst, fundamental, event, and IV-spread
families. A focused hypothesis pass on the top decorrelated option8/news pair is
the first matching strategy because it tests a specific cross-theme idea while
honoring the EXPLORE-first novelty rule.

## Phase 1 Candidate Slate

Batch tag: `skew_news_r1`

1. `ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(news_open_vol), 5)`
   - Mechanism: Directly test the top factor-merge pair, where long-dated IV skew and opening news volatility are negatively correlated diversifiers.
   - Sign: positive, long high skew plus high opening news volatility.

2. `ts_decay_linear(rank(implied_volatility_mean_skew_1080) + rank(ts_mean(news_open_vol, 22)), 5)`
   - Mechanism: Use the longest-maturity skew profile and smooth the news leg to reduce the known news turnover problem.
   - Sign: positive.

3. `ts_decay_linear(rank(implied_volatility_mean_skew_720) + rank(ts_mean(news_open_vol, 22)), 5)`
   - Mechanism: Same smoothed-news blend with the 720-day skew field, which has similar standalone behavior but slightly different temporal correlation.
   - Sign: positive.

4. `ts_decay_linear(rank(implied_volatility_mean_skew_360) * rank(ts_mean(news_open_vol, 22)), 5)`
   - Mechanism: Nonlinear confirmation; only emphasize names where both option skew and opening news volatility are elevated.
   - Sign: positive.

5. `ts_decay_linear(rank(implied_volatility_mean_skew_1080) * rank(ts_mean(news_open_vol, 22)), 5)`
   - Mechanism: Test whether the cleaner mixed-regime 1080-day skew profile works better as a nonlinear interaction.
   - Sign: positive.

6. `rank(rank(implied_volatility_mean_skew_360) / (1 + rank(ts_mean(news_open_vol, 22))))`
   - Mechanism: Rank-ratio test for option skew that is high relative to realized opening news volatility.
   - Sign: positive.

7. `ts_decay_linear(rank(ts_mean(implied_volatility_mean_skew_360, 5) - ts_mean(implied_volatility_mean_skew_360, 22)) + rank(ts_mean(news_open_vol, 22)), 5)`
   - Mechanism: Multi-horizon skew acceleration blended with smoothed opening news volatility.
   - Sign: positive.

8. `ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_delta(ts_mean(news_open_vol, 10), 5)), 5)`
   - Mechanism: Static skew plus rising opening-news volatility, testing whether the news leg must be changing rather than merely high.
   - Sign: positive.

9. `ts_decay_linear(rank(ts_corr(implied_volatility_mean_skew_360, news_open_vol, 20)), 5)`
   - Mechanism: Dynamic inter-factor alignment; alpha comes from names where option skew and opening news volatility recently co-move.
   - Sign: positive.

10. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.01)`
    - Mechanism: Volatility-regime gate; only trade the skew/news blend when realized volatility is elevated.
    - Sign: positive.

11. `trade_when(ts_delta(close, 5) < 0, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)), 5), ts_delta(close, 5) > 0)`
    - Mechanism: Drawdown-regime gate; option/news information may matter most after short-term price weakness.
    - Sign: positive.

12. `ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)) + rank(fnd6_cshtr), 5)`
    - Mechanism: Add a cash-flow treasury-share theme that appears as a secondary decorrelating partner for skew fields, testing whether a broad fundamental stabilizer lifts grade.
    - Sign: positive.

Submitted via HF queue with tags `20260616-001` and `skew_news_r1`, priority 5,
USA TOP3000, SUBINDUSTRY neutralization, decay 6.

## Phase 2 Round 1 Results

Batch completed with 12/12 simulations done, 0 failures, and 1 aggregate
gate-passer.

| Alpha | Variant | Grade | S | F | Turnover | BRAIN Checks | Verdict |
|-------|---------|-------|---|---|----------|--------------|---------|
| RRpJgbVn | volatility-regime `trade_when` on skew + smoothed news | AVERAGE | 1.70 | 1.03 | 19.32% | `LOW_SUB_UNIVERSE_SHARPE` FAIL 0.71 vs 0.74 | BLOCKED |

### Round 1 Findings

The plain unsmoothed blend had strong Sharpe (S=1.94) but impossible turnover
(129.48%), confirming the news leg's known turnover problem. Smoothing news
fixed turnover but left fitness below gate. Nonlinear product improved fitness
(S=1.53, F=0.80) but did not gate-pass. The volatility-regime gate was the only
structure to cross aggregate gates, suggesting the option-skew/news relationship
is conditional on elevated realized volatility.

The failure is narrow and specific (`LOW_SUB_UNIVERSE_SHARPE` 0.71 vs 0.74), so
round 2 refines the volatility gate and adds broad stabilizers rather than
changing the mechanism.

## Phase 3 Candidate Slate

Batch tag: `skew_news_refine_r2`

1. `trade_when(ts_std_dev(returns, 20) > 0.015, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.008)`
   - Lower entry threshold to broaden sub-universe coverage while keeping a low-volatility exit.

2. `trade_when(ts_std_dev(returns, 20) > 0.018, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.009)`
   - Middle threshold between the blocked gate and broader coverage.

3. `trade_when(ts_std_dev(returns, 30) > 0.018, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 30) < 0.009)`
   - Longer volatility window to smooth regime membership and reduce sub-universe instability.

4. `trade_when(ts_std_dev(returns, 30) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 30) < 0.01)`
   - Same threshold as the winner but smoother regime detection.

5. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 44)), 5), ts_std_dev(returns, 20) < 0.01)`
   - Heavier news smoothing to improve cross-sectional stability.

6. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)) + rank(ts_mean(scl12_buzz, 5)), 5), ts_std_dev(returns, 20) < 0.01)`
   - Add high-coverage social attention as a stabilizer without using the banned `flag * (-ret)` driver.

7. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) + rank(ts_mean(news_open_vol, 22)) + rank(fnd6_cshtr), 5), ts_std_dev(returns, 20) < 0.01)`
   - Add the secondary decorrelating `fnd6_cshtr` partner to test whether a broad fundamental leg repairs sub-universe.

8. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_1080) + rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.01)`
   - Test whether the mixed-regime 1080-day skew field improves the same volatility-gated template.

9. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_720) + rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.01)`
   - Test the 720-day skew field in the winning gate.

10. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(implied_volatility_mean_skew_360) * rank(ts_mean(news_open_vol, 22)), 5), ts_std_dev(returns, 20) < 0.01)`
    - Apply the volatility gate to the best nonlinear product variant from round 1.

Submitted via HF queue with tags `20260616-001` and `skew_news_refine_r2`,
priority 5, USA TOP3000, SUBINDUSTRY neutralization, decay 6.

## Phase 4 Round 2 Results

Batch completed with 9/10 simulations done, 1 failed simulation, and 2 aggregate
gate-passers.

| Alpha | Variant | Grade | S | F | Turnover | BRAIN Checks | Self-Corr | Verdict |
|-------|---------|-------|---|---|----------|--------------|-----------|---------|
| YPpjReEW | volatility-gated skew/news product | AVERAGE | 1.74 | 1.09 | 18.38% | ALL PASS | 0.4613 PASS | QUEUED |
| akdr52L9 | 30d volatility-gated additive blend | INFERIOR | 1.66 | 1.00 | 19.07% | `LOW_SUB_UNIVERSE_SHARPE` FAIL 0.66 vs 0.72 | not checked | BLOCKED |

### Final Verdict

The hypothesis is partially confirmed. The raw option-skew/news blend is too
turnover-heavy and simple smoothing is too weak, but volatility-regime gating
turns the interaction into a viable low-correlation book filler. The best
candidate, `YPpjReEW`, passes all computable BRAIN checks and has BRAIN
self-correlation 0.4613, so it was recorded as `status: PENDING`, queued for
human submission review, and labeled on the BRAIN platform.

This is not an EXCELLENT+ breakthrough: it is an AVERAGE-grade decorrelated
filler. Further refinement should only continue if the goal is to improve this
specific volatility-gated product template; the additive versions are capped by
sub-universe or low-fitness failures.

## Phase 5 Continuation Target

The user requested continuation until at least one EXCELLENT+ submittable alpha
is found. A scan of recent high-grade candidates showed:

- `6XEkGV3O` (`-ts_zscore(fnd6_fyrc, 63)`) is a technical-code artifact and fails
  `CONCENTRATED_WEIGHT` 0.50 vs 0.10.
- IV90/IV120 SPECTACULAR variants such as `1YgMZ6OW` and `9qRnjZMq` pass
  computable checks but fail self-correlation at 0.9655 and 0.9911.
- Event/itci variants have strong metrics but local PnL correlation 0.64-0.68
  against the active book, and they share fields, so BRAIN is likely to inflate
  them above the 0.70 self-corr gate.

Round 3 therefore tests whether MARKET neutralization and removal/softening of
the buzz-reversal leg can preserve EXCELLENT+ metrics while reducing self-corr.

## Phase 6 Candidate Slate

Batch tag: `event_market_decorr_r3`

1. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 5)`
   - MARKET-neutralized rerun of the strongest event/leverage/buzz template.

2. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 10) * (-1 * returns)), 5)`
   - MARKET-neutralized version of the lower local-corr 10d buzz variant.

3. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + ts_decay_linear(rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 3), 3)`
   - MARKET-neutralized nested-buzz decay variant with high Sharpe.

4. `rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + ts_decay_linear(rank(ts_mean(scl12_buzz, 5) * (-1 * returns)), 3)`
   - MARKET-neutralized unwrapped high-Sharpe variant.

5. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5)), 5)`
   - Remove the returns-reversal leg to test whether buzz as attention stabilizer lowers self-corr.

6. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) * rank(ts_mean(scl12_buzz, 5)), 5)`
   - Nonlinear leverage-attention confirmation instead of additive reversal.

7. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5)), 5)`
   - Nonlinear event-leverage confirmation with a separate attention stabilizer.

8. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(ts_mean(scl12_buzz, 5)), 5), ts_std_dev(returns, 20) < 0.01)`
   - Volatility-regime gate for the no-return buzz version.

9. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close), 5)`
   - Replace buzz reversal with a capital-intensity leg to reduce overlap with sentiment-reversal book entries.

10. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close) + rank(ts_mean(scl12_buzz, 5)), 5)`
    - Capital-intensity plus attention stabilizer.

11. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(fnd6_fatl / close) + rank(ts_mean(scl12_buzz, 5)), 5)`
    - Remove leverage to test whether leverage is the cross-book correlation driver.

12. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(ts_mean(scl12_buzz, 5)) + rank(fnd6_fatl / close), 5)`
    - Event-attention product plus capital-intensity stabilizer.

Submitted via HF queue with tags `20260616-001` and `event_market_decorr_r3`,
priority 5, USA TOP3000, MARKET neutralization, decay 6.

## Phase 7 Round 3 Results

The MARKET-neutralized batch produced five EXCELLENT aggregate gate-passers, all
passing computable BRAIN checks. However, BRAIN self-correlation failed the
buzz-reversal variants:

| Alpha | Variant | Grade | S | F | Turnover | Self-Corr / Status | Verdict |
|-------|---------|-------|---|---|----------|--------------------|---------|
| xAxA0noq | 10d buzz reversal MARKET | EXCELLENT | 2.03 | 2.35 | 12.67% | 0.7458 FAIL vs `d5Q3ZmWv` | BLOCKED |
| A1w1MnoW | 5d buzz reversal MARKET | EXCELLENT | 2.05 | 2.29 | 13.72% | 0.7492 FAIL | BLOCKED |
| MPpPoaNn | nested buzz reversal MARKET | EXCELLENT | 2.00 | 2.19 | 14.02% | timed out, likely same family | BLOCKED / unverified |
| vRLR3PVd | unwrapped buzz reversal MARKET | EXCELLENT | 2.16 | 2.24 | 17.29% | local corr 0.717 | BLOCKED / unverified |
| zq9qpaE8 | event + leverage + `fnd6_fatl` MARKET | EXCELLENT | 2.00 | 2.39 | 2.50% | check timed out; local top corr 0.722 vs `np30Odjd` | REFINE |

### Round 3 Finding

MARKET neutralization preserves EXCELLENT metrics but does not solve the
buzz-reversal event-family self-corr wall against `d5Q3ZmWv`. The only promising
direction is the no-buzz `zq9qpaE8` shape, but its `fnd6_fatl` stabilizer creates
correlation with `np30Odjd`. Round 4 swaps or reshapes that stabilizer while
keeping MARKET neutralization.

## Phase 8 Candidate Slate

Batch tag: `event_market_stabilizer_r4`

1. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_fate / close), 5)`
   - Sister capital-intensity field to test whether `fate` reduces `np30Odjd` overlap versus `fatl`.

2. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_dlto / close), 5)`
   - Debt substitute for capital intensity, expected lower correlation with `np30Odjd`.

3. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_acdo), 5)`
   - Accrual/discontinued-ops stabilizer with strong standalone history but different peer cluster.

4. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(open / close - 1), 5)`
   - Intraday dislocation stabilizer to reduce fundamental/capital-intensity overlap.

5. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(anl4_netdebt_flag), 5)`
   - Analyst net-debt confirmation without `fatl` or buzz reversal.

6. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(anl4_ptpr_flag), 5)`
   - Analyst pre-tax profit confirmation as an alternative to capital intensity.

7. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(fnd6_fatl / close) + rank(open / close - 1), 5)`
   - Remove leverage and add intraday dislocation to test whether leverage drives `np30Odjd`/fundamental overlap.

8. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(fnd6_fatl / close) + rank(-1 * equity / assets), 5)`
   - Product form to make `fatl` conditional on event magnitude rather than an additive peer-like leg.

9. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) * rank(fnd6_fatl / close), 5)`
   - Product form to make leverage conditional on capital intensity.

10. `trade_when(ts_std_dev(returns, 20) > 0.02, ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close), 5), ts_std_dev(returns, 20) < 0.01)`
    - Volatility gate for the `zq9qpaE8` shape to alter position overlap.

11. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 5))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close), 5)`
    - Longer event-delta horizon to change the event leg's position profile.

12. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 1))) + rank(-1 * equity / assets) + rank(fnd6_fatl / close), 5)`
    - Shorter event-delta horizon to test a more event-like profile.

Submitted via HF queue with tags `20260616-001` and `event_market_stabilizer_r4`,
priority 5, USA TOP3000, MARKET neutralization, decay 6.

## Phase 9 Round 4 Results

Round 4 produced 8 EXCELLENT+ candidates, all passing computable BRAIN checks.
The best local self-corr profile was `GrwrVP5G` (EXCELLENT, S=2.04, F=2.29,
local max 0.517), followed by `d5x5w982` (EXCELLENT, local max 0.589) and
`1Y7Y5W5J` (SPECTACULAR, local max 0.673). BRAIN's self-corr endpoint remained
asynchronously pending for `GrwrVP5G`, `1Y7Y5W5J`, and `d5x5w982`, so none can
be called authoritative SAFE yet.

Because all candidates still share `fnd6_itci` with multiple active book entries,
round 5 tests product/conditional event structures to reduce shared-field
position overlap below the local 0.35 safety zone while preserving EXCELLENT+
metrics.

## Phase 10 Candidate Slate

Batch tag: `event_product_decorr_r5`

1. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(open / close - 1) + rank(-1 * equity / assets), 5)`
   - Event magnitude only contributes when confirmed by intraday dislocation.

2. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(open / close - 1) + rank(fnd6_fatl / close), 5)`
   - Product event/intraday leg plus capital-intensity stabilizer.

3. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(-1 * equity / assets) + rank(open / close - 1), 5)`
   - Event magnitude gated by leverage, with intraday dislocation as stabilizer.

4. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(anl4_netdebt_flag) + rank(-1 * equity / assets), 5)`
   - Event magnitude only when confirmed by analyst net-debt revisions.

5. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(anl4_ptpr_flag) + rank(-1 * equity / assets), 5)`
   - Event magnitude only when confirmed by pre-tax profit revisions.

6. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(fnd6_acdo) + rank(open / close - 1), 5)`
   - Event magnitude gated by accrual/discontinued-ops quality.

7. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(fnd6_dlto / close) + rank(open / close - 1), 5)`
   - Event magnitude gated by debt value.

8. `ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) * rank(fnd6_fatl / close) + rank(open / close - 1), 5)`
   - Event magnitude gated by capital intensity, using intraday dislocation instead of leverage.

9. `trade_when(rank(open / close - 1) > 0.6, ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets), 5), rank(open / close - 1) < 0.4)`
   - Trade the event/leverage core only in high intraday-dislocation names.

10. `trade_when(rank(fnd6_fatl / close) > 0.6, ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets), 5), rank(fnd6_fatl / close) < 0.4)`
    - Trade event/leverage only in high capital-intensity names.

11. `trade_when(rank(anl4_netdebt_flag) > 0.6, ts_decay_linear(rank(abs(ts_delta(fnd6_itci / close, 3))) + rank(-1 * equity / assets), 5), rank(anl4_netdebt_flag) < 0.4)`
    - Trade event/leverage only with analyst confirmation.

12. `ts_decay_linear(rank(ts_corr(fnd6_itci / close, returns, 20)) + rank(open / close - 1) + rank(-1 * equity / assets), 5)`
    - Dynamic event-return coupling instead of event magnitude, designed to change position overlap.

Submitted via HF queue with tags `20260616-001` and `event_product_decorr_r5`,
priority 5, USA TOP3000, MARKET neutralization, decay 6.

## Phase 11 Round 5 Results

Round 5 produced 5 EXCELLENT+ candidates, all passing computable BRAIN checks:

| Alpha | Variant | Grade | S | F | Turnover | Local Self-Corr | Verdict |
|-------|---------|-------|---|---|----------|-----------------|---------|
| YPpPXl6q | event × intraday + `fatl` | SPECTACULAR | 2.05 | 2.58 | 7.91% | 0.641 | BLOCKED / high local |
| RRpR07nn | event × intraday + leverage | EXCELLENT | 2.13 | 2.43 | 8.18% | 0.663 | BLOCKED / high local |
| P0p0rNvE | event × `fatl` + intraday | EXCELLENT | 1.97 | 2.20 | 19.31% | 0.732 | BLOCKED |
| qMAMk91V | event × `dlto` + intraday | EXCELLENT | 2.00 | 2.08 | 21.88% | 0.717 | BLOCKED |
| wpRpXAgQ | event × leverage + intraday | EXCELLENT | 2.03 | 2.04 | 22.32% | 0.754 | BLOCKED |

### Continuation Outcome

The continuation did not get an authoritative BRAIN self-correlation PASS because
the BRAIN self-corr endpoint stayed asynchronously pending for new EXCELLENT+
candidates. The best available EXCELLENT+ candidate is `GrwrVP5G` from round 4:

- EXCELLENT, S=2.04, F=2.29, turnover 2.89%.
- All computable BRAIN checks PASS.
- Local PnL max correlation 0.517 vs active local book.
- Labeled on BRAIN and queued as RISKY pending final authoritative self-corr.

This satisfies the EXCELLENT+ discovery target but should not be officially
submitted until `scripts/pnl_correlation.py --alphas GrwrVP5G --brain-check`
returns `SELF_CORRELATION: PASS` or the platform submission dialog confirms the
self-corr gate clears.
