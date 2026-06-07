import ast
import os
from arch_agent.core.models import Architecture, Route, Schema

class RepoScanner:
    def scan(self, path: str) -> Architecture:
        arch = Architecture(name=os.path.basename(path), summary="Scanned architecture")

        for root, dirs, files in os.walk(path):
            if '.git' in dirs:
                dirs.remove('.git')

            for file in files:
                if file.endswith('.py'):
                    self._analyze_file(os.path.join(root, file), arch)

        return arch

    def _analyze_file(self, filepath: str, arch: Architecture):
        try:
            with open(filepath, "r") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                # Look for FastAPI/Flask style routes
                if isinstance(node, ast.Call) and hasattr(node.func, 'attr'):
                    if node.func.attr in ['get', 'post', 'put', 'delete', 'patch']:
                        if node.args and isinstance(node.args[0], ast.Constant):
                            arch.routes.append(Route(
                                path=node.args[0].value,
                                method=node.func.attr.upper(),
                                description=f"Found in {os.path.basename(filepath)}"
                            ))

                # Look for Pydantic models as a proxy for schemas
                if isinstance(node, ast.ClassDef):
                    for base in node.bases:
                        if isinstance(base, ast.Name) and base.id == 'BaseModel':
                            columns = {}
                            for item in node.body:
                                if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                                    columns[item.target.id] = "unknown" # Could improve with type extraction
                            arch.schemas.append(Schema(table_name=node.name, columns=columns))
        except Exception as e:
            arch.next_steps.append(f"Error parsing {filepath}: {str(e)}")
