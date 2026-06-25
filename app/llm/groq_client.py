from groq import Groq
from app.config.settings import settings

class GroqClient:
    def __init__(self):
        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )
        self.model = settings.GROQ_MODEL
    def generate(
        self,
        prompt: str,
        temperature: float = 0.2
    ) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=temperature,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return (
            response
            .choices[0]
            .message
            .content
        )
groq_client = GroqClient()