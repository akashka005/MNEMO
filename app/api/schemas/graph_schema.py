from pydantic import BaseModel

class GraphNode(BaseModel):
    id: str
    label: str
    node_type: str
    confidence: float
class GraphEdge(BaseModel):
    source: str
    target: str
    relation: str
    weight: float
class GraphResponse(BaseModel):
    nodes: list[GraphNode]
    edges: list[GraphEdge]
    total_nodes: int
    total_edges: int