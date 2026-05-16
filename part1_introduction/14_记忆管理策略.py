"""
记忆管理策略：
    修剪:
       修剪消息并不是真正的删除消息，在AgentState中的消息列表依然是完整的，只不过发送给LLM之前会进行修剪，只保留一部分消息。

    删除：
       删除消息与修剪不同：
        - 修剪消息：只是从State中选取一部分消息发送给模型
        - 删除消息：直接删除State中保存的消息，也就是说消息历史中不再存在！

    总结：
        不管是修剪还是删除，都会导致一部分消息丢失，从而丢失记忆。所以就有了第三种策略：总结消息（Summarize Messages）
        它的思路很简单，就是把历史的消息利用大模型总结出摘要，然后把最新的消息拼接在一起作为新的消息列表发送给大模型，
        这样既不会超出模型的上下文窗口限制，还能尽量保留所有的记忆。

        LangChain提供了总结消息的默认实现：SummarizationMiddleware

    自定义：


"""

from langchain import messages
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware

# from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.runnables import RunnableConfig
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

# 连接sqlite
connection = sqlite3.connect("resource/checkpointTwo.db", check_same_thread=False)
# 初始化checkpointer
checkpointer = SqliteSaver(connection)
# 自动建表
checkpointer.setup()

middleware = SummarizationMiddleware(
    model="deepseek-v4-flash",
    trigger=("messages", 3),  # 触发时机，当消息超过3条，进行总结
    keep=("messages", 1),  # 保留会话1条
)

agent = create_agent(
    "deepseek-v4-flash", middleware=[middleware], checkpointer=checkpointer
)

from langchain.messages import HumanMessage

config = {"configurable": {"thread_id": "thread_3"}}

agent.invoke({"messages": [HumanMessage(content="你好，我是宁宁")]}, config)
agent.invoke({"messages": [HumanMessage(content="我喜欢看电影")]}, config)
agent.invoke({"messages": [HumanMessage(content="我喜欢吃米饭")]}, config)

final_response = agent.invoke(
    {"messages": HumanMessage(content="你还记得我吗？")}, config
)
print(final_response["messages"])

for message in final_response["messages"]:
    message.pretty_print()
