from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv("DASHSCOPE_BASE_URL")
api_key = os.getenv("DASHSCOPE_API_KEY")
model = init_chat_model(
    model="qwen3.5-plus",
    model_provider="openai",
    base_url=base_url,
    api_key=api_key
)

# 方式一
agent = create_agent(model=model)

# 方式二
# agent2 = create_agent(model="deepseek-v4-flash")

# 阻塞式调用
# response = agent.invoke({
#     "messages": [{"role": "user", "content": "你是谁？"}]
# })
# print(response)

# 流式调用
messages = agent.stream(
    {"messages": [{"role": "user", "content": "你是谁？"}]},
    stream_mode="messages"
)
print(type(messages))
for token, metadata in messages:
    if token.content:
        print(token.content, end="", flush=True)
