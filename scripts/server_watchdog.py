"""
Watchdog for the HF submission queue server.

Periodically checks server health and restarts the Space if stuck.
Run as a background process or cron job.

Usage:
    uv run python3 scripts/server_watchdog.py                    # Check once
    uv run python3 scripts/server_watchdog.py --loop --interval 3600  # Check every hour
    uv run python3 scripts/server_watchdog.py --restart           # Force restart now
"""

import argparse
import os
import sys
import time

import httpx
from dotenv import load_dotenv

load_dotenv()

HF_URL = os.environ.get("HF_SERVER_URL", "").rstrip("/")
HF_API_KEY = os.environ.get("HF_API_KEY", "")
HF_TOKEN = os.environ.get("HF_TOKEN", "")
SPACE_ID = os.environ.get("SPACE_ID", "")

HEADERS = {"Authorization": f"Bearer {HF_TOKEN}", "X-API-Key": HF_API_KEY}

_NO_SERVER_URL = (
    "HF_SERVER_URL is not set. Copy .env.example to .env and point it at your own "
    "deployment of the submission queue server (see server/)."
)


def check_health() -> dict:
    try:
        r = httpx.get(f"{HF_URL}/health", timeout=15.0)
        if r.status_code != 200:
            return {"healthy": False, "reason": f"HTTP {r.status_code}"}
        return {"healthy": True, **r.json()}
    except httpx.ConnectError:
        return {"healthy": False, "reason": "Connection refused (Space may be sleeping)"}
    except httpx.TimeoutException:
        return {"healthy": False, "reason": "Timeout (Space may be unresponsive)"}
    except Exception as e:
        return {"healthy": False, "reason": str(e)}


def check_stats() -> dict | None:
    try:
        r = httpx.get(f"{HF_URL}/v1/stats", headers=HEADERS, timeout=15.0)
        if r.status_code == 200:
            return r.json()
    except Exception:
        pass
    return None


def restart_space() -> dict:
    if not SPACE_ID:
        return {"restarted": False, "error": "SPACE_ID is not set; cannot restart the Space"}
    try:
        r = httpx.post(
            f"https://huggingface.co/api/spaces/{SPACE_ID}/restart",
            headers={"Authorization": f"Bearer {HF_TOKEN}"},
            timeout=30.0,
        )
        if r.status_code == 200:
            return {"restarted": True}
        return {"restarted": False, "error": f"HTTP {r.status_code}: {r.text[:200]}"}
    except Exception as e:
        return {"restarted": False, "error": str(e)}


def should_restart(health: dict, stats: dict | None, stale_minutes: int = 30) -> tuple[bool, str]:
    if not health["healthy"]:
        return True, f"Unhealthy: {health.get('reason', 'unknown')}"

    if health.get("worker") == "stopped":
        return True, "Worker stopped"

    if stats:
        uptime = stats.get("uptime_seconds", 0)
        if uptime > 86400:
            return True, f"Uptime {uptime/3600:.1f}h (>24h), proactive restart"

        pending = stats.get("pending_jobs", 0)
        worker_status = stats.get("worker_status", "")

        if pending > 0 and worker_status in ("paused_backoff", "rate_limited"):
            return True, f"Worker {worker_status} with {pending} pending jobs"

        last_success = stats.get("last_successful_job_at")
        if pending > 0 and last_success:
            from datetime import datetime, timezone
            try:
                last_dt = datetime.fromisoformat(last_success.replace("Z", "+00:00"))
                elapsed = (datetime.now(timezone.utc) - last_dt).total_seconds()
                if elapsed > stale_minutes * 60:
                    return True, (
                        f"Stale: {pending} pending but last success was "
                        f"{elapsed/60:.0f}m ago (threshold {stale_minutes}m)"
                    )
            except (ValueError, TypeError):
                pass

        total_failed = stats.get("total_failed", 0)
        total_results = stats.get("total_results", 0)
        if total_results > 0 and total_failed > 0:
            fail_rate = total_failed / (total_results + total_failed)
            sims_today = stats.get("sims_today", 0)
            if sims_today > 10 and fail_rate > 0.5:
                return True, (f"High failure rate: {fail_rate:.0%} ({total_failed} failed / "
                      f"{total_results + total_failed} total today)")

    return False, "OK"


def run_check(force_restart: bool = False) -> None:
    now = time.strftime("%Y-%m-%d %H:%M:%S")

    health = check_health()
    stats = check_stats()

    status_line = f"[{now}] "
    if health["healthy"]:
        uptime = health.get("uptime_seconds", 0)
        status_line += f"UP ({uptime/3600:.1f}h) worker={health.get('worker', '?')}"
        if stats:
            status_line += (f" pending={stats.get('pending_jobs', '?')}"
                        f" done={stats.get('total_results', '?')}"
                        f" budget={stats.get('daily_budget_remaining', '?')}")
    else:
        status_line += f"DOWN: {health.get('reason', '?')}"

    print(status_line)

    need_restart, reason = should_restart(health, stats)
    if force_restart:
        need_restart = True
        reason = "Forced by user"

    if need_restart:
        print(f"  -> Restarting: {reason}")
        result = restart_space()
        if result.get("restarted"):
            print("  -> Restart initiated. Space will be back in ~30-60s.")
        else:
            print(f"  -> Restart failed: {result.get('error', '?')}")
    else:
        print(f"  -> {reason}")


def main():
    if not HF_URL:
        sys.exit(_NO_SERVER_URL)

    parser = argparse.ArgumentParser(description="HF server watchdog")
    parser.add_argument("--loop", action="store_true", help="Run continuously")
    parser.add_argument("--interval", type=int, default=3600, help="Check interval in seconds (default 3600 = 1h)")
    parser.add_argument("--restart", action="store_true", help="Force restart now")
    args = parser.parse_args()

    if args.loop:
        print(f"Watchdog running. Checking every {args.interval}s. Ctrl+C to stop.")
        while True:
            run_check()
            time.sleep(args.interval)
    else:
        run_check(force_restart=args.restart)


if __name__ == "__main__":
    main()
