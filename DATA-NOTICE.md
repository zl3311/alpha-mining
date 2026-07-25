# Notice about the `data/` directory

The code in this repository is MIT licensed (see [LICENSE](LICENSE)). The `data/` directory
is different: it is a research archive documenting work carried out on the WorldQuant BRAIN
platform, and a few things about it are worth stating explicitly before you reuse any of it.

## Submitted alphas are WorldQuant's property

`data/book/` contains 68 records of alphas submitted to BRAIN, including their complete
FASTEXPR expressions and performance metrics. Under the BRAIN Agreement, alphas submitted to
the platform become WorldQuant's property. These records are published here as a **research
record of what was tried and what resulted** — the equivalent of a laboratory notebook — not
as an assertion of ownership over the expressions and not as material offered for
redistribution or commercial use.

If you intend to do anything with these expressions beyond reading them, check WorldQuant's
current terms yourself. I am not in a position to grant rights I do not hold.

## Field metadata derives from the BRAIN platform

`data/knowledge/factor_profiles/` (1,669 files) and `data/reference/brain_data_catalog.md`
contain BRAIN data-field identifiers, field descriptions, coverage statistics, and
community usage counts obtained from the platform's `data-fields` API while I had an
account. `data/reference/brain_alphas_seed.json` and
`data/reference/brain_probe_representatives.json` are similar.

This material is descriptive metadata about the platform's catalogue, retained because the
research log is unintelligible without knowing which fields were tested. It is **not** the
underlying market or fundamental data, none of which is included here — that data is
licensed to WorldQuant by third-party vendors and is not mine to publish. Nothing in this
repository lets you reconstruct any vendor dataset.

## Performance figures are backtests, not returns

Every Sharpe, fitness, turnover, and drawdown number in this archive is an in-sample
backtest produced by BRAIN's simulator on a US equity universe, under a specific set of
neutralization, decay, and truncation settings recorded alongside each result. They are not
live trading results, they are not out-of-sample, and they carry all the usual caveats about
backtested performance plus a few specific to this project:

- Alphas were selected *because* they passed backtest gates, so the reported distribution is
  survivorship-biased by construction.
- The search ran roughly 53,000 simulations. At that scale, some apparently strong results
  are multiple-comparisons artifacts. I make no claim about which.
- Alpha decay is real and these signals are from 2026. Anything that worked then may not now.

**This is not investment advice and nothing here is a trading recommendation.**

## Papers are cited, not redistributed

Earlier revisions of this repository contained full-text markdown conversions of academic
papers. Those were removed before publication, both because redistributing full paper text
is a copyright problem and because one of them — Kakushadze's *101 Formulaic Alphas* — states
in its own text that WorldQuant LLC retains all rights in the formulae reproduced in its
Appendix A. See [`data/reference/papers/REFERENCES.md`](data/reference/papers/REFERENCES.md)
for citations and arXiv links.

## Reusing the archive

For the parts I can speak to — the methodology, the session narratives, the knowledge base
structure, the agent skills, and my own written analysis — treat them as MIT licensed
alongside the code, and a citation is appreciated (see `CITATION.cff`).

For the platform-derived material described above, use your own judgement and check
WorldQuant's terms. If WorldQuant objects to anything in this archive, open an issue and I
will remove it.

## No affiliation

This project is not affiliated with, endorsed by, or supported by WorldQuant. "WorldQuant"
and "BRAIN" are used descriptively to identify the platform the research was performed on.
