from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Requirement(BaseModel):
    id: str
    description: str
    priority: str = "Medium"

class Schema(BaseModel):
    table_name: str
    columns: Dict[str, str] = {}
    relationships: List[str] = []

class Route(BaseModel):
    path: str
    method: str
    description: str = ""
    parameters: List[str] = []

class SecurityFeature(BaseModel):
    feature: str
    description: str
    type: str = "Authentication" # Authentication, Authorization, etc.

class Integration(BaseModel):
    service: str
    protocol: str
    description: str

class Algorithm(BaseModel):
    name: str
    logic: str
    complexity: str = "O(1)"

class Infrastructure(BaseModel):
    component: str
    scaling_strategy: str
    deployment: str

class Architecture(BaseModel):
    name: str
    summary: str
    stack: List[str] = []
    requirements: List[Requirement] = []
    schemas: List[Schema] = []
    routes: List[Route] = []
    security_features: List[SecurityFeature] = []
    integrations: List[Integration] = []
    algorithms: List[Algorithm] = []
    infrastructure: List[Infrastructure] = []
    next_steps: List[str] = []
