"""
Orchestrator: end-to-end pipeline runner for alpha mining.

Provides multiple modes:
- run_expression: Direct expression -> BRAIN backtest (manual/interactive)
- run_single: End-to-end for one PDF (extraction -> hypothesis -> formula -> backtest)
- run_batch: Process all PDFs in a directory
- ingest_paper: Extract and store a paper without LLM/BRAIN
- Hypothesis management: list, add, view, trace

Can be invoked from CLI:
    python3 -m alpha_mining.orchestrator --expression "rank(close)"
    python3 -m alpha_mining.orchestrator --ingest data/papers/some_paper.pdf
    python3 -m alpha_mining.orchestrator --papers
    python3 -m alpha_mining.orchestrator --hypotheses
"""

from __future__ import annotations

import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path

from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table

from .brain.client import BrainClient
from .brain.constants import ENDPOINTS
from .brain.models import SimulationConfig, SimulationResult
from .config import get_settings
from .naming import generate_alpha_name
from .pipeline.evaluation import evaluate_results
from .pipeline.prefilter import validate_expression
from .storage.db import AlphaDB
from .storage.models import (
    AlphaRecord,
    PaperImageRecord,
    PaperRecord,
    ResultRecord,
    SessionRecord,
    SimulationRecord,
)

logger = logging.getLogger(__name__)
console = Console()


# =====================================================================
# Expression simulation
# =====================================================================


async def run_expression(
    expression: str,
    *,
    region: str = "USA",
    universe: str = "TOP3000",
    decay: int = 6,
    neutralization: str = "SUBINDUSTRY",
    language: str = "FASTEXPR",
    source: str = "manual",
    name: str = "",
) -> SimulationResult | None:
    """Submit a single expression to BRAIN and return the result."""
    settings = get_settings()

    pre_check = validate_expression(expression, language=language)
    if not pre_check:
        console.print(f"[red]Pre-filter failed:[/red] {pre_check.issues}")
        return None

    config = SimulationConfig(
        expression=expression,
        language=language,
        region=region,
        universe=universe,
        decay=decay,
        neutralization=neutralization,
    )

    alpha_name = name or generate_alpha_name(expression, source)
    console.print(f"[bold]Submitting:[/bold] {alpha_name}")
    console.print(f"  Expression: {expression}")
    console.print(f"  Region={region} Universe={universe} Decay={decay} Neut={neutralization}")

    async with BrainClient(settings) as client:
        result = await client.simulate(config)

        if result.succeeded and result.alpha_id:
            color = _fitness_color(result.metrics.fitness)
            await client.set_alpha_properties(
                result.alpha_id,
                name=alpha_name,
                tags=[source, language.lower()],
                color=color,
                description=expression[:200],
            )

    _display_result(result, alpha_name)

    async with AlphaDB(settings.db_path) as db:
        session_id, session_eid = await db.create_session(
            SessionRecord(source=source, name=alpha_name)
        )
        await _persist_result(db, result, alpha_name, session_id=session_id)

    return result


async def run_expression_batch(
    expressions: list[str],
    *,
    source: str = "batch",
    session_id: int | None = None,
    **kwargs,
) -> list[SimulationResult]:
    """Submit multiple expressions concurrently."""
    settings = get_settings()

    valid = []
    for expr in expressions:
        pre_check = validate_expression(expr)
        if pre_check:
            valid.append(expr)
        else:
            console.print(f"[yellow]Skipping:[/yellow] {expr[:60]} -- {pre_check.issues}")

    if not valid:
        console.print("[red]No valid expressions to submit.[/red]")
        return []

    configs = [SimulationConfig(expression=expr, **kwargs) for expr in valid]

    console.print(f"[bold]Submitting {len(configs)} expressions...[/bold]")

    async with BrainClient(settings) as client:
        results = await client.simulate_batch(configs)

    summary = evaluate_results(results)
    _display_summary(summary)

    async with AlphaDB(settings.db_path) as db:
        if session_id is None:
            session_id, _ = await db.create_session(
                SessionRecord(source=source, name=f"batch-{len(valid)}")
            )
        for r in results:
            alpha_name = generate_alpha_name(r.config.expression, source)
            await _persist_result(db, r, alpha_name, session_id=session_id)

    return results


# =====================================================================
# Paper ingestion
# =====================================================================


async def ingest_paper(
    pdf_path: str,
    *,
    title: str = "",
) -> tuple[int, str]:
    """
    Extract a PDF via Marker and store in DB. No LLM key needed.

    Returns (internal_id, entity_id) of the created paper.
    """
    from .pipeline.extraction import extract_and_save

    settings = get_settings()
    path = Path(pdf_path)

    if not path.exists():
        console.print(f"[red]File not found:[/red] {pdf_path}")
        return -1, ""

    paper_title = title or path.stem.replace("_", " ").replace("-", " ").title()
    console.print(f"[bold]Ingesting:[/bold] {paper_title}")

    markdown, images, md_path, img_paths = extract_and_save(
        path, api_key=settings.datalab_api_key
    )
    console.print(f"  Extracted {len(markdown)} chars, {len(images)} images")

    async with AlphaDB(settings.db_path) as db:
        paper_id, paper_eid = await db.insert_paper(
            PaperRecord(
                title=paper_title,
                pdf_path=str(path),
                markdown_path=str(md_path),
                extracted_markdown=markdown,
            )
        )

        for filename, img_data_b64 in images.items():
            raw_b64 = img_data_b64
            if "," in raw_b64:
                raw_b64 = raw_b64.split(",", 1)[1]

            ext = Path(filename).suffix.lower()
            content_type = {
                ".png": "image/png",
                ".jpg": "image/jpeg",
                ".jpeg": "image/jpeg",
                ".gif": "image/gif",
                ".svg": "image/svg+xml",
            }.get(ext, "image/png")

            await db.insert_paper_image(
                PaperImageRecord(
                    paper_id=paper_id,
                    filename=filename,
                    content_type=content_type,
                    image_data_b64=raw_b64,
                )
            )

    console.print(f"  Stored as {paper_eid}")
    console.print(f"  Markdown: {md_path}")
    return paper_id, paper_eid


# =====================================================================
# Full pipeline (PDF -> hypotheses -> alphas -> BRAIN)
# =====================================================================


async def run_single(pdf_path: str) -> list[SimulationResult]:
    """Full pipeline for a single PDF. Requires LLM_API_KEY."""
    settings = get_settings()

    if not settings.llm_api_key:
        console.print(
            "[red]LLM_API_KEY not set.[/red] Set it in .env for the full pipeline, "
            "or use --expression for direct expression testing."
        )
        return []

    from .llm.provider import LLMProvider
    from .pipeline.extraction import extract_pdf
    from .pipeline.hypothesis import generate_hypotheses
    from .pipeline.translation import translate_hypothesis

    console.print(f"[bold]Processing:[/bold] {pdf_path}")
    paper_text = extract_pdf(pdf_path, api_key=settings.datalab_api_key)
    console.print(f"  Extracted {len(paper_text)} chars")

    llm = LLMProvider(settings)

    async with AlphaDB(settings.db_path) as db:
        few_shot = await db.get_top_quartile_for_feedback(limit=5)

    few_shot_examples = [
        {"excerpt": "", "hypothesis": r.get("mechanism", ""), "formula": r.get("expression", ""),
         "sharpe": r.get("sharpe", 0), "fitness": r.get("fitness", 0)}
        for r in few_shot
    ] if few_shot else None

    hypotheses = generate_hypotheses(paper_text, llm, few_shot_examples=few_shot_examples)
    console.print(f"  Generated {len(hypotheses)} hypotheses")

    expressions = []
    for hyp in hypotheses:
        formula = translate_hypothesis(hyp, llm, few_shot_examples=few_shot_examples)
        if formula:
            pre_check = validate_expression(formula)
            if pre_check:
                expressions.append(formula)
            else:
                console.print(f"  [yellow]Filtered:[/yellow] {formula[:60]} -- {pre_check.issues}")

    console.print(f"  {len(expressions)} expressions passed pre-filter")

    if not expressions:
        console.print("[yellow]No valid expressions generated.[/yellow]")
        return []

    return await run_expression_batch(expressions, source="paper")


# =====================================================================
# Display helpers
# =====================================================================


def _fitness_color(fitness: float) -> str:
    """Map fitness score to a hex color for BRAIN platform visualization."""
    if fitness >= 1.0:
        return "#00FF00"  # green -- passes gate
    elif fitness >= 0.8:
        return "#FFD700"  # gold -- close, worth iterating
    elif fitness >= 0.5:
        return "#FF8C00"  # orange -- moderate
    else:
        return "#FF4444"  # red -- poor


def _display_result(result: SimulationResult, alpha_name: str = "") -> None:
    if not result.succeeded:
        console.print(f"[red]FAILED:[/red] {result.error_message}")
        return

    m = result.metrics
    status_color = "green" if m.passes_submission_gates else "yellow"

    title = f"Result: {alpha_name}" if alpha_name else f"Result: {result.config.expression[:60]}"
    table = Table(title=title)
    table.add_column("Metric", style="bold")
    table.add_column("Value")
    table.add_column("Gate", style="dim")

    if alpha_name:
        table.add_row("Name", alpha_name, "")
    table.add_row("Expression", result.config.expression[:60], "")
    table.add_row("Sharpe", f"{m.sharpe:.3f}", ">= 1.25" if m.sharpe >= 1.25 else "[red]< 1.25[/red]")
    table.add_row("Fitness", f"{m.fitness:.3f}", ">= 1.0" if m.fitness >= 1.0 else "[red]< 1.0[/red]")
    table.add_row("Turnover", f"{m.turnover * 100:.1f}%", "1-70%")
    table.add_row("Returns", f"{m.returns:.4f}", "")
    table.add_row("Drawdown", f"{m.drawdown:.4f}", "")

    if m.self_correlation is not None:
        table.add_row("Self-Corr", f"{m.self_correlation:.3f}", "< 0.7")

    checks_pass = sum(1 for c in m.checks if c.result == "PASS")
    table.add_row("Checks", f"{checks_pass}/{len(m.checks)} PASS", "")

    grade = result.raw_response.get("grade", "")
    if grade:
        table.add_row("Grade", grade, "")

    console.print(table)
    console.print(f"  [{status_color}]Submittable: {m.passes_submission_gates}[/{status_color}]")
    if result.platform_url:
        console.print(f"  URL: {result.platform_url}")


def _display_summary(summary) -> None:
    table = Table(title="Batch Summary")
    table.add_column("Metric", style="bold")
    table.add_column("Value")
    table.add_row("Total", str(summary.total))
    table.add_row("Succeeded", str(summary.succeeded))
    table.add_row("Failed", str(summary.failed))
    table.add_row("Submittable", str(summary.submittable))
    table.add_row("Avg Sharpe", f"{summary.avg_sharpe:.3f}")
    table.add_row("Max Sharpe", f"{summary.max_sharpe:.3f}")
    table.add_row("Avg Fitness", f"{summary.avg_fitness:.3f}")
    table.add_row("Max Fitness", f"{summary.max_fitness:.3f}")
    console.print(table)


# =====================================================================
# Persistence (new schema)
# =====================================================================


async def _persist_result(
    db: AlphaDB,
    result: SimulationResult,
    alpha_name: str = "",
    session_id: int | None = None,
) -> None:
    """Save a simulation result across the new schema tables."""
    language = result.config.language
    alpha_id, alpha_eid = await db.insert_alpha(
        AlphaRecord(
            name=alpha_name,
            expression=result.config.expression,
            language=language.value if hasattr(language, "value") else str(language),
        )
    )

    raw = result.raw_response
    sim_id, sim_eid = await db.insert_simulation(
        SimulationRecord(
            alpha_id=alpha_id,
            sim_config_json=json.dumps(result.config.to_api_payload()["settings"]),
            status=result.status.value.lower(),
            brain_alpha_id=result.alpha_id,
            platform_url=result.platform_url,
            brain_grade=raw.get("grade", ""),
            brain_stage=raw.get("stage", ""),
            brain_status=raw.get("status", ""),
            brain_classifications_json=json.dumps(raw.get("classifications", [])),
            brain_tags_json=json.dumps(raw.get("tags", [])),
        )
    )

    if result.metrics:
        await db.insert_result(
            ResultRecord(
                simulation_id=sim_id,
                sharpe=result.metrics.sharpe,
                fitness=result.metrics.fitness,
                turnover=result.metrics.turnover,
                returns=result.metrics.returns,
                drawdown=result.metrics.drawdown,
                self_correlation=result.metrics.self_correlation,
                checks_json=json.dumps([c.model_dump() for c in result.metrics.checks]),
                raw_response_json=json.dumps(result.raw_response),
            )
        )


# =====================================================================
# CLI
# =====================================================================


def main():
    parser = argparse.ArgumentParser(
        description="Alpha Mining Pipeline",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    sim_group = parser.add_argument_group("Simulation")
    sim_group.add_argument("--expression", "-e", help="Single expression to simulate")
    sim_group.add_argument("--region", default="USA")
    sim_group.add_argument("--universe", default="TOP3000")
    sim_group.add_argument("--decay", type=int, default=6)
    sim_group.add_argument("--neutralization", default="SUBINDUSTRY")
    sim_group.add_argument("--language", "-l", default="FASTEXPR",
                          choices=["PYTHON", "FASTEXPR", "EXPRESSION"],
                          help="Alpha language (default: FASTEXPR, PYTHON may require consultant tier)")
    sim_group.add_argument("--name", "-n", help="Manual name override")
    sim_group.add_argument("--source", "-s", default="manual", help="Source tag")

    paper_group = parser.add_argument_group("Papers")
    paper_group.add_argument("--ingest", "-i", help="Ingest a PDF (or directory of PDFs)")
    paper_group.add_argument("--papers", action="store_true", help="List all ingested papers")
    paper_group.add_argument("--paper", help="View a paper by entity_id")
    paper_group.add_argument("--search-papers", help="Full-text search across papers")

    hyp_group = parser.add_argument_group("Hypotheses")
    hyp_group.add_argument("--hypotheses", action="store_true", help="List hypotheses")
    hyp_group.add_argument("--add-hypothesis", help="Add a hypothesis (mechanism text)")
    hyp_group.add_argument("--hyp-paper", help="Paper entity_id to link hypothesis to")
    hyp_group.add_argument("--hyp-sign", default="", help="Predicted sign (positive/negative)")
    hyp_group.add_argument("--hyp-horizon", default="", help="Time horizon")
    hyp_group.add_argument("--hypothesis", help="View hypothesis detail by entity_id")

    pipeline_group = parser.add_argument_group("Full Pipeline")
    pipeline_group.add_argument("--pdf", "-p", help="PDF file for full pipeline")
    pipeline_group.add_argument("--batch", "-b", help="Directory of PDFs for full pipeline")

    export_group = parser.add_argument_group("Export & Stats")
    export_group.add_argument("--export", action="store_true", help="Export results to markdown")
    export_group.add_argument("--export-top", type=int, help="Export top N results")
    export_group.add_argument("--stats", action="store_true", help="Show database statistics")
    export_group.add_argument("--top", type=int, help="Show top N results")
    export_group.add_argument("--session", help="View session summary by entity_id")

    submit_group = parser.add_argument_group("Submission")
    submit_group.add_argument("--submit-alpha", help="Submit a BRAIN alpha by its alpha_id (from platform URL)")
    submit_group.add_argument("--submit-name", help="Name to set on the alpha before submitting")
    submit_group.add_argument("--submit-tags", help="Comma-separated tags to set before submitting")
    submit_group.add_argument("--submit-desc", help="Description to set before submitting")
    submit_group.add_argument("--list-alphas", action="store_true",
                              help="List recent alphas from BRAIN with grade/status")
    submit_group.add_argument("--list-limit", type=int, default=15,
                              help="Number of alphas to list (default: 15)")
    submit_group.add_argument("--list-order", default="-dateCreated",
                              help="Sort order (e.g. -is.fitness, -is.sharpe, -dateCreated)")

    screen_group = parser.add_argument_group("Local Screening")
    screen_group.add_argument("--screen", action="append", metavar="EXPR",
                             help="Screen expression(s) locally before BRAIN submission (repeatable)")
    screen_group.add_argument("--screen-region", default="us", help="Region for local data (default: us)")
    screen_group.add_argument("--screen-universe", type=int, default=200,
                             help="Universe size for local data (default: 200)")
    screen_group.add_argument("--refresh-data", action="store_true",
                             help="Force refresh of cached local market data")

    parser.add_argument("-v", "--verbose", action="store_true", help="Debug logging")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(message)s",
        handlers=[RichHandler(console=console, rich_tracebacks=True)],
    )

    # Dispatch
    if args.stats:
        asyncio.run(_show_stats())
    elif args.top:
        asyncio.run(_show_top(args.top))
    elif args.expression:
        asyncio.run(run_expression(
            args.expression, region=args.region, universe=args.universe,
            decay=args.decay, neutralization=args.neutralization,
            language=args.language,
            source=args.source, name=args.name or "",
        ))
    elif args.ingest:
        asyncio.run(_cli_ingest(args.ingest))
    elif args.papers:
        asyncio.run(_cli_list_papers())
    elif args.paper:
        asyncio.run(_cli_view_paper(args.paper))
    elif args.search_papers:
        asyncio.run(_cli_search_papers(args.search_papers))
    elif args.hypotheses:
        asyncio.run(_cli_list_hypotheses())
    elif args.add_hypothesis:
        asyncio.run(_cli_add_hypothesis(
            args.add_hypothesis, paper_eid=args.hyp_paper,
            sign=args.hyp_sign, horizon=args.hyp_horizon,
        ))
    elif args.hypothesis:
        asyncio.run(_cli_view_hypothesis(args.hypothesis))
    elif args.session:
        asyncio.run(_cli_view_session(args.session))
    elif args.export or args.export_top:
        asyncio.run(_cli_export(args.export_top or 20))
    elif args.submit_alpha:
        asyncio.run(_cli_submit_alpha(
            args.submit_alpha,
            name=args.submit_name or "",
            tags=args.submit_tags or "",
            description=args.submit_desc or "",
        ))
    elif args.list_alphas:
        asyncio.run(_cli_list_brain_alphas(limit=args.list_limit, order=args.list_order))
    elif args.screen:
        _cli_screen(args.screen, args.screen_region, args.screen_universe, args.refresh_data)
    elif args.pdf:
        asyncio.run(run_single(args.pdf))
    elif args.batch:
        pdfs = list(Path(args.batch).glob("*.pdf"))
        if not pdfs:
            console.print(f"[red]No PDFs found in {args.batch}[/red]")
            sys.exit(1)
        for pdf in pdfs:
            asyncio.run(run_single(str(pdf)))
    else:
        parser.print_help()


# =====================================================================
# CLI helpers
# =====================================================================


async def _show_stats():
    settings = get_settings()
    async with AlphaDB(settings.db_path) as db:
        stats = await db.get_stats()
    table = Table(title="Database Statistics")
    table.add_column("Metric", style="bold")
    table.add_column("Value")
    for key, val in stats.items():
        table.add_row(key, str(val))
    console.print(table)


async def _show_top(limit: int):
    settings = get_settings()
    async with AlphaDB(settings.db_path) as db:
        rows = await db.get_top_results(limit=limit)
    if not rows:
        console.print("[yellow]No results yet.[/yellow]")
        return
    table = Table(title=f"Top {limit} Results")
    table.add_column("#", style="dim")
    table.add_column("Name")
    table.add_column("Expression")
    table.add_column("Sharpe", justify="right")
    table.add_column("Fitness", justify="right")
    table.add_column("Turnover", justify="right")
    for i, row in enumerate(rows, 1):
        table.add_row(
            str(i), str(row.get("name", ""))[:35],
            str(row.get("expression", ""))[:45],
            f"{row.get('sharpe', 0):.3f}", f"{row.get('fitness', 0):.3f}",
            f"{row.get('turnover', 0) * 100:.1f}%",
        )
    console.print(table)


async def _cli_ingest(path_str: str):
    path = Path(path_str)
    if path.is_dir():
        pdfs = list(path.glob("*.pdf"))
        if not pdfs:
            console.print(f"[red]No PDFs found in {path}[/red]")
            return
        for pdf in pdfs:
            await ingest_paper(str(pdf))
    else:
        await ingest_paper(path_str)


async def _cli_list_papers():
    settings = get_settings()
    async with AlphaDB(settings.db_path) as db:
        papers = await db.list_papers()
    if not papers:
        console.print("[yellow]No papers ingested yet.[/yellow]")
        return
    table = Table(title="Ingested Papers")
    table.add_column("Entity ID", style="dim")
    table.add_column("Title")
    table.add_column("Chars", justify="right")
    table.add_column("Date")
    for p in papers:
        table.add_row(
            p["entity_id"], p["title"][:50],
            str(p.get("char_count", 0)), str(p["created_at"])[:10],
        )
    console.print(table)


async def _cli_view_paper(entity_id: str):
    settings = get_settings()
    async with AlphaDB(settings.db_path) as db:
        paper = await db.get_paper(entity_id)
    if not paper:
        console.print(f"[red]Paper not found:[/red] {entity_id}")
        return
    console.print(f"[bold]{paper['title']}[/bold]")
    console.print(f"Entity ID: {paper['entity_id']}")
    console.print(f"Source: {paper['source_url']}")
    console.print(f"Markdown path: {paper['markdown_path']}")
    console.print("\n--- Extracted text (first 2000 chars) ---\n")
    console.print(paper["extracted_markdown"][:2000])


async def _cli_search_papers(query: str):
    settings = get_settings()
    async with AlphaDB(settings.db_path) as db:
        results = await db.search_papers(query)
    if not results:
        console.print(f"[yellow]No papers matching '{query}'[/yellow]")
        return
    table = Table(title=f"Search: '{query}'")
    table.add_column("Entity ID", style="dim")
    table.add_column("Title")
    table.add_column("Snippet")
    for r in results:
        table.add_row(r["entity_id"], r["title"][:40], str(r.get("snippet", ""))[:60])
    console.print(table)


async def _cli_list_hypotheses():
    settings = get_settings()
    async with AlphaDB(settings.db_path) as db:
        hyps = await db.list_hypotheses()
    if not hyps:
        console.print("[yellow]No hypotheses yet.[/yellow]")
        return
    table = Table(title="Hypotheses")
    table.add_column("Entity ID", style="dim")
    table.add_column("Mechanism")
    table.add_column("Sign")
    table.add_column("Paper")
    table.add_column("Alphas", justify="right")
    table.add_column("Best Sharpe", justify="right")
    for h in hyps:
        table.add_row(
            h["entity_id"], str(h["mechanism"])[:50],
            h["predicted_sign"] or "-",
            str(h.get("paper_title") or "-")[:20],
            str(h.get("alpha_count", 0)),
            f"{h['best_sharpe']:.3f}" if h.get("best_sharpe") else "-",
        )
    console.print(table)


async def _cli_add_hypothesis(mechanism: str, paper_eid: str = None, sign: str = "", horizon: str = ""):
    settings = get_settings()
    async with AlphaDB(settings.db_path) as db:
        paper_id = None
        if paper_eid:
            paper = await db.get_paper(paper_eid)
            if paper:
                paper_id = paper["id"]
            else:
                console.print(f"[yellow]Paper not found: {paper_eid}[/yellow]")

        hyp_id, hyp_eid = await db.add_hypothesis(
            mechanism=mechanism,
            predicted_sign=sign,
            time_horizon=horizon,
            paper_id=paper_id,
        )
    console.print(f"[green]Hypothesis created:[/green] {hyp_eid}")
    console.print(f"  Mechanism: {mechanism}")


async def _cli_view_hypothesis(entity_id: str):
    settings = get_settings()
    async with AlphaDB(settings.db_path) as db:
        hyp = await db.get_hypothesis(entity_id)
        if not hyp:
            console.print(f"[red]Hypothesis not found:[/red] {entity_id}")
            return
        results = await db.get_hypothesis_results(entity_id)

    console.print(f"[bold]Hypothesis:[/bold] {hyp['entity_id']}")
    console.print(f"  Mechanism: {hyp['mechanism']}")
    console.print(f"  Sign: {hyp['predicted_sign']}, Horizon: {hyp['time_horizon']}")

    if results:
        table = Table(title="Alpha Results")
        table.add_column("Alpha")
        table.add_column("Expression")
        table.add_column("Sharpe", justify="right")
        table.add_column("Fitness", justify="right")
        table.add_column("Status")
        for r in results:
            table.add_row(
                str(r.get("alpha_eid", ""))[:25],
                str(r.get("expression", ""))[:40],
                f"{r['sharpe']:.3f}" if r.get("sharpe") else "-",
                f"{r['fitness']:.3f}" if r.get("fitness") else "-",
                r.get("status", "-"),
            )
        console.print(table)
    else:
        console.print("  No alphas/results yet.")


async def _cli_view_session(entity_id: str):
    settings = get_settings()
    async with AlphaDB(settings.db_path) as db:
        summary = await db.get_session_summary(entity_id)
    if not summary:
        console.print(f"[red]Session not found:[/red] {entity_id}")
        return
    sess = summary["session"]
    console.print(f"[bold]Session:[/bold] {sess['entity_id']}")
    console.print(f"  Source: {sess['source']}, Name: {sess['name']}")
    console.print(f"  Hypotheses: {summary['hypothesis_count']}")
    console.print(f"  Alphas: {summary['alpha_count']}")
    console.print(f"  Simulations: {summary['simulation_count']}")
    console.print(f"  Best Sharpe: {summary['best_sharpe']}")
    console.print(f"  Best Fitness: {summary['best_fitness']}")


async def _cli_export(limit: int):
    from .export import export_top_results
    settings = get_settings()
    async with AlphaDB(settings.db_path) as db:
        paths = await export_top_results(db, limit=limit)
    if paths:
        console.print(f"[green]Exported {len(paths)} results to data/exports/[/green]")
        for p in paths:
            console.print(f"  {p}")
    else:
        console.print("[yellow]No results to export.[/yellow]")


async def _cli_submit_alpha(alpha_id: str, name: str = "", tags: str = "", description: str = ""):
    """Set metadata and submit an alpha to BRAIN for official scoring."""
    settings = get_settings()
    async with BrainClient(settings) as client:
        # Step 1: Set metadata
        if name or tags or description:
            console.print("[bold]Step 1: Setting metadata...[/bold]")
            tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []
            result = await client.set_alpha_properties(
                alpha_id, name=name, tags=tag_list or None, description=description,
            )
            if "error" in result:
                console.print(f"[yellow]Metadata warning: {result}[/yellow]")
            else:
                console.print(f"  Name: {name}")
                if tag_list:
                    console.print(f"  Tags: {tag_list}")

        # Step 2: Submit
        console.print("[bold]Step 2: Submitting for scoring...[/bold]")
        result = await client.submit_alpha(alpha_id)

        if result.get("status") == "completed":
            sc_pass = result.get("self_correlation_pass")
            sc_val = result.get("self_correlation_value")
            if sc_pass:
                console.print("[green]Submitted successfully![/green]")
                console.print(f"  Self-correlation: PASS (value: {sc_val})")
            else:
                console.print("[red]Submission failed self-correlation check[/red]")
                console.print(f"  Self-correlation value: {sc_val} (must be < 0.7)")
        elif result.get("status") == "not_found":
            console.print("[red]Alpha not found. Check the alpha_id.[/red]")
        else:
            console.print(f"[yellow]Submission status: {result}[/yellow]")

        console.print(f"  URL: https://platform.worldquantbrain.com/alpha/{alpha_id}")


async def _cli_list_brain_alphas(limit: int = 15, order: str = "-dateCreated"):
    """List recent alphas directly from BRAIN API with grade and status."""
    settings = get_settings()
    async with BrainClient(settings) as client:
        url = f"{ENDPOINTS['users_self']}/alphas?limit={limit}&offset=0&order={order}"
        r = await client._client.get(url)
        data = r.json()

    results = data.get("results", [])
    if not results:
        console.print("[yellow]No alphas found on BRAIN.[/yellow]")
        return

    table = Table(title="Recent BRAIN Alphas")
    table.add_column("ID", style="dim")
    table.add_column("Expression")
    table.add_column("Sharpe", justify="right")
    table.add_column("Fitness", justify="right")
    table.add_column("Turn", justify="right")
    table.add_column("Grade")
    table.add_column("Status")

    for a in results:
        is_data = a.get("is", {})
        code = a.get("regular", {}).get("code", "") if isinstance(a.get("regular"), dict) else str(a.get("regular", ""))
        grade = a.get("grade", "")
        status = a.get("status", "")
        stage = a.get("stage", "")

        grade_style = {"EXCELLENT": "green", "GOOD": "green", "AVERAGE": "yellow", "INFERIOR": "red"}.get(grade, "")
        status_str = f"{status} ({stage})"

        table.add_row(
            a.get("id", ""),
            code[:45],
            f"{is_data.get('sharpe', 0):.2f}",
            f"{is_data.get('fitness', 0):.2f}",
            f"{is_data.get('turnover', 0) * 100:.1f}%",
            f"[{grade_style}]{grade}[/{grade_style}]" if grade_style else grade,
            status_str,
        )

    console.print(table)


def _cli_screen(expressions: list[str], region: str, universe: int, refresh: bool):
    """Screen expression(s) locally using yfinance data and rank IC analysis."""
    from .local import screen_batch

    console.print(f"[bold]Local screening: {len(expressions)} expression(s)[/bold]")
    console.print(f"  Region: {region}, Universe: top {universe}, Refresh: {refresh}")
    console.print()

    try:
        results = screen_batch(expressions, region=region, universe=universe, refresh=refresh)
    except Exception as e:
        console.print(f"[red]Screening failed:[/red] {e}")
        return

    if len(results) == 1:
        r = results[0]
        table = Table(title="Local Screen Result")
        table.add_column("Metric", style="bold")
        table.add_column("Value")
        table.add_row("Expression", r.expression[:80])
        if r.error:
            table.add_row("Error", f"[red]{r.error}[/red]")
        else:
            ic_style = "green" if abs(r.rank_ic) > 0.015 else "yellow" if abs(r.rank_ic) > 0.005 else "red"
            table.add_row("Rank IC", f"[{ic_style}]{r.rank_ic:+.4f}[/{ic_style}]")
            table.add_row("IC IR", f"{r.ic_ir:.2f}")
            table.add_row("Est. Turnover", f"{r.est_turnover:.1%}")
            table.add_row("Coverage", f"{r.coverage:.0%}")
            verdict_style = {"PROMISING": "green", "WEAK": "yellow", "DEAD": "red"}.get(r.verdict, "")
            table.add_row("Verdict", f"[{verdict_style}]{r.verdict}[/{verdict_style}]")
        console.print(table)
    else:
        table = Table(title=f"Local Screen: {len(results)} expressions (sorted by |IC|)")
        table.add_column("#", style="dim")
        table.add_column("Expression")
        table.add_column("Rank IC", justify="right")
        table.add_column("IC IR", justify="right")
        table.add_column("Turnover", justify="right")
        table.add_column("Coverage", justify="right")
        table.add_column("Verdict")

        for i, r in enumerate(results, 1):
            if r.error:
                table.add_row(str(i), r.expression[:50], "", "", "", "", f"[red]ERROR: {r.error[:30]}[/red]")
            else:
                ic_style = "green" if abs(r.rank_ic) > 0.015 else "yellow" if abs(r.rank_ic) > 0.005 else "red"
                verdict_style = {"PROMISING": "green", "WEAK": "yellow", "DEAD": "red"}.get(r.verdict, "")
                table.add_row(
                    str(i), r.expression[:50],
                    f"[{ic_style}]{r.rank_ic:+.4f}[/{ic_style}]",
                    f"{r.ic_ir:.2f}", f"{r.est_turnover:.1%}", f"{r.coverage:.0%}",
                    f"[{verdict_style}]{r.verdict}[/{verdict_style}]",
                )
        console.print(table)


if __name__ == "__main__":
    main()
