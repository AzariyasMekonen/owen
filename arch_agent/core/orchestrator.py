from typing import List
from arch_agent.core.agent import BaseAgent
from arch_agent.core.models import Architecture

class Orchestrator:
    def __init__(self):
        self.agents: List[BaseAgent] = []

    def add_agent(self, agent: BaseAgent):
        self.agents.append(agent)

    async def run_workflow(self, initial_context: Architecture) -> Architecture:
        context = initial_context
        for agent in self.agents:
            print(f"Running agent: {agent.name} ({agent.role})")
            context = await agent.process(context)
        return context
