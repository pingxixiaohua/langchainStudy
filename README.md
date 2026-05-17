# LangChain 1.2 学习项目

基于 LangChain 1.2 的入门学习项目，涵盖模型调用、智能体、工具、记忆等核心概念。

## 环境要求

- Python >= 3.12
- 使用 [uv](https://docs.astral.sh/uv/) 管理依赖

## 快速开始

```bash
# 安装依赖
uv sync

# 运行任意脚本
uv run python part1_introduction/01_初始化模型.py
```

需要在项目根目录创建 `.env` 文件配置 API 密钥：

```
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
DASHSCOPE_API_KEY=your_api_key
```

## 目录结构

```
├── main.py                  # 入口文件
├── langgraph.json           # LangGraph 部署配置（本地调试用）
├── part1_introduction/      # 入门教程（按序号递进）
│   ├── 01_初始化模型.py      # 模型初始化（init_chat_model / ChatTongyi）
│   ├── 02_调用模型.py        # invoke 与 stream 两种调用方式
│   ├── 03_创建智能体.py      # create_agent 创建智能体，阻塞与流式调用
│   ├── 04_使用messages.py    # SystemMessage / HumanMessage / AIMessage
│   ├── 05_多模态.py          # 图片输入，多模态理解
│   ├── 06_提示词工程.py      # 通过 System Prompt 控制模型行为
│   ├── 07_fewShot示例.py     # Few-shot 提示词示例
│   ├── 08_结构化输出.py       # 提示词驱动 JSON 结构化输出
│   ├── 09_基于model的结构化输出.py  # response_format + Pydantic 结构化输出
│   ├── 10_工具tools.py       # @tool 装饰器定义工具，绑定到 Agent
│   ├── 11.langchain内部预设工具.py  # TavilySearch 等预置工具的使用
│   ├── 12_短期记忆.py         # InMemorySaver 实现短期记忆
│   ├── 13_短期记忆持久存储.py  # SqliteSaver 持久化存储会话状态
│   ├── 14_记忆管理策略.py     # SummarizationMiddleware 总结压缩会话
│   └── 15_综合构建一个智能体.py  # 综合实战，LangGraph Platform 部署 Agent
├── pro_engineer/             # 实战项目
│   └── agents/
│       └── personal_chief.py # AI 私厨助手：多模态食材识别 + 食谱搜索 + 智能推荐
└── resource/                 # 资源文件（SQLite checkpoint 数据库等）
```

## 学习路线

| 编号 | 主题 | 要点 |
|------|------|------|
| 01 | 模型初始化 | `init_chat_model` 多种初始化方式，OpenAI 兼容 provider |
| 02 | 模型调用 | `invoke` 阻塞调用 vs `stream` 流式输出 |
| 03 | 创建智能体 | `create_agent`，`stream_mode="messages"` 流式消息 |
| 04 | Messages | `SystemMessage` / `HumanMessage` / `AIMessage` 构建对话 |
| 05 | 多模态 | `HumanMessage` 携带图片 URL，多模态理解 |
| 06 | 提示词工程 | System Prompt 设定角色、指令，控制输出风格 |
| 07 | Few-shot | 在 System Prompt 中给出示例，引导模型输出 |
| 08 | 结构化输出 | 提示词指定 JSON 格式输出 |
| 09 | Model 结构化输出 | `response_format=PydanticModel` 原生结构化输出 |
| 10 | 工具定义 | `@tool` 装饰器、Pydantic `args_schema`，工具绑定 Agent |
| 11 | 预置工具 | TavilySearch 等 LangChain 内置工具，注意描述复杂度 |
| 12 | 短期记忆 | `AgentState` + `InMemorySaver`，`thread_id` 区分会话 |
| 13 | 持久存储 | `SqliteSaver` 将 checkpoint 持久化到 SQLite |
| 14 | 记忆管理 | `SummarizationMiddleware` 触发式总结，避免上下文超限 |
| 15 | 综合实战 | 综合前面知识构建智能体，LangGraph Platform 托管部署 |

## 实战项目

### AI 私厨助手 (`pro_engineer/agents/personal_chief.py`)

综合运用多模态模型、搜索引擎、Agent 开发的完整实战项目：

1. **多模态识别** — 使用 `qwen3.6-plus` 识别用户提供的食材照片
2. **智能检索** — 调用 TavilySearch 搜索适配食谱
3. **多维度评估** — 从营养价值、制作难度对候选食谱量化打分排序
4. **结构化输出** — 生成包含食谱信息、得分、推荐理由的报告

通过 `langgraph.json` 配置部署到 LangGraph Platform，支持本地调试和 LangSmith 可观测性。

```bash
# 本地启动 LangGraph 调试服务器
uvx langgraph dev --port 2024
```

## 依赖

主要依赖包括：

- **langchain** (>=1.2.17) — 核心框架
- **langchain-community** — 社区模型（如 ChatTongyi）
- **langchain-openai** / **langchain-deepseek** — 模型 provider
- **langgraph-checkpoint-sqlite** — SQLite checkpoint 持久化
- **langchain-tavily** — Tavily 搜索工具
- **dashscope** — 阿里云 DashScope（通义千问）
- **langgraph-cli[inmem]** — LangGraph CLI 本地调试服务器
- **openai** — OpenAI SDK
