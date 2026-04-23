from app.memory.load_data import load_knowledge

@app.on_event("startup")
def startup():
    load_knowledge()