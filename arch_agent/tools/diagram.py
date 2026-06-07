from arch_agent.core.models import Architecture

class DiagramGenerator:
    def generate_mermaid(self, arch: Architecture) -> str:
        lines = ["graph TD"]

        # Add high-level components from summary or infrastructure
        if arch.infrastructure:
            for infra in arch.infrastructure:
                lines.append(f"    {infra.component.replace(' ', '_')} --> {infra.deployment}")

        # Add routes
        if arch.routes:
            lines.append("    subgraph API_Routes")
            for route in arch.routes:
                lines.append(f"        {route.method}_{route.path.replace('/', '_')}['{route.method} {route.path}']")
            lines.append("    end")

        return "\n".join(lines)

if __name__ == "__main__":
    from arch_agent.core.models import Infrastructure, Route
    test_arch = Architecture(name="Test", summary="Test Arch")
    test_arch.infrastructure.append(Infrastructure(component="Web App", scaling_strategy="None", deployment="Cloud"))
    test_arch.routes.append(Route(path="/api/test", method="GET", description="Test"))

    gen = DiagramGenerator()
    print(gen.generate_mermaid(test_arch))
