from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI(title="大狗超级获客智能体")

# 示例 IP 账号
class IPAccount(BaseModel):
    id: int
    name: str
    industry: str
    product: str
    persona: str
    customer_profile: str

ip_accounts_db: List[IPAccount] = []

@app.post('/ip_account')
def create_ip_account(account: IPAccount):
    ip_accounts_db.append(account)
    return {'message': 'IP账号创建成功', 'account': account}

@app.get('/ip_accounts')
def list_ip_accounts():
    return ip_accounts_db

# 文案生成示例
class CopyRequest(BaseModel):
    ip_id: int
    theme: str

@app.post('/generate_copy')
def generate_copy(req: CopyRequest):
    copy_text = f"AI生成文案示例: 针对IP {req.ip_id}, 主题 {req.theme}"
    return {'copy': copy_text}

# 其它模块接口
content_calendar: List[Dict] = [{'date': '2026-04-27', 'title': '示例内容'}]
knowledge_base: List[Dict] = [{'title': '行业指南示例'}]
materials: List[Dict] = [{'name': '示例素材'}]
data_board: Dict = {'total_copies': 5, 'ip_count': len(ip_accounts_db)}

@app.get('/content_calendar')
def get_content_calendar():
    return content_calendar

@app.get('/knowledge_base')
def get_knowledge_base():
    return knowledge_base

@app.get('/materials')
def get_materials():
    return materials

@app.get('/data_board')
def get_data_board():
    return data_board

# 深度学习、爆款选题、AI视频接口示例
deep_learning_samples: List[Dict] = [{'title': '示例文案样本'}]
@app.get('/deep_learning_samples')
def get_deep_learning_samples():
    return deep_learning_samples

hot_topics: List[Dict] = [{'title': '爆款选题示例'}]
@app.get('/hot_topics')
def get_hot_topics():
    return hot_topics

ai_videos: List[Dict] = [{'title': 'AI生成视频示例'}]
@app.get('/ai_videos')
def get_ai_videos():
    return ai_videos