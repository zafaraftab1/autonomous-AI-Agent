# Purpose: Stream response from Ollama

import requests
import json
from app.core.config import settings

def stream_response(prompt: str):
    """
    Streams response from Ollama token by token
    """

    response = requests.post(
        f"{settings.OLLAMA_URL}/api/generate",
        json={
            "model": "phi3",
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            yield data.get("response", "")