import arxiv

from app.ingestion.base_parser import BaseParser
from app.ingestion.models import ParsedDocument


class PaperParser(BaseParser):

    def parse(
        self,
        source: str
    ) -> ParsedDocument:

        client = arxiv.Client()

        search = arxiv.Search(
            query=source,
            max_results=1
        )

        results = list(
            client.results(search)
        )

        if not results:
            raise ValueError(
                "Paper not found"
            )

        paper = results[0]

        text = f"""
Title:
{paper.title}

Authors:
{", ".join(
    author.name
    for author in paper.authors
)}

Summary:
{paper.summary}
"""

        return ParsedDocument(
            source="paper",
            text=text.strip()
        )