from arch_agent.core.agent import BaseAgent
from arch_agent.core.models import Architecture, SecurityFeature

class SecurityEngineerAgent(BaseAgent):
    def __init__(self):
        super().__init__("Security Engineer", "Identifies vulnerabilities and suggests hardening")

    async def process(self, context: Architecture) -> Architecture:
        if not context.security_features:
            context.security_features = []
        context.security_features.append(SecurityFeature(feature="Input Sanitization", description="Prevent SQL Injection and XSS", type="Hardening"))
        return context
