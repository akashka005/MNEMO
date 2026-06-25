<div align="center">
  <h1>MNEMO</h1>
  <p><b>Continuous Knowledge Engineering via LLM-Graph Orchestration</b></p>
</div>

---

## Overview

MNEMO is a research-focused knowledge engineering platform that transforms passive document ingestion into an active graph reasoning system.

Instead of treating new text as raw vectors only, MNEMO:

- evaluates semantic overlap, extension, and contradiction,
- maps new content to explicit graph relationships,
- preserves conflicting knowledge instead of overwriting it,
- and exposes query and research analysis workflows on top of a Neo4j knowledge graph.

---

## Core Concepts

### Continuous Knowledge Engineering (CKE)

The ingestion pipeline uses a four-state coherence model:

- **MERGE**: incoming content matches an existing node and reinforces it.
- **EXTEND**: incoming content expands an existing concept with a new child or detail.
- **CONFLICT**: incoming content contradicts existing knowledge and is linked as a counterpoint.
- **EMERGE**: incoming content is semantically distant and becomes a new concept.

These decisions are made by combining embedding similarity with LLM classification.

### Graph Relationships

MNEMO stores knowledge in Neo4j using typed relationships:

- `SUPPORTS` for positive reinforcement
- `EXTENDS` for elaboration and detail
- `CONTRADICTS` for opposing claims
- `EMERGES_FROM` for distant or bridging concepts

---

## Architecture

```mermaid
graph TD
    A[User / Client] --> B[Frontend (React + Vite)]
    B --> C[FastAPI Backend]
    C --> D[Ingestion Pipeline]
    C --> E[Query Agent]
    C --> F[Research Orchestrator]
    D --> G[Neo4j Knowledge Graph]
    E --> G
    F --> G
```

---

## Key Components

- `app/main.py` — FastAPI app and endpoint registration
- `app/api/routes/` — REST routes for ingestion, query, graph retrieval, insights, and research analysis
- `app/ingestion/` — source ingestion, text chunking, and document parsing
- `app/agents/` — orchestration of ingestion, coherence, dialogue, query, insight, and evolution logic
- `app/graph/` — Neo4j client, node/edge operations, and query utilities
- `app/llm/` — Groq client and prompt templates
- `app/research_agents/` — multi-agent research analysis pipeline
- `frontend/` — React-based dashboard and graph visualization

---

## What This Project Does

1. Ingests raw text into `app.ingestion.ingestion_pipeline.IngestionPipeline`
2. Chunks the document and embeds each piece
3. Stores content as graph nodes with embeddings in Neo4j
4. Uses `app.agents.coherence_agent.CoherenceAgent` to compare new chunks against existing nodes
5. Applies graph operations according to semantic similarity and LLM reasoning
6. Answers queries through `app.agents.dialogue_agent.DialogueAgent`
7. Provides research insights using `app.research_agents.research_orchestrator.ResearchOrchestrator`

---

## API Endpoints

### Ingestion

- `POST /ingest`
  - Request: `{ "text": "...", "source": "manual" }`
  - Response: status, message, created node metadata, and CKE operation details

### Query

- `POST /query`
  - Request: `{ "question": "...", "mode": "factual" }`
  - Supported modes: `factual`, `socratic`
  - Response: answer text plus source node IDs and contradiction metadata

### Graph

- `GET /graph` — returns nodes and edges from Neo4j for visualization

### Insights

- `GET /insights/` — returns contradictions, bridges, low-confidence nodes, and graph summary

### Research Analysis

- `POST /research/analyze`
  - Accepts `texts`, `nodes`, and `graph`
  - Returns literature, hypotheses, contradictions, and novelty analysis

---

## Configuration

Configuration is loaded from `.env` using `app.config.settings.Settings`.

Default values in the code:

- `GROQ_API_KEY` — required
- `GROQ_MODEL=llama-3.1-8b-instant`
- `NEO4J_URI=bolt://localhost:7687`
- `NEO4J_USER=neo4j`
- `NEO4J_PASSWORD=password`
- `EMBED_MODEL=BAAI/bge-small-en-v1.5`
- `MERGE_THRESHOLD=0.88`
- `EXTEND_THRESHOLD=0.70`
- `CONFLICT_THRESHOLD=0.72`
- `EMERGE_THRESHOLD=0.50`
- `DECAY_DAYS=30`
- `EMBED_DIMENSION=384`

---

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker
- Groq API key

### 1. Start Neo4j

```bash
docker-compose up -d
```

This launches Neo4j on `localhost:7474` and `localhost:7687`.

### 2. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file in the repository root:

```env
GROQ_API_KEY=your_groq_api_key
GROQ_MODEL=llama-3.1-8b-instant
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password
```

### 4. Start the API Server

```bash
uvicorn app.main:app --reload --port 8000
```

### 5. Launch the Frontend

```bash
cd frontend
npm install
npm run dev
```

Open the frontend in your browser at the port shown by Vite.

---

## Example Usage

### Ingest Text

```bash
curl -X POST http://localhost:8000/ingest \
  -H "Content-Type: application/json" \
  -d '{"text": "A new paper on graph-based knowledge engineering.", "source": "manual"}'
```

### Query the Graph

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What are the main contradictions in the knowledge graph?", "mode": "socratic"}'
```

---

## Notes

- The ingestion route currently processes chunks synchronously in `app.ingestion.ingestion_pipeline.IngestionPipeline`.
- `app.agents.coherence_agent.CoherenceAgent` uses both semantic similarity and Groq LLM classification to select graph operations.
- `app.agents.dialogue_agent.DialogueAgent` includes a `socratic` query mode that enriches prompts with active contradictions.

---

## Frontend

The frontend is a Vite/React app located in `frontend/`.

Key packages include:

- `react`
- `react-dom`
- `react-router-dom`
- `react-force-graph-2d`
- `framer-motion`

---

## Why MNEMO?

MNEMO turns knowledge ingestion into an active engineering process, not a passive database write. It preserves nuance, captures contradictions, and builds an explainable semantic graph for intelligent queries and research analysis.

---

## Project Structure

- `app/main.py` — primary FastAPI app
- `app/api/routes/` — API endpoint definitions
- `app/ingestion/` — ingestion, parsing, chunking
- `app/agents/` — agent workflows and coherence logic
- `app/graph/` — graph persistence and queries
- `app/llm/` — Groq integration and prompt templates
- `app/research_agents/` — research aggregation and novel insight generation
- `frontend/` — browser UI and graph dashboard
