from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="大狗智能体管理")

# -------------------------
# 跨域配置，允许所有来源
# -------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名访问
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有 HTTP 方法
    allow_headers=["*"],  # 允许所有请求头
)

# -------------------------
# 数据模型
# -------------------------
class IPAccount(BaseModel):
    id: int
    name: str
    industry: str
    product: str
    persona: str = ""
    customer_profile: str = ""

class CopyRequest(BaseModel):
    ip_id: int
    topic: str

# -------------------------
# 数据存储（示例）
# -------------------------
ip_accounts = {}

# -------------------------
# 创建 IP 账号
# -------------------------
@app.post("/ip_account")
def create_ip_account(account: IPAccount):
    if account.id in ip_accounts:
        return {"message": "IP账号已存在", "account": ip_accounts[account.id]}
    
    ip_accounts[account.id] = account.dict()
    return {"message": "IP账号创建成功", "account": ip_accounts[account.id]}

# -------------------------
# 生成文案
# -------------------------
@app.post("/generate_copy")
def generate_copy(req: CopyRequest):
    if req.ip_id not in ip_accounts:
        return {"detail": "IP账号不存在"}

    account = ip_accounts[req.ip_id]
    copy_text = f"AI生成文案示例: 针对IP {req.ip_id}, 主题 {req.topic}, 产品 {account['product']}"
    return {"copy": copy_text}

# -------------------------
# 简单示例接口
# -------------------------
@app.get("/ping")
def ping():
    return {"message": "pong"}