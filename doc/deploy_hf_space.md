# 部署到 Hugging Face Spaces

本文档说明如何将 xianyu-auto-reply 部署到 Hugging Face Spaces。

## 前置条件

- Hugging Face 账户（免费注册于 https://huggingface.co）
- 本仓库已 fork 或你拥有访问权限
- 必要的环境变量和密钥准备好

## 部署文件说明

本仓库新增以下文件以支持 HF Space 部署：

- **app.py** - HF Space 的入口点，配置端口和初始化必要目录
- **apt.txt** - 系统级依赖列表（Chromium、字体、X11 库等）
- **postBuild** - 构建后脚本，用于安装 Playwright 浏览器

## 创建 HF Space 的步骤

### 1. 创建新 Space
- 访问 https://huggingface.co/new-space
- 填写信息：
  - **Space 名称**：任意（如 `xianyu-auto-reply`）
  - **所有者**：选择你的用户名或组织
  - **License**：选择合适的开源协议
  - **Space SDK**：选择 **Docker**
  - **Visibility**：选择 Private（因为包含敏感配置）

### 2. 连接仓库
- Space 创建后，选择 "Connect a repo from Git"
- 粘贴你的仓库 URL：`https://github.com/liye-hk/xianyu-auto-reply`
- 选择分支（通常是 `main` 或 `master`）

### 3. 配置环境变量和密钥
在 Space 设置中添加以下环境变量（根据你的实际配置）：

**必需（示例）**：
- `COOKIES_STR` - 你的闲鱼账户 Cookie（从浏览器复制）
- `OPENAI_API_KEY` - OpenAI API 密钥（如使用 AI 功能）

**可选**：
- `OPENAI_API_BASE` - OpenAI API 基础 URL（如使用代理）
- `SMTP_HOST` - 邮件服务器地址
- `SMTP_USER` - 邮件账户
- `SMTP_PASSWORD` - 邮件密码
- `TZ` - 时区（默认 `Asia/Shanghai`）

**在 Space Settings → Secrets 中添加敏感信息**

### 4. 部署启动
- 保存设置后，HF Space 自动开始构建
- 首次构建需要 5-15 分钟（取决于依赖安装）
- 查看 "Building" 页面的日志以跟踪进度

## 验证部署

部署成功后：
- Space 状态变为 "Running"（绿色指示）
- 访问 Space URL（如 `https://huggingface.co/spaces/your-username/xianyu-auto-reply`）
- 应该看到登录或管理界面
- 检查浏览器开发者工具查看是否有错误

## 存储与持久化

- **data/** - 包含数据库和持久化数据
- **logs/** - 应用日志
- **backups/** - 备份文件
- **static/uploads/images/** - 上传的图片

**注意**：HF Space 的持久化存储有限制，长期运行可能需要额外考虑数据备份。

## 常见问题

### 1. Playwright 下载缓慢或超时
- 这是常见的问题，可在 Space 设置中增加构建超时时间
- 或在本地预构建 Playwright 并添加到仓库

### 2. 权限被拒绝
- 确保 `postBuild` 有执行权限：`chmod +x postBuild`
- 或检查文件编码是否为 UTF-8（无 BOM）

### 3. 端口错误或无法访问
- HF Space 自动将应用绑定到 `0.0.0.0:7860`
- `app.py` 会自动读取 `PORT` 环境变量

### 4. 环境变量未生效
- 修改环境变量后需要重启 Space（点击 "Restart this Space"）
- 某些变量可能需要在构建时而非运行时设置

### 5. 更新代码
- 推送代码到 GitHub 后，HF Space 会自动检测并重新构建
- 手动重启可访问 Space 设置中的 "Restart this Space"

## 高级配置

### 自定义硬件（可选付费）
- 默认为免费 CPU 硬件
- 可升级到 GPU 或更高配置（需付费）
- 在 Space Settings → Hardware 中配置

### 持久性存储
- 启用 "Persistent Storage" 以保留 data、logs 等目录
- 这样即使 Space 重启也不会丢失数据

### 私有仓库
- 如果使用私有 GitHub 仓库，需要在 Space 中配置 GitHub token

## 监控和调试

- **实时日志**：在 Space 页面查看 "Logs" 标签
- **Space 状态**：绿色 Running = 正常，红色 = 需要调查
- **重新构建**：在 Settings 中点击 "Rebuild space" 强制重新构建

## 更多资源

- HF Space 官方文档：https://huggingface.co/docs/hub/spaces
- Docker 运行时指南：https://huggingface.co/docs/hub/spaces-docker
