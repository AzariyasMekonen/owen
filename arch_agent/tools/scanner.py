import ast
import os
import re
from arch_agent.core.models import Architecture, Route, Schema

class RepoScanner:
    def scan(self, path: str) -> Architecture:
        arch = Architecture(name=os.path.basename(path), summary="Scanned architecture")

        for root, dirs, files in os.walk(path):
            if '.git' in dirs:
                dirs.remove('.git')
            if 'node_modules' in dirs:
                dirs.remove('node_modules')

            for file in files:
                filepath = os.path.join(root, file)
                if file.endswith('.py'):
                    self._analyze_python(filepath, arch)
                elif file.endswith(('.js', '.ts', '.tsx', '.jsx')):
                    self._analyze_js_ts(filepath, arch)
                elif file.endswith('.go'):
                    self._analyze_go(filepath, arch)

        return arch

    def _analyze_python(self, filepath: str, arch: Architecture):
        try:
            with open(filepath, "r") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and hasattr(node.func, 'attr'):
                    if node.func.attr in ['get', 'post', 'put', 'delete', 'patch']:
                        if node.args and isinstance(node.args[0], ast.Constant):
                            arch.routes.append(Route(
                                path=node.args[0].value,
                                method=node.func.attr.upper(),
                                description=f"Found in {os.path.basename(filepath)}"
                            ))

                if isinstance(node, ast.ClassDef):
                    for base in node.bases:
                        if isinstance(base, ast.Name) and base.id == 'BaseModel':
                            columns = {}
                            for item in node.body:
                                if isinstance(item, ast.AnnAssign) and isinstance(item.target, ast.Name):
                                    columns[item.target.id] = "unknown"
                            arch.schemas.append(Schema(table_name=node.name, columns=columns))
        except Exception as e:
            arch.next_steps.append(f"Error parsing Python {filepath}: {str(e)}")

    def _analyze_js_ts(self, filepath: str, arch: Architecture):
        try:
            with open(filepath, "r") as f:
                content = f.read()

            # Simple regex for Express/Fastify routes
            route_matches = re.finditer(r'\.(get|post|put|delete|patch)\s*\(\s*[\'"]([^\'"]+)[\'"]', content)
            for match in route_matches:
                arch.routes.append(Route(
                    path=match.group(2),
                    method=match.group(1).upper(),
                    description=f"Found in {os.path.basename(filepath)}"
                ))

            # Simple regex for interface/type/class as schemas
            schema_matches = re.finditer(r'(interface|type|class)\s+(\w+)\s*\{', content)
            for match in schema_matches:
                arch.schemas.append(Schema(table_name=match.group(2), columns={}))
        except Exception as e:
            arch.next_steps.append(f"Error parsing JS/TS {filepath}: {str(e)}")

    def _analyze_go(self, filepath: str, arch: Architecture):
        try:
            with open(filepath, "r") as f:
                content = f.read()

            # Simple regex for Go http routes
            route_matches = re.finditer(r'\.Handle(Func)?\s*\(\s*[\'"]([^\'"]+)[\'"]', content)
            for match in route_matches:
                arch.routes.append(Route(
                    path=match.group(2),
                    method="UNKNOWN",
                    description=f"Found in {os.path.basename(filepath)}"
                ))

            # Simple regex for Go structs
            schema_matches = re.finditer(r'type\s+(\w+)\s+struct\s*\{', content)
            for match in schema_matches:
                arch.schemas.append(Schema(table_name=match.group(1), columns={}))
        except Exception as e:
            arch.next_steps.append(f"Error parsing Go {filepath}: {str(e)}")
