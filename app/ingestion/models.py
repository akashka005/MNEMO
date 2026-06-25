from pydantic import (
    BaseModel
)


class ParsedDocument(
    BaseModel
):

    source: str

    text: str