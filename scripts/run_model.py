import os
from anthropic import AnthropicFoundry

# Load credentials
api_key = os.getenv("ANTHROPIC_API_KEY")
endpoint = os.getenv("ANTHROPIC_BASE_URL")
deployment_name = "claude-opus-4-6"

# Initialize client
client = AnthropicFoundry(
    api_key=api_key,
    base_url=endpoint
)

# Your prompt
user_prompt = "Generate a sample cybersecurity architecture control matrix."

# Send request
response = client.messages.create(
    model=deployment_name,
    messages=[{"role": "user", "content": user_prompt}],
    max_tokens=1024
)

# Print response
print("Claude response:\n")
print(response.content)