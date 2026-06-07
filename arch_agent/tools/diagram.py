from arch_agent.core.models import Architecture

class DiagramGenerator:
    def generate_mermaid(self, arch: Architecture) -> str:
        lines = ["graph TD"]

        # Add high-level components from infrastructure
        if arch.infrastructure:
            for infra in arch.infrastructure:
                comp = infra.component.replace(' ', '_').replace('-', '_')
                depl = infra.deployment.replace(' ', '_').replace('-', '_')
                lines.append(f"    {comp} --> {depl}")

        # Add routes
        if arch.routes:
            lines.append("    subgraph API_Routes")
            for route in arch.routes:
                path_id = route.path.replace('/', '_').replace('-', '_').replace(':', '_')
                if not path_id or path_id == '_': path_id = 'root'
                lines.append(f"        {route.method}_{path_id}['{route.method} {route.path}']")
            lines.append("    end")

        return "\n".join(lines)
