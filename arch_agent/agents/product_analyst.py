from arch_agent.core.agent import BaseAgent
from arch_agent.core.models import Architecture, Requirement
from arch_agent.core.llm import LLMClient
import json

class ProductAnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__("Product Analyst", "Converts idea to requirements")
        self.llm = LLMClient()

    async def process(self, context: Architecture) -> Architecture:
        prompt = f"Convert the following project idea into a list of formal technical requirements. Return ONLY a JSON list of requirements with 'id', 'description', and 'priority' fields.\n\nIdea: {context.summary}"

        response = await self.llm.complete(prompt, system_prompt="You are a Product Analyst. Output only valid JSON.")

        try:
            # Try to extract JSON if LLM returned extra text
            start = response.find('[')
            end = response.rfind(']') + 1
            if start != -1 and end != -1:
                reqs_data = json.loads(response[start:end])
                for req in reqs_data:
                    context.requirements.append(Requirement(**req))
            else:
                raise ValueError("No JSON found")
        except Exception:
            # Fallback to heuristic if LLM fails or no key
            if "auth" in context.summary.lower():
                context.requirements.append(Requirement(id="REQ-1", description="Secure authentication", priority="High"))
            else:
                context.requirements.append(Requirement(id="REQ-GEN", description=f"Requirement for {context.name}", priority="Medium"))

        return context
