from fastapi import FastAPI
from routers import chat

app = FastAPI(title="LLM Agent API")
app.include_router(chat.router, prefix="/api")
