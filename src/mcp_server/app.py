from fastapi import FastAPI
from health import router as health_router
from memory_tools import router as memory_router
from database import engine
from models import Base

app = FastAPI(title="AI Academic Advisor MCP Server")

Base.metadata.create_all(bind=engine)

app.include_router(health_router)
app.include_router(memory_router)


@app.get("/")
def root():
    return {"message": "MCP Server Running"}