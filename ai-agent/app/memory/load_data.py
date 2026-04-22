# Purpose: Load initial knowledge into FAISS

from app.memory.vector_store import vector_store

def load_knowledge():
    """
    Add domain knowledge (can be logs, docs, etc.)
    """

    data = [
        "Pipeline failure happens due to timeout errors",
        "User service runs on port 8000",
        "ETL jobs run every 6 hours",
        "API latency issues caused by DB bottleneck"
    ]

    for item in data:
        vector_store.add(item)