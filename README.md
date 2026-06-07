# ArchAgent

An agentic AI assistant system for software architecture engineering and design.

## Features
- **Repo Scanning**: Automatically analyze existing repositories to extract architecture, schemas, and routes using AST parsing.
- **Idea to Architecture**: Convert high-level ideas into detailed system designs via a multi-agent workflow.
- **Interactive API**: FastAPI server to trigger scans and generation.
- **Multi-Agent Workflow**:
  - **Product Analyst**: Idea -> Requirements
  - **System Architect**: Requirements -> High-level Design
  - **Database Architect**: Schemas & Data Modeling
  - **Backend Architect**: API Routes & Algorithms
  - **Security Engineer**: Security hardening & Audits
  - **Infrastructure Architect**: Scaling & Deployment
  - **Review Board**: Quality Assurance

## Getting Started

1. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn pydantic pytest pytest-asyncio
   ```

2. **Run the API**:
   ```bash
   export PYTHONPATH=$PYTHONPATH:.
   uvicorn arch_agent.api.main:app --reload
   ```

3. **Scan a Repository**:
   ```bash
   curl -X POST "http://localhost:8000/scan?path=/path/to/your/repo"
   ```

4. **Generate Architecture from Idea**:
   ```bash
   curl -X POST "http://localhost:8000/generate-architecture?idea=Build a secure cloud-native e-commerce platform"
   ```

## LLM Integration

To integrate real LLMs (e.g., OpenAI, Anthropic):
1. Update `arch_agent/core/agent.py` to include an LLM client.
2. In each agent's `process` method, replace the heuristic logic with a prompt to the LLM.
3. Use Pydantic's `model_validate_json` to parse the LLM's response into the structured models.

## Structure
- `arch_agent/core`: Orchestration and base agent logic.
- `arch_agent/agents`: Specialized agent implementations.
- `arch_agent/tools`: Repository scanning and diagram generation.
- `arch_agent/api`: FastAPI server.
