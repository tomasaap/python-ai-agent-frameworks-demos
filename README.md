<!--
---
name: AI Agents with Python Demos
description: Collection of Python examples demonstrating various AI agent patterns, frameworks, and integration techniques.
languages:
- python
products:
- azure-openai
- azure
page_type: sample
urlFragment: python-ai-agents-demos
---
-->
# AI Agents with Python Demos

[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&skip_quickstart=true&machine=basicLinux32gb&repo=784926917&devcontainer_path=.devcontainer%2Fdevcontainer.json&geo=WestUs2)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/Azure-Samples/python-ai-agents-demos)

This repository provides examples and code samples demonstrating AI agent patterns, frameworks, and integration techniques using Python. It covers various frameworks for building, deploying, and using AI agents for different tasks and scenarios.

* [Features](#features)
* [Getting started](#getting-started)
  * [GitHub Codespaces](#github-codespaces)
  * [VS Code Dev Containers](#vs-code-dev-containers)
  * [Local environment](#local-environment)
* [Running the Python examples](#running-the-python-examples)
* [Guidance](#guidance)
  * [Costs](#costs)
  * [Security guidelines](#security-guidelines)
* [Resources](#resources)

## Features

* Examples of different AI agent frameworks and libraries
* Demonstrations of agent-based workflows and patterns
* Integration samples with various data sources and tools
* Code for building autonomous agents with different capabilities

### Agent Architectures

Various agent architectures and patterns are demonstrated, including:

* Task-specific agents
* Multi-agent systems
* Tool-using agents
* Reasoning and planning agents

## Getting started

You have a few options for getting started with this repository.
The quickest way to get started is GitHub Codespaces, since it will setup all the tools for you, but you can also [set it up locally](#local-environment).

### GitHub Codespaces

You can run this repository virtually by using GitHub Codespaces. The button will open a web-based VS Code instance in your browser:

1. Open the repository (this may take several minutes):

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Azure-Samples/python-ai-agents-demos)

2. Open a terminal window
3. Continue with the steps to run the examples

### VS Code Dev Containers

A related option is VS Code Dev Containers, which will open the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1. Start Docker Desktop (install it if not already installed)
2. Open the project:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/python-ai-agents-demos)

3. In the VS Code window that opens, once the project files show up (this may take several minutes), open a terminal window.
4. Continue with the steps to run the examples

### Local environment

1. Make sure the following tools are installed:

    * [Python 3.9+](https://www.python.org/downloads/)
    * Git

2. Clone the repository:

    ```shell
    git clone https://github.com/Azure-Samples/python-ai-agents-demos.git
    cd python-ai-agents-demos
    ```

3. Set up a virtual environment:

    ```shell
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4. Install the requirements:

    ```shell
    pip install -r requirements.txt
    ```

## Running the Python examples

1. Configure your environment variables by copying the `.env.example` to `.env` and updating the values:

    ```shell
    cp .env.example .env
    ```

2. Edit the `.env` file with your API keys and configuration settings.

3. Run an example by using:

    ```shell
    python examples/example_filename.py
    ```

   or select the `Run` button on the opened file in VS Code.

## Guidance

### Costs

Some examples in this repository use cloud-based AI services like Azure OpenAI, which incur costs based on usage. 
The pricing is based on the number of tokens used, with around 1-3 tokens used per word. You can find the pricing details 
for various AI services on their respective pricing pages.

### Security guidelines

When using API keys for authentication to AI services, ensure that:

1. You do not commit API keys to version control
2. Use environment variables to store sensitive information
3. Consider using managed identities or other keyless authentication methods for production deployments

For higher security in production environments, consider:
- Deploying services inside a private virtual network (VNet)
- Using private endpoints for service access
- Implementing proper role-based access control

## Resources

* [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
* [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
* [Semantic Kernel Documentation](https://learn.microsoft.com/semantic-kernel/overview/)
* [AutoGen Documentation](https://microsoft.github.io/autogen/)
