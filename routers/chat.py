from fastapi import APIRouter
from datetime import datetime
import time
from agents.ollama import OllamaAgent, generate_ids
from db.sqlite import insert_chat
from models.chat import ChatRequest, ChatResponse

router = APIRouter()
agent = OllamaAgent()

@router.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    start_time = time.time()
    response = await agent.run(req.message)
    processing_time = time.time() - start_time
    user_id, session_id = generate_ids(req.user_id, req.session_id)
    insert_chat({
        "message": req.message,
        "response": response,
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "user_id": user_id,
        "session_id": session_id,
        "intent": "general_chat",
        "response_length": len(response),
        "language": "fa",
        "processing_time": processing_time,
        "tool_used": "OllamaAgent"
    })
    return {"response": response}
