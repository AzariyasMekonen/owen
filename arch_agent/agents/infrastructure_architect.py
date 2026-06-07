from arch_agent.core.agent import BaseAgent
from arch_agent.core.models import Architecture, Infrastructure

class InfrastructureArchitectAgent(BaseAgent):
    def __init__(self):
        super().__init__("Infrastructure Architect", "Designs scaling and deployment strategies")

    async def process(self, context: Architecture) -> Architecture:
        context.infrastructure.append(Infrastructure(component="API Service", scaling_strategy="Horizontal Pod Autoscaler", deployment="Kubernetes"))
        context.infrastructure.append(Infrastructure(component="Database", scaling_strategy="Read Replicas", deployment="Managed RDS"))
        return context
