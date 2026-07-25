"""
Tests for the redesigned storage layer.

Covers the full workflow lineage: sessions -> papers (M2M) -> hypotheses -> alphas -> simulations -> results.
Includes FTS5 search, hypothesis management, and stats.
"""

from pathlib import Path

import pytest
import pytest_asyncio

from alpha_mining.storage.db import AlphaDB, expression_hash
from alpha_mining.storage.models import (
    AlphaRecord,
    PaperImageRecord,
    PaperRecord,
    ResultRecord,
    SessionRecord,
    SimulationRecord,
)

_TEST_DB = Path("/tmp/test_alpha_mining_v2.db")


@pytest_asyncio.fixture
async def db():
    if _TEST_DB.exists():
        _TEST_DB.unlink()
    async with AlphaDB(_TEST_DB) as database:
        yield database
    if _TEST_DB.exists():
        _TEST_DB.unlink()


# ---------------------------------------------------------------------------
# Sessions
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_create_session(db):
    sid, eid = await db.create_session(SessionRecord(source="cursor", name="test"))
    assert sid == 1
    assert eid.startswith("sess_")


@pytest.mark.asyncio
async def test_get_session(db):
    _, eid = await db.create_session(SessionRecord(source="manual", name="my-session"))
    sess = await db.get_session(eid)
    assert sess is not None
    assert sess["source"] == "manual"
    assert sess["name"] == "my-session"


@pytest.mark.asyncio
async def test_get_session_not_found(db):
    result = await db.get_session("sess_0_000000")
    assert result is None


# ---------------------------------------------------------------------------
# Papers
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_insert_paper(db):
    pid, eid = await db.insert_paper(PaperRecord(title="101 Formulaic Alphas"))
    assert pid == 1
    assert eid.startswith("paper_")


@pytest.mark.asyncio
async def test_get_paper(db):
    _, eid = await db.insert_paper(PaperRecord(title="Test Paper", source_url="https://arxiv.org"))
    paper = await db.get_paper(eid)
    assert paper is not None
    assert paper["title"] == "Test Paper"


@pytest.mark.asyncio
async def test_list_papers(db):
    await db.insert_paper(PaperRecord(title="Paper A"))
    await db.insert_paper(PaperRecord(title="Paper B"))
    papers = await db.list_papers()
    assert len(papers) == 2


@pytest.mark.asyncio
async def test_search_papers(db):
    await db.insert_paper(PaperRecord(
        title="Momentum Reversal in Equities",
        extracted_markdown="This paper studies short-term momentum reversal effects...",
    ))
    await db.insert_paper(PaperRecord(
        title="Value Factor Analysis",
        extracted_markdown="Fundamental value signals predict returns...",
    ))
    results = await db.search_papers("momentum reversal")
    assert len(results) >= 1
    assert "Momentum" in results[0]["title"]


@pytest.mark.asyncio
async def test_search_papers_no_match(db):
    await db.insert_paper(PaperRecord(title="Test", extracted_markdown="some content"))
    results = await db.search_papers("nonexistent query xyz123")
    assert len(results) == 0


# ---------------------------------------------------------------------------
# Session-Paper M2M
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_link_session_paper(db):
    sid, _ = await db.create_session(SessionRecord(source="cursor"))
    pid, _ = await db.insert_paper(PaperRecord(title="Test"))
    await db.link_session_paper(sid, pid)
    # Linking again should not error (INSERT OR IGNORE)
    await db.link_session_paper(sid, pid)


# ---------------------------------------------------------------------------
# Paper images
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_insert_paper_image(db):
    pid, _ = await db.insert_paper(PaperRecord(title="Test"))
    img_id = await db.insert_paper_image(PaperImageRecord(
        paper_id=pid, filename="figure1.png", image_data_b64="iVBORw0KGgo=",
    ))
    assert img_id == 1
    images = await db.get_paper_images(pid)
    assert len(images) == 1
    assert images[0]["filename"] == "figure1.png"

    b64 = await db.get_paper_image_b64(pid, "figure1.png")
    assert b64 == "iVBORw0KGgo="

    all_imgs = await db.get_all_paper_images_b64(pid)
    assert len(all_imgs) == 1
    assert all_imgs[0]["image_data_b64"] == "iVBORw0KGgo="

    assert await db.get_paper_image_b64(pid, "nonexistent.png") is None


# ---------------------------------------------------------------------------
# Hypotheses
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_add_hypothesis(db):
    hid, heid = await db.add_hypothesis(mechanism="Momentum reversal after volume spikes")
    assert hid == 1
    assert heid.startswith("hyp_")


@pytest.mark.asyncio
async def test_add_hypothesis_with_paper(db):
    pid, _ = await db.insert_paper(PaperRecord(title="Test Paper"))
    hid, heid = await db.add_hypothesis(
        mechanism="Short-term mean reversion", paper_id=pid,
        predicted_sign="negative", time_horizon="1-5 days",
    )
    hyp = await db.get_hypothesis(heid)
    assert hyp is not None
    assert hyp["paper_id"] == pid


@pytest.mark.asyncio
async def test_list_hypotheses(db):
    await db.add_hypothesis(mechanism="Hypothesis A")
    await db.add_hypothesis(mechanism="Hypothesis B")
    hyps = await db.list_hypotheses()
    assert len(hyps) == 2


@pytest.mark.asyncio
async def test_list_hypotheses_filter_by_paper(db):
    pid, _ = await db.insert_paper(PaperRecord(title="Paper X"))
    await db.add_hypothesis(mechanism="From paper", paper_id=pid)
    await db.add_hypothesis(mechanism="No paper")
    hyps = await db.list_hypotheses(paper_id=pid)
    assert len(hyps) == 1
    assert "From paper" in hyps[0]["mechanism"]


@pytest.mark.asyncio
async def test_get_hypothesis_results_empty(db):
    _, heid = await db.add_hypothesis(mechanism="Test")
    results = await db.get_hypothesis_results(heid)
    assert len(results) == 0


@pytest.mark.asyncio
async def test_get_hypothesis_results_with_data(db):
    hid, heid = await db.add_hypothesis(mechanism="Test")
    aid, _ = await db.insert_alpha(AlphaRecord(hypothesis_id=hid, expression="rank(close)"))
    sid, _ = await db.insert_simulation(SimulationRecord(alpha_id=aid, status="done"))
    await db.insert_result(ResultRecord(simulation_id=sid, sharpe=1.5, fitness=1.2))
    results = await db.get_hypothesis_results(heid)
    assert len(results) == 1
    assert results[0]["sharpe"] == 1.5


# ---------------------------------------------------------------------------
# Alphas
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_insert_alpha(db):
    aid, aeid = await db.insert_alpha(AlphaRecord(expression="rank(close)", name="test"))
    assert aid == 1
    assert aeid.startswith("alpha_")


@pytest.mark.asyncio
async def test_insert_alpha_with_language(db):
    aid, _ = await db.insert_alpha(AlphaRecord(
        expression="rank(close)", name="test", language="PYTHON"
    ))
    assert aid == 1


@pytest.mark.asyncio
async def test_alpha_default_language_is_fastexpr(db):
    alpha = AlphaRecord(expression="rank(close)")
    assert alpha.language == "FASTEXPR"


@pytest.mark.asyncio
async def test_expression_exists(db):
    await db.insert_alpha(AlphaRecord(expression="rank(close)"))
    assert await db.expression_exists("rank(close)")
    assert await db.expression_exists("RANK( CLOSE )")
    assert not await db.expression_exists("rank(volume)")


# ---------------------------------------------------------------------------
# Simulations
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_insert_simulation(db):
    aid, _ = await db.insert_alpha(AlphaRecord(expression="rank(close)"))
    sid, seid = await db.insert_simulation(SimulationRecord(alpha_id=aid, status="done"))
    assert sid == 1
    assert seid.startswith("sim_")


@pytest.mark.asyncio
async def test_simulation_with_brain_metadata(db):
    aid, _ = await db.insert_alpha(AlphaRecord(expression="rank(close)"))
    sid, seid = await db.insert_simulation(SimulationRecord(
        alpha_id=aid,
        status="done",
        brain_alpha_id="abc123",
        brain_grade="INFERIOR",
        brain_stage="IS",
        brain_status="UNSUBMITTED",
        brain_classifications_json='[{"id": "DATA_USAGE:SINGLE_DATA_SET", "name": "Single Data Set Alpha"}]',
        brain_tags_json='["momentum", "short-horizon"]',
    ))
    assert sid == 1


@pytest.mark.asyncio
async def test_multiple_simulations_per_alpha(db):
    aid, _ = await db.insert_alpha(AlphaRecord(expression="rank(close)"))
    s1, _ = await db.insert_simulation(SimulationRecord(
        alpha_id=aid, sim_config_json='{"region":"USA"}', status="done"
    ))
    s2, _ = await db.insert_simulation(SimulationRecord(
        alpha_id=aid, sim_config_json='{"region":"CHN"}', status="done"
    ))
    assert s1 != s2


# ---------------------------------------------------------------------------
# Results
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_insert_result(db):
    aid, _ = await db.insert_alpha(AlphaRecord(expression="rank(close)"))
    sid, _ = await db.insert_simulation(SimulationRecord(alpha_id=aid, status="done"))
    rid, reid = await db.insert_result(ResultRecord(simulation_id=sid, sharpe=1.5, fitness=1.2))
    assert rid == 1
    assert reid.startswith("result_")


@pytest.mark.asyncio
async def test_get_top_results(db):
    for expr, sharpe, fitness in [
        ("rank(close)", 1.5, 1.2),
        ("rank(volume)", 0.5, 0.3),
        ("ts_delta(close, 3)", 2.0, 1.8),
    ]:
        aid, _ = await db.insert_alpha(AlphaRecord(expression=expr, name=f"test-{expr}"))
        sid, _ = await db.insert_simulation(SimulationRecord(alpha_id=aid, status="done"))
        await db.insert_result(ResultRecord(simulation_id=sid, sharpe=sharpe, fitness=fitness, turnover=0.3))

    top = await db.get_top_results(limit=2, min_sharpe=1.0)
    assert len(top) == 2
    assert top[0]["fitness"] >= top[1]["fitness"]


@pytest.mark.asyncio
async def test_get_top_results_empty(db):
    assert len(await db.get_top_results()) == 0


# ---------------------------------------------------------------------------
# Session summary
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_session_summary(db):
    sid, seid = await db.create_session(SessionRecord(source="cursor", name="test"))
    hid, _ = await db.add_hypothesis(mechanism="Test hyp", session_id=sid)
    aid, _ = await db.insert_alpha(AlphaRecord(hypothesis_id=hid, expression="rank(close)"))
    simid, _ = await db.insert_simulation(SimulationRecord(alpha_id=aid, status="done"))
    await db.insert_result(ResultRecord(simulation_id=simid, sharpe=1.5, fitness=1.2))

    summary = await db.get_session_summary(seid)
    assert summary["hypothesis_count"] == 1
    assert summary["alpha_count"] == 1
    assert summary["simulation_count"] == 1
    assert summary["best_sharpe"] == 1.5


@pytest.mark.asyncio
async def test_session_summary_not_found(db):
    result = await db.get_session_summary("sess_0_000000")
    assert result == {}


# ---------------------------------------------------------------------------
# Budget
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_sim_budget(db):
    assert await db.get_daily_sim_count("2026-05-16") == 0
    await db.increment_sim_count("2026-05-16")
    await db.increment_sim_count("2026-05-16")
    assert await db.get_daily_sim_count("2026-05-16") == 2


# ---------------------------------------------------------------------------
# Stats
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_stats_empty(db):
    stats = await db.get_stats()
    assert stats["sessions"] == 0
    assert stats["papers"] == 0
    assert stats["alphas"] == 0


@pytest.mark.asyncio
async def test_stats_with_data(db):
    await db.create_session(SessionRecord(source="test"))
    await db.insert_paper(PaperRecord(title="Test"))
    aid, _ = await db.insert_alpha(AlphaRecord(expression="rank(close)"))
    sid, _ = await db.insert_simulation(SimulationRecord(alpha_id=aid, status="done"))
    await db.insert_result(ResultRecord(simulation_id=sid, sharpe=1.5, fitness=1.2))
    stats = await db.get_stats()
    assert stats["sessions"] == 1
    assert stats["papers"] == 1
    assert stats["alphas"] == 1
    assert stats["simulations"] == 1
    assert stats["results"] == 1
    assert stats["max_sharpe"] == 1.5


# ---------------------------------------------------------------------------
# Expression hash
# ---------------------------------------------------------------------------


def test_expression_hash_normalization():
    h1 = expression_hash("rank(close)")
    h2 = expression_hash("rank( close )")
    h3 = expression_hash("RANK(CLOSE)")
    assert h1 == h2 == h3


def test_expression_hash_different():
    assert expression_hash("rank(close)") != expression_hash("rank(volume)")
