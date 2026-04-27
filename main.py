from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# -------------------------
# 模型定义
# -------------------------
class IPAccount(BaseModel):
    ip: str
    username: str
    password: str

# -------------------------
# 内存数据库（临时存储）
# -------------------------
ip_accounts_db: List[IPAccount] = []

# -------------------------
# 首页
# -------------------------
@app.get("/")
def home():
    return {"message": "大狗智能体后端运行中"}

# -------------------------
# POST /ip_account - 添加 IP 账号
# -------------------------
@app.post("/ip_account")
def add_ip_account(account: IPAccount):
    ip_accounts_db.append(account)
    return {"status": "success", "account": account}

# -------------------------
# GET /ip_accounts - 获取所有 IP 账号
# -------------------------
@app.get("/ip_accounts")
def get_ip_accounts():
    return {"accounts": ip_accounts_db}

# -------------------------
# 示例：其他接口可以在这里继续添加
# -------------------------
# @app.post("/generate_copy")
# def generate_copy():
#     pass