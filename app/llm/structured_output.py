import json
from pydantic import BaseModel
from app.llm.groq_client import groq_client

class StructuredOutput:
    @staticmethod
    def generate(
        prompt: str,
        schema: type[BaseModel]
    ):
        full_prompt = f"""
Return ONLY valid JSON.

Schema:

{schema.model_json_schema()}

Task:

{prompt}
"""
        response = groq_client.generate(
            full_prompt
        )
        data = json.loads(
            response
        )
        return schema(
            **data
        )