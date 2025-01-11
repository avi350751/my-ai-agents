from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

load_dotenv()

finance_agent = Agent(
    name= "Finance Agent",
    role= "Get Financial data",
    model = OpenAIChat(id="gpt-4o"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tools_calls=True,
    markdown=True,
    instructions=["use tables to display data"],
    debug_mode = True

)

web_agent = Agent(
    name= "Web Agent",
    role= "Get Financial data",
    model = OpenAIChat(id="gpt-4o"),
    tools = [DuckDuckGo()],
    show_tools_calls=True,
    markdown=True,
    instructions=["Always include sources"],
    debug_mode = True

)

agent_team = Agent(
    team = [finance_agent, web_agent],
    instructions= ["use tables to display data","always include sources"],
    show_tool_calls=True,
    markdown=True,
)

# Agents use tools to get the latest information
agent_team.print_response("Summarize analyst recommendations and share latest news on NVIDIA", stream=True)