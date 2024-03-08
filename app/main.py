from fastapi import FastAPI
from .api.v1.probes.web_query_prober import probe_router

app = FastAPI()

app.include_router(probe_router)

@app.get("/")
def root(): 
    return { "message": "This is root!" }

