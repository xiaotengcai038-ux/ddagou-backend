# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="大狗智能体后端")

# ------------------------------
# 数据模型示例
# ------------------------------
class IPAccount(BaseModel):
    ip: str
    account: str

class CopyRequest(BaseModel):
    source_id: str
    target_id: str

# 模拟数据库（内存）
ip_accounts_db: List[IPAccount] = []
content_calendar_db: List[Dict] = []
knowledge_base_db: List[Dict] = []
materials_db: List[Dict] = []
data_board_db: List[Dict] = []
deep_learning_samples_db: List[Dict] = []

# ------------------------------
# 根接口
# ------------------------------
@app.get("/")
def home():
    return {"message": "大狗智能体后端运行中"}

# ------------------------------
# IP 账号接口
# ------------------------------
@app.post("/ip_account")
def add_ip_account(account: IPAccount):
    ip_accounts_db.append(account)
    return {"status": "success", "account": account}

@app.get("/ip_accounts")
def get_ip_accounts():
    return {"accounts": ip_accounts_db}

# ------------------------------
# 文案生成接口
# ------------------------------
@app.post("/generate_copy")
def generate_copy(req: CopyRequest):
    # 这里写你的生成逻辑，我先返回示例
    return {"status": "success", "message": f"文案已从 {req.source_id} 生成到 {req.target_id}"}

# ------------------------------
# 内容日历接口
# ------------------------------
@app.get("/content_calendar")
def get_content_calendar():
    return {"content_calendar": content_calendar_db}

# ------------------------------
# 知识库接口
# ------------------------------
@app.get("/knowledge_base")
def get_knowledge_base():
    return {"knowledge_base": knowledge_base_db}

# ------------------------------
# 素材接口
# ------------------------------
@app.get("/materials")
def get_materials():
    return {"materials": materials_db}

# ------------------------------
# 数据看板接口
# ------------------------------
@app.get("/data_board")
def get_data_board():
    return {"data_board": data_board_db}

# ------------------------------
# 深度学习示例接口
# ------------------------------
@app.get("/deep_learning_samples")
def get_deep_learning_samples():
    return {"samples": deep_learning_samples_db}