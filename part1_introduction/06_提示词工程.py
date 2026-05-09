from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

# 通过优化System Prompt从而让模型输出更理想的结果的这一过程，我们称为提示词工程（Prompt Engineering）。
# 设定角色和指定

system_prompt = """
    # 身份： 
    - 你是一个编程助手，帮助用户编写python代码

    # 指令
    - 定义变量时，使用snake case命名法，而不是camel case命名法
    - 不要返回markdown格式说明，返回代码即可
"""

agent = create_agent(model="deepseek-chat", system_prompt=system_prompt)

for token, metadata in agent.stream(
    {"messages": [HumanMessage(content="定义一个string变量类型")]},
    stream_mode="messages",
):
    print(token.content, end="", flush=True)
