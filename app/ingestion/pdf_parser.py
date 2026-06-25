from pathlib import Path
from pypdf import PdfReader

from app.ingestion.base_parser import BaseParser
from app.ingestion.models import ParsedDocument


class PDFParser(BaseParser):

    def parse(
        self,
        source: str
    ) -> ParsedDocument:

        pdf_path = Path(source)

        if not pdf_path.exists():
            raise FileNotFoundError(
                f"PDF not found: {source}"
            )

        reader = PdfReader(
            str(pdf_path)
        )

        text_parts = []

        for page in reader.pages:

            try:
                page_text = page.extract_text()

                if page_text:
                    text_parts.append(
                        page_text
                    )

            except Exception:
                continue

        full_text = "\n".join(
            text_parts
        )

        return ParsedDocument(
            source="pdf",
            text=full_text
        )