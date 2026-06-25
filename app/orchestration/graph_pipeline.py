from app.agents.ingestion_agent import IngestionAgent
from app.agents.coherence_agent import CoherenceAgent
from app.agents.state import AgentState

class GraphPipeline:
    @staticmethod
    def process(text: str):
        state = AgentState()
        ingestion_result = (
            IngestionAgent.ingest(text)
        )
        state.node_id = (
            ingestion_result["node_id"]
        )
        state.text = text
        coherence_result = (
            CoherenceAgent.process(
                ingestion_result["node_id"],
                ingestion_result["embedding"]
            )
        )
        if coherence_result:
            state.last_operation = (
                coherence_result.operation.value
            )
            state.confidence = (
                coherence_result.confidence
            )
        return {
            "state": state,
            "coherence": coherence_result
        }