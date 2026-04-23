# Purpose: Modular pipeline for agent execution (extensible)

class AgentPipeline:

    def __init__(self, steps):
        self.steps = steps

    def run(self, context: dict):
        """
        Runs each step sequentially
        """
        for step in self.steps:
            context = step(context)
        return context



pipeline = AgentPipeline([
    memory_step,
    rag_step,
    decision_step,
    guardrail_step,
    tool_step,
    response_step
])