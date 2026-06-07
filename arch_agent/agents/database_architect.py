from arch_agent.core.agent import BaseAgent
from arch_agent.core.models import Architecture, Schema

class DatabaseArchitectAgent(BaseAgent):
    def __init__(self):
        super().__init__("Database Architect", "Designs data schemas")

    async def process(self, context: Architecture) -> Architecture:
        context.schemas.append(Schema(table_name="users", columns={"id": "UUID", "username": "VARCHAR", "password_hash": "VARCHAR"}))
        return context
