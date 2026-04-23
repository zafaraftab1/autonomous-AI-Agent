# Purpose: Streaming endpoint

from fastapi.responses import StreamingResponse
from app.agent.agent import run_agent_stream

@router.post("/chat/stream")
async def chat_stream(request: ChatRequest):

    generator = run_agent_stream(request.user_id, request.message)

    return StreamingResponse(generator, media_type="text/plain")