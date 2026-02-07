from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    user_id: str = None
    session_id: str = None

class ChatResponse(BaseModel):
    response: str
