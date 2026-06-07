from abc import ABC, abstractmethod
from arch_agent.core.models import Architecture

class BaseAgent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    async def process(self, context: Architecture) -> Architecture:
        pass
