import os

from google.adk.agents import Agent
from google.adk.models import LiteLlm

from news_agent.tools import news_search

MODEL = "openai/mlx-community/gemma-4-12B-it-OptiQ-4bit"
MODEL_BASE_URL = os.getenv("MODEL_BASE_URL", "http://localhost:8080/v1")


root_agent = Agent(
    model=LiteLlm(
        model=MODEL,
        api_base=MODEL_BASE_URL,
        api_key="not-needed",
        extra_body={
            "chat_template_kwargs": {
                "enable_thinking": True  # Enable thinking
            },
            "skip_special_tokens": False,  # Should be set to False
        },
    ),
    name="news_agent",
    description="Agent to answer questions about news articles",
    instruction=(
        """
        You are a helpful assistant that answers questions about news articles.
        You have access to the following tools: fetch_news_sources.
        Use these tools to gather information about news sources and articles to answer the user's questions."
        """
    ),
    tools=[news_search.fetch_news_sources, news_search.fetch_news_articles],
)
