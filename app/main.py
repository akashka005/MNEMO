from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.ingest import (
    router as ingest_router
)

from app.api.routes.query import (
    router as query_router
)

from app.api.routes.graph import (
    router as graph_router
)

from app.api.routes.insights import (
    router as insights_router
)

from app.api.routes.research import (
    router as research_router
)

from app.api.routes.graph_dashboard import (
    router as dashboard_router
)

app = FastAPI(
    title="MENMO"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(
    ingest_router
)

app.include_router(
    query_router
)

app.include_router(
    graph_router
)

app.include_router(
    insights_router
)

app.include_router(
    research_router
)
app.include_router(
    dashboard_router
)