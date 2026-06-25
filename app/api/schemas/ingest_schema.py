from pydantic import BaseModel, Field

class IngestRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Knowledge content to ingest"
    )
    source: str = Field(
        default="manual",
        description="Source of knowledge"
    )
class IngestResponse(BaseModel):
    status: str
    message: str
    node_created: bool
    cke_operation: str | None = None
    cke_target: str | None = None
    cke_explanation: str | None = None
    node_id: str | None = None