# Purpose: Central orchestrator using pipeline

from app.agent.pipeline import AgentPipeline
from app.agent.steps import (
    memory_step,
    rag_step,
    decision_step,
    tool_step,
    response_step
)

pipeline = AgentPipeline([
    memory_step,
    rag_step,
    decision_step,
    tool_step,
    response_step
])


def run_agent_logic(user_id: str, message: str) -> str:

    context = {
        "user_id": user_id,
        "message": message
    }

    result = pipeline.run(context)

    return result.get("response")

# Purpose: Streaming version of agent

from app.llm.ollama_client import stream_response

def run_agent_stream(user_id: str, message: str):
    """
    Same logic but streams final response
    """

    # reuse existing pipeline
    context = {
        "user_id": user_id,
        "message": message
    }

    result = pipeline.run(context)

    final_prompt = result.get("response")

    # stream response
    return stream_response(final_prompt)