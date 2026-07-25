"""Tests for scripts/hf_poll.py pure logic (no live server).

Covers brute-force combinations of:
- minutes_since: valid/invalid/empty timestamps, tz-aware and naive
- is_stale: every status x age combination around the threshold
- is_gate_passer: gate boundary conditions on sharpe/fitness/turnover, NULLs
- summarize: batch aggregation, completion detection, stale counting
"""

import importlib.util
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "hf_poll.py"
_spec = importlib.util.spec_from_file_location("hf_poll", _SCRIPT)
hf_poll = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(hf_poll)


NOW = datetime(2026, 6, 5, 0, 0, 0, tzinfo=timezone.utc)


def _ago(minutes: float) -> str:
    return (NOW - timedelta(minutes=minutes)).isoformat()


# ---------------------------------------------------------------------------
# minutes_since
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("missing", [None, ""])
def test_minutes_since_missing_returns_zero(missing):
    assert hf_poll.minutes_since(missing, now=NOW) == 0.0


def test_minutes_since_invalid_returns_zero():
    assert hf_poll.minutes_since("not-a-timestamp", now=NOW) == 0.0


@pytest.mark.parametrize("mins", [1, 5, 12, 30, 120])
def test_minutes_since_elapsed(mins):
    got = hf_poll.minutes_since(_ago(mins), now=NOW)
    assert got == pytest.approx(mins, abs=0.01)


def test_minutes_since_handles_trailing_z():
    ts = (NOW - timedelta(minutes=10)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert hf_poll.minutes_since(ts, now=NOW) == pytest.approx(10, abs=0.5)


def test_minutes_since_naive_timestamp_assumes_utc():
    naive = (NOW - timedelta(minutes=15)).replace(tzinfo=None).isoformat()
    assert hf_poll.minutes_since(naive, now=NOW) == pytest.approx(15, abs=0.01)


# ---------------------------------------------------------------------------
# is_stale -- status x age matrix
# ---------------------------------------------------------------------------

ALL_STATUSES = ["pending", "running", "submitted", "done", "failed", "failed_permanent"]


@pytest.mark.parametrize("status", ALL_STATUSES)
@pytest.mark.parametrize("age", [0, 5, 11, 13, 30])
def test_is_stale_matrix(status, age):
    job = {"status": status, "started_at": _ago(age)}
    got = hf_poll.is_stale(job, stale_min=12.0, now=NOW)
    expected = status in ("running", "submitted") and age > 12.0
    assert got is expected


def test_is_stale_pending_never_stale_even_if_old():
    job = {"status": "pending", "started_at": _ago(999)}
    assert hf_poll.is_stale(job, stale_min=12.0, now=NOW) is False


def test_is_stale_running_no_started_at_not_stale():
    job = {"status": "running", "started_at": None}
    assert hf_poll.is_stale(job, stale_min=12.0, now=NOW) is False


# ---------------------------------------------------------------------------
# is_gate_passer -- boundary conditions
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("sharpe,fitness,turnover,expected", [
    (1.25, 1.0, 0.05, True),     # exact thresholds
    (1.24, 1.0, 0.05, False),    # sharpe just below
    (1.25, 0.99, 0.05, False),   # fitness just below
    (1.5, 2.0, 0.009, False),    # turnover below min
    (1.5, 2.0, 0.71, False),     # turnover above max
    (1.5, 2.0, 0.01, True),      # turnover at min
    (1.5, 2.0, 0.70, True),      # turnover at max
    (2.0, 2.5, 0.05, True),      # comfortably inside
])
def test_is_gate_passer_boundaries(sharpe, fitness, turnover, expected):
    job = {"sharpe": sharpe, "fitness": fitness, "turnover": turnover}
    assert hf_poll.is_gate_passer(job) is expected


@pytest.mark.parametrize("job", [
    {"sharpe": None, "fitness": 2.0, "turnover": 0.05},
    {"sharpe": 2.0, "fitness": None, "turnover": 0.05},
    {"sharpe": 2.0, "fitness": 2.0, "turnover": None},
    {},
])
def test_is_gate_passer_null_metrics(job):
    assert hf_poll.is_gate_passer(job) is False


# ---------------------------------------------------------------------------
# summarize
# ---------------------------------------------------------------------------

def test_summarize_empty_not_complete():
    s = hf_poll.summarize([], stale_min=12.0, now=NOW)
    assert s["total"] == 0
    assert s["complete"] is False


def test_summarize_all_terminal_is_complete():
    jobs = [
        {"status": "done", "sharpe": 2.0, "fitness": 2.0, "turnover": 0.05, "started_at": _ago(5)},
        {"status": "failed", "started_at": _ago(5)},
        {"status": "failed_permanent", "started_at": _ago(5)},
    ]
    s = hf_poll.summarize(jobs, stale_min=12.0, now=NOW)
    assert s["complete"] is True
    assert s["done"] == 1
    assert s["failed"] == 2
    assert s["active"] == 0
    assert len(s["gate_passers"]) == 1


def test_summarize_active_blocks_completion():
    jobs = [
        {"status": "done", "sharpe": 1.0, "fitness": 1.0, "turnover": 0.05, "started_at": _ago(5)},
        {"status": "running", "started_at": _ago(2)},
    ]
    s = hf_poll.summarize(jobs, stale_min=12.0, now=NOW)
    assert s["complete"] is False
    assert s["running"] == 1
    assert s["active"] == 1


def test_summarize_counts_stale():
    jobs = [
        {"status": "running", "started_at": _ago(20)},   # stale
        {"status": "running", "started_at": _ago(2)},    # fresh
        {"status": "submitted", "started_at": _ago(30)}, # stale
        {"status": "pending", "started_at": _ago(99)},   # never stale
    ]
    s = hf_poll.summarize(jobs, stale_min=12.0, now=NOW)
    assert s["stale"] == 2


def test_summarize_corr_checked_counts_as_done():
    jobs = [
        {"status": "corr_checked", "sharpe": 2.0, "fitness": 2.0, "turnover": 0.05,
         "started_at": _ago(5)},
        {"status": "running", "started_at": _ago(2)},
    ]
    s = hf_poll.summarize(jobs, stale_min=12.0, now=NOW)
    assert s["done"] == 1
    assert s["complete"] is False
    assert len(s["gate_passers"]) == 1


def test_summarize_all_corr_checked_is_complete():
    jobs = [
        {"status": "corr_checked", "sharpe": 2.0, "fitness": 2.0, "turnover": 0.05,
         "started_at": _ago(5)},
        {"status": "failed", "started_at": _ago(5)},
    ]
    s = hf_poll.summarize(jobs, stale_min=12.0, now=NOW)
    assert s["complete"] is True
    assert s["done"] == 1
    assert s["failed"] == 1


def test_summarize_gate_passers_only_done():
    # A high-metric row that is still running must NOT count as a gate-passer.
    jobs = [
        {"status": "running", "sharpe": 3.0, "fitness": 3.0, "turnover": 0.05,
         "started_at": _ago(1)},
        {"status": "done", "sharpe": 1.5, "fitness": 1.5, "turnover": 0.05,
         "started_at": _ago(5)},
    ]
    s = hf_poll.summarize(jobs, stale_min=12.0, now=NOW)
    # not complete (one running), but gate_passers reflects only the done row
    assert len(s["gate_passers"]) == 1
    assert s["gate_passers"][0]["sharpe"] == 1.5
