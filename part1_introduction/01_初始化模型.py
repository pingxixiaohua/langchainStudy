from langchain.chat_models import init_chat_model

# 方式一
# model = init_chat_model(model="deepseek-v4-flash")
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
print(type(model))

# 方式三
# 社区依赖，第三方
from langchain_community.chat_models.tongyi import ChatTongyi
model2 = ChatTongyi(
    model="qwen3.5-plus"
)
print(type(model2))

