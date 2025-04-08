# Clear the contents of the .env file
Set-Content -Path .env -Value ""

# Append new values to the .env file
$azureOpenAiDeployment = azd env get-value AZURE_OPENAI_DEPLOYMENT
$azureOpenAiModel = azd env get-value AZURE_OPENAI_MODEL
$azureOpenAiService = azd env get-value AZURE_OPENAI_SERVICE
$azureTenantId = azd env get-value AZURE_TENANT_ID
$azureOpenAiApiEndpoint = azd env get-value AZURE_OPENAI_API_ENDPOINT

Add-Content -Path .env -Value "API_HOST=azure"
Add-Content -Path .env -Value "AZURE_OPENAI_DEPLOYMENT=$azureOpenAiDeployment"
Add-Content -Path .env -Value "AZURE_OPENAI_MODEL=$azureOpenAiModel"
Add-Content -Path .env -Value "AZURE_OPENAI_SERVICE=$azureOpenAiService"
Add-Content -Path .env -Value "AZURE_OPENAI_API_ENDPOINT=$azureOpenAiApiEndpoint"
Add-Content -Path .env -Value "AZURE_TENANT_ID=$azureTenantId"
Add-Content -Path .env -Value "AZURE_OPENAI_VERSION=2024-10-21"