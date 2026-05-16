from langchain.agents import create_agent
from langchain.messages import HumanMessage

# agent = create_agent(model="deepseek-v4-flash")

# 智能体当前是没有记忆的，只能回答一次
# response = agent.invoke({"messages": [HumanMessage(content="你好，我我叫宁宁")]})
# print(response)

"""
Memory:
    短期记忆（short-term memory）：当前任务或回话的上下
    长期记忆（long-term memory）：跨任务或会话的经验和知识

    这里只实现短期记忆

    langchain的短期记忆通过agentState实现的，会话历史是agentState的一部分

    通过Checkpointer对象保存AgentState，每次与ai交互都会生成一个快照，纪录为一个checkpoint
    同一个会话多个checkpointer组成一个组，通过thread_id来标记

"""
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    "deepseek-v4-flash",
    checkpointer=InMemorySaver(),
)

config = {"configurable": {"thread_id": "thread_1"}}

response = agent.invoke(
    {"messages": [HumanMessage(content="你好，我是宁宁，你是？")]}, config
)
print(response["messages"][-1].content)

response = agent.invoke({"messages": [HumanMessage("你最想去的国家是哪里？")]}, config)

print(response["messages"][-1].content)
