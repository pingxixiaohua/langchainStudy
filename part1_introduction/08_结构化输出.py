from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

system_prompt = """
# 身份
- 你是一个科幻作家，根据用户的要求创建一个太空之都。

# 指令
- 请务必以JSON格式输出，不要加任何markdown样式。

# 示例：
user: 月球的首都是什么？
assistant:
{
    "name": "月华市（Lunaria）",
    "location": "位于月球正面赤道附近的静海基地遗址之上，依托巨大的穹顶与地下网络建成",
    "vibe": "冷冽、高效、革新",
    "economy": "氦-3能源开采、量子通信枢纽、尖端生物圈农业"
}
"""

agent = create_agent(model="deepseek-chat", system_prompt=system_prompt)

response = agent.invoke(
    {"messages": [HumanMessage(content="金星的首都是什么?")]},
)

print(response["messages"][-1].content)
