import os

from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    markdown=True
)

# Agents use tools to get the latest information
agent.print_response("Write me a short poem on zoo animals")

