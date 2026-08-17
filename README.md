# 🚀 Zero to Tech

> **从 0 开始，构建属于自己的全栈技术空间。**

**Zero to Tech** 是一个正在持续开发中的全栈个人项目。

这个项目从最基础的网页开发开始，逐步加入 **Next.js 前端、Python/FastAPI 后端、REST API、前后端数据交互、Linux 云服务器、Nginx 部署** 等内容。

它既是一个个人技术网站，也是一个用于学习和实践现代全栈开发的长期项目。

---

## 📖 项目简介

为什么叫 **Zero to Tech**？

因为这个项目并不是从一个完整模板开始，而是希望从最基础的代码开始，一步一步搭建：

```text
一个页面
   ↓
一个前端项目
   ↓
一个后端 API
   ↓
前后端通信
   ↓
数据库 / AI / 更多服务
   ↓
Linux 服务器
   ↓
Nginx
   ↓
真正上线
```

在这个过程中，不只是学习某一个框架，而是尝试理解一个完整 Web 项目背后的运行机制：

> **代码是如何运行的？前端和后端是如何通信的？HTTP 请求是如何到达服务器的？一个项目又是如何从本地开发环境部署到云服务器的？**

Zero to Tech 就是对这些问题的持续实践。

---

# ✨ 项目目标

目前项目主要围绕以下几个方向持续完善：

- 🖥️ 构建个人技术主页
- 🎨 探索现代前端开发
- 🔌 实现前后端 API 通信
- 🐍 使用 Python 构建后端服务
- 📦 探索 Next.js 静态导出
- 🌐 使用 Nginx 部署前端
- ☁️ 实践 Ubuntu 云服务器部署
- 🤖 后续逐步加入 AI 能力
- 🗄️ 后续加入数据库与数据持久化
- ⚙️ 持续完善工程化与部署流程

---

# 🛠️ 技术栈

## 前端

| 技术 | 用途 |
|---|---|
| **Next.js 15** | 前端框架 |
| **React** | UI 构建 |
| **JavaScript / TypeScript** | 前端开发 |
| **HTML / CSS** | 页面结构与样式 |
| **npm** | 包管理 |

---

## 后端

| 技术 | 用途 |
|---|---|
| **Python 3.14** | 后端开发 |
| **FastAPI** | REST API 服务 |
| **Pydantic** | 请求数据验证 |
| **JSON** | 前后端数据交换 |
| **HTTP** | 前后端通信 |

项目开发过程中也使用 Python 标准库中的 `http.server` 实现过基础 HTTP API，用于理解 Web Server、HTTP Request 和 HTTP Response 的基本工作机制。

---

## 部署

| 技术 | 用途 |
|---|---|
| **Ubuntu** | 云服务器操作系统 |
| **Nginx** | 静态文件服务器 / 反向代理 |
| **Git** | 版本控制 |
| **GitHub** | 代码托管 |
| **SSH** | 服务器管理 |

---

# 🏗️ 项目架构

目前项目采用前后端分离的基本架构。

```text
                         ┌──────────────────┐
                         │      用户浏览器    │
                         └────────┬─────────┘
                                  │
                         HTTP / HTTPS
                                  │
                                  ▼
                         ┌──────────────────┐
                         │      Nginx       │
                         └────────┬─────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │                           │
                    ▼                           ▼
             静态前端资源                    /api/*
                    │                           │
                    ▼                           ▼
              Next.js out/                  FastAPI
                                                │
                                                ▼
                                          后端业务逻辑
```

开发环境下：

```text
浏览器
  │
  ├── localhost:3000
  │       ↓
  │    Next.js
  │
  └── localhost:8000
          ↓
       FastAPI
          ↓
       API
```

生产环境下：

```text
Internet
    │
    ▼
  Nginx
    │
    ├── 前端静态资源
    │       ↓
    │      out/
    │
    └── /api/*
            ↓
         FastAPI
```

---

# 📂 项目结构

项目结构会随着开发持续调整，目前整体思路如下：

```text
zero-to-tech/
│
├── frontend/                 # Next.js 前端
│   ├── app/                  # 页面与路由
│   ├── components/           # 页面组件
│   ├── public/               # 静态资源
│   └── ...
│
├── backend/                  # Python 后端
│   ├── .venv/                # Python 虚拟环境
│   ├── API 文件
│   └── ...
│
├── next.config.js            # Next.js 配置
├── package.json              # 前端依赖
├── package-lock.json
└── README.md
```

> 注：随着项目持续开发，目录结构可能会发生变化。

---

# 🎨 前端

前端使用 **Next.js 15** 构建。

启动开发服务器：

```bash
npm install
npm run dev
```

默认访问：

```text
http://localhost:3000
```

Next.js 开发模式下第一次访问页面时可能需要进行页面编译，因此第一次加载可能会比后续访问慢。

---

# 📦 Next.js 静态导出

项目目前采用：

```javascript
const nextConfig = {
    output: 'export',
};

export default nextConfig;
```

这一配置意味着：

> 将 Next.js 项目构建为可以直接由 Nginx、Apache 或 CDN 托管的静态网站。

执行：

```bash
npm run build
```

之后会生成：

```text
out/
├── index.html
├── _next/
│   ├── static/
│   └── ...
└── ...
```

这些文件已经是最终的前端生产文件。

因此生产环境不需要通过：

```text
Node.js
    ↓
Next.js Server
    ↓
页面渲染
```

来提供静态页面，而是：

```text
浏览器
   ↓
Nginx
   ↓
out/index.html
```

直接返回。

---

# 🐍 后端

后端使用 Python 构建。

进入后端目录：

```bash
cd backend
```

创建虚拟环境：

```bash
python -m venv .venv
```

### Windows

```powershell
.\.venv\Scripts\Activate.ps1
```

### Ubuntu / Linux

```bash
source .venv/bin/activate
```

安装依赖：

```bash
pip install -r requirements.txt
```

启动 FastAPI：

```bash
python <api-file>.py
```

默认服务地址：

```text
http://localhost:8000
```

---

# 🔌 API

项目目前已经实现基础 API，用于进行前后端数据通信。

---

## GET `/api/profile`

获取个人主页信息。

请求：

```text
GET http://localhost:8000/api/profile
```

返回：

```json
{
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品"
}
```

该接口用于提供前端页面展示所需要的数据。

---

## POST `/api/analyze`

向后端发送文本，并获取分析结果。

请求：

```json
{
    "text": "今天的风很轻，适合把想法写下来"
}
```

返回结果包含：

```json
{
    "text": "...",
    "score": 0.5,
    "label": "...",
    "pinyin": "..."
}
```

目前该 API 主要用于实践：

- POST 请求
- JSON Request Body
- FastAPI 数据验证
- JSON Response
- 前后端数据交互

后续会进一步扩展文本分析能力。

---

# 🧪 API 测试

## 浏览器测试 GET API

可以直接访问：

```text
http://localhost:8000/api/profile
```

如果返回：

```json
{
    "heroTitle": "关于我",
    "heroSubtitle": "项目，创意，灵感，心得，我的作品"
}
```

说明后端服务正常。

---

## Windows PowerShell 测试 POST API

推荐使用：

```powershell
Invoke-RestMethod http://localhost:8000/api/analyze -Method POST -ContentType "application/json" -Body '{"text":"今天的风很轻，适合把想法写下来"}'
```

---

## Linux / macOS 测试

```bash
curl http://localhost:8000/api/analyze \
  -H "Content-Type: application/json" \
  -d '{"text":"今天的风很轻，适合把想法写下来"}'
```

---

# 🔄 前后端通信

前端与后端通过 HTTP API 进行通信。

例如：

```text
Next.js
   │
   │ POST /api/analyze
   │
   │ JSON
   ▼
FastAPI
   │
   │ 数据处理
   ▼
JSON Response
   │
   ▼
Next.js
   │
   ▼
页面展示
```

这也是项目从“单纯的网页”逐渐发展成“全栈应用”的重要一步。

---

# ☁️ 云服务器部署

项目目前使用 **Ubuntu + Nginx** 进行部署。

---

## 1. 获取项目

服务器上：

```bash
git clone https://github.com/Kleon26/zero-to-tech.git
cd zero-to-tech
```

---

## 2. 安装前端依赖

```bash
npm install
```

---

## 3. 构建前端

```bash
npm run build
```

由于配置了：

```javascript
output: 'export'
```

构建成功后会生成：

```text
out/
```

---

## 4. Nginx 托管静态文件

例如：

```nginx
server {
    listen 80;
    server_name your-domain.com;

    root /var/www/zero-to-tech/out;

    location / {
        try_files $uri $uri.html $uri/ =404;
    }
}
```

检查配置：

```bash
sudo nginx -t
```

重新加载：

```bash
sudo systemctl reload nginx
```

---

# ⚙️ 为什么使用 `output: 'export'`？

Next.js 默认情况下可以作为一个需要 Node.js Runtime 的 Web Server 运行：

```text
浏览器
   ↓
Nginx
   ↓
Next.js
   ↓
Node.js
```

而项目目前采用静态导出：

```text
Next.js
   ↓
npm run build
   ↓
out/
   ↓
Nginx
   ↓
浏览器
```

这样做的优点是：

- 不需要常驻 Next.js Node 服务
- 不需要 PM2 管理前端进程
- Nginx 可以直接托管页面
- 部署结构简单
- 静态资源可以方便地使用 CDN
- 服务器资源消耗较低

但同时也意味着部分依赖 Next.js 服务端 Runtime 的功能不能直接使用。

因此目前项目更适合：

> **静态前端 + 独立后端 API**

的架构。

---

# 🔐 关于后端服务

生产环境中，FastAPI 与 Next.js 静态文件可以分别运行。

例如：

```text
                    Internet
                       │
                       ▼
                    Nginx
                       │
            ┌──────────┴──────────┐
            │                     │
            ▼                     ▼
       Static Files             /api/*
            │                     │
            ▼                     ▼
          out/                  FastAPI
                                  │
                                  ▼
                           Business Logic
```

这样可以让：

- Nginx 负责前端
- FastAPI 负责后端 API
- 前端与后端职责分离
- 后端可以独立扩展
- 后续可以加入数据库、AI 服务等组件

---

# 🧩 开发中的问题与实践

这个项目的一部分价值并不只是最终代码，也包括开发过程中遇到的问题。

例如：

### Windows PowerShell 与 curl

Windows PowerShell 中：

```powershell
curl
```

通常对应：

```text
Invoke-WebRequest
```

而：

```powershell
curl.exe
```

才是真正的 curl。

因此在 Windows 下测试 JSON API 时，可以使用：

```powershell
Invoke-RestMethod
```

避免 PowerShell 与 curl 参数解析之间的差异。

---

### UTF-8 中文编码

后端返回 JSON 时使用：

```python
json.dumps(data, ensure_ascii=False)
```

并通过 UTF-8 编码发送：

```python
body.encode("utf-8")
```

HTTP Header 推荐明确指定：

```text
Content-Type: application/json; charset=utf-8
```

浏览器能够正常解析 UTF-8 JSON，而部分 Windows 终端可能因为终端编码设置不同而出现中文乱码。

---

# 📈 当前开发状态

项目目前处于：

> 🚧 **持续开发中**

目前已经完成：

- [x] Next.js 前端基础环境
- [x] Python 后端环境
- [x] 基础 HTTP API
- [x] JSON 数据交互
- [x] GET API
- [x] POST API
- [x] FastAPI 接口测试
- [x] Next.js Static Export
- [x] Ubuntu 云服务器部署
- [x] Nginx 静态网站部署
- [x] 前后端基础通信

---

# 🗺️ Roadmap

接下来计划逐步完善：

### 前端

- [ ] 完善个人主页
- [ ] 优化响应式设计
- [ ] 增加项目展示
- [ ] 增加文章 / 技术笔记
- [ ] 增加动画与交互
- [ ] 优化 SEO
- [ ] 优化页面性能

### 后端

- [ ] 完善 API 结构
- [ ] 统一 API Response 格式
- [ ] 增加异常处理
- [ ] 增加日志系统
- [ ] 增加数据持久化
- [ ] 接入数据库
- [ ] 完善文本分析能力

### AI

- [ ] 接入 AI API
- [ ] AI 文本分析
- [ ] AI 辅助内容生成
- [ ] AI 工具页面
- [ ] 统一 AI API 调用层

### 工程化

- [ ] Docker
- [ ] CI/CD
- [ ] 自动化测试
- [ ] 环境变量管理
- [ ] Production Logging
- [ ] 服务监控
- [ ] 自动部署

---

# 📚 项目意义

Zero to Tech 并不是一个单纯用于展示技术栈的 Demo。

更希望通过持续开发这个项目，理解一个真实 Web 项目的完整生命周期：

```text
需求
 ↓
设计
 ↓
前端
 ↓
后端
 ↓
API
 ↓
数据
 ↓
测试
 ↓
Build
 ↓
Linux
 ↓
Nginx
 ↓
Cloud Server
 ↓
上线
 ↓
维护
 ↓
持续迭代
```

从最开始的：

```text
Hello World
```

逐渐走向：

```text
一个真正可以访问、
可以交互、
可以部署、
可以持续维护的全栈项目。
```

---

# 🎯 项目定位

**Zero to Tech = Learning + Building + Shipping**

它既是：

- 🧑‍💻 一个全栈开发实践项目
- 📚 一个技术学习记录
- 🌐 一个个人技术网站
- 🧪 一个技术实验场
- ☁️ 一个云服务器部署实践
- 🤖 一个未来持续扩展 AI 能力的平台

---

# 🤝 Contributing

目前这是一个个人持续开发项目。

如果你对项目有建议、发现 Bug 或者有更好的实现方式，欢迎提交 Issue 或 Pull Request。

---

# ⭐ Repository

GitHub：

https://github.com/Kleon26/zero-to-tech

---

# 📄 License

项目 License 将在后续开发阶段确定。

---

<div align="center">

**Zero to Tech**

### 从 0 开始写代码，从 0 开始理解技术，从 0 开始构建自己的东西。

**Build from Zero · Learn by Building · Ship for Real**

</div>