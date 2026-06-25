from pathlib import Path

from app.ingestion.pdf_parser import PDFParser
from app.ingestion.text_parser import TextParser
from app.ingestion.url_parser import URLParser
from app.ingestion.paper_parser import PaperParser


class DocumentIngestor:

    @staticmethod
    def ingest(source: str):
        from app.ingestion.models import ParsedDocument
        
        if source.startswith("http://") or source.startswith("https://"):
            if "arxiv.org" in source or "doi.org" in source:
                parser = PaperParser()
            else:
                parser = URLParser()
            return parser.parse(source)

        try:
            path = Path(source)
            if path.exists() and path.is_file():
                if path.suffix.lower() == ".pdf":
                    return PDFParser().parse(source)
                return TextParser().parse(source)
        except OSError:
            # If source is too long, Path() will throw an OSError on Windows.
            pass

        # Treat as raw text
        return ParsedDocument(
            source="manual_text",
            text=source
        )