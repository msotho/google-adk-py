from google.adk.agents import Agent

from analyst.tools import web_search_skill

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-3.1-flash-lite",
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a city."
    ),
    tools=[search_skill],
)
