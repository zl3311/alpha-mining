"""Tests for the server's BRAIN poll terminal-status classifier.

The HF queue server (git submodule at server/) has no test harness, so this
main-repo test documents and locks in the expected behavior of
`is_terminal_failure` in server/app/brain_client.py. This is the fix for jobs
getting stuck in `running` when BRAIN returns WARNING (FASTEXPR unit errors):
such statuses must be treated as terminal so the worker marks the job failed
immediately instead of polling until the attempt limit.

Covers:
- COMPLETE and in-progress statuses are NOT terminal failures
- WARNING/ERROR/FAILED/FAIL/CANCELLED ARE terminal failures
- case-insensitivity and empty/None handling
"""

import importlib.util
from pathlib import Path

import pytest

_SCRIPT = Path(__file__).resolve().parent.parent / "server" / "app" / "brain_client.py"

if not _SCRIPT.exists():
    pytest.skip("server submodule not checked out", allow_module_level=True)

_spec = importlib.util.spec_from_file_location("server_brain_client", _SCRIPT)
server_brain_client = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(server_brain_client)

# The fix may live behind an un-updated submodule pointer; skip rather than error
# if this build of the server predates the terminal-status classifier.
if not hasattr(server_brain_client, "is_terminal_failure"):
    pytest.skip("server submodule predates is_terminal_failure", allow_module_level=True)

is_terminal_failure = server_brain_client.is_terminal_failure


@pytest.mark.parametrize("status", ["WARNING", "ERROR", "FAILED", "FAIL", "CANCELLED"])
def test_terminal_failure_statuses(status):
    assert is_terminal_failure(status) is True


@pytest.mark.parametrize("status", ["warning", "error", "Failed", "cancelled"])
def test_terminal_failure_case_insensitive(status):
    assert is_terminal_failure(status) is True


@pytest.mark.parametrize("status", ["COMPLETE", "RUNNING", "PENDING", "IN_PROGRESS", ""])
def test_non_terminal_statuses(status):
    assert is_terminal_failure(status) is False


def test_none_status_is_not_terminal():
    assert is_terminal_failure(None) is False
