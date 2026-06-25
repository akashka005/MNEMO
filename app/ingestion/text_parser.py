from pathlib import Path

from app.ingestion.models import (
    ParsedDocument
)

from app.ingestion.base_parser import (
    BaseParser
)


class TextParser(
    BaseParser
):

    def parse(
        self,
        source: str
    ):

        path = Path(source)

        text = path.read_text(
            encoding="utf-8"
        )

        return ParsedDocument(
            source="text",
            text=text
        )