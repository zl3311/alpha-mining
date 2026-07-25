"""
Query the HF submission queue server for simulation results.

Usage:
    uv run python3 scripts/hf_query.py --stats
    uv run python3 scripts/hf_query.py --gate-passers
    uv run python3 scripts/hf_query.py --gate-passers --min-fitness 1.5
    uv run python3 scripts/hf_query.py --gate-passers --self-corr-check
    uv run python3 scripts/hf_query.py --new-24h
    uv run python3 scripts/hf_query.py --sql "SELECT j.expression, r.sharpe FROM ..."
"""

import argparse
import json
import os
import sys

import httpx
from dotenv import load_dotenv

load_dotenv()

HF_URL = os.environ.get("HF_SERVER_URL", "").rstrip("/")
HF_API_KEY = os.environ.get("HF_API_KEY", "")
HF_TOKEN = os.environ.get("HF_TOKEN", "")

HEADERS = {"Authorization": f"Bearer {HF_TOKEN}", "X-API-Key": HF_API_KEY}

_NO_SERVER_URL = (
    "HF_SERVER_URL is not set. Copy .env.example to .env and point it at your own "
    "deployment of the submission queue server (see server/)."
)

SELF_CORR_SAFE = 0.60
SELF_CORR_BLOCKED = 0.70


def query(sql: str) -> dict:
    r = httpx.get(f"{HF_URL}/v1/db/query", params={"sql": sql}, headers=HEADERS, timeout=15.0)
    return r.json()


def build_tag_clause(tag: str | None) -> str:
    """Build an optional SQL AND-clause filtering jobs by a tag substring."""
    if not tag:
        return ""
    return f" AND j.tags_json LIKE '%{tag}%'"


def _self_corr_verdict(value: float) -> str:
    if value < SELF_CORR_SAFE:
        return "SAFE"
    if value < SELF_CORR_BLOCKED:
        return "RISKY"
    return "BLOCKED"


def main():
    if not HF_URL:
        sys.exit(_NO_SERVER_URL)

    parser = argparse.ArgumentParser(description="Query HF submission queue server")
    parser.add_argument("--stats", action="store_true", help="Show server stats")
    parser.add_argument("--gate-passers", action="store_true", help="All results with S>=1.0, F>=0.8")
    parser.add_argument("--min-fitness", type=float, default=0.8, help="Min fitness for gate-passers (default 0.8)")
    parser.add_argument("--min-sharpe", type=float, default=1.0, help="Min sharpe for gate-passers (default 1.0)")
    parser.add_argument("--new-24h", action="store_true", help="Results from last 24 hours")
    parser.add_argument("--tag", help="Filter --gate-passers/--new-24h by a tag in tags_json")
    parser.add_argument("--self-corr-check", action="store_true",
                        help="With --gate-passers: filter out BLOCKED, show verdicts")
    parser.add_argument("--sql", help="Run arbitrary SQL query")
    parser.add_argument("--limit", type=int, default=50, help="Max results (default 50)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    args = parser.parse_args()

    if args.self_corr_check and not args.gate_passers:
        print("ERROR: --self-corr-check requires --gate-passers", file=sys.stderr)
        sys.exit(1)

    tag_clause = build_tag_clause(args.tag)
    has_self_corr_col = False

    if args.stats:
        r = httpx.get(f"{HF_URL}/v1/stats", headers=HEADERS, timeout=10.0)
        d = r.json()
        print(json.dumps(d, indent=2) if args.json else
              f"Results: {d['total_results']}, Pending: {d['pending_jobs']}, "
        f"Budget: {d['daily_budget_remaining']}, Worker: {d['worker_status']}")
        return

    if args.sql:
        data = query(args.sql)
    elif args.new_24h:
        data = query(f"""
            SELECT j.expression, r.sharpe, r.fitness, r.turnover, r.grade, r.alpha_id
            FROM jobs j JOIN results r ON r.job_id = j.id
            WHERE r.sharpe >= {args.min_sharpe} AND j.completed_at > datetime('now', '-24 hours'){tag_clause}
            ORDER BY r.fitness DESC LIMIT {args.limit}
        """)
    elif args.gate_passers:
        has_self_corr_col = True
        data = query(f"""
            SELECT j.expression, r.sharpe, r.fitness, r.turnover, r.grade, r.alpha_id, j.self_corr, j.corr_result
            FROM jobs j JOIN results r ON r.job_id = j.id
            WHERE r.sharpe >= {args.min_sharpe} AND r.fitness >= {args.min_fitness}{tag_clause}
            ORDER BY r.fitness DESC LIMIT {args.limit}
        """)
    else:
        parser.print_help()
        return

    rows = data.get("rows", [])

    if args.self_corr_check and has_self_corr_col:
        rows = [r for r in rows if not (
            (len(r) >= 8 and r[7] == "FAIL")
            or (len(r) < 8 or r[7] is None) and (len(r) >= 7 and r[6] is not None and r[6] >= 0.7)
        )]

    if args.json:
        data["rows"] = rows
        print(json.dumps(data, indent=2))
        return

    if not rows:
        print("No results.")
        return

    print(f"{len(rows)} results:")

    if args.sql:
        cols = data.get("columns", [])
        for row in rows:
            if cols:
                print("  " + " | ".join(f"{c}={row[i]}" for i, c in enumerate(cols)))
            else:
                print(f"  {row}")
        return

    for row in rows:
        if len(row) < 5:
            print(f"  {row}")
            continue

        expr = (row[0] or "")[:70]
        sharpe = row[1] if row[1] is not None else 0.0
        fitness = row[2] if row[2] is not None else 0.0
        turnover = row[3] if row[3] is not None else 0.0
        grade = row[4] or "?"

        corr_str = ""
        brain_verdict = row[7] if len(row) >= 8 else None
        if brain_verdict:
            corr_val = f"{row[6]:.3f}" if row[6] is not None else "?"
            corr_str = f" corr={corr_val}({brain_verdict})"
        elif has_self_corr_col and len(row) >= 7 and row[6] is not None:
            corr_str = f" corr={row[6]:.3f}({_self_corr_verdict(row[6])})"
        elif has_self_corr_col and args.self_corr_check:
            corr_str = " corr=?(UNCHECKED)"

        print(f"  {grade:>10} S={sharpe:>5.2f} F={fitness:>5.2f} T={turnover*100:>5.1f}%{corr_str}  {expr}")


if __name__ == "__main__":
    main()
