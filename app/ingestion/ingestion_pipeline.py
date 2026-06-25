from app.ingestion.document_ingestor import (
    DocumentIngestor
)

from app.ingestion.chunker import (
    Chunker
)

from app.agents.ingestion_agent import (
    IngestionAgent
)


class IngestionPipeline:

    @staticmethod
    def run(
        source: str,
        chunk_size: int = 500
    ):

        document = (
            DocumentIngestor.ingest(
                source
            )
        )

        chunks = Chunker.chunk_text(
            document.text,
            chunk_size=chunk_size
        )

        results = []

        for chunk in chunks:

            result = (
                IngestionAgent.ingest(
                    chunk
                )
            )

            results.append(result)

        return {
            "source": document.source,
            "chunks": len(chunks),
            "results": results
        }