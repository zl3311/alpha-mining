"""Tests for scripts/brain_metadata.py and the PATCH payload it relies on.

Covers:
- _parse_frontmatter: valid, no-frontmatter, malformed YAML
- _metadata_from_book: name/tags/description extraction and description fallback
- BrainClient.set_alpha_properties: PATCH payload shape (the wire contract this
  script depends on), including the regular.description nesting and tag/name keys
"""

import importlib.util
from pathlib import Path

import pytest

from alpha_mining.brain.client import BrainClient
from alpha_mining.config import Settings

_SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "brain_metadata.py"
_spec = importlib.util.spec_from_file_location("brain_metadata", _SCRIPT)
brain_metadata = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(brain_metadata)


# ---------------------------------------------------------------------------
# _parse_frontmatter
# ---------------------------------------------------------------------------

def test_parse_frontmatter_valid(tmp_path):
    p = tmp_path / "a.md"
    p.write_text('---\nalpha_id: "ABC"\ntags:\n  - x\n  - y\n---\nbody')
    fm = brain_metadata._parse_frontmatter(p)
    assert fm["alpha_id"] == "ABC"
    assert fm["tags"] == ["x", "y"]


def test_parse_frontmatter_no_frontmatter(tmp_path):
    p = tmp_path / "b.md"
    p.write_text("# just a heading\nno frontmatter")
    assert brain_metadata._parse_frontmatter(p) == {}


def test_parse_frontmatter_malformed(tmp_path):
    p = tmp_path / "c.md"
    p.write_text("---\nbad: : : yaml\n  - broken\n---\nbody")
    # Malformed YAML must not raise; returns {}.
    assert brain_metadata._parse_frontmatter(p) == {}


# ---------------------------------------------------------------------------
# _metadata_from_book
# ---------------------------------------------------------------------------

def test_metadata_from_book_full(tmp_path):
    p = tmp_path / "vRm07LP3.md"
    p.write_text(
        '---\n'
        'alpha_id: "vRm07LP3"\n'
        'name: "iv_spread_zscore"\n'
        'tags:\n  - options\n  - iv_spread\n'
        'description: "Pure options IV spread"\n'
        'family: "options_iv_spread"\n'
        'expression: "ts_decay_linear(zscore(x), 10)"\n'
        '---\nbody'
    )
    name, tags, desc = brain_metadata._metadata_from_book(p)
    assert name == "iv_spread_zscore"
    assert tags == ["options", "iv_spread"]
    assert desc == "Pure options IV spread"


def test_metadata_from_book_description_fallback(tmp_path):
    # No explicit description -> fall back to "family | expression".
    p = tmp_path / "x.md"
    p.write_text(
        '---\n'
        'alpha_id: "X1"\n'
        'family: "options_iv_spread"\n'
        'expression: "rank(close)"\n'
        '---\nbody'
    )
    name, tags, desc = brain_metadata._metadata_from_book(p)
    assert name == ""
    assert tags == []
    assert desc == "options_iv_spread | rank(close)"


def test_metadata_from_book_empty_when_no_fields(tmp_path):
    p = tmp_path / "y.md"
    p.write_text('---\nalpha_id: "Y1"\n---\nbody')
    name, tags, desc = brain_metadata._metadata_from_book(p)
    assert (name, tags, desc) == ("", [], "")


# ---------------------------------------------------------------------------
# PATCH payload shape (the wire contract brain_metadata depends on)
# ---------------------------------------------------------------------------

class _FakeResponse:
    def __init__(self, status_code=200, payload=None):
        self.status_code = status_code
        self._payload = payload or {}
        self.text = ""

    def json(self):
        return self._payload


class _RecordingClient:
    """Minimal stand-in for httpx.AsyncClient capturing the PATCH call."""

    def __init__(self, response):
        self._response = response
        self.calls = []

    async def patch(self, url, json=None):
        self.calls.append({"url": url, "json": json})
        return self._response


def _client_with(response) -> BrainClient:
    settings = Settings()
    client = BrainClient(settings)
    client._authenticated = True  # skip network auth
    client._client = _RecordingClient(response)
    return client


@pytest.mark.asyncio
async def test_set_properties_payload_has_name_and_tags():
    resp = _FakeResponse(200, {"id": "ABC", "name": "n", "tags": ["a", "b"]})
    client = _client_with(resp)
    await client.set_alpha_properties("ABC", name="n", tags=["a", "b"])
    call = client._client.calls[0]
    assert call["url"].endswith("/ABC")
    assert call["json"]["name"] == "n"
    assert call["json"]["tags"] == ["a", "b"]


@pytest.mark.asyncio
async def test_set_properties_description_nested_under_regular():
    resp = _FakeResponse(200, {"id": "ABC"})
    client = _client_with(resp)
    await client.set_alpha_properties("ABC", description="why it works")
    payload = client._client.calls[0]["json"]
    assert payload["regular"] == {"description": "why it works"}


@pytest.mark.asyncio
async def test_set_properties_omits_unset_fields():
    resp = _FakeResponse(200, {"id": "ABC"})
    client = _client_with(resp)
    await client.set_alpha_properties("ABC", name="only-name")
    payload = client._client.calls[0]["json"]
    assert "name" in payload
    assert "tags" not in payload
    assert "regular" not in payload


@pytest.mark.asyncio
async def test_set_properties_error_on_non_200():
    resp = _FakeResponse(400, {})
    client = _client_with(resp)
    result = await client.set_alpha_properties("ABC", name="n")
    assert "error" in result
    assert result["error"] == 400
