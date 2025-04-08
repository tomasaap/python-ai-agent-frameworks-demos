# https://docs.llamaindex.ai/en/stable/examples/agent/react_agent_with_query_engine/

import os
import requests
from pathlib import Path

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from llama_index.llms.openai_like import OpenAILike
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.tools import QueryEngineTool
from llama_index.core.agent.workflow import ReActAgent
from llama_index.core.workflow import Context
from llama_index.core.agent.workflow import ToolCallResult, AgentStream

Settings.llm = OpenAILike(
    model=os.getenv("GITHUB_MODEL", "gpt-4o"),
    api_base="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
    is_chat_model=True,
)

Settings.embed_model = OpenAIEmbedding(
  model="text-embedding-3-small",
  api_base="https://models.inference.ai.azure.com",
  api_key=os.environ["GITHUB_TOKEN"]
)

# Try to load the index from storage
try:
    storage_context = StorageContext.from_defaults(
        persist_dir="./storage/docs1"
    )
    index1 = load_index_from_storage(storage_context)

    storage_context = StorageContext.from_defaults(
        persist_dir="./storage/docs2"
    )
    index2 = load_index_from_storage(storage_context)

    index_loaded = True
except:
    index_loaded = False

if not index_loaded:
    curr_dir = Path(__file__).parent

    docs1 = SimpleDirectoryReader(input_files=[curr_dir / "employee_handbook.pdf"]).load_data()
    docs2 = SimpleDirectoryReader(input_files=[curr_dir / "PerksPlus.pdf"]).load_data()
    index1 = VectorStoreIndex.from_documents(docs1)
    index2 = VectorStoreIndex.from_documents(docs2)

    index1.storage_context.persist(persist_dir="./storage/docs1")
    index2.storage_context.persist(persist_dir="./storage/docs2")

engine1 = index1.as_query_engine(similarity_top_k=3)
engine2 = index2.as_query_engine(similarity_top_k=3)

query_engine_tools = [
    QueryEngineTool.from_defaults(
        query_engine=engine1,
        name="engine1",
        description=(
            "Provides information about Contoso employee handbook - covering basic job roles, policies, workplace safety, HR, etc."
        ),
    ),
    QueryEngineTool.from_defaults(
        query_engine=engine2,
        name="engine2",
        description=(
            "Provides information about Contoso PerksPlus program, including what can be reimbursed. "
        ),
    ),
]

async def main():
    agent = ReActAgent(
        tools=query_engine_tools,
        llm=Settings.llm
    )
    ctx = Context(agent)

    handler = agent.run("can i get my gardening tools reimbursed?", ctx=ctx)

    async for ev in handler.stream_events():
        # if isinstance(ev, ToolCallResult):
        #     print(f"\nCall {ev.tool_name} with {ev.tool_kwargs}\nReturned: {ev.tool_result}")
        if isinstance(ev, AgentStream):
            print(f"{ev.delta}", end="", flush=True)

    response = await handler
    print(str(response))


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())