from arch_agent.core.agent import BaseAgent
from arch_agent.core.models import Architecture, Route

class BackendArchitectAgent(BaseAgent):
    def __init__(self):
        super().__init__("Backend Architect", "Designs API routes and logic")

    async def process(self, context: Architecture) -> Architecture:
        context.routes.append(Route(path="/login", method="POST", description="Authenticate user"))
        context.routes.append(Route(path="/profile", method="GET", description="Get user profile"))
        return context
