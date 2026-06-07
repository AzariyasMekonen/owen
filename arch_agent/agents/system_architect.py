from arch_agent.core.agent import BaseAgent
from arch_agent.core.models import Architecture

class SystemArchitectAgent(BaseAgent):
    def __init__(self):
        super().__init__("System Architect", "Converts requirements to high-level design")

    async def process(self, context: Architecture) -> Architecture:
        req_count = len(context.requirements)
        if req_count > 5:
            context.summary = f"A complex microservices architecture designed to handle {req_count} key requirements."
        else:
            context.summary = f"A streamlined monolithic or serverless architecture optimized for {req_count} requirements."

        context.next_steps.append("Perform detailed database modeling")
        return context
