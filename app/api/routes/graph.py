from fastapi import APIRouter

from app.api.schemas.graph_schema import (
GraphResponse,
GraphNode,
GraphEdge
)

from app.graph.neo4j_client import (
neo4j_client
)

router = APIRouter(
prefix="/graph",
tags=["KnowledgeGraph"]
)

@router.get(
"/",
response_model=GraphResponse
)
async def get_graph():
    node_query = """
    MATCH (n)
    
    RETURN
        coalesce(
            n.id,
            n.text,
            n.name,
            "Unknown"
        ) AS id,
    
        coalesce(
            n.label,
            n.text,
            n.name,
            "Unknown"
        ) AS label,
    
        coalesce(
            labels(n)[0],
            "Concept"
        ) AS node_type,
    
        coalesce(
            n.confidence,
            1.0
        ) AS confidence
    """
    
    edge_query = """
    MATCH (a)-[r]->(b)
    
    RETURN
        coalesce(
            a.id,
            a.text,
            a.name,
            "Unknown"
        ) AS source,
    
        coalesce(
            b.id,
            b.text,
            b.name,
            "Unknown"
        ) AS target,
    
        type(r) AS relation,
    
        coalesce(
            r.weight,
            1.0
        ) AS weight
    """
    
    node_records = neo4j_client.execute_query(node_query)
    edge_records = neo4j_client.execute_query(edge_query)
    
    nodes = []
    for node in node_records:
        nodes.append(
            GraphNode(
                id=str(node.get("id", "Unknown")),
                label=str(node.get("label", "Unknown")),
                node_type=str(node.get("node_type", "Concept")),
                confidence=float(node.get("confidence", 1.0))
            )
        )
    
    edges = []
    for edge in edge_records:
        edges.append(
            GraphEdge(
                source=str(edge.get("source", "Unknown")),
                target=str(edge.get("target", "Unknown")),
                relation=str(edge.get("relation", "RELATED_TO")),
                weight=float(edge.get("weight", 1.0))
            )
        )
    
    return GraphResponse(
        nodes=nodes,
        edges=edges,
        total_nodes=len(nodes),
        total_edges=len(edges)
    )