from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

system_prompt = """
# 身份
- 你是一个科幻作家，根据用户的要求创建一个太空之都。

# 示例
user：月球的首都是什么？
assistant：月华城（Lunara）—— 镶嵌在月球静海环形山中的水晶穹顶都市，其核心是一座利用月球潮汐能驱动的巨型生态循环塔。

user：火星的首都是什么？
assistant：赤晶城（Aresia）—— 深嵌于火星奥林匹斯山熔岩管内的蜂巢都市，地表仅露出由火星红土烧制而成的螺旋尖塔。
"""

# 创建智能体
agent = create_agent(model="deepseek-chat", system_prompt=system_prompt)

for token, metadata in agent.stream(
    {"messages": [HumanMessage(content="金星的首都是什么?")]}, stream_mode="messages"
):
    print(token.content, end="", flush=True)
