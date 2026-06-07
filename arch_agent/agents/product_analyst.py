from arch_agent.core.agent import BaseAgent
from arch_agent.core.models import Architecture, Requirement

class ProductAnalystAgent(BaseAgent):
    def __init__(self):
        super().__init__("Product Analyst", "Converts idea to requirements")

    async def process(self, context: Architecture) -> Architecture:
        # Simulate AI identifying requirements from the summary (idea)
        idea = context.summary.lower()
        if "auth" in idea or "user" in idea:
            context.requirements.append(Requirement(id="REQ-AUTH", description="Robust User Authentication and Authorization", priority="High"))
        if "api" in idea or "backend" in idea:
            context.requirements.append(Requirement(id="REQ-API", description="RESTful API for backend communication", priority="High"))
        if "data" in idea or "db" in idea or "database" in idea:
            context.requirements.append(Requirement(id="REQ-DATA", description="Scalable database schema for persistent storage", priority="Medium"))

        if not context.requirements:
            context.requirements.append(Requirement(id="REQ-GENERIC", description=f"Core functionality for {context.name}", priority="Medium"))
        return context
