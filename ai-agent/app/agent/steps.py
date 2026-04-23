# Purpose: Each step is independent and reusable

from app.memory.vector_store import vector_store
from app.memory.chat_memory import get_history
from app.llm.ollama_client import generate_response
from app.tools.tool_registry import TOOLS
import json


def memory_step(context):
    user_id = context["user_id"]
    context["history"] = get_history(user_id)
    return context


def rag_step(context):
    message = context["message"]
    context["retrieved_docs"] = vector_store.search(message)
    return context


def decision_step(context):
    message = context["message"]

    prompt = f"""
    Tools:
    - get_user_details(user_id)

    Return JSON:
    {{
      "action": "...",
      "input": {{}}
    }}

    Query: {message}
    """

    response = generate_response(prompt)

    try:
        context["decision"] = json.loads(response)
    except:
        context["decision"] = {"action": "none", "input": {}}

    return context


def tool_step(context):
    decision = context["decision"]
    action = decision.get("action")

    if action in TOOLS:
        try:
            result = TOOLS[action](**decision.get("input", {}))
            context["tool_output"] = result
        except Exception as e:
            context["tool_output"] = f"Error: {str(e)}"
    return context


def response_step(context):
    if "tool_output" in context:
        context["response"] = context["tool_output"]
        return context

    prompt = f"""
    History: {context.get("history")}
    Context: {context.get("retrieved_docs")}
    User: {context.get("message")}
    """

    context["response"] = generate_response(prompt)
    return context