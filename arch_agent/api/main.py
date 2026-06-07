from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from arch_agent.core.models import Architecture
from arch_agent.core.orchestrator import Orchestrator
from arch_agent.agents.product_analyst import ProductAnalystAgent
from arch_agent.agents.system_architect import SystemArchitectAgent
from arch_agent.agents.database_architect import DatabaseArchitectAgent
from arch_agent.agents.backend_architect import BackendArchitectAgent
from arch_agent.agents.security_engineer import SecurityEngineerAgent
from arch_agent.agents.infrastructure_architect import InfrastructureArchitectAgent
from arch_agent.agents.review_board import ReviewBoardAgent
from arch_agent.tools.scanner import RepoScanner
from arch_agent.tools.diagram import DiagramGenerator

app = FastAPI()

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "ArchAgent API is running"}

@app.post("/scan")
async def scan_repo(path: str):
    scanner = RepoScanner()
    arch = scanner.scan(path)
    return arch

@app.post("/generate-architecture")
async def generate_architecture(idea: str):
    orchestrator = Orchestrator()
    orchestrator.add_agent(ProductAnalystAgent())
    orchestrator.add_agent(SystemArchitectAgent())
    orchestrator.add_agent(DatabaseArchitectAgent())
    orchestrator.add_agent(BackendArchitectAgent())
    orchestrator.add_agent(SecurityEngineerAgent())
    orchestrator.add_agent(InfrastructureArchitectAgent())
    orchestrator.add_agent(ReviewBoardAgent())

    initial_context = Architecture(name="New Project", summary=idea)
    final_arch = await orchestrator.run_workflow(initial_context)

    diagram_gen = DiagramGenerator()
    mermaid_diagram = diagram_gen.generate_mermaid(final_arch)

    return {
        "architecture": final_arch,
        "diagram": mermaid_diagram
    }

@app.post("/refine-architecture")
async def refine_architecture(arch: Architecture, feedback: str):
    # Simulate agentic refinement
    orchestrator = Orchestrator()
    # In a real system, we might only add agents relevant to the feedback
    orchestrator.add_agent(ReviewBoardAgent())

    arch.summary += f"\n\nRefined with feedback: {feedback}"
    final_arch = await orchestrator.run_workflow(arch)

    diagram_gen = DiagramGenerator()
    mermaid_diagram = diagram_gen.generate_mermaid(final_arch)

    return {
        "architecture": final_arch,
        "diagram": mermaid_diagram
    }
