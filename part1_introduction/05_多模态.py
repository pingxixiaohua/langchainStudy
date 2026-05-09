from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

load_dotenv()
base_url = os.getenv("DASHSCOPE_BASE_URL")
api_key = os.getenv("DASHSCOPE_API_KEY")
model = init_chat_model(
    model="qwen3.5-plus", model_provider="openai", base_url=base_url, api_key=api_key
)
agent = create_agent(model=model)

message = HumanMessage(
    [
        {"type": "text", "text": "请描述下面这张图片内容"},
        {
            "type": "image",
            "url": "https://img.shetu66.com/2023/06/29/1688025012523974.png",
        },
    ]
)

stream = agent.stream(
    {"messages": [message]},
    stream_mode="messages",
)
for chunk, metadata in stream:
    if chunk.content:
        print(chunk.content, end="", flush=True)
