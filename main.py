from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# =======================
# 根路径，避免 404
# =======================
@app.get("/")
def home():
    return {"message": "大狗智能体后端运行中"}

# =======================
# 数据模型
# =======================
class IPAccount(BaseModel):
    ip: str = "示例IP"
    account: str = "示例账户"

class GenerateCopyRequest(BaseModel):
    content: str = "示例内容"

# =======================
# 示例数据（可改为数据库）
# =======================
ip_accounts_db = []
content_calendar_db = [{"id": 1, "content": "示例日程"}]
knowledge_base_db = [{"id": 1, "knowledge": "示例知识"}]
materials_db = [{"id": 1, "material": "示例素材"}]
data_board_db = [{"id": 1, "stat": "示例统计"}]
deep_learning_samples_db = [{"id": 1, "sample": "示例深度学习样本"}]

# =======================
# 接口
# =======================

# POST /ip_account
@app.post("/ip_account")
def add_ip_account(ip_account: IPAccount = IPAccount()):
    ip_accounts_db.append(ip_account.dict())
    return {"message": "IP账户添加成功", "data": ip_account}

# GET /ip_accounts
@app.get("/ip_accounts")
def get_ip_accounts():
    return {"data": ip_accounts_db}

# POST /generate_copy
@app.post("/generate_copy")
def generate_copy(req: GenerateCopyRequest = GenerateCopyRequest()):
    generated = req.content + " - 生成文案示例"
    return {"generated_copy": generated}

# GET /content_calendar
@app.get("/content_calendar")
def get_content_calendar():
    return {"data": content_calendar_db}

# GET /knowledge_base
@app.get("/knowledge_base")
def get_knowledge_base():
    return {"data": knowledge_base_db}

# GET /materials
@app.get("/materials")
def get_materials():
    return {"data": materials_db}

# GET /data_board
@app.get("/data_board")
def get_data_board():
    return {"data": data_board_db}

# GET /deep_learning_samples
@app.get("/deep_learning_samples")
def get_deep_learning_samples():
    return {"data": deep_learning_samples_db}