# chat_interface.py
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import json
import random

app = FastAPI()

# 加载训练数据
try:
    with open('training_data.json', 'r', encoding='utf-8') as f:
        training_data = json.load(f)
except:
    # 如果无法加载训练数据，使用空列表
    training_data = []

class ChatRequest(BaseModel):
    user_input: str

@app.post("/api/chat")
async def handle_chat_request(request: ChatRequest):
    """
    处理聊天请求，模拟用户A的语言风格生成响应。

    参数:
        request (ChatRequest): 包含用户输入的请求对象。

    返回:
        dict: 包含机器人响应的字典。
    """
    user_input = request.user_input

    # 随机选择一条训练数据作为响应
    if training_data:
        response_data = random.choice(training_data)
        bot_response = response_data['response']
    else:
        bot_response = "嗯，我在这里，有什么我可以帮你的吗？"

    return {"bot_response": bot_response}

@app.get("/")
async def read_root():
    """
    返回聊天界面的HTML页面。
    """
    from fastapi.responses import HTMLResponse
    return HTMLResponse(content="""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <meta charset="UTF-8">
    <head>
        <title>聊天测试界面</title>
    </head>
    <body>
        <h1>与用户A聊天</h1>
        <div id="chat-box" style="border: 1px solid #ccc; padding: 10px; height: 300px; overflow-y: scroll;"></div>
        <input type="text" id="user-input" placeholder="输入你的消息..." style="width: 80%; padding: 10px;">
        <button onclick="sendMessage()" style="padding: 10px;">发送</button>
        <script>
            async function sendMessage() {
                const userInput = document.getElementById('user-input').value;
                if (!userInput) return;

                const response = await fetch('/api/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ user_input: userInput }),
                });

                const data = await response.json();
                const chatBox = document.getElementById('chat-box');
                chatBox.innerHTML += `<p><strong>你:</strong> ${userInput}</p>`;
                chatBox.innerHTML += `<p><strong>用户A:</strong> ${data.bot_response}</p>`;
                chatBox.scrollTop = chatBox.scrollHeight;
                document.getElementById('user-input').value = '';
            }
        </script>
    </body>
    </html>
    """, media_type="text/html; charset=utf-8")