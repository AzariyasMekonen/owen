from arch_agent.core.agent import BaseAgent
from arch_agent.core.models import Architecture, SecurityVulnerability

class SecurityEngineerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Security Engineer", "Identifies vulnerabilities and suggests hardening")

    async def process(self, context: Architecture) -> Architecture:
        context.security_issues.append(SecurityVulnerability(severity="High", description="Potential for SQL Injection if inputs aren't sanitized", mitigation="Use parameterized queries"))
        return context
