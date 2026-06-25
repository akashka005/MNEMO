from fastapi import APIRouter, HTTPException
from app.graph.neo4j_client import neo4j_client

router = APIRouter(
    prefix="/insights",
    tags=["Insights"]
)

@router.get("/")
async def get_insights():
    try:
        # Fetch real contradictions
        contradictions_query = """
        MATCH (a)-[r:CONTRADICTS]->(b)
        RETURN a.text AS a, b.text AS b, r.weight AS weight
        LIMIT 20
        """
        contradictions = neo4j_client.execute_query(contradictions_query)

        # Fetch bridge (EMERGES_FROM) edges
        bridges_query = """
        MATCH (a)-[r:EMERGES_FROM]->(b)
        RETURN a.text AS a, b.text AS b
        LIMIT 20
        """
        bridges = neo4j_client.execute_query(bridges_query)

        # Knowledge gaps = nodes with very low confidence
        gaps_query = """
        MATCH (n)
        WHERE n.confidence IS NOT NULL AND n.confidence < 0.5
        RETURN n.id AS id, n.text AS text, n.confidence AS confidence
        ORDER BY n.confidence ASC
        LIMIT 10
        """
        gaps = neo4j_client.execute_query(gaps_query)

        # Graph stats
        stats_query = """
        MATCH (n)
        RETURN count(n) AS total_nodes
        """
        stats = neo4j_client.execute_query(stats_query)
        total_nodes = stats[0].get("total_nodes", 0) if stats else 0

        summary = (
            f"Graph has {total_nodes} nodes, "
            f"{len(contradictions)} contradictions, "
            f"{len(bridges)} bridges, and "
            f"{len(gaps)} low-confidence nodes."
        )

        return {
            "contradictions": [
                {"a": c.get("a", ""), "b": c.get("b", ""), "weight": c.get("weight", 1.0)}
                for c in contradictions
            ],
            "bridges": [
                {"a": b.get("a", ""), "b": b.get("b", "")}
                for b in bridges
            ],
            "knowledge_gaps": [
                {"id": g.get("id", ""), "text": g.get("text", ""), "confidence": g.get("confidence", 0)}
                for g in gaps
            ],
            "summary": summary,
            "total_nodes": total_nodes
        }
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Database unavailable: {str(e)}. Make sure Neo4j is running (docker-compose up -d)."
        )
