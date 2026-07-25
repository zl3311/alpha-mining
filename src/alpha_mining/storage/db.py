"""
SQLite database operations for the alpha mining pipeline.

Full workflow lineage: sessions -> papers (M2M) -> hypotheses -> alphas -> simulations -> results.
Uses FTS5 for full-text search on papers. All entities have globally unique entity_ids.
Provides async CRUD via aiosqlite.
"""

from __future__ import annotations

import hashlib
import json
import logging
from pathlib import Path

import aiosqlite

from ..ids import generate_entity_id
from .models import (
    AlphaRecord,
    HypothesisRecord,
    PaperImageRecord,
    PaperRecord,
    ResultRecord,
    SessionRecord,
    SimulationRecord,
)

logger = logging.getLogger(__name__)

_SCHEMA = """
-- Sessions: a unit of work (Cursor chat, CLI run, periodic job)
CREATE TABLE IF NOT EXISTS sessions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT UNIQUE NOT NULL,
    source TEXT NOT NULL DEFAULT 'manual',
    name TEXT NOT NULL DEFAULT '',
    notes TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_sessions_entity ON sessions(entity_id);

-- Papers: independent research papers
CREATE TABLE IF NOT EXISTS papers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL DEFAULT '',
    source_url TEXT NOT NULL DEFAULT '',
    pdf_path TEXT NOT NULL DEFAULT '',
    markdown_path TEXT NOT NULL DEFAULT '',
    extracted_markdown TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_papers_entity ON papers(entity_id);

-- Many-to-many: sessions <-> papers
CREATE TABLE IF NOT EXISTS session_papers (
    session_id INTEGER NOT NULL REFERENCES sessions(id),
    paper_id INTEGER NOT NULL REFERENCES papers(id),
    PRIMARY KEY (session_id, paper_id)
);

-- Images extracted from papers (base64 for agent-friendly access)
CREATE TABLE IF NOT EXISTS paper_images (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    paper_id INTEGER NOT NULL REFERENCES papers(id),
    filename TEXT NOT NULL DEFAULT '',
    content_type TEXT NOT NULL DEFAULT 'image/png',
    image_data_b64 TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);

-- Hypotheses: alpha ideas from papers or conversations
CREATE TABLE IF NOT EXISTS hypotheses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT UNIQUE NOT NULL,
    session_id INTEGER REFERENCES sessions(id),
    paper_id INTEGER REFERENCES papers(id),
    mechanism TEXT NOT NULL DEFAULT '',
    predicted_sign TEXT NOT NULL DEFAULT '',
    time_horizon TEXT NOT NULL DEFAULT '',
    relevant_fields TEXT NOT NULL DEFAULT '[]',
    confidence TEXT NOT NULL DEFAULT '',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_hypotheses_entity ON hypotheses(entity_id);
CREATE INDEX IF NOT EXISTS idx_hypotheses_session ON hypotheses(session_id);
CREATE INDEX IF NOT EXISTS idx_hypotheses_paper ON hypotheses(paper_id);

-- Alphas: expression identity (no sim config)
CREATE TABLE IF NOT EXISTS alphas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT UNIQUE NOT NULL,
    hypothesis_id INTEGER REFERENCES hypotheses(id),
    name TEXT NOT NULL DEFAULT '',
    expression TEXT NOT NULL,
    expression_hash TEXT NOT NULL,
    language TEXT NOT NULL DEFAULT 'FASTEXPR',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_alphas_entity ON alphas(entity_id);
CREATE INDEX IF NOT EXISTS idx_alphas_hash ON alphas(expression_hash);

-- Simulations: individual BRAIN submissions with specific config
CREATE TABLE IF NOT EXISTS simulations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT UNIQUE NOT NULL,
    alpha_id INTEGER NOT NULL REFERENCES alphas(id),
    sim_config_json TEXT NOT NULL DEFAULT '{}',
    status TEXT NOT NULL DEFAULT 'pending',
    brain_alpha_id TEXT NOT NULL DEFAULT '',
    platform_url TEXT NOT NULL DEFAULT '',
    brain_grade TEXT NOT NULL DEFAULT '',
    brain_stage TEXT NOT NULL DEFAULT '',
    brain_status TEXT NOT NULL DEFAULT '',
    brain_classifications_json TEXT NOT NULL DEFAULT '[]',
    brain_tags_json TEXT NOT NULL DEFAULT '[]',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_simulations_entity ON simulations(entity_id);
CREATE INDEX IF NOT EXISTS idx_simulations_alpha ON simulations(alpha_id);
CREATE INDEX IF NOT EXISTS idx_simulations_status ON simulations(status);

-- Results: metrics from BRAIN simulations
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entity_id TEXT UNIQUE NOT NULL,
    simulation_id INTEGER NOT NULL REFERENCES simulations(id),
    sharpe REAL NOT NULL DEFAULT 0,
    fitness REAL NOT NULL DEFAULT 0,
    turnover REAL NOT NULL DEFAULT 0,
    returns REAL NOT NULL DEFAULT 0,
    drawdown REAL NOT NULL DEFAULT 0,
    self_correlation REAL,
    checks_json TEXT NOT NULL DEFAULT '[]',
    raw_response_json TEXT NOT NULL DEFAULT '{}',
    created_at TEXT NOT NULL DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_results_entity ON results(entity_id);
CREATE INDEX IF NOT EXISTS idx_results_simulation ON results(simulation_id);
CREATE INDEX IF NOT EXISTS idx_results_sharpe ON results(sharpe);
CREATE INDEX IF NOT EXISTS idx_results_fitness ON results(fitness);

-- Daily simulation budget
CREATE TABLE IF NOT EXISTS simulation_budget (
    date_est TEXT PRIMARY KEY,
    count INTEGER NOT NULL DEFAULT 0,
    last_updated TEXT NOT NULL DEFAULT (datetime('now'))
);
"""

_FTS_SCHEMA = """
CREATE VIRTUAL TABLE IF NOT EXISTS papers_fts USING fts5(
    title, extracted_markdown, content=papers, content_rowid=id
);

CREATE TRIGGER IF NOT EXISTS papers_ai AFTER INSERT ON papers BEGIN
    INSERT INTO papers_fts(rowid, title, extracted_markdown)
    VALUES (new.id, new.title, new.extracted_markdown);
END;

CREATE TRIGGER IF NOT EXISTS papers_au AFTER UPDATE ON papers BEGIN
    INSERT INTO papers_fts(papers_fts, rowid, title, extracted_markdown)
    VALUES ('delete', old.id, old.title, old.extracted_markdown);
    INSERT INTO papers_fts(rowid, title, extracted_markdown)
    VALUES (new.id, new.title, new.extracted_markdown);
END;
"""


def expression_hash(expr: str) -> str:
    """Deterministic hash of a normalized expression for deduplication."""
    normalized = "".join(expr.lower().split())
    return hashlib.sha256(normalized.encode()).hexdigest()[:16]


class AlphaDB:
    """
    Async database interface for the alpha mining pipeline.

    Manages connection lifecycle, schema initialization, and all CRUD
    operations. All external-facing methods accept/return entity_ids.
    Internal joins use integer PKs for performance.

    Usage:
        async with AlphaDB(Path("data/alpha_mining.db")) as db:
            sess_id = await db.create_session(SessionRecord(source="cursor"))
            paper_eid = await db.insert_paper(PaperRecord(title="101 Alphas"))
            results = await db.search_papers("momentum reversal")
    """

    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path
        self._conn: aiosqlite.Connection | None = None

    async def __aenter__(self) -> AlphaDB:
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = await aiosqlite.connect(str(self._db_path))
        self._conn.row_factory = aiosqlite.Row
        await self._conn.executescript(_SCHEMA)
        try:
            await self._conn.executescript(_FTS_SCHEMA)
        except Exception as e:
            logger.warning("FTS5 setup skipped (may already exist): %s", e)
        await self._conn.commit()
        logger.info("Database initialized at %s", self._db_path)
        return self

    async def __aexit__(self, *exc) -> None:
        if self._conn:
            await self._conn.close()
            self._conn = None

    # ------------------------------------------------------------------
    # Sessions
    # ------------------------------------------------------------------

    async def create_session(self, session: SessionRecord) -> tuple[int, str]:
        """Create a session. Returns (internal_id, entity_id)."""
        cursor = await self._conn.execute(
            "INSERT INTO sessions (entity_id, source, name, notes) VALUES (?, ?, ?, ?)",
            (session.entity_id, session.source, session.name, session.notes),
        )
        await self._conn.commit()
        return cursor.lastrowid, session.entity_id

    async def get_session(self, entity_id: str) -> dict | None:
        cursor = await self._conn.execute(
            "SELECT * FROM sessions WHERE entity_id = ?", (entity_id,)
        )
        row = await cursor.fetchone()
        return dict(row) if row else None

    async def get_session_summary(self, entity_id: str) -> dict:
        """Full session overview: hypothesis count, alpha count, best sharpe, etc."""
        sess = await self.get_session(entity_id)
        if not sess:
            return {}

        sid = sess["id"]
        summary = {"session": sess}

        cursor = await self._conn.execute(
            "SELECT COUNT(*) FROM hypotheses WHERE session_id = ?", (sid,)
        )
        summary["hypothesis_count"] = (await cursor.fetchone())[0]

        cursor = await self._conn.execute(
            """SELECT COUNT(DISTINCT a.id) FROM alphas a
               JOIN hypotheses h ON a.hypothesis_id = h.id
               WHERE h.session_id = ?""",
            (sid,),
        )
        summary["alpha_count"] = (await cursor.fetchone())[0]

        cursor = await self._conn.execute(
            """SELECT COUNT(s.id), MAX(r.sharpe), MAX(r.fitness)
               FROM simulations s
               JOIN alphas a ON s.alpha_id = a.id
               JOIN hypotheses h ON a.hypothesis_id = h.id
               LEFT JOIN results r ON r.simulation_id = s.id
               WHERE h.session_id = ?""",
            (sid,),
        )
        row = await cursor.fetchone()
        summary["simulation_count"] = row[0] or 0
        summary["best_sharpe"] = round(row[1], 3) if row[1] else 0
        summary["best_fitness"] = round(row[2], 3) if row[2] else 0

        return summary

    async def link_session_paper(self, session_id: int, paper_id: int) -> None:
        await self._conn.execute(
            "INSERT OR IGNORE INTO session_papers (session_id, paper_id) VALUES (?, ?)",
            (session_id, paper_id),
        )
        await self._conn.commit()

    # ------------------------------------------------------------------
    # Papers
    # ------------------------------------------------------------------

    async def insert_paper(self, paper: PaperRecord) -> tuple[int, str]:
        """Insert a paper. Returns (internal_id, entity_id)."""
        cursor = await self._conn.execute(
            """INSERT INTO papers (entity_id, title, source_url, pdf_path, markdown_path, extracted_markdown)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                paper.entity_id, paper.title, paper.source_url,
                paper.pdf_path, paper.markdown_path, paper.extracted_markdown,
            ),
        )
        await self._conn.commit()
        return cursor.lastrowid, paper.entity_id

    async def get_paper(self, entity_id: str) -> dict | None:
        cursor = await self._conn.execute(
            "SELECT * FROM papers WHERE entity_id = ?", (entity_id,)
        )
        row = await cursor.fetchone()
        return dict(row) if row else None

    async def get_paper_by_internal_id(self, paper_id: int) -> dict | None:
        cursor = await self._conn.execute("SELECT * FROM papers WHERE id = ?", (paper_id,))
        row = await cursor.fetchone()
        return dict(row) if row else None

    async def list_papers(self) -> list[dict]:
        """List all papers with id, entity_id, title, date, and character count."""
        cursor = await self._conn.execute(
            """SELECT id, entity_id, title, source_url, created_at,
                      LENGTH(extracted_markdown) as char_count
               FROM papers ORDER BY created_at DESC"""
        )
        return [dict(row) for row in await cursor.fetchall()]

    async def search_papers(self, query: str, limit: int = 10) -> list[dict]:
        """Full-text search across paper titles and content."""
        cursor = await self._conn.execute(
            """SELECT p.id, p.entity_id, p.title, p.source_url, p.created_at,
                      LENGTH(p.extracted_markdown) as char_count,
                      snippet(papers_fts, 1, '**', '**', '...', 30) as snippet
               FROM papers_fts
               JOIN papers p ON p.id = papers_fts.rowid
               WHERE papers_fts MATCH ?
               ORDER BY rank
               LIMIT ?""",
            (query, limit),
        )
        return [dict(row) for row in await cursor.fetchall()]

    # ------------------------------------------------------------------
    # Paper images
    # ------------------------------------------------------------------

    async def insert_paper_image(self, image: PaperImageRecord) -> int:
        cursor = await self._conn.execute(
            "INSERT INTO paper_images (paper_id, filename, content_type, image_data_b64) VALUES (?, ?, ?, ?)",
            (image.paper_id, image.filename, image.content_type, image.image_data_b64),
        )
        await self._conn.commit()
        return cursor.lastrowid

    async def get_paper_images(self, paper_id: int) -> list[dict]:
        cursor = await self._conn.execute(
            "SELECT id, filename, content_type, LENGTH(image_data_b64) as size_b64"
            " FROM paper_images WHERE paper_id = ?",
            (paper_id,),
        )
        return [dict(row) for row in await cursor.fetchall()]

    async def get_paper_image_b64(self, paper_id: int, filename: str) -> str | None:
        """Retrieve base64-encoded image data by paper_id and filename. Agent/MCP ready."""
        cursor = await self._conn.execute(
            "SELECT image_data_b64 FROM paper_images WHERE paper_id = ? AND filename = ?",
            (paper_id, filename),
        )
        row = await cursor.fetchone()
        return row[0] if row else None

    async def get_all_paper_images_b64(self, paper_id: int) -> list[dict]:
        """Retrieve all images for a paper as base64. Agent/MCP ready."""
        cursor = await self._conn.execute(
            "SELECT filename, content_type, image_data_b64 FROM paper_images WHERE paper_id = ?",
            (paper_id,),
        )
        return [dict(row) for row in await cursor.fetchall()]

    # ------------------------------------------------------------------
    # Hypotheses
    # ------------------------------------------------------------------

    async def add_hypothesis(
        self,
        mechanism: str,
        predicted_sign: str = "",
        time_horizon: str = "",
        relevant_fields: list[str] | None = None,
        confidence: str = "medium",
        session_id: int | None = None,
        paper_id: int | None = None,
    ) -> tuple[int, str]:
        """Create a hypothesis. Returns (internal_id, entity_id)."""
        eid = generate_entity_id("hypothesis")
        fields_json = json.dumps(relevant_fields or [])
        cursor = await self._conn.execute(
            """INSERT INTO hypotheses (entity_id, session_id, paper_id, mechanism,
               predicted_sign, time_horizon, relevant_fields, confidence)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (eid, session_id, paper_id, mechanism, predicted_sign,
             time_horizon, fields_json, confidence),
        )
        await self._conn.commit()
        return cursor.lastrowid, eid

    async def insert_hypothesis_record(self, hyp: HypothesisRecord) -> tuple[int, str]:
        """Insert from a HypothesisRecord model."""
        cursor = await self._conn.execute(
            """INSERT INTO hypotheses (entity_id, session_id, paper_id, mechanism,
               predicted_sign, time_horizon, relevant_fields, confidence)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                hyp.entity_id, hyp.session_id, hyp.paper_id, hyp.mechanism,
                hyp.predicted_sign, hyp.time_horizon,
                json.dumps(hyp.relevant_fields), hyp.confidence,
            ),
        )
        await self._conn.commit()
        return cursor.lastrowid, hyp.entity_id

    async def list_hypotheses(
        self,
        session_id: int | None = None,
        paper_id: int | None = None,
        limit: int = 50,
    ) -> list[dict]:
        """List hypotheses with optional session/paper filters. Includes alpha count and best sharpe."""
        conditions = []
        params: list = []

        if session_id is not None:
            conditions.append("h.session_id = ?")
            params.append(session_id)
        if paper_id is not None:
            conditions.append("h.paper_id = ?")
            params.append(paper_id)

        where = f"WHERE {' AND '.join(conditions)}" if conditions else ""
        params.append(limit)

        cursor = await self._conn.execute(
            f"""SELECT h.id, h.entity_id, h.mechanism, h.predicted_sign, h.time_horizon,
                       h.confidence, h.created_at,
                       p.title as paper_title, p.entity_id as paper_entity_id,
                       COUNT(DISTINCT a.id) as alpha_count,
                       MAX(r.sharpe) as best_sharpe
                FROM hypotheses h
                LEFT JOIN papers p ON h.paper_id = p.id
                LEFT JOIN alphas a ON a.hypothesis_id = h.id
                LEFT JOIN simulations s ON s.alpha_id = a.id
                LEFT JOIN results r ON r.simulation_id = s.id
                {where}
                GROUP BY h.id
                ORDER BY h.created_at DESC
                LIMIT ?""",
            params,
        )
        return [dict(row) for row in await cursor.fetchall()]

    async def get_hypothesis(self, entity_id: str) -> dict | None:
        cursor = await self._conn.execute(
            "SELECT * FROM hypotheses WHERE entity_id = ?", (entity_id,)
        )
        row = await cursor.fetchone()
        return dict(row) if row else None

    async def get_hypothesis_results(self, entity_id: str) -> list[dict]:
        """Full lineage: hypothesis -> alphas -> simulations -> results."""
        cursor = await self._conn.execute(
            """SELECT a.entity_id as alpha_eid, a.name, a.expression,
                      s.entity_id as sim_eid, s.status, s.platform_url,
                      r.sharpe, r.fitness, r.turnover, r.returns, r.drawdown
               FROM hypotheses h
               JOIN alphas a ON a.hypothesis_id = h.id
               LEFT JOIN simulations s ON s.alpha_id = a.id
               LEFT JOIN results r ON r.simulation_id = s.id
               WHERE h.entity_id = ?
               ORDER BY r.fitness DESC""",
            (entity_id,),
        )
        return [dict(row) for row in await cursor.fetchall()]

    async def link_hypothesis_to_paper(self, hypothesis_id: int, paper_id: int) -> None:
        await self._conn.execute(
            "UPDATE hypotheses SET paper_id = ? WHERE id = ?",
            (paper_id, hypothesis_id),
        )
        await self._conn.commit()

    # ------------------------------------------------------------------
    # Alphas
    # ------------------------------------------------------------------

    async def insert_alpha(self, alpha: AlphaRecord) -> tuple[int, str]:
        """Insert an alpha expression. Returns (internal_id, entity_id)."""
        h = expression_hash(alpha.expression) if not alpha.expression_hash else alpha.expression_hash
        cursor = await self._conn.execute(
            "INSERT INTO alphas (entity_id, hypothesis_id, name, expression, expression_hash,"
            " language) VALUES (?, ?, ?, ?, ?, ?)",
            (alpha.entity_id, alpha.hypothesis_id, alpha.name, alpha.expression, h, alpha.language),
        )
        await self._conn.commit()
        return cursor.lastrowid, alpha.entity_id

    async def expression_exists(self, expr: str) -> bool:
        h = expression_hash(expr)
        cursor = await self._conn.execute(
            "SELECT COUNT(*) FROM alphas WHERE expression_hash = ?", (h,)
        )
        return (await cursor.fetchone())[0] > 0

    # ------------------------------------------------------------------
    # Simulations
    # ------------------------------------------------------------------

    async def insert_simulation(self, sim: SimulationRecord) -> tuple[int, str]:
        """Insert a simulation record. Returns (internal_id, entity_id)."""
        cursor = await self._conn.execute(
            """INSERT INTO simulations (entity_id, alpha_id, sim_config_json, status, brain_alpha_id,
               platform_url, brain_grade, brain_stage, brain_status, brain_classifications_json, brain_tags_json)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (sim.entity_id, sim.alpha_id, sim.sim_config_json, sim.status,
             sim.brain_alpha_id, sim.platform_url, sim.brain_grade, sim.brain_stage,
             sim.brain_status, sim.brain_classifications_json, sim.brain_tags_json),
        )
        await self._conn.commit()
        return cursor.lastrowid, sim.entity_id

    async def update_simulation_status(self, sim_id: int, status: str, **kwargs) -> None:
        sets = ["status = ?"]
        params: list = [status]
        for key in ("brain_alpha_id", "platform_url"):
            if key in kwargs:
                sets.append(f"{key} = ?")
                params.append(kwargs[key])
        params.append(sim_id)
        await self._conn.execute(
            f"UPDATE simulations SET {', '.join(sets)} WHERE id = ?", params
        )
        await self._conn.commit()

    # ------------------------------------------------------------------
    # Results
    # ------------------------------------------------------------------

    async def insert_result(self, result: ResultRecord) -> tuple[int, str]:
        """Insert simulation results. Returns (internal_id, entity_id)."""
        cursor = await self._conn.execute(
            """INSERT INTO results (entity_id, simulation_id, sharpe, fitness, turnover, returns,
               drawdown, self_correlation, checks_json, raw_response_json)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                result.entity_id, result.simulation_id, result.sharpe,
                result.fitness, result.turnover, result.returns,
                result.drawdown, result.self_correlation,
                result.checks_json, result.raw_response_json,
            ),
        )
        await self._conn.commit()
        return cursor.lastrowid, result.entity_id

    async def get_top_results(
        self, *, limit: int = 20, min_sharpe: float = 0.0
    ) -> list[dict]:
        """Top results joined with alpha expressions and simulation details."""
        cursor = await self._conn.execute(
            """SELECT r.entity_id as result_eid, r.sharpe, r.fitness, r.turnover, r.returns, r.drawdown,
                      a.entity_id as alpha_eid, a.name, a.expression,
                      s.entity_id as sim_eid, s.platform_url, s.sim_config_json
               FROM results r
               JOIN simulations s ON r.simulation_id = s.id
               JOIN alphas a ON s.alpha_id = a.id
               WHERE r.sharpe >= ?
               ORDER BY r.fitness DESC
               LIMIT ?""",
            (min_sharpe, limit),
        )
        return [dict(row) for row in await cursor.fetchall()]

    async def get_top_quartile_for_feedback(self, limit: int = 10) -> list[dict]:
        """Top alphas for few-shot prompt examples."""
        cursor = await self._conn.execute(
            """SELECT a.expression, h.mechanism, r.sharpe, r.fitness
               FROM results r
               JOIN simulations s ON r.simulation_id = s.id
               JOIN alphas a ON s.alpha_id = a.id
               LEFT JOIN hypotheses h ON a.hypothesis_id = h.id
               WHERE r.sharpe > 0
               ORDER BY r.fitness DESC
               LIMIT ?""",
            (limit,),
        )
        return [dict(row) for row in await cursor.fetchall()]

    # ------------------------------------------------------------------
    # Simulation budget
    # ------------------------------------------------------------------

    async def get_daily_sim_count(self, date_est: str) -> int:
        cursor = await self._conn.execute(
            "SELECT count FROM simulation_budget WHERE date_est = ?", (date_est,)
        )
        row = await cursor.fetchone()
        return row[0] if row else 0

    async def increment_sim_count(self, date_est: str) -> int:
        await self._conn.execute(
            """INSERT INTO simulation_budget (date_est, count, last_updated)
               VALUES (?, 1, datetime('now'))
               ON CONFLICT(date_est)
               DO UPDATE SET count = count + 1, last_updated = datetime('now')""",
            (date_est,),
        )
        await self._conn.commit()
        cursor = await self._conn.execute(
            "SELECT count FROM simulation_budget WHERE date_est = ?", (date_est,)
        )
        return (await cursor.fetchone())[0]

    # ------------------------------------------------------------------
    # Stats
    # ------------------------------------------------------------------

    async def get_stats(self) -> dict:
        stats = {}
        for table in ["sessions", "papers", "hypotheses", "alphas", "simulations", "results"]:
            cursor = await self._conn.execute(f"SELECT COUNT(*) FROM {table}")
            stats[table] = (await cursor.fetchone())[0]

        cursor = await self._conn.execute(
            "SELECT AVG(sharpe), MAX(sharpe), AVG(fitness), MAX(fitness) FROM results"
        )
        row = await cursor.fetchone()
        if row and row[0] is not None:
            stats["avg_sharpe"] = round(row[0], 3)
            stats["max_sharpe"] = round(row[1], 3)
            stats["avg_fitness"] = round(row[2], 3)
            stats["max_fitness"] = round(row[3], 3)

        return stats
