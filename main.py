from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="大狗智能体后端")

# 数据存储示例
ip_accounts = []

class IPAccount(BaseModel):
    name: str
    ip: str

# 获取所有 IP 账户
@app.get("/ip_accounts")
def get_ip_accounts():
    return {"data": ip_accounts}

# 添加新的 IP 账户
@app.post("/ip_accounts")
def create_ip_account(account: IPAccount):
    ip_accounts.append(account.dict())
    return {"message": "新增成功", "data": account.dict()}

# 测试接口
@app.get("/ping")
def ping():
    return {"message": "pong"}