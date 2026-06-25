from fastapi import APIRouter, BackgroundTasks
from app.api.schemas.ingest_schema import IngestRequest, IngestResponse
from app.ingestion.ingestion_pipeline import IngestionPipeline

router = APIRouter(
    prefix="/ingest",
    tags=["Ingestion"]
)

@router.post("/", response_model=IngestResponse)
async def ingest_data(request: IngestRequest, background_tasks: BackgroundTasks):
    text = getattr(request, 'text', '') or getattr(request, 'content', '') or str(request.model_dump())
    
    # Run the pipeline synchronously for now to ensure it works, 
    # but ideally this should be a background task or celery job.
    result = IngestionPipeline.run(source=text, chunk_size=500)
    
    # Extract CKE data from the first chunk if available
    first_result = result.get('results', [{}])[0] if result.get('results') else {}
    
    return IngestResponse(
        status="success",
        message=first_result.get("cke_explanation", f"Knowledge processed into {result.get('chunks', 0)} chunks."),
        node_created=True,
        cke_operation=first_result.get("cke_operation"),
        cke_target=first_result.get("cke_target"),
        cke_explanation=first_result.get("cke_explanation"),
        node_id=first_result.get("node_id")
    )