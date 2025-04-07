import os
import asyncio

from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled, function_tool
from openai import AsyncOpenAI


load_dotenv(override=True)
client = AsyncOpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"])
set_tracing_disabled(disabled=True)

@function_tool
def get_weather(city: str) -> str:
    return {
        "city": city,
        "temperature": 72,
        "description": "Sunny",
    }

agent = Agent(
    name="Weather agent",
    instructions="You can only provide weather information.",
    tools=[get_weather],
)


spanish_agent = Agent(
    name="Spanish agent",
    instructions="You only speak Spanish.",
    tools=[get_weather],
    model=OpenAIChatCompletionsModel(model="gpt-4o", openai_client=client),
)

english_agent = Agent(
    name="English agent",
    instructions="You only speak English",
    tools=[get_weather],
    model=OpenAIChatCompletionsModel(model="gpt-4o", openai_client=client),
)

triage_agent = Agent(
    name="Triage agent",
    instructions="Handoff to the appropriate agent based on the language of the request.",
    handoffs=[spanish_agent, english_agent],
    model=OpenAIChatCompletionsModel(model="gpt-4o", openai_client=client))


async def main():
    result = await Runner.run(triage_agent, input="Hola, ¿cómo estás? ¿Puedes darme el clima para San Francisco CA?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())