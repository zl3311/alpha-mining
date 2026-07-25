"""Poll the HF submission queue for a tagged batch until all jobs are terminal.

Replaces ad-hoc heredoc poll loops. Given a session/batch tag, this repeatedly
queries the HF server for all jobs whose `tags_json` contains the tag, prints a
status summary each interval, and exits when every job reaches a terminal state
(`done`, `failed`, `failed_permanent`).

It also flags STALE jobs: a job stuck in `running`/`submitted` longer than
`--stale-min` minutes. This catches the failure mode where the server leaves a
job mid-poll (e.g. a BRAIN WARNING/unit error) and never marks it terminal. The
flag is advisory; with the worker fix (terminal WARNING handling) stale jobs
should not occur, but the detector remains a safety net.

Usage:
    uv run python3 scripts/hf_poll.py --tag 20260604-001
    uv run python3 scripts/hf_poll.py --tag zscore_r3 --interval 60 --stale-min 12
    uv run python3 scripts/hf_poll.py --tag 20260604-001 --max-polls 45 --json

Exit codes:
    0  all jobs terminal (batch complete)
    2  timed out (--max-polls reached with jobs still active)
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

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

# Terminal: simulation finished. The worker promotes gate-passers from `done` to
# `corr_checked` after BRAIN self-correlation — both must count as complete.
TERMINAL_STATUSES = ("done", "corr_checked", "failed", "failed_permanent")
COMPLETED_STATUSES = ("done", "corr_checked")
ACTIVE_STATUSES = ("pending", "running", "submitted", "corr_checking")

GATE_MIN_SHARPE = 1.25
GATE_MIN_FITNESS = 1.0
GATE_MIN_TURNOVER = 0.01
GATE_MAX_TURNOVER = 0.70


def minutes_since(iso_ts: str | None, now: datetime | None = None) -> float:
    """Return minutes elapsed since an ISO-8601 timestamp.

    Args:
        iso_ts: ISO timestamp string (may include trailing 'Z'); None/empty -> 0.
        now: Reference time (defaults to current UTC). Injected for testing.

    Returns:
        Elapsed minutes as a float; 0.0 when the timestamp is missing or invalid.
    """
    if not iso_ts:
        return 0.0
    now = now or datetime.now(timezone.utc)
    try:
        started = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return 0.0
    if started.tzinfo is None:
        started = started.replace(tzinfo=timezone.utc)
    return (now - started).total_seconds() / 60.0


def is_stale(job: dict, stale_min: float, now: datetime | None = None) -> bool:
    """Decide whether a job is stuck in a non-terminal running state.

    A job is stale when it is in `running`/`submitted` AND its `started_at` is
    older than `stale_min` minutes. Pending jobs are never stale (they are just
    queued behind the backlog).

    Args:
        job: Job row mapping with `status` and `started_at` keys.
        stale_min: Threshold in minutes.
        now: Reference time (defaults to current UTC). Injected for testing.

    Returns:
        True if the job should be treated as stale.
    """
    if job.get("status") not in ("running", "submitted"):
        return False
    return minutes_since(job.get("started_at"), now=now) > stale_min


def is_gate_passer(job: dict) -> bool:
    """Return True if a completed job's metrics clear the submission gates.

    Gates: Sharpe >= 1.25, Fitness >= 1.0, turnover within [1%, 70%].

    Args:
        job: Job row mapping with `sharpe`, `fitness`, `turnover` keys.

    Returns:
        True when all gate thresholds are satisfied.
    """
    s = job.get("sharpe")
    f = job.get("fitness")
    t = job.get("turnover")
    if s is None or f is None or t is None:
        return False
    return (
        s >= GATE_MIN_SHARPE
        and f >= GATE_MIN_FITNESS
        and GATE_MIN_TURNOVER <= t <= GATE_MAX_TURNOVER
    )


def summarize(jobs: list[dict], stale_min: float, now: datetime | None = None) -> dict:
    """Aggregate a batch of job rows into counts and derived flags.

    Args:
        jobs: List of job row mappings.
        stale_min: Stale threshold in minutes.
        now: Reference time (defaults to current UTC). Injected for testing.

    Returns:
        Mapping with keys: total, done, failed, active, pending, running,
        stale (count), complete (bool: all jobs terminal), gate_passers (list).
    """
    counts = {"done": 0, "failed": 0, "pending": 0, "running": 0, "submitted": 0,
              "corr_checking": 0}
    stale = 0
    for j in jobs:
        st = j.get("status", "")
        if st == "failed_permanent":
            counts["failed"] += 1
        elif st in COMPLETED_STATUSES:
            counts["done"] += 1
        elif st in counts:
            counts[st] += 1
        if is_stale(j, stale_min, now=now):
            stale += 1
    active = (
        counts["pending"] + counts["running"] + counts["submitted"]
        + counts["corr_checking"]
    )
    gate_passers = [
        j for j in jobs if j.get("status") in COMPLETED_STATUSES and is_gate_passer(j)
    ]
    return {
        "total": len(jobs),
        "done": counts["done"],
        "failed": counts["failed"],
        "pending": counts["pending"],
        "running": counts["running"] + counts["submitted"] + counts["corr_checking"],
        "active": active,
        "stale": stale,
        "complete": len(jobs) > 0 and active == 0,
        "gate_passers": gate_passers,
    }


def fetch_jobs(tag: str) -> list[dict]:
    """Query the HF server for all jobs whose tags contain `tag`.

    Args:
        tag: Substring matched against `jobs.tags_json`.

    Returns:
        List of job row mappings joined with their result metrics.
    """
    sql = f"""
        SELECT j.id, j.expression, j.status, j.started_at, j.created_at,
               r.sharpe, r.fitness, r.turnover, r.grade, r.alpha_id
        FROM jobs j LEFT JOIN results r ON r.job_id = j.id
        WHERE j.tags_json LIKE '%{tag}%'
        ORDER BY j.created_at
    """
    r = httpx.get(f"{HF_URL}/v1/db/query", params={"sql": sql}, headers=HEADERS, timeout=30.0)
    data = r.json()
    cols = data.get("columns", [])
    return [dict(zip(cols, row)) for row in data.get("rows", [])]


def print_gate_passers(gate_passers: list[dict]) -> None:
    """Print a ranked table of gate-passing jobs (highest fitness first)."""
    if not gate_passers:
        print("\nNo gate-passers (S>=1.25, F>=1.0).")
        return
    print(f"\nGATE-PASSERS ({len(gate_passers)}):")
    for j in sorted(gate_passers, key=lambda x: x.get("fitness", 0), reverse=True):
        expr = (j.get("expression") or "")[:70]
        print(
            f"  {j.get('grade', '?'):>10} S={j.get('sharpe', 0):.2f} "
            f"F={j.get('fitness', 0):.2f} T={(j.get('turnover') or 0) * 100:.1f}% "
            f"{j.get('alpha_id', '?')}  {expr}"
        )


def main() -> None:
    """CLI entry point: poll the tagged batch until terminal or timed out."""
    if not HF_URL:
        sys.exit(_NO_SERVER_URL)

    parser = argparse.ArgumentParser(description="Poll HF queue for a tagged batch")
    parser.add_argument("--tag", required=True, help="Session/batch tag to match in tags_json")
    parser.add_argument("--interval", type=int, default=60, help="Seconds between polls (def 60)")
    parser.add_argument("--stale-min", type=float, default=12.0,
                        help="Flag running jobs older than this many minutes (default 12)")
    parser.add_argument("--max-polls", type=int, default=45, help="Max poll iterations (def 45)")
    parser.add_argument("--json", action="store_true", help="Emit final summary as JSON")
    args = parser.parse_args()

    print(f"=== Polling tag '{args.tag}' every {args.interval}s (stale>{args.stale_min:.0f}m) ===",
          flush=True)

    for i in range(1, args.max_polls + 1):
        jobs = fetch_jobs(args.tag)
        s = summarize(jobs, args.stale_min)
        ts = time.strftime("%H:%M:%S")
        print(
            f"[{ts}] #{i}: done={s['done']}/{s['total']} running={s['running']} "
            f"pending={s['pending']} failed={s['failed']} stale={s['stale']}",
            flush=True,
        )
        for j in jobs:
            if is_stale(j, args.stale_min):
                mins = minutes_since(j.get("started_at"))
                print(f"  STALE {mins:.0f}m: {(j.get('expression') or '')[:60]}", flush=True)

        if s["complete"]:
            print("\n=== BATCH COMPLETE ===", flush=True)
            print_gate_passers(s["gate_passers"])
            if args.json:
                out = {
                    "tag": args.tag,
                    "total": s["total"],
                    "done": s["done"],
                    "failed": s["failed"],
                    "gate_passers": [
                        {"alpha_id": j.get("alpha_id"), "sharpe": j.get("sharpe"),
                         "fitness": j.get("fitness"), "grade": j.get("grade"),
                         "expression": j.get("expression")}
                        for j in s["gate_passers"]
                    ],
                }
                print(json.dumps(out, indent=2))
            sys.exit(0)

        if i < args.max_polls:
            time.sleep(args.interval)

    print(f"\n=== TIMEOUT after {args.max_polls} polls; jobs still active ===", flush=True)
    sys.exit(2)


if __name__ == "__main__":
    main()
