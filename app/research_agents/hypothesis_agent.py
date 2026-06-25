import json
from app.llm.groq_client import groq_client
from app.llm.prompts.research_prompts import HYPOTHESIS_PROMPT

class HypothesisAgent:
    @staticmethod
    def generate(nodes):
        if not nodes:
            return []
            
        combined_nodes = "\n".join(nodes)
        prompt = HYPOTHESIS_PROMPT.format(nodes=combined_nodes)
        
        try:
            response = groq_client.generate(prompt, temperature=0.7)
            start = response.find("[")
            end = response.rfind("]") + 1
            if start != -1 and end != 0:
                return json.loads(response[start:end])
        except Exception as e:
            print(f"HypothesisAgent error: {e}")
            
        return []