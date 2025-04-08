import os
from typing import Literal

import azure.identity
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI, AsyncOpenAI
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.messages import ModelMessage
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.usage import Usage, UsageLimits
from rich.prompt import Prompt

# Setup the OpenAI client to use either Azure OpenAI or GitHub Models
load_dotenv(override=True)
API_HOST = os.getenv("API_HOST", "github")

if API_HOST == "github":
    client = AsyncOpenAI(api_key=os.environ["GITHUB_TOKEN"], base_url="https://models.inference.ai.azure.com")
    model = OpenAIModel("gpt-4o", provider=OpenAIProvider(openai_client=client))
elif API_HOST == "azure":
    token_provider = azure.identity.get_bearer_token_provider(
        azure.identity.DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
    )
    client = AsyncAzureOpenAI(
        api_version=os.environ["AZURE_OPENAI_VERSION"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        azure_ad_token_provider=token_provider,
    )
    model = OpenAIModel(
        os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT"],
        provider=OpenAIProvider(openai_client=client))

class FlightDetails(BaseModel):
    flight_number: str


class Failed(BaseModel):
    """Unable to find a satisfactory choice."""


flight_search_agent = Agent(
    model,
    result_type=FlightDetails | Failed,
    system_prompt=('Use the "flight_search" tool to find a flight ' "from the given origin to the given destination."),
)


@flight_search_agent.tool
async def flight_search(ctx: RunContext[None], origin: str, destination: str) -> FlightDetails | None:
    # in reality, this would call a flight search API or
    # use a browser to scrape a flight search website
    return FlightDetails(flight_number="AK456")


usage_limits = UsageLimits(request_limit=15)


async def find_flight(usage: Usage) -> FlightDetails | None:
    message_history: list[ModelMessage] | None = None
    for _ in range(3):
        prompt = Prompt.ask(
            "Where would you like to fly from and to?",
        )
        result = await flight_search_agent.run(
            prompt,
            message_history=message_history,
            usage=usage,
            usage_limits=usage_limits,
        )
        if isinstance(result.data, FlightDetails):
            return result.data
        else:
            message_history = result.all_messages(result_tool_return_content="Please try again.")


class SeatPreference(BaseModel):
    row: int = Field(ge=1, le=30)
    seat: Literal["A", "B", "C", "D", "E", "F"]


# This agent is responsible for extracting the user's seat selection
seat_preference_agent = Agent(
    model,
    result_type=SeatPreference | Failed,
    system_prompt=(
        "Extract the user's seat preference. "
        "Seats A and F are window seats. "
        "Row 1 is the front row and has extra leg room. "
        "Rows 14, and 20 also have extra leg room. "
    ),
)


async def find_seat(usage: Usage) -> SeatPreference:
    message_history: list[ModelMessage] | None = None
    while True:
        answer = Prompt.ask("What seat would you like?")

        result = await seat_preference_agent.run(
            answer,
            message_history=message_history,
            usage=usage,
            usage_limits=usage_limits,
        )
        if isinstance(result.data, SeatPreference):
            return result.data
        else:
            print("Could not understand seat preference. Please try again.")
            message_history = result.all_messages()


async def main():
    usage: Usage = Usage()

    opt_flight_details = await find_flight(usage)
    if opt_flight_details is not None:
        print(f"Flight found: {opt_flight_details.flight_number}")
        # > Flight found: AK456
        seat_preference = await find_seat(usage)
        print(f"Seat preference: {seat_preference}")
        # > Seat preference: row=1 seat='A'


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
