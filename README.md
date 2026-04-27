# 大狗智能体后端

## 部署方式

### Railway
- 自动使用 `uvicorn main:app --host 0.0.0.0 --port $PORT` 启动
- 访问 Railway 提供的域名即可

### 本地调试
```bash
uvicorn main:app --reload