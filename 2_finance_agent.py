import os

from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv
import os

load_dotenv()


def get_company_symbol(company:str) -> str:
    
    """Use this function to get the symbol of the company.
    Args : 
    company(str) : Name of the company.

    Returns:
    str : Symbol of the company.
    """
    symbols = {
        "Phidata" : "MSFT",
        "NVIDIA" : "NVDA",
        "Infosys" : "INFY",
        "TESLA" : "TSLA",
        "AMAZON" : "AMZN"
    }
    return symbols.get(company, "Unknown")


agent = Agent(
    # model=Groq(id="llama-3.3-70b-versatile"),
    model = OpenAIChat(id="gpt-4o"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    show_tools_calls=True,
    markdown=True,
    instructions=["use tables to display data",
                  "If you do not know the company symbol use the tool get_company_symbol even it is not a public company"],
    debug_mode = True

)

# Agents use tools to get the latest information
agent.print_response("Compare the two stocks Tesla and Phidata on analyst recommendation and fundamentals")

