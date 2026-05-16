import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
from langchain.agents import create_agent

# 连接sqlite
connection = sqlite3.connect("resource/checkpoint.db", check_same_thread=False)
# 初始化checkpointer
checkpointer = SqliteSaver(connection)
# 自动建表
checkpointer.setup()

agent = create_agent("deepseek-v4-flash", checkpointer=checkpointer)

from langchain.messages import HumanMessage

config = {"configurable": {"thread_id": "thread_2"}}

# 第一次对话，对话完注释调
# response = agent.invoke({"messages": [HumanMessage(content="你好，我叫宁宁")]}, config)
# print(response["messages"][-1].content)

# 第二次对话
response2 = agent.invoke(
    {"messages": [HumanMessage(content="你知道我叫什么吗？")]}, config
)
print(response2["messages"][-1].content)
