# Purpose: Auto-discover tools dynamically

import inspect
import app.tools.sample_tool as sample_tool

TOOLS = {}

for name, func in inspect.getmembers(sample_tool, inspect.isfunction):
    TOOLS[name] = func