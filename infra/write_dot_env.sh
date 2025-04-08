#!/bin/bash

# Clear the contents of the .env file
> .env

# Append new values to the .env file
echo "API_HOST=azure" >> .env
echo "AZURE_OPENAI_DEPLOYMENT=$(azd env get-value AZURE_OPENAI_DEPLOYMENT)" >> .env
echo "AZURE_OPENAI_MODEL=$(azd env get-value AZURE_OPENAI_MODEL)" >> .env
echo "AZURE_OPENAI_SERVICE=$(azd env get-value AZURE_OPENAI_SERVICE)" >> .env
echo "AZURE_OPENAI_ENDPOINT=$(azd env get-value AZURE_OPENAI_ENDPOINT)" >> .env
echo "AZURE_TENANT_ID=$(azd env get-value AZURE_TENANT_ID)" >> .env
echo "AZURE_OPENAI_VERSION=2024-10-21" >> .env