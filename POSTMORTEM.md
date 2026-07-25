# Postmortem

I spent about ten weeks building an LLM-agent pipeline that mined formulaic trading alphas
on WorldQuant BRAIN. It worked better than I expected. Then my account was locked without
explanation, my inquiries went unanswered, and the project ended.

This document records what was built, what it achieved, what I got wrong, and what I would
do differently. Everything numeric below is reproducible from this repository unless I say
otherwise.

## Timeline

| Date | Event |
|---|---|
| 2026-05-16 | First commit. Five alpha variants pass all BRAIN submission gates the same day. |
| 2026-05-17 | Third alpha submitted. |
| 2026-06-04 | First implied-volatility-spread alpha graded EXCELLENT. |
| 2026-06-26 | First fully autonomous cron-triggered session. |
| 2026-07-19 | Last mining session (`20260719-001`). It completed normally. |
| 2026-07-24 | Last commit — housekeeping, consolidating draft session branches. |

Access ended after that. The repository contains no record of when or why, for reasons I
explain below.

## What the system produced

```
Active period          2026-05-16 to 2026-07-24 (~10 weeks)
Commits                267 across all branches
Mining sessions        63
Submitted alphas       64 live (53 ACTIVE + 11 PENDING)
Book records           68 total (also 3 SUPERSEDED, 1 REJECTED)
Mechanism families     60 distinct, across the 64 live alphas
Grades (live)          22 SPECTACULAR, 37 EXCELLENT, 1 GOOD, 4 AVERAGE
Sharpe (68 records)    mean 2.30, median 2.26, max 3.09
Fitness (68 records)   mean 2.50, median 2.32, max 5.14
Turnover (54 records)  mean 11.0%, median 10.8%
Simulations           ~53,000 cumulative through the queue server by mid-July
Knowledge artifacts    1,669 factor profiles, 29 patterns, 28 dead zones, 18 rules
Python                 12,914 lines tracked, 446 offline tests
```

Verify any of it:

```bash
uv run python3 scripts/parse_frontmatter.py --dir data/book --field status,grade,family
```

On platform standing: the last snapshot recorded anywhere in this repository is Gold tier at
roughly 14,000 points in mid-July. The account kept accruing after that — with a 2,000
point daily cap and 50+ EXCELLENT-or-better alphas active, the final total was
substantially higher than that snapshot. I never captured the closing figure and no longer
have access to check, so I am not going to state a number I cannot support. The alpha counts
and grades above are exact, because they come from files in this repository rather than from
memory.

## What actually worked

**Economics-first generation.** The agent was required to articulate a mechanism — why
should this quantity predict returns — before writing an expression. This sounds like
process theatre. It was the single highest-leverage rule. Mechanism-free candidates
generated from operator recombination passed backtests at a much lower rate and, more
importantly, produced alphas that correlated heavily with existing ones because they were
rediscovering the same underlying effect through different syntax.

**A file-based knowledge base instead of a clever agent.** There is no planner, no tree
search, no reinforcement learning. There is a directory of markdown files the agent reads
at the start of every session and appends to at the end. `dead_zones/` prevented re-testing
exhausted directions; `patterns/` captured transferable structure; `rules/` recorded
constraints learned by violating them. Almost all of the compounding came from this, not
from model capability. A stateless agent with the same model was dramatically worse.

**Satisficing over optimising.** Early sessions burned enormous budget hunting for the
*best* candidate. Changing the goal to "stop at the first candidate that clears every gate"
roughly tripled throughput of submitted alphas per unit of compute. In a search space this
large with a hard decorrelation constraint, marginal quality mattered far less than
diversity of submissions.

**Trusting the platform's own verdict.** My local PnL correlation estimate systematically
understated BRAIN's self-correlation figure — by roughly 1.5x when two alphas shared data
fields. Every candidate had to be validated against BRAIN's authoritative
`/alphas/{id}/check` endpoint before I would believe it. Several apparently clean
candidates were rejected there.

## What I got wrong

**I underestimated the decorrelation wall by an order of magnitude.** Generating a
plausible alpha is easy; a language model with a decent operator reference does it readily.
The binding constraint is that BRAIN requires self-correlation below 0.7 against your own
submitted alphas, so each submission shrinks the space available to the next. By roughly 50
alphas I was spending most of my budget not on finding signal but on finding signal
*orthogonal to signal I already had*. I designed the system around signal quality when I
should have designed it around correlation budget from the start.

**I put self-correlation in the pre-filter on paper, which is impossible.** The original
design (still visible in `context/llm_alpha_mining_context.md`) gated self-correlation
before backtesting. It cannot work: the check needs a realised PnL series, which only exists
after a backtest. So every candidate costs a simulation before you learn whether it is even
admissible. Had I understood this on day one, I would have prioritised generating
*deliberately* decorrelated candidates rather than good ones and filtering afterwards.

**I discovered negation far too late.** Negating a building block — `rank(-1 * x)` instead
of `rank(x)` — opens a substantially larger set of independent directions than the positive
direction alone, because a factor and its negation load differently against an existing
book. I found this after the positive direction was near saturation. It should have been
part of the search space from the beginning.

**I let two persistence models coexist.** The agent loop stored everything in markdown; the
orchestrator CLI stored everything in SQLite. Neither was wrong, but the documentation
described one as "legacy" while code actively used it, and I misled myself about my own
architecture for weeks. Fixed while preparing this release.

**I did not snapshot platform state.** No points total, no rank, no leaderboard position is
recorded anywhere in 63 session files. I tracked what I could compute locally and assumed
the platform would always be there to tell me the rest. This is the mistake I would most
like back — not because the number matters, but because *"I can always look it up later"* is
exactly the assumption that fails when access disappears.

## On the account lock

My BRAIN account was locked. I was given no explanation. I asked, more than once, and
received no response. That is the whole of what I know.

I want to be precise about the limits of this account, because I think that matters more
than venting. **This repository contains no record of the lock** — no date, no error log, no
support correspondence, no failed authentication trace. The final session on 2026-07-19
completed normally, and the commits through 2026-07-24 are ordinary housekeeping. Everything
in this section is my recollection rather than something you can verify from the archive,
and I would rather say so plainly than imply documentation I do not have.

I also will not speculate about their reasons. I do not know them. I can note what is
visible in this repository so you can form your own view: the work was automated, it ran
through a self-hosted job queue against the platform API rather than the web interface, and
it operated at a scale of roughly 53,000 simulations. Whether any of that was the trigger, I
genuinely cannot say. A human being reviewed and approved every single submission — the
agent was explicitly forbidden from submitting — but the *generation and backtesting* were
automated, and I am not going to pretend otherwise now that it is inconvenient.

What I am disappointed about is not the outcome. Platforms are entitled to set their rules
and enforce them. What I found genuinely dispiriting was the silence: no notice, no stated
reason, no route to reply. Ten weeks of work and 64 submitted alphas ended with an
unexplained door closing and unanswered emails. Even a one-line "you violated section X"
would have let me learn something. That is a poor way to treat people who are, by design,
contributing unpaid research to your platform.

So I am publishing the work instead. It has value independent of my standing with any
particular platform.

## If you are starting something similar

1. **Design around the decorrelation budget, not signal quality.** Assume every submission
   makes the next one harder, and plan the search accordingly.
2. **Build the knowledge base before the agent.** The compounding is in the accumulated
   notes, not the model. Write down failures with the same care as successes; `dead_zones/`
   saved me more compute than any optimisation.
3. **Snapshot external state you do not control.** Points, ranks, standings, IDs. Write them
   to a file on a schedule. Assume the API will be gone the day you want it.
4. **Satisfice.** Stop at the first thing that clears the bar. Optimisation is a luxury for
   problems where you can afford to be picky.
5. **Read the terms of service properly, and take them seriously.** I do not know that this
   is why my account was locked. But I do know I was operating on assumptions about
   acceptable automation that I had never actually verified, and I would not repeat that.

## What is in the archive

If you only look at three things:

- [`data/knowledge/dead_zones/`](data/knowledge/dead_zones) — 28 things that did not work
  and why. Rarer and more useful than the successes.
- [`data/sessions/`](data/sessions) — 63 sessions of an agent reasoning through research
  decisions in real time, including the confused ones.
- [`.cursor/skills/`](.cursor/skills) — the entire methodology as prose instructions. The
  interesting artifact is how much of a research process can be specified in English rather
  than code.

The alpha expressions in [`data/book/`](data/book) are real and complete. Read
[DATA-NOTICE.md](DATA-NOTICE.md) before reusing them; alphas submitted to BRAIN become
WorldQuant's property under their agreement, and I am publishing this as a research record
rather than as a portfolio you should trade.
