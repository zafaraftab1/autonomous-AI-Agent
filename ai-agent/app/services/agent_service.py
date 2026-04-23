# Purpose: Add memory tracking

from app.agent.agent import run_agent_logic
from app.memory.chat_memory import add_message

async def run_agent(user_id: str, message: str) -> str:

    add_message(user_id, message)

    response = run_agent_logic(user_id, message)

    add_message(user_id, response)

    return response