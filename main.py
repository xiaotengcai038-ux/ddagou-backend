from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="大狗智能体后端")

# -------------------------
# 数据模型
# -------------------------
class IPAccount(BaseModel):
    ip: str
    username: str
    password: str

class CopyRequest(BaseModel):
    source_id: str
    target_id: str

# -------------------------
# 内存数据库（示例）
# -------------------------
ip_accounts_db: List[IPAccount] = []
content_calendar_db: List[Dict] = [{"id":1,"content":"示例日程"}]
knowledge_base_db: List[Dict] = [{"id":1,"knowledge":"示例知识"}]
materials_db: List[Dict] = [{"id":1,"material":"示例素材"}]
data_board_db: List[Dict] = [{"id":1,"stat":"示例统计"}]
deep_learning_samples_db: List[Dict] = [{"id":1,"sample":"示例深度学习样本"}]

# -------------------------
# 根路径
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
# POST /generate_copy
# -------------------------
@app.post("/generate_copy")
def generate_copy(req: CopyRequest):
    generated = f"文案已从 {req.source_id} 生成到 {req.target_id}"
    return {"generated_copy": generated}

# -------------------------
# GET /content_calendar
# -------------------------
@app.get("/content_calendar")
def get_content_calendar():
    return {"data": content_calendar_db}

# -------------------------
# GET /knowledge_base
# -------------------------
@app.get("/knowledge_base")
def get_knowledge_base():
    return {"data": knowledge_base_db}

# -------------------------
# GET /materials
# -------------------------
@app.get("/materials")
def get_materials():
    return {"data": materials_db}

# -------------------------
# GET /data_board
# -------------------------
@app.get("/data_board")
def get_data_board():
    return {"data": data_board_db}

# -------------------------
# GET /deep_learning_samples
# -------------------------
@app.get("/deep_learning_samples")
def get_deep_learning_samples():
    return {"data": deep_learning_samples_db}