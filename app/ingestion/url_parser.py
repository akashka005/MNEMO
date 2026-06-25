import requests

from bs4 import BeautifulSoup

from app.ingestion.base_parser import BaseParser
from app.ingestion.models import ParsedDocument


class URLParser(BaseParser):

    def parse(
        self,
        source: str
    ) -> ParsedDocument:

        response = requests.get(
            source,
            timeout=20,
            headers={
                "User-Agent":
                "MNEMO/0.1"
            }
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for tag in soup(
            [
                "script",
                "style",
                "noscript"
            ]
        ):
            tag.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        return ParsedDocument(
            source="url",
            text=text
        )