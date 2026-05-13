from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from pydantic import BaseModel


class CapitalInfo(BaseModel):
    name: str
    location: str
    vibe: str
    economy: str


agent = create_agent(
    model="deepseek-chat",
    system_prompt="你是一个科幻作家，根据用户的要求创建一个太空之都",
    response_format=CapitalInfo,
)

response = agent.invoke({"messages": [HumanMessage(content="月球的首都是什么？")]})
# print(response)

city = response["structured_response"]
print(city)

print(
    f"{city.name}位于{city.location}，是一座{city.vibe}的城市，其主要产业包括{city.economy}。"
)
