import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage



# 加载 .env 文件中的环境变量
load_dotenv()

search_tool = TavilySearch(
    max_results=5,
    topic="general",
)
result = search_tool.invoke("特朗普访华")
# print(result)

# 创建智能体，使用预定义工具tavily
agent = create_agent(
    model="deepseek-chat",
    tools=[search_tool],
    system_prompt="你是一个智能助手，你使用工具来解决用户问题。"
)

# 调用工具
for chunk in agent.stream(
    {"messages": [HumanMessage(content="特朗普访华?")]},
    stream_mode="updates"
):
    for step, data in chunk.items():
        print(f"step: {step}")
        print(f"content: {data['messages'][-1].content_blocks}")
        print()

"""
注意，LangChain提供的TavilySearch工具描述非常复杂
参数也很多。会有额外的网络消耗
如果我们仅仅是需要query参数，建议自定义工具

# 使用tavily作为web搜索工具
tavily = TavilySearch(
    max_results=5,
    topic="general"
)

@tool
def web_search(query: str):
    "Search the web for information"
    return tavily.invoke(query)

"""