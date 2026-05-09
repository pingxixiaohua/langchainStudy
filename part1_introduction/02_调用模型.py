from langchain.chat_models import init_chat_model

# 方式一
# model = init_chat_model(model="deepseek-chat")
# print(type(model))

# 方式二
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

# 输出方式：invoke方式
# response = model.invoke("你是谁？")
# print(response.content)

# response = model.invoke([
#     {"role": "system", "content": "你是一个ai助手，回答的时候请简约"},
#     {"role": "user", "content": "你是谁？"},
# ])

# print(response.content)

# 输出方式：stream方式
stream = model.stream("你是谁？")
print(stream)
for chunk in stream:
    print(chunk.content, end="", flush=True)