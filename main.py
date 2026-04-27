from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="大狗智能体后端")

# 示例数据
ip_accounts = []
materials = []
data_board = []
ai_videos = []

# 示例模型
class IPAccount(BaseModel):
    name: str
    ip: str

# 接口示例
@app.get("/ip_accounts")
def get_ip_accounts():
    return {"data": ip_accounts}

@app.post("/ip_accounts")
def create_ip_account(account: IPAccount):
    ip_accounts.append(account.dict())
    return {"message": "新增成功", "data": account.dict()}

@app.get("/materials")
def get_materials():
    return {"data": materials}

@app.get("/data_board")
def get_data_board():
    return {"data": data_board}

@app.get("/ai_videos")
def get_ai_videos():
    return {"data": ai_videos}

# 可按需增加其他接口