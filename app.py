import asyncio
import os
from pathlib import Path

# 读取 HF 提供的 PORT 环境变量
port = int(os.getenv("PORT", 7860))
os.environ.setdefault("API_PORT", str(port))
os.environ.setdefault("WEB_PORT", str(port))
os.environ.setdefault("TZ", "Asia/Shanghai")

# 创建必要的目录
for directory in ["data", "logs", "backups", "static/uploads/images"]:
    Path(directory).mkdir(parents=True, exist_ok=True)

# 导入并运行主程序
from Start import main
import uvicorn

if __name__ == "__main__":
    # 直接用指定端口启动 uvicorn
    uvicorn.run("reply_server:app", host="0.0.0.0", port=port, reload=False)
