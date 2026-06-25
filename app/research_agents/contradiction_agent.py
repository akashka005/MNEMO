import json
from app.llm.groq_client import groq_client
from app.llm.prompts.research_prompts import CONTRADICTION_PROMPT

class ContradictionAgent:
    @staticmethod
    def analyze(texts):
        if not texts:
            return []
            
        combined_text = "\n".join(texts)
        prompt = CONTRADICTION_PROMPT.format(texts=combined_text)
        
        try:
            response = groq_client.generate(prompt, temperature=0.3)
            start = response.find("[")
            end = response.rfind("]") + 1
            if start != -1 and end != 0:
                return json.loads(response[start:end])
        except Exception as e:
            print(f"ContradictionAgent error: {e}")
            
        return []