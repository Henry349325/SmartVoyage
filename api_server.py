from fastapi import FastAPI
from pydantic import BaseModel
from main import initialize_system, process_user_input
import uvicorn

# 初始化 Agent 系统 (这步在启动 FastAPI 时只执行一次)
initialize_system()

app = FastAPI(title="SmartVoyage API", description="基于A2A协议的多智能体旅行助手")

# 定义请求体格式
class ChatRequest(BaseModel):
    query: str

# 定义聊天接口
@app.post("/chat")
def chat(req: ChatRequest):
    # 调用你原有的处理逻辑
    response = process_user_input(req.query)
    return {"reply": response}

# 启动命令：python api_server.py
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
