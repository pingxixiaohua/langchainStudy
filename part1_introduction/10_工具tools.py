from langchain import messages
from langchain_core.tools import tool


# 方式一@tool装饰器，函数名加函数描述
@tool("square_root", description="Calculate the square root of a number")
def tool1(x: float) -> float:
    return x**0.5


# 方式二，使用函数名加文档注释
@tool
def tool2(x: float) -> float:
    """Calculate the square root of a number"""
    return x**0.5


# 包含多个参数
# 定义一个查询天气的tool
@tool
def get_weather(
    location: str, units: str = "celsius", include_forecast: bool = False
) -> str:
    """
    Get current weather and optional forecast.
    Args:
        location: city name or optional forecast
        units: unit of degrees
        include_forecast: does it include the weather forecast
    """
    temp = 22 if units == "celsius" else 72
    result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
    if include_forecast:
        result += "\nNext 5 days: Sunny"
    return result


# 方式三，参数类型比较复杂时，用Pydantic Model描述参数
from pydantic import BaseModel, Field
from typing import Literal


class WeatherInput(BaseModel):
    """
    查询天气的输入参数
    """

    location: str = Field(description="City name or  coordinates")
    units: Literal["celsius", "fahrenheit"] = Field(
        default="celsius", description="Temperature unit preference"
    )
    include_forecast: bool = Field(default=False, description="Include 5-day forecast")


@tool(args_schema=WeatherInput)
def get_weather2(
    location: str, units: str = "celsius", include_forecast: bool = False
) -> str:
    """
    get current weather and optional forecast
    """
    temp = 22 if units == "celsius" else 72
    result = f"Current weather in {location}: {temp} degrees {units[0].upper()}"
    if include_forecast:
        result += "\nNext 5 days: sunny"
    return result


# 调用
# 调用数学工具
tool1.invoke({"x": 467})

# 调用查询天气工具
get_weather.invoke({"location": "杭州", "include_forecast": True})


# 测试
from langchain.agents import create_agent
from langchain.messages import HumanMessage

agent = create_agent(model="deepseek-chat", tools=[tool1, get_weather])

for token, metadata in agent.stream(
    {"messages": [HumanMessage(content="杭州接下来天气如何？")]}, stream_mode="messages"
):
    print(token.content, end="", flush=True)
