from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


@tool
def get_weather(location: str) -> str:
    """
    查询天气
    参数： 城市名称
    """
    return f"{location}今天是晴天"


agent = create_agent(model="deepseek-chat", tools=[get_weather])

response = agent.invoke(
    {
        "messages": [
            SystemMessage(content="请使用工具来获取天气"),
            HumanMessage(content="你好，我是华哥"),
            AIMessage(content="你好华哥，很高兴认识你"),
            HumanMessage(content="杭州天气怎么样？"),
        ]
    }
)

print(response)

for message in response["messages"]:
    message.pretty_print()
