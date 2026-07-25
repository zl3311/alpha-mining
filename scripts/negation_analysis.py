"""
Analyze negation sweep results and produce a structured report.

Reads the regenerated sweep_data.csv (which now includes negation results),
identifies gate-passers, negation-only winners, and blend candidates.
Outputs a markdown report suitable for the session results file.

Usage:
    uv run python3 scripts/negation_analysis.py
    uv run python3 scripts/negation_analysis.py --output local/test_scripts/negation_report.md
"""

import argparse
import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SWEEP_CSV = ROOT / "local" / "sweep_analysis" / "sweep_data.csv"
PROFILES_DIR = ROOT / "data" / "knowledge" / "factor_profiles"
BOOK_DIR = ROOT / "data" / "book"
DEAD_ZONES_DIR = ROOT / "data" / "knowledge" / "dead_zones"

NEGATED_TEMPLATES = {"neg_rank_level", "neg_rank_value_norm", "rank_neg_delta"}

DEAD_ZONE_DATASETS = {"news12", "news18", "model16", "model51", "option9"}
PV_REVERSAL_FIELDS = {
    "returns", "close", "open", "high", "low", "vwap", "volume", "cap",
    "adv5", "adv10", "adv15", "adv20", "adv60", "adv120", "adv180",
    "sharesout", "split", "dividend",
}


def is_dead_zone(field: str, dataset: str) -> bool:
    if dataset in DEAD_ZONE_DATASETS:
        return True
    if field in PV_REVERSAL_FIELDS and dataset == "pv1":
        return True
    return False


def load_sweep_data() -> list[dict]:
    with open(SWEEP_CSV) as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        for col in ("sharpe", "fitness", "turnover", "returns", "drawdown"):
            r[col] = float(r[col]) if r[col] else 0.0
    return rows


def load_book_fields() -> set[str]:
    """Get fields referenced in the submitted book (from tags matching known factor fields)."""
    known_fields = set()
    if PROFILES_DIR.exists():
        for p in PROFILES_DIR.glob("*.md"):
            known_fields.add(p.stem)

    fields = set()
    if not BOOK_DIR.exists():
        return fields
    for path in BOOK_DIR.glob("*.md"):
        text = path.read_text()
        for line in text.split("\n"):
            stripped = line.strip()
            if stripped.startswith("- \""):
                tag = stripped.lstrip("- ").strip('"').strip("'")
                if tag in known_fields:
                    fields.add(tag)
    return fields


def analyze_negation_sweep(rows: list[dict]) -> dict:
    """Core analysis of negation sweep results."""
    neg_rows = [r for r in rows if r["template"] in NEGATED_TEMPLATES]
    pos_rows = [r for r in rows if r["template"] not in NEGATED_TEMPLATES]

    # Per-field aggregation
    neg_by_field: dict[str, list[dict]] = defaultdict(list)
    pos_by_field: dict[str, list[dict]] = defaultdict(list)
    for r in neg_rows:
        neg_by_field[r["field"]].append(r)
    for r in pos_rows:
        pos_by_field[r["field"]].append(r)

    # Gate-passers: negated sims with Sharpe >= 1.0
    gate_passers = sorted(
        [r for r in neg_rows if r["sharpe"] >= 1.0],
        key=lambda r: -r["sharpe"],
    )

    # Strong gate-passers (S >= 1.25)
    strong_passers = [r for r in gate_passers if r["sharpe"] >= 1.25]

    # Negation-only winners: fields where negated best >> positive best
    negation_winners = []
    for field, neg_field_rows in neg_by_field.items():
        neg_best = max(neg_field_rows, key=lambda r: r["sharpe"])
        pos_field_rows = pos_by_field.get(field, [])
        pos_best_sharpe = max((r["sharpe"] for r in pos_field_rows), default=0.0)

        gap = neg_best["sharpe"] - pos_best_sharpe
        if gap > 0.3 and neg_best["sharpe"] >= 1.0:
            negation_winners.append({
                "field": field,
                "dataset": neg_best["dataset"],
                "neg_sharpe": neg_best["sharpe"],
                "neg_fitness": neg_best["fitness"],
                "neg_grade": neg_best["grade"],
                "neg_expression": neg_best["expression"],
                "pos_best_sharpe": pos_best_sharpe,
                "direction_gap": round(gap, 2),
                "is_dead_zone": is_dead_zone(field, neg_best["dataset"]),
            })
    negation_winners.sort(key=lambda x: -x["neg_sharpe"])

    # Grade distribution of negated results
    grade_dist = defaultdict(int)
    for r in neg_rows:
        grade_dist[r["grade"]] += 1

    # Template effectiveness within negation
    template_stats = {}
    for tpl in NEGATED_TEMPLATES:
        tpl_rows = [r for r in neg_rows if r["template"] == tpl]
        if tpl_rows:
            sharpes = [r["sharpe"] for r in tpl_rows]
            template_stats[tpl] = {
                "count": len(tpl_rows),
                "mean_sharpe": sum(sharpes) / len(sharpes),
                "max_sharpe": max(sharpes),
                "gate_pass_rate": sum(1 for s in sharpes if s >= 1.0) / len(sharpes),
            }

    return {
        "total_negated": len(neg_rows),
        "total_fields_with_negation": len(neg_by_field),
        "gate_passers": gate_passers,
        "strong_passers": strong_passers,
        "negation_winners": negation_winners,
        "grade_dist": dict(grade_dist),
        "template_stats": template_stats,
    }


def format_report(analysis: dict, book_fields: set[str]) -> str:
    """Format the analysis into a markdown report."""
    lines = []
    lines.append("---")
    lines.append('id: "negation-analysis"')
    lines.append('date: "2026-07-05"')
    lines.append('strategy: "SYSTEMATIC_ANALYSIS"')
    lines.append('research_question: "Analyze completed negation sweep results and identify new building blocks"')
    lines.append("budget_used: 0")
    lines.append("budget_cap: null")
    lines.append('trigger: "manual"')
    lines.append(f"gate_passers: {len(analysis['strong_passers'])}")
    lines.append("submissions: 0")
    lines.append('status: "completed"')
    lines.append("tags:")
    lines.append("  - negation_sweep")
    lines.append("  - factor_profiling")
    lines.append("  - direction_analysis")
    lines.append("---")
    lines.append("")
    lines.append("# Negation Sweep Analysis Report")
    lines.append("")
    lines.append("## Executive Summary")
    lines.append("")
    lines.append(
        f"Analyzed **{analysis['total_negated']:,}** negated-direction simulations across "
        f"**{analysis['total_fields_with_negation']:,}** fields. Found "
        f"**{len(analysis['strong_passers'])}** strong gate-passers (S >= 1.25) and "
        f"**{len(analysis['negation_winners'])}** negation-dominant fields "
        f"(where reversing the signal improves Sharpe by > 0.3)."
    )
    lines.append("")

    # Overview stats
    lines.append("## Overview Statistics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Total negated simulations | {analysis['total_negated']:,} |")
    lines.append(f"| Fields with negation data | {analysis['total_fields_with_negation']:,} |")
    lines.append(f"| Gate-passers (S >= 1.0) | {len(analysis['gate_passers'])} |")
    lines.append(f"| Strong gate-passers (S >= 1.25) | {len(analysis['strong_passers'])} |")
    lines.append(f"| Negation-dominant fields (gap > 0.3) | {len(analysis['negation_winners'])} |")
    lines.append("")

    # Grade distribution
    lines.append("### Grade Distribution (negated sims)")
    lines.append("")
    lines.append("| Grade | Count | Pct |")
    lines.append("|-------|-------|-----|")
    total = analysis["total_negated"]
    for grade in ["SPECTACULAR", "EXCELLENT", "GOOD", "AVERAGE", "INFERIOR"]:
        cnt = analysis["grade_dist"].get(grade, 0)
        pct = cnt / total * 100 if total > 0 else 0
        if cnt > 0:
            lines.append(f"| {grade} | {cnt:,} | {pct:.1f}% |")
    lines.append("")

    # Template effectiveness
    lines.append("### Template Effectiveness (negated)")
    lines.append("")
    lines.append("| Template | Count | Mean S | Max S | Gate-pass Rate |")
    lines.append("|----------|-------|--------|-------|----------------|")
    for tpl, stats in sorted(analysis["template_stats"].items(), key=lambda x: -x[1]["max_sharpe"]):
        lines.append(
            f"| {tpl} | {stats['count']:,} | {stats['mean_sharpe']:.2f} | "
            f"{stats['max_sharpe']:.2f} | {stats['gate_pass_rate']:.1%} |"
        )
    lines.append("")

    # Top gate-passers
    lines.append("## Top Gate-Passers (S >= 1.25)")
    lines.append("")
    lines.append("| # | Field | Expression | S | F | Grade | Dataset | In Book |")
    lines.append("|---|-------|------------|---|---|-------|---------|---------|")
    seen_fields = set()
    rank = 0
    for r in analysis["strong_passers"]:
        field = r["field"]
        if field in seen_fields:
            continue
        seen_fields.add(field)
        rank += 1
        in_book = "YES" if field in book_fields else ""
        dead = " (DEAD ZONE)" if is_dead_zone(field, r["dataset"]) else ""
        lines.append(
            f"| {rank} | {field}{dead} | `{r['expression']}` | "
            f"{r['sharpe']:.2f} | {r['fitness']:.2f} | {r['grade']} | "
            f"{r['dataset']} | {in_book} |"
        )
        if rank >= 30:
            break
    lines.append("")

    # Negation-dominant fields (the key discovery)
    lines.append("## Negation-Dominant Fields")
    lines.append("")
    lines.append(
        "Fields where the negated direction significantly outperforms the positive direction "
        "(direction gap > 0.3, negated S >= 1.0). These represent **new building blocks** "
        "not accessible via positive-direction templates."
    )
    lines.append("")
    lines.append("| # | Field | Dataset | Neg S | Pos S | Gap | Grade | Dead Zone | In Book |")
    lines.append("|---|-------|---------|-------|-------|-----|-------|-----------|---------|")
    actionable_winners = [w for w in analysis["negation_winners"] if not w["is_dead_zone"]]
    dead_winners = [w for w in analysis["negation_winners"] if w["is_dead_zone"]]

    for i, w in enumerate(actionable_winners[:30], 1):
        in_book = "YES" if w["field"] in book_fields else ""
        lines.append(
            f"| {i} | {w['field']} | {w['dataset']} | {w['neg_sharpe']:.2f} | "
            f"{w['pos_best_sharpe']:.2f} | {w['direction_gap']:+.2f} | "
            f"{w['neg_grade']} | | {in_book} |"
        )
    lines.append("")
    if dead_winners:
        lines.append(f"*{len(dead_winners)} additional negation-dominant fields are in dead zones (excluded).*")
        lines.append("")

    # Actionable candidates for blending
    lines.append("## Actionable Building Blocks")
    lines.append("")
    lines.append(
        "Negation-dominant fields NOT in dead zones and NOT already in the book. "
        "Sorted by negated Sharpe. These are prime candidates for multi-factor blends."
    )
    lines.append("")
    blend_candidates = [
        w for w in actionable_winners
        if w["field"] not in book_fields and w["neg_sharpe"] >= 1.0
    ]
    if blend_candidates:
        lines.append("| # | Field | Dataset | Expression | S | F | Grade |")
        lines.append("|---|-------|---------|-----------|---|---|-------|")
        for i, w in enumerate(blend_candidates[:20], 1):
            lines.append(
                f"| {i} | {w['field']} | {w['dataset']} | "
                f"`{w['neg_expression']}` | {w['neg_sharpe']:.2f} | "
                f"{w['neg_fitness']:.2f} | {w['neg_grade']} |"
            )
        lines.append("")
        lines.append(f"**Total actionable negation building blocks: {len(blend_candidates)}**")
    else:
        lines.append("No actionable negation building blocks found.")
    lines.append("")

    # Recommended next steps
    lines.append("## Recommended Next Steps")
    lines.append("")
    lines.append("1. **Multi-factor blends**: Combine top negation building blocks with "
                 "positive-direction factors from uncorrelated clusters")
    lines.append("2. **BRAIN checks**: Run `brain_check.py` on GOOD/AVERAGE grade negation "
                 "alphas to verify full submittability")
    lines.append("3. **Self-correlation check**: Test top candidates against the existing book")
    lines.append("4. **Template enhancement**: Apply `decay_linear` or `trade_when` wrappers "
                 "to boost fitness of high-Sharpe/low-fitness fields")
    lines.append("5. **Cross-direction blends**: `0.5 * rank(field) + 0.5 * rank(-1 * other_field)` "
                 "for decorrelated pair signals")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Analyze negation sweep results")
    parser.add_argument(
        "--output",
        default=str(ROOT / "local" / "test_scripts" / "negation_report.md"),
    )
    args = parser.parse_args()

    print("Loading sweep data...")
    rows = load_sweep_data()
    print(f"  {len(rows)} total rows")

    print("Analyzing negation sweep...")
    analysis = analyze_negation_sweep(rows)
    print(f"  {analysis['total_negated']} negated sims across {analysis['total_fields_with_negation']} fields")
    print(f"  {len(analysis['gate_passers'])} gate-passers (S >= 1.0)")
    print(f"  {len(analysis['strong_passers'])} strong (S >= 1.25)")
    print(f"  {len(analysis['negation_winners'])} negation-dominant fields")

    print("Loading book fields...")
    book_fields = load_book_fields()
    print(f"  {len(book_fields)} fields in book")

    print("Generating report...")
    report = format_report(analysis, book_fields)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report)
    print(f"\nReport written to: {output_path}")
    print(f"  Total gate-passers: {len(analysis['gate_passers'])}")
    print(f"  Strong passers (S >= 1.25): {len(analysis['strong_passers'])}")
    print(f"  Negation-dominant fields: {len(analysis['negation_winners'])}")
    actionable = [w for w in analysis['negation_winners'] if not w['is_dead_zone'] and w['field'] not in book_fields]
    print(f"  Actionable building blocks: {len(actionable)}")


if __name__ == "__main__":
    main()
