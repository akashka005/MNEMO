from app.ingestion.ingestion_pipeline import (
    IngestionPipeline
)


class MemoryOrchestrator:

    @staticmethod
    def ingest(source: str):

        return IngestionPipeline.run(
            source
        )