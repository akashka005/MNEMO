import json
from app.llm.groq_client import groq_client
from app.llm.prompts.research_prompts import LITERATURE_PROMPT

class LiteratureAgent:
    @staticmethod
    def analyze(texts):
        if not texts:
            return {"trends": [], "gaps": []}
            
        combined_text = "\n".join(texts)
        prompt = LITERATURE_PROMPT.format(texts=combined_text)
        
        try:
            response = groq_client.generate(prompt, temperature=0.2)
            # Find JSON block in response
            start = response.find("{")
            end = response.rfind("}") + 1
            if start != -1 and end != 0:
                return json.loads(response[start:end])
        except Exception as e:
            print(f"LiteratureAgent error: {e}")
            
        return {"trends": [], "gaps": []}