import pytest
from arch_agent.core.models import Architecture
from arch_agent.core.orchestrator import Orchestrator
from arch_agent.agents.product_analyst import ProductAnalystAgent
from arch_agent.agents.system_architect import SystemArchitectAgent

@pytest.mark.asyncio
async def test_orchestrator_workflow():
    orchestrator = Orchestrator()
    orchestrator.add_agent(ProductAnalystAgent())
    orchestrator.add_agent(SystemArchitectAgent())

    initial_context = Architecture(name="Test Project", summary="Test Summary")
    final_context = await orchestrator.run_workflow(initial_context)

    assert len(final_context.requirements) > 0
    assert "architecture" in final_context.summary
