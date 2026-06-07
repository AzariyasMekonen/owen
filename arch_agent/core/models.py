from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Requirement(BaseModel):
    id: str
    description: str
    priority: str = "Medium"

class Schema(BaseModel):
    table_name: str
    columns: Dict[str, str]
    relationships: List[str] = []

class Route(BaseModel):
    path: str
    method: str
    description: str
    parameters: List[str] = []

class SecurityVulnerability(BaseModel):
    severity: str
    description: str
    mitigation: str

class Infrastructure(BaseModel):
    component: str
    scaling_strategy: str
    deployment: str

class Architecture(BaseModel):
    name: str
    summary: str
    requirements: List[Requirement] = []
    schemas: List[Schema] = []
    routes: List[Route] = []
    security_issues: List[SecurityVulnerability] = []
    infrastructure: List[Infrastructure] = []
    next_steps: List[str] = []
