import os

from smolagents import CodeAgent, DuckDuckGoSearchTool, OpenAIServerModel

model = OpenAIServerModel(
    model_id="gpt-4o", api_base="https://models.inference.ai.azure.com", api_key=os.environ["GITHUB_TOKEN"]
)

agent = CodeAgent(tools=[DuckDuckGoSearchTool()], model=model)

agent.run("How many seconds would it take for a leopard at full speed to run through Pont des Arts?")
