from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="大狗智能体后端")

# 内存存储示例
ip_accounts = []

# 数据模型
class IPAccount(BaseModel):
    name: str
    ip: str

# 测试接口
@app.get("/ping")
def ping():
    return {"message": "pong"}

# 获取所有 IP 账户
@app.get("/ip_accounts")
def get_ip_accounts():
    return {"data": ip_accounts}

# 添加新的 IP 账户
@app.post("/ip_accounts")
def create_ip_account(account: IPAccount):
    for a in ip_accounts:
        if a["ip"] == account.ip:
            raise HTTPException(status_code=400, detail="IP 已存在")
    ip_accounts.append(account.dict())
    return {"message": "新增成功", "data": account.dict()}

# 删除 IP 账户
@app.delete("/ip_accounts/{ip}")
def delete_ip_account(ip: str):
    global ip_accounts
    ip_accounts = [a for a in ip_accounts if a["ip"] != ip]
    return {"message": f"删除 {ip} 成功"}

# 更新 IP 账户
@app.put("/ip_accounts/{ip}")
def update_ip_account(ip: str, account: IPAccount):
    for i, a in enumerate(ip_accounts):
        if a["ip"] == ip:
            ip_accounts[i] = account.dict()
            return {"message": "更新成功", "data": account.dict()}
    raise HTTPException(status_code=404, detail="IP 未找到")