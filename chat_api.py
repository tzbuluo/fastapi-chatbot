# chat_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

class ChatRequest(BaseModel):
    session_id: str = None
    model_id: str
    user_input: str

@app.post("/api/chat")
async def handle_chat_request(request: ChatRequest):
    # Call Tencent Cloud DeepSeek API
    tencent_url = "https://tencent_api_gateway/deepseek/chat"
    headers = {"X-API-Key": "your_api_key"}
    payload = {
        "session_id": request.session_id,
        "model_id": request.model_id,
        "user_input": request.user_input
    }

    response = requests.post(tencent_url, headers=headers, json=payload)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="DeepSeek服务异常")

    return {
        "session_id": response.json().get("session_id"),
        "bot_response": response.json().get("bot_response"),
        "status": "success"
    }